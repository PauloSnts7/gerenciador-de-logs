# LogsProject

## Descrição
Este projeto é um exemplo de **monitoramento e logging de erros em Python** utilizando as bibliotecas `loguru` e `sentry-sdk`.  
Ele registra logs críticos localmente e envia eventos de erro para o Sentry, permitindo acompanhar falhas em aplicações de forma remota.



## Funcionalidades

- Configuração de logging com `loguru` e `logging` do Python.  
- Integração com **Sentry** para envio de erros e exceções.  
- Registro de logs críticos usando `logging.critical()`.  
- Demonstração do envio de eventos para Sentry.


## Instalação

1. Clonar o repositório:
git clone https://github.com/SEU_USUARIO/LogsProject.git

2. Entrar na pasta do projeto:
cd LogsProject/src/apps

3. Criar e ativar um ambiente virtual:

python -m venv venv
.\venv\Scripts\activate   # Windows
# ou
source venv/bin/activate  # Linux/Mac

4. Instalar dependências:

pip install loguru sentry-sdk

--5. Como usar: 

6. Certifique-se de que o ambiente virtual está ativo.

7. Execute o script:

python logsProject.py

8. Você verá no console o log crítico:

CRITICAL:root:Quebou a aplicação

9. O Sentry tentará enviar o evento para monitoramento remoto.

Observações importantes
Substitua o DSN do Sentry pelo seu próprio caso queira usar sua conta.

Esse projeto é apenas um exemplo de integração de logging e monitoramento de erros, podendo ser expandido para aplicações reais.

Para adicionar mais logs, utilize logger.info(), logger.warning(), logger.error(), etc.

Autor
Paulo Ricardo dos Santos Junior
