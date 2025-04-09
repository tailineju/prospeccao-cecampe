
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Registro de Ligações", layout="wide")
st.title("📞 Registro de Ligações com Escolas")

# Carregar dados
escolas = pd.read_excel("escolas.xlsx")
ligacoes = pd.read_excel("ligacoes.xlsx")

# Seleção da escola
st.sidebar.header("🔍 Buscar Escola")
nome_busca = st.sidebar.text_input("Digite o nome da escola ou parte do nome:")
escolas_filtradas = escolas[escolas["Nome da Escola"].str.contains(nome_busca, case=False, na=False)]

if not escolas_filtradas.empty:
    escola = escolas_filtradas.iloc[0]
    st.subheader(f"🏫 {escola['Nome da Escola']}")
    st.write(f"**Endereço:** {escola['Endereço']}")
    st.write(f"**Telefone:** {escola['Telefone']}")
    st.write(f"**Diretor:** {escola['Diretor']}")
    st.write(f"**Tem UEx?** {escola['Tem UEx']}")

    with st.form("form_ligacao"):
        st.write("### 📋 Formulário da Ligação")
        data = st.date_input("Data da ligação", value=datetime.today())
        quem_ligou = st.text_input("Quem ligou?")
        resultado = st.selectbox("Resultado da chamada", ["", "Não atendeu", "Número não existe/não é da escola", 
                                                           "O número é da escola, mas o diretor não pode atender agora", 
                                                           "O número é da escola e o diretor pode atender agora"])
        
        respondente = st.selectbox("Vínculo do respondente com a escola", ["", "Diretor", "Professor", "Funcionário", "Membro comunidade", "Servidor da Seduc/prefeitura"])

        conhece_pdde, recebeu_pdde, programas, razao_nao_recebeu = "", "", "", ""
        if respondente and respondente != "Servidor da Seduc/prefeitura":
            conhece_pdde = st.radio("Conhece o PDDE?", ["Sim", "Não"])
            if conhece_pdde == "Sim":
                recebeu_pdde = st.radio("A escola já recebeu recursos do PDDE?", ["Sim", "Não", "Não sei"])
                if recebeu_pdde == "Sim":
                    programas = st.text_input("Quais programas? Ano/período")
                    razao_nao_recebeu = st.text_input("Por que razão deixou de receber?")
        
        tem_uex = st.selectbox("A escola tem Unidade Executora (UEx)?", ["", "Sim", "Não", "Não sei"])
        agendamento = st.radio("Podemos agendar uma conversa com a assessoria?", ["Sim", "Não"])
        motivo_nao_agendou = ""
        if agendamento == "Não":
            motivo_nao_agendou = st.text_input("Se não, por que?")
        observacoes = st.text_area("Observações gerais")

        submitted = st.form_submit_button("💾 Salvar ligação")
        if submitted:
            nova_ligacao = {
                "ID": len(ligacoes) + 1,
                "Escola_ID": escola["ID"],
                "Data": data,
                "Quem Ligou": quem_ligou,
                "Resultado": resultado,
                "Respondente": respondente,
                "Conhece PDDE": conhece_pdde,
                "Recebeu PDDE?": recebeu_pdde,
                "Programas": programas,
                "Razão não recebe PDDE": razao_nao_recebeu,
                "Tem UEx": tem_uex,
                "Agendamento": agendamento,
                "Por que não agendou?": motivo_nao_agendou,
                "Observações": observacoes
            }
            ligacoes = pd.concat([ligacoes, pd.DataFrame([nova_ligacao])], ignore_index=True)
            ligacoes.to_excel("ligacoes.xlsx", index=False)
            st.success("✅ Ligação registrada com sucesso!")
else:
    st.warning("Digite um nome de escola válido para começar.")
