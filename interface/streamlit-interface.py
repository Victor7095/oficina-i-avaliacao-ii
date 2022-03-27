import streamlit as st
from PIL import Image

st.set_page_config(layout="centered", page_icon="🎥", page_title="Movies App")

# Primeira área de interação
with st.container():

    st.title("🎥")
    html_title = """
        <h2 style="color:white;text-align:center;">Sistema de Recomendação de Filmes</h2>
    """
    st.title("").markdown(
        html_title, unsafe_allow_html=True)

    html_temp = """
        <div style="padding:10px">
        <h3 style="color:white;text-align:center;">🤔 Quem vai assistir?</h3>
        </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    test_user = st.text_input(
        "Informe o ID do usuário que você deseja prevê as recomendações：")

    col1, col2, col3 = st.columns([6, 3, 6])

    col2.button("🔮Previsão🔮")

st.markdown("")

with st.container():

    html_temp = """
            <div style=padding:15px">
            <h3 style="color:white;text-align:center;">✅ Assistidos</h3>
            </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

st.markdown("")

with st.container():
    html_temp = """
            <div style=padding:10px">
            <h3 style="color:white;text-align:center;">👍 Recomendados</h3>
            </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
