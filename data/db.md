## Estrutura do Banco de Dados

```mermaid
classDiagram
    class clientes
    clientes: +int idCliente
    clientes: +varchar nomeCliente
    clientes: +varchar contato
    clientes: +varchar email
    clientes: +float saldoDevedor
    clientes: +int taxaJuros
    clientes: +date diaPagamento
    clientes: +date vencimento
    clientes: +timestamp atualizadoEm

    class caixa
    caixa: +int idCaixa
    caixa: +float saldoCaixa
    caixa: +float taxtaProlabore
    caixa: +date timeStamp

```