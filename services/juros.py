from decimal import Decimal, getcontext, ROUND_HALF_EVEN
from datetime import date
from enum import Enum
from typing import Literal, Optional, Dict

getcontext().prec = 28  # IEEE 754 Decimal128
getcontext().rounding = ROUND_HALF_EVEN


class Base_Counting(Enum):
    ACT365 = "ACT/365"
    ACT360 = "ACT/360"
    B30360 = "30/360"


# multiplicar o dia do juros pela quantidade de dias em atraso
class Juros_Service:
    def __init__(
        self,
        base: Base_Counting = Base_Counting.ACT365,
        casas_moeda: int = 2,
        multa_moratoria: Decimal = Decimal("0.02"),  # 2%
        mora_am: Decimal = Decimal("0.01"),  # 1%
    ):

        self.base = base
        self.casas = casas_moeda
        self.multa = multa_moratoria
        self.mora_am = mora_am

    # ------- conversoes de taxa -----------
    def efetiva_am_de_aa(self, taxa_aa: Decimal) -> Decimal:
        # (1+i_a.a.)^(1/12)-1
        return (Decimal(1) + taxa_aa) ** (Decimal(1) / Decimal(12)) - Decimal(1)

    def efetiva_aa_de_am(self, taxa_am: Decimal) -> Decimal:
        return (Decimal(1) + taxa_am) ** Decimal(12) - Decimal(1)

    def nominal_para_efetiva(self, nominal: Decimal, periocidade: int) -> Decimal:
        # i_eff = (1 + i_nom/m)^m - 1
        return (Decimal(1) + nominal / Decimal(periocidade)) ** Decimal(
            periocidade
        ) - Decimal(1)

    # ---------- Contagem de dias ----------
    def fracao_periodo(self, inicial: date, fim: date) -> Decimal:
        if fim < inicial:
            raise ValueError("data final menor que a data inicio")
        if self.base == Base_Counting.ACT365:
            dias = (fim - inicial).days
            return Decimal(dias) / Decimal(365)
        if self.base == Base_Counting.ACT360:
            dias = (fim - inicial).days
            return Decimal(dias) / Decimal(360)
        # 30/360 Brasil
        d1, m1, y1 = inicial.day, inicial.month, inicial.year
        d2, m2, y2 = fim.day, fim.month, fim.year
        d1 = min(d1, 30)
        d2 = 30 if d2 == 31 and d1 == 30 else min(d2, 30)
        dias_30360 = (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)
        return Decimal(dias_30360) / Decimal(360)

    # ---------- Juros simples / compostos ----------
    def juros_mora_linear(self, juros_mensal: Decimal, dias_atraso: int) -> Decimal:
        juros_dia = juros_mensal / Decimal(30)
        return (juros_dia * Decimal(dias_atraso)).quantize("0.01")

    def juros_simples(
        self, principal: Decimal, taxa: Decimal, fracao: Decimal
    ) -> Decimal:
        return (principal * taxa * fracao).quantize(Decimal(10) ** -self.casas)

    def juros_compostos(
        self, principal: Decimal, taxa_efetiva_periodo: Decimal, n_periodos: Decimal
    ) -> Decimal:
        fator = (Decimal(1) + taxa_efetiva_periodo) ** n_periodos
        montante = principal * fator
        juros = montante - principal
        return juros.quantize(Decimal(10) ** -self.casas)

    # ---------- Atraso ----------
    def multa_atraso(self, principal_parcela: Decimal) -> Decimal:
        return (principal_parcela * self.multa).quantize(Decimal(10) ** -self.casas)

    def juros_mora_pro_rata(
        self, principal_parcela: Decimal, dias_atraso: int
    ) -> Decimal:
        # Converte mora a.m. para a.d. efetiva (aprox. 30 dias/mês)
        taxa_ad = (Decimal(1) + self.mora_am) ** (Decimal(1) / Decimal(30)) - Decimal(1)
        fator = (Decimal(1) + taxa_ad) ** Decimal(dias_atraso)
        juros = principal_parcela * (fator - Decimal(1))
        return juros.quantize(Decimal(10) ** -self.casas)

        # ---------- Utilitário de breakdown ----------

    def calcular_atraso(
        self, valor_parcela: Decimal, venc: date, pago_em: date
    ) -> Dict[str, Decimal]:
        if pago_em <= venc:
            return {
                "multa": Decimal("0.00"),
                "mora": Decimal("0.00"),
                "total": valor_parcela,
            }
        dias = (pago_em - venc).days
        multa = self.multa_atraso(valor_parcela)
        mora = self.juros_mora_pro_rata(valor_parcela, dias)
        total = (valor_parcela + multa + mora).quantize(Decimal(10) ** -self.casas)
        return {"multa": multa, "mora": mora, "total": total}


