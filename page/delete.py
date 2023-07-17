import streamlit as st
import controller.cliente as cliente
import services.database as db

def deletar():
    st.title('deletar dados')
    
    with st.form(key='delete'):
        cpf = st.number_input(label='digite seu CPF', format='%d')
        buttom_submit = st.form_submit_button('deletar')

    if buttom_submit:
        cliente.deletar(cpf)
        st.success('cliente excluído com sucesso')
