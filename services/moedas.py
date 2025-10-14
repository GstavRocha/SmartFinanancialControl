from __future__ import annotations
from decimal import Decimal, getcontext, ROUND_HALF_EVEN
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, Optional, Protocol

getcontext().prec = 28
getcontext().rounding = ROUND_HALF_EVEN

# --- Metadados ISO 4217 comuns (adicione mais conforme necessário) ---
CURRENCY_META: Dict[str, Dict[str, object]] = {
    "BRL": {"symbol": "R$", "minor_units": 2},
    "USD": {"symbol": "$",  "minor_units": 2},
    "EUR": {"symbol": "€",  "minor_units": 2},
    "GBP": {"symbol": "£",  "minor_units": 2},
    "JPY": {"symbol": "¥",  "minor_units": 0},
    "ARS": {"symbol": "$",  "minor_units": 2},
    "CLP": {"symbol": "$",  "minor_units": 0},
    "COP": {"symbol": "$",  "minor_units": 0},
    "CNY": {"symbol": "¥",  "minor_units": 2},
}

def _minor_units(code: str) -> int:
    meta = CURRENCY_META.get(code.upper())
    if not meta:
        raise ValueError(f"Moeda não suportada: {code}")
    return int(meta["minor_units"])

def _symbol(code: str) -> str:
    meta = CURRENCY_META.get(code.upper())
    if not meta:
        raise ValueError(f"Moeda não suportada: {code}")
    return str(meta["symbol"])

def _quantize(amount: Decimal, code: str) -> Decimal:
    places = _minor_units(code)
    exp = Decimal(10) ** (-places) if places > 0 else Decimal(1)
    return amount.quantize(exp)

# --------- Provedor de taxas (pluggable) ---------
class Rate_Provider(Protocol):
    """Contrato para provedores de taxa de câmbio.
    Deve retornar um dicionário: {'USD': Decimal('5.61'), ...} relativo à moeda base."""
    def fetch(self, base_currency: str) -> Dict[str, Decimal]:
        ...

@dataclass
class StaticRate_Provider:
    """Provedor estático para testes/dev. Valores são 1 BASE = rate * TARGET.
    Ex.: base=BRL, rates['USD']=Decimal('5.60') => 1 USD = 5.60 BRL."""
    rates: Dict[str, Decimal]

    def fetch(self, base_currency: str) -> Dict[str, Decimal]:
        # Normaliza chaves e garante base = 1
        norm = {k.upper(): Decimal(v) for k, v in self.rates.items()}
        norm[base_currency.upper()] = Decimal("1")
        return norm

# --------- Serviço de Moedas ---------
class Moedas_Service:
    """Conversão e formatação de moedas com cache de taxas e arredondamento bancário."""
    def __init__(
        self,
        base_currency: str = "BRL",
        provider: Optional[Rate_Provider] = None,
        cache_ttl_seconds: int = 3600,
    ):
        self.base_currency = base_currency.upper()
        self.provider = provider or StaticRate_Provider(
            # taxas exemplo (ajuste conforme seu contexto)
            rates={
                "BRL": Decimal("1"),
                "USD": Decimal("5.60"),
                "EUR": Decimal("6.10"),
                "GBP": Decimal("7.20"),
                "JPY": Decimal("0.036"),
            }
        )
        self.cache_ttl = timedelta(seconds=cache_ttl_seconds)
        self._rates: Dict[str, Decimal] = {}
        self._last_fetch: Optional[datetime] = None

    # --- taxas & cache ---
    def _ensure_rates(self) -> None:
        if not self._rates or self._is_cache_expired():
            self._rates = self.provider.fetch(self.base_currency)
            self._last_fetch = datetime.utcnow()

    def _is_cache_expired(self) -> bool:
        if self._last_fetch is None:
            return True
        return datetime.utcnow() - self._last_fetch > self.cache_ttl

    def list_moedas(self) -> Dict[str, Decimal]:
        self._ensure_rates()
        return dict(self._rates)

    def set_rate(self, code: str, rate_vs_base: Decimal) -> None:
        """Ajusta manualmente uma taxa (útil para overrides ou testes)."""
        self._ensure_rates()
        self._rates[code.upper()] = Decimal(rate_vs_base)

    def get_rate(self, from_code: str, to_code: str) -> Decimal:
        """Retorna o fator de conversão de from_code -> to_code."""
        self._ensure_rates()
        f = from_code.upper()
        t = to_code.upper()
        if f not in self._rates or t not in self._rates:
            raise ValueError(f"Moeda não suportada ou sem taxa carregada: {f} / {t}")
        # taxas são armazenadas vs base: 1 UNIT = rate_vs_base BASE
        # Para converter f->t: (valor em BASE) = valor * rate_f; depois divide por rate_t
        rate_f = self._rates[f]
        rate_t = self._rates[t]
        return (rate_f / rate_t)

    # --- conversão & formato ---
    def converter(self, valor: Decimal, de: str, para: str) -> Decimal:
        """Converte valor de 'de' para 'para' com arredondamento por moeda destino."""
        fator = self.get_rate(de, para)
        convertido = Decimal(valor) * fator
        return _quantize(convertido, para)

    def formatar(self, valor: Decimal, code: str, separador_milhar: bool = True) -> str:
        """Formata valor com símbolo e casas corretas (ex.: R$ 1.234,56)."""
        code = code.upper()
        arred = _quantize(Decimal(valor), code)
        places = _minor_units(code)

        # string numérica com ponto decimal
        s = f"{arred:.{places}f}"
        inteiro, _, frac = s.partition(".")
        if separador_milhar:
            inteiro = "{:,}".format(int(inteiro)).replace(",", ".")  # 1,234 -> 1.234 (pt-BR)
        if places > 0:
            s_local = f"{inteiro},{frac}"
        else:
            s_local = inteiro
        return f"{_symbol(code)} {s_local}"

    def parse(self, texto: str, code: str) -> Decimal:
        """Converte string local (ex.: 'R$ 1.234,56') em Decimal normalizado."""
        code = code.upper()
        t = texto.strip()
        # remove símbolo e espaços
        sym = _symbol(code)
        if t.startswith(sym):
            t = t[len(sym):].strip()
        # pt-BR: milhar '.' e decimal ','
        t = t.replace(".", "").replace(",", ".")
        valor = Decimal(t)
        return _quantize(valor, code)
