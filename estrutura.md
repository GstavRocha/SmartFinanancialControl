.
├── assets
├── build
├── data
│   ├── db.md
│   ├── financeiro.db
│   ├── __init__.py
│   ├── inserts_example.py
│   └── __pycache__
├── Database_Manager.py
├── dist
├── estrutura.md
├── main.py
├── models
│   ├── clientes.py
│   ├── DAO_utils.py
│   ├── emprestimos.py
│   ├── __init__.py
│   ├── pagamentos.py
│   ├── parcelas.py
│   ├── __pycache__
│   │   ├── clientes.cpython-310.pyc
│   │   ├── DAO_utils.cpython-310.pyc
│   │   ├── emprestimos.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── pagamentos.cpython-310.pyc
│   │   ├── parcelas.cpython-310.pyc
│   │   ├── query_util.cpython-310.pyc
│   │   └── usuarios.cpython-310.pyc
│   ├── query_util.py
│   ├── usuarios.py
│   └── validators
│       ├── date_validation.py
│       ├── __pycache__
│       │   ├── date_validation.cpython-310.pyc
│       │   └── status_validation.cpython-310.pyc
│       └── status_validation.py
├── presenters
├── __pycache__
│   └── Database_Manager.cpython-310.pyc
├── README.md
├── requeriments.txt
├── seed.py
├── services
│   ├── amortizacao.py
│   ├── auditoria.py
│   ├── backup.py
│   ├── chart.py
│   ├── clientes.py
│   ├── config.py
│   ├── data.py
│   ├── emprestimos.py
│   ├── forecast.py
│   ├── forms.py
│   ├── __init__.py
│   ├── juros.py
│   ├── migrations.py
│   ├── models.py
│   ├── moedas.py
│   ├── navigation.py
│   ├── pagamentos.py
│   ├── parcelas.py
│   ├── __pycache__
│   │   ├── clientes.cpython-310.pyc
│   │   ├── emprestimos.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── pagamentos.cpython-310.pyc
│   │   ├── parcelas.cpython-310.pyc
│   │   └── usuario.cpython-310.pyc
│   ├── relatorio.py
│   ├── scheduler.py
│   ├── score.py
│   ├── simulador_cenario.py
│   ├── state.py
│   ├── test.py
│   ├── theme.py
│   ├── usuario.py
│   └── validators
│       ├── DTOS.py
│       ├── execptionsp.py
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── execptionsp.cpython-310.pyc
│       │   ├── __init__.cpython-310.pyc
│       │   └── validacao.cpython-310.pyc
│       └── validacao.py
└── views
    ├── assets
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   └── __init__.cpython-310.pyc
    │   └── styles
    │       ├── collors.py
    │       ├── __init__.py
    │       └── __pycache__
    │           ├── collors.cpython-310.pyc
    │           └── __init__.cpython-310.pyc
    ├── clientes_view.py
    ├── components
    │   ├── __init__.py
    │   ├── table.py
    │   └── toolbar.py
    ├── dashboard.py
    ├── __ini__.py
    ├── login.py
    ├── pagamentos_view.py
    ├── parcelas_view.py
    └── __pycache__
        └── login.cpython-310.pyc

22 directories, 86 files


Perfeito! Com essa estrutura, o **JurosService** deve ficar em `services/juros.py` e ser um serviço puro de cálculo (sem I/O de GUI), usado por `emprestimos.py`, `parcelas.py`, `pagamentos.py`, `amortizacao.py` e `relatorio.py`. Abaixo estão as abordagens essenciais para fazê-lo bem e “à prova de futuro”.

# 1) Escopo e responsabilidades

* **Entrada**: valores, datas e taxas (ao mês/ano/dia), tipo de amortização, políticas de atraso.
* **Saída**: juros apurados, multa, correção (opcional), taxa efetiva, fatores (acumulação), e utilitários para conversão de taxas.
* **Sem efeitos colaterais**: não tocar em DB; quem persiste é o layer de DAO/Services de negócio.
* **Determinístico e transparente**: toda regra documentada e coberta por testes.

# 2) Modelagem de cálculos (o que o serviço precisa suportar)

1. **Juros simples** (educacional/avulso).
2. **Juros compostos** (padrão para empréstimos).
3. **Conversões de taxa**: a.a. ↔ a.m. ↔ a.d., **nominal ↔ efetiva**.
4. **Pro-rata por dias**: base **ACT/365**, **ACT/360** ou **30/360** (selecione por configuração).
5. **Amortização** (em apoio ao `services/amortizacao.py`):

   * **Price (Francês)** – parcelas fixas.
   * **SAC** – amortização constante, parcela decrescente.
   * **Americano** – amortiza só no final.
6. **Atraso**:

   * **Multa moratória fixa** (ex.: 2%).
   * **Juros de mora** (ex.: 1% a.m. pro-rata/dia).
   * Política de **carência** e **período de tolerância** (grace period).
7. **Liquidação antecipada**:

   * Cálculo do **saldo devedor** + **abatimento de juros futuros** conforme política.

# 3) Precisão e arredondamento (crítico para finanças)

* Use **`decimal.Decimal`** com `getcontext(prec=28)` e **arredondamento bancário** (`ROUND_HALF_EVEN`).
* Padronize casas decimais: **2** para moeda, **8** para taxas/fatores.
* Arredonde **apenas** no momento de expor/registrar valores (evite arredondar a cada passo do cálculo).

# 4) Datas e contagem de dias

* Centralize regra de contagem em um **enum** (ex.: `BaseContagem.ACT365 | ACT360 | B30360`).
* Funções utilitárias:

  * `dias_entre(data_ini, data_fim, base)` → dias e fração de período.
  * `meses_entre` quando a régua for mensal (útil para Price/SAC).
* Trate **ano bissexto**, **finais de semana** (apenas para política de cobrança, se aplicável).

# 5) Integração com Parcelas & Pagamentos

* `ParcelasService` chama `JurosService` para:

  * Calcular **juros de período** de cada parcela.
  * Recalcular **juros de atraso** na consulta do boleto/tela.
* `PagamentosService`:

  * Ao registrar pagamento, calcula **juros + multa + eventuais descontos** e devolve breakdown.
* `AmortizacaoService`:

  * Obtém **fator de acumulação** do `JurosService` e monta tabela (Price/SAC/Americano).

# 6) Configuração de políticas

* Centralize em `services/config.py` (ou `.env`) chaves como:

  * `JUROS_BASE_CONTAGEM` (ACT365/ACT360/30/360),
  * `MORA_A_M` (ex.: 0.01 = 1% a.m.),
  * `MULTA_MORATORIA` (ex.: 0.02 = 2%),
  * `ARREDONDAMENTO` (2 casas para BRL),
  * `POLITICA_ARREDONDAMENTO` (ROUND_HALF_EVEN).
* Permita **override por empréstimo** (campo na tabela `emprestimos`).

# 7) Validação e erros

* Reuse `services/validators/validacao.py` e exceções em `execptionsp.py`.
* Regras mínimas:

  * Taxa ≥ 0, valor principal > 0.
  * Data fim ≥ data início.
  * Proibir taxas simultâneas conflitantes (ex.: efetiva **e** nominal ao mesmo tempo).
* Mensagens claras (ex.: “Taxa mensal negativa não permitida”).

# 8) Testes (essenciais)

* **Unitários**: cada fórmula, cada base de contagem, cada política de atraso.
* **Golden tests**: tabela Price e SAC com casos conhecidos.
* **Pro-rata**: cenários atravessando anos bissextos.
* **Arredondamento**: garanta reprodutibilidade.

# 9) Interface pública sugerida (API do serviço)

Coloque algo assim em `services/juros.py`:

```python
from decimal import Decimal, getcontext, ROUND_HALF_EVEN
from datetime import date
from enum import Enum
from typing import Literal, Optional, Dict

getcontext().prec = 28
getcontext().rounding = ROUND_HALF_EVEN

class BaseContagem(Enum):
    ACT365 = "ACT/365"
    ACT360 = "ACT/360"
    B30360 = "30/360"

class JurosService:
    def __init__(
        self,
        base: BaseContagem = BaseContagem.ACT365,
        casas_moeda: int = 2,
        multa_moratoria: Decimal = Decimal("0.02"),   # 2%
        mora_am: Decimal = Decimal("0.01"),          # 1% a.m.
    ):
        self.base = base
        self.casas = casas_moeda
        self.multa = multa_moratoria
        self.mora_am = mora_am

    # ---------- Conversões de taxa ----------
    def efetiva_am_de_aa(self, taxa_aa: Decimal) -> Decimal:
        # (1+i_a.a.)^(1/12)-1
        return (Decimal(1) + taxa_aa) ** (Decimal(1)/Decimal(12)) - Decimal(1)

    def efetiva_aa_de_am(self, taxa_am: Decimal) -> Decimal:
        return (Decimal(1) + taxa_am) ** Decimal(12) - Decimal(1)

    def nominal_para_efetiva(self, nominal: Decimal, periodicidade: int) -> Decimal:
        # i_eff = (1 + i_nom/m)^m - 1
        return (Decimal(1) + nominal/Decimal(periodicidade))**Decimal(periodicidade) - Decimal(1)

    # ---------- Contagem de dias ----------
    def fracao_periodo(self, ini: date, fim: date) -> Decimal:
        if fim < ini:
            raise ValueError("data fim menor que data início")
        if self.base == BaseContagem.ACT365:
            dias = (fim - ini).days
            return Decimal(dias)/Decimal(365)
        if self.base == BaseContagem.ACT360:
            dias = (fim - ini).days
            return Decimal(dias)/Decimal(360)
        # 30/360 (Basileia)
        d1, m1, y1 = ini.day, ini.month, ini.year
        d2, m2, y2 = fim.day, fim.month, fim.year
        d1 = min(d1, 30)
        d2 = 30 if d2 == 31 and d1 == 30 else min(d2, 30)
        dias_30360 = (y2 - y1)*360 + (m2 - m1)*30 + (d2 - d1)
        return Decimal(dias_30360)/Decimal(360)

    # ---------- Juros simples / compostos ----------
    def juros_simples(self, principal: Decimal, taxa: Decimal, fracao: Decimal) -> Decimal:
        return (principal * taxa * fracao).quantize(Decimal(10) ** -self.casas)

    def juros_compostos(self, principal: Decimal, taxa_efetiva_periodo: Decimal, n_periodos: Decimal) -> Decimal:
        fator = (Decimal(1) + taxa_efetiva_periodo) ** n_periodos
        montante = principal * fator
        juros = montante - principal
        return juros.quantize(Decimal(10) ** -self.casas)

    # ---------- Atraso ----------
    def multa_atraso(self, principal_parcela: Decimal) -> Decimal:
        return (principal_parcela * self.multa).quantize(Decimal(10) ** -self.casas)

    def juros_mora_pro_rata(self, principal_parcela: Decimal, dias_atraso: int) -> Decimal:
        # Converte mora a.m. para a.d. efetiva (aprox. 30 dias/mês)
        taxa_ad = (Decimal(1) + self.mora_am) ** (Decimal(1)/Decimal(30)) - Decimal(1)
        fator = (Decimal(1) + taxa_ad) ** Decimal(dias_atraso)
        juros = principal_parcela * (fator - Decimal(1))
        return juros.quantize(Decimal(10) ** -self.casas)

    # ---------- Utilitário de breakdown ----------
    def calcular_atraso(self, valor_parcela: Decimal, venc: date, pago_em: date) -> Dict[str, Decimal]:
        if pago_em <= venc:
            return {"multa": Decimal("0.00"), "mora": Decimal("0.00"), "total": valor_parcela}
        dias = (pago_em - venc).days
        multa = self.multa_atraso(valor_parcela)
        mora = self.juros_mora_pro_rata(valor_parcela, dias)
        total = (valor_parcela + multa + mora).quantize(Decimal(10) ** -self.casas)
        return {"multa": multa, "mora": mora, "total": total}
```

> Observação: mantenha o serviço **agnóstico** ao tipo de amortização; quem define a sequência de períodos e o saldo devedor é o `AmortizacaoService`. O **JurosService** fornece apenas os **fatores e montantes de juros** para cada intervalo.

# 10) Fluxos típicos (como usar)

* **Montar tabela Price**:

  1. `AmortizacaoService` calcula parcela fixa com taxa efetiva a.m. (usa `efetiva_am_de_aa` se a taxa vier anual).
  2. Para cada mês, usa `juros_compostos` sobre o **saldo devedor** do período para obter a parte de juros; amortização = parcela − juros.
* **Consultar parcela em atraso**:

  * `JurosService.calcular_atraso(valor, venc, hoje)` → retorna multa, mora e total.
* **Quitar antecipado**:

  * Obter saldo devedor (amortização), **não** considerar juros futuros; se política permitir desconto, aplicar.

# 11) Onde plugar

* `services/emprestimos.py`: criação do contrato → define política (base de contagem, taxa, mora, multa).
* `services/parcelas.py`: geração e re-cálculo (chama `JurosService`).
* `services/pagamentos.py`: consolida multa/juros no ato do pagamento.
* `services/relatorio.py`: exibe breakdown com valores arredondados.
* `services/auditoria.py`: registre a política usada no cálculo (traço de auditoria).

Se quiser, já te entrego o **arquivo pronto** `services/juros.py` com essas funções e mais 3 testes unitários base (Price, SAC, atraso). Quer que eu gere o código completo com `Decimal`, enums e docstrings?

Depois do **JurosService**, o próximo passo ideal é o **AmortizacaoService**. Ele é o “motor” que usa as taxas/fatores do JurosService para montar o cronograma (tabela) do empréstimo e alimentar Parcelas/Pagamentos.

## Ordem sugerida (com motivo)

1. **AmortizacaoService** (Price, SAC, Americano)

   * Gera a **tabela de fluxo**: parcela, juros do período, amortização e saldo devedor por competência.
   * Saída vira insumo direto para criação de parcelas.

2. **ParcelasService**

   * Persiste as parcelas geradas pelo AmortizacaoService (DAO).
   * Recalcula **atraso** sob demanda usando JurosService (multa + mora pro-rata).

3. **PagamentosService**

   * Liquidação de parcelas (total/valor parcial), baixa, estorno, e conciliação.
   * Usa JurosService para compor acréscimos e descontos no ato do pagamento.

4. **RelatorioService** (ou aproveitar `relatorio.py`)

   * Extratos por cliente, DRE simplificada do portfólio, aging de parcelas.

5. **AuditoriaService**

   * Guarda a **política de cálculo** aplicada (base de contagem, taxas, arredondamento) para rastreabilidade.

---

## AmortizacaoService — escopo mínimo

* **Entradas**: principal, taxa (a.m. efetiva), número de parcelas, data inicial, sistema (`"PRICE" | "SAC" | "AMERICANO"`), carência (opcional).
* **Saída**: lista de períodos com `{n, data_venc, parcela, juros, amortizacao, saldo_devedor}`.

### Assinatura sugerida

```python
# services/amortizacao.py
from decimal import Decimal
from datetime import date
from typing import List, Literal, Dict

TipoAmort = Literal["PRICE", "SAC", "AMERICANO"]

class AmortizacaoService:
    def __init__(self, juros_service):
        self.j = juros_service  # injeção do JurosService

    def gerar_tabela(
        self,
        principal: Decimal,
        taxa_am: Decimal,
        n_meses: int,
        primeira_competencia: date,
        sistema: TipoAmort,
        carencia_meses: int = 0,
    ) -> List[Dict]:
        ...
```

### Critérios de aceite

* **PRICE**: parcela fixa (fórmula PMT), juros = saldo_anterior * taxa, amortização = parcela – juros.
* **SAC**: amortização = principal / n; parcela = amortização + juros; saldo decresce linear.
* **AMERICANO**: parcela = juros até a penúltima; última parcela = juros + principal.
* Saldo nunca negativo; diferenças residuais ≤ R$0,01 ajustadas na última parcela.
* Datas de vencimento: +1 mês sequencial (respeitar virada de mês).

---

## ParcelasService — pontos-chave

* `criar_por_tabela(emprestimo_id, tabela)` → insere em `parcelas`.
* `recalcular_atraso(id_parcela, hoje)` → usa `JurosService.calcular_atraso`.
* Valida **dupla geração** (idempotência por emprestimo_id).

---

## PagamentosService — pontos-chave

* `registrar_pagamento(id_parcela, valor_pago, data_pgto)`

  * Calcula multa+mora (JurosService) → compõe valor devido.
  * Aceita **pagamento parcial** (gera “remanescente/ajuste” ou marca parcialmente pago).
  * Atualiza status: `pendente` → `pago`/`parcial`/`atrasado`.
* `quitar_antecipada(emprestimo_id, data_ref)`

  * Usa saldo devedor (AmortizacaoService) e **remove juros futuros** conforme política.

---

## Validações & DTOs

* DTOs em `services/validators/DTOS.py` para entrada/saída dos serviços.
* Reaproveitar `execptionsp.py` para **ValidationError**, **DomainError**.
* Checagens: principal > 0, n_meses ≥ 1, taxa ≥ 0, datas válidas.

---

## Testes mínimos (unit)

* PRICE/SAC/AMERICANO com casos “golden”.
* Carência: 0 e >0.
* Ajuste de centavos na última parcela.
* Recalcular atraso (multa + mora) alinhado ao JurosService.

---

Se quiser, já monto o **esqueleto do AmortizacaoService** com a fórmula PMT, geração das competências mensais e integração pronta para o ParcelasService.
