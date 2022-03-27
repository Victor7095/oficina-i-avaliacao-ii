import streamlit as st


def form_movie():

    col1, col_Centered, col3 = st.columns([9, 5, 6])

    # Nome filme
    with col_Centered:
        # Nome filme
        st.write(f"Filme: ")

        # Avaliação
        st.write(f"Rating: ")

        # Gênero
        st.write(f"Gênero: ")

        # Ano
        st.write(f"Ano: ")

        # Sinopese
        st.write(f"Sinopese")


def main():
    st.set_page_config(layout="centered", page_icon="🎥",
                       page_title="Movies App")

    # Primeira área de interação
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

    col1, col2, col3 = st.columns([2, 1, 2])

    predict = col2.button("🔮Previsão🔮")

    st.markdown("")

    c01, c02 = st.columns(2)

    if predict:
        # Segunda área de interação
        html_assistidos = """
                <div style=padding: 15px;">
                <h3 style="color:white;text-align:center;">✅ Assistidos</h3>
                </div>
            """
        st.markdown(html_assistidos, unsafe_allow_html=True)

        # Percorre a lista de filmes assistidos pelo o usuário """
        for i in range(0, 3):
            # Passar lista de filmes assistidos pelo usuário
            # para captura dos dados referentes ao filme (nome, ano, gênero, etc.)
            st.markdown('---')
            form_movie()

        # Terceira área de interação
        html_recomendados = """
                <div style=padding:10px; margin-top:30px;">
                <h3 style="color:white;text-align:center;">👍 Recomendados</h3>
                </div>
            """
        st.markdown(html_recomendados, unsafe_allow_html=True)

        # Percorre a lista de filmes recomendados ao usuário
        for i in range(0, 3):
            # Passar lista de filmes recomendados ao usuário
            # para captura dos dados referentes ao filme (nome, ano, gênero, etc.)
            form_movie()
            st.markdown('---')


if __name__ == '__main__':
    main()
