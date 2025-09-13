# SmartFinanancialControl
# Sistema Financeiro Desktop

💡This system uses python with tkint for UI presentation and SQLite to Database.

## Como executar

```bash
cd src
python main.py

smartFinancial/
├── data/
│   └── financeiro.db
├── models/
│   └── cliente.py
├── presenters/
│   └── cliente_presenter.py
├── views/
│   └── cliente_view.py
├── db.py
└── main.py
  # Documentação básica do projeto

```

* abrir uma notificação;
* soma de entrada e valor total;
* lembrete com notificação;
* Os usuários em abertos devem ser notifificados,
* Fazer os gráficos dos rendimentos por mês;


https://www.sqlitetutorial.net/sqlite-data-types/

https://www.sqlitetutorial.net/sqlite-python/insert/

## About MPV Achitecture:

1. **VIEW**: This has resposabilies to  User Interface Layer;
2. **MODEL**: Is reponsabile for managing the date, and some business logic;
3. It is the layer of the middle about the Model and the View. 

**REFERENCE**
<br/>
On this reference we have some informations about Model View Present:
[DEV MEDIA](https://www.devmedia.com.br/o-padrao-mvp-model-view-presenter/3043)

## Anotations In English about smartfinancial

## Some Functions
* Make calculum about "parcelas" and juros every transaction

# Checklist de *Services* — Monólito **Python + SQLite + Tkinter/CustomTkinter**

## Núcleo de negócio

* [ ] **ClientesService** — CRUD, busca/filtros, validações (duplicidade nome+contato/email), foto (path)
* [ ] **UsuariosAuthService** — CRUD, login/logout, hash/salt de senha, política de senha, perfis (admin/operador/consulta)
* [ ] **EmprestimosService** — criar/editar, status (`ativo`/`quitado`/`atrasado`), validações (cliente existe, juros>0, parcelas>0)
* [ ] **ParcelasService** — gerar cronograma, atualizar status por datas, recomputar saldo após pagamentos parciais
* [ ] **PagamentosService** — registrar/estornar, conciliação com parcela, baixa parcial (principal × juros)

## Regras financeiras (cálculo)

* [ ] **AmortizacaoService** — geração PRICE e/ou SAC; parametrizações
* [ ] **JurosService** — juros mensal/diário, pró-rata em atraso/adiantamento
* [ ] **MultaMoraService** — multa (%) + juros de mora/dia; política configurável
* [ ] **MoedaService** — operar em centavos (inteiros), arredondamentos e formatação

## Relatórios & Dashboard

* [ ] **RelatoriosService** — fluxo de caixa mensal, carteira por status, inadimplência, exportar CSV/XLSX
* [ ] **DashboardService** — KPIs (ticket médio, % atraso, receita de juros, carteira ativa) e séries temporais (matplotlib)

## Preditivo (rendimentos & risco)

* [ ] **DatasetService (ETL interno)** — consolidar histórico de parcelas/pagamentos/juros; features (idade do empréstimo, % pago, histórico de atraso, sazonalidade)
* [ ] **ForecastService** — previsão mensal de **rendimentos/juros** e **entradas de caixa**; backtesting (janela móvel), MAE/MAPE
* [ ] **ScoreAtrasoService** — probabilidade de atraso por parcela/cliente; classes A/B/C de risco e impacto na projeção
* [ ] **SimuladorCenariosService** — “E se”: alterar juros, inadimplência, adiantamentos; recalcular projeções
* [ ] **ModelRegistryService** — versionar modelos, métricas, *drift*; persistir/carregar (ex.: `joblib`)

## Operação & Dados

* [ ] **BackupService (SQLite)** — backup/restore, verificação de integridade; `PRAGMA foreign_keys=ON`, WAL
* [ ] **ImportExportService** — importar CSV (clientes/emprestimos/parcelas/pagamentos) com validação/dry-run; exportações
* [ ] **SchedulerService** — tarefas diárias (atualizar status de parcelas, recomputar KPIs e previsões)
* [ ] **AuditoriaLogService** — trilha de ações (quem, quando, o quê) + erros

## Camada de aplicação (suporte à UI)

* [ ] **NavigationService** — roteamento entre telas (Clientes, Empréstimos, Parcelas, Pagamentos, Dashboard, Previsões)
* [ ] **FormsValidationService** — validação de inputs (datas, números, obrigatórios)
* [ ] **ChartService** — gráficos matplotlib embutidos; salvar PNG/PDF
* [ ] **ThemeService** — temas CustomTkinter (claro/escuro), espaçamentos, responsividade básica
* [ ] **StateService** — estado global (usuário logado, filtros, seleção ativa)

## Qualidade & Config

* [ ] **MigrationsService** — evolução do schema (scripts idempotentes), *seeds* (usuário admin)
* [ ] **ErrorsService** — mapa de exceções → mensagens amigáveis na UI
* [ ] **TestsService** — testes de cálculo (juros/multa/amortização), geração de parcelas, conciliação e relatórios
* [ ] **ConfigService** — arquivo único de configs (taxas padrão, políticas de atraso, caminhos de backup, tema)

## Ordem sugerida (enxuta)

1. Núcleo: Clientes → Usuários/Auth → Empréstimos → Parcelas → Pagamentos
2. Cálculos: Amortização → Juros → Multa/Mora → Moeda
3. Relatórios/Dashboard (+ ChartService)
4. Preditivo: Dataset → Forecast → Score → Simulador → ModelRegistry
5. Operação: Backup, Import/Export, Scheduler, Auditoria
6. UI: Navigation, Forms, Chart, Theme, State
7. Qualidade: Migrations, Errors, Tests, Config
