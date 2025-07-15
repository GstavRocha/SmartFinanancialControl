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