import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados')
    
    
    with st.form(key='insert'):
        nome_completo = st.text_input(label='Insira o nome:')
        cpf = st.number_input(label='digite seu CPF', format='%d')
        data_nasc = st.date_input(label='insira sua data de nascimento')
        telefone = st.text_input(label= 'insira seu telefone')
        email = st.text_input(label= 'insira seu e-mail')
        senha = st.text_input(label= 'digite sua senha:' , type='password')

        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(nome_completo, int(cpf), data_nasc, telefone, email, senha)
            st.success('Cliente incluido com sucesso')
