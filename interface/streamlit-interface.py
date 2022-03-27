import streamlit as st
from PIL import Image


def form_movie():
    with st.form(key="form_movies"):
        # Nome filme
        st.write()

        # Avaliação
        st.write()

        # Gênero
        st.write()

        # Ano
        st.write()

        # Sinopese
        st.write(descricao)


def main():
    st.set_page_config(layout="centered", page_icon="🎥",
                       page_title="Movies App")

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

        userId = st.text_input(
            "Informe o ID do usuário que você deseja prevê as recomendações：")

        col1, col2, col3 = st.columns([6, 3, 6])

        predict = col2.button("🔮Previsão🔮")

    st.markdown("")

    # Segunda área de interação
    html_temp = """
            <div style=padding:15px">
            <h3 style="color:white;text-align:center;">✅ Assistidos</h3>
            </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    with st.form(key="list_rating_movies"):
        """ Percorre a lista de filmes assistidos pelo o usuário """
        for i in range(len()):
            """ Passar lista de filmes assistidos pelo usuário 
            para captura dos dados referentes ao filme (nome, ano, gênero, etc.)"""
            form_movie()

    st.markdown("")

    # Terceira área de interação
    html_temp = """
            <div style=padding:10px">
            <h3 style="color:white;text-align:center;">👍 Recomendados</h3>
            </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    with st.form(key="list_recommendation_movies"):
        """ Percorre a lista de filmes recomendados ao usuário """
        for i in range(len()):
            """ Passar lista de filmes recomendados ao usuário 
            para captura dos dados referentes ao filme (nome, ano, gênero, etc.)"""
            form_movie()


if __name__ == '__main__':
    main()
