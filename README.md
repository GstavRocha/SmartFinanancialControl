# SmartFinanancialControl

financeiro_desktop/
├── src/
│   ├── __init__.py                 # Arquivo vazio para indicar pacote
│   ├── main.py                     # Ponto de entrada da aplicação
│   ├── db.py                       # Funções de inicialização e acesso ao banco
│   ├── calculos.py                 # Funções de saldo, fluxo, devedores
│   ├── ui.py                       # Interface Tkinter (ou outra)
│   └── graficos.py                 # Funções para gerar os gráficos
│
├── data/
│   └── financeiro.db               # Arquivo do banco de dados (gerado em runtime)
│
├── assets/
│   └── icone.ico                   # Ícone opcional para o executável
│
├── dist/                           # Onde o PyInstaller vai gerar o exe
│
├── build/                          # Pasta de build do PyInstaller
│
├── requirements.txt                # Dependências (ex.: matplotlib)
└── README.md                       # Documentação básica do projeto
