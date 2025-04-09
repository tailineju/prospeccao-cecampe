# 📞 Busca Ativa e Assessoria 

Aplicativo interativo desenvolvido para apoiar as ações de prospecção de escolas no âmbito do projeto -censura-, com foco no **monitoramento do financiamento público educacional**.

O sistema permite registrar chamadas telefônicas realizadas para escolas, verificar e confirmar dados existentes, coletar informações importantes sobre o PDDE (Programa Dinheiro Direto na Escola), e organizar agendamentos para conversas futuras com a equipe de assessoria.

## Acesse o app online

🔗 [https://prospeccao-cecampe.streamlit.app/](https://prospeccao-cecampe.streamlit.app/)


## Funcionalidades atuais

- Busca por nome da escola com exibição de dados (endereço, telefone, UEx etc.)
- Registro de ligações conforme roteiro estruturado
- Coleta de dados sobre conhecimento e recebimento do PDDE
- Agendamento de conversas futuras
- Armazenamento local em arquivos Excel (`ligacoes.xlsx` e `escolas.xlsx`)


## 🛠️ Requisitos para execução local

- Python 3.9 ou superior
- [Streamlit](https://streamlit.io/)
- Pandas
- Openpyxl

### Instale com:

```bash
pip install -r requirements.txt
```

### Execute localmente com:

```bash
streamlit run app.py
```

## Estrutura dos arquivos

- `app.py`: Código principal do app em Streamlit  
- `escolas.xlsx`: Base de dados com informações das escolas  
- `ligacoes.xlsx`: Registro de ligações realizadas  
- `requirements.txt`: Dependências do projeto

## 📌 Licença

Projeto de uso interno, adaptado às necessidades do projeto. 
**Uso autorizado apenas mediante consentimento da equipe responsável.**

