import filtering
import streamlit as st
import pandas as pd
import sys
sys.path.append("lib")


def form_movie(movies):

    col1, col_Centered, col3 = st.columns([7, 5, 6])

    # Nome filme
    with col_Centered:
        # Nome filme
        st.write(f"Filme: {movies['title']}")

        # Avaliação
        st.write(f"Rating: {movies['rating']}")

        # Gênero
        st.write(f"Gênero: {movies['genres']}")

        # Ano
        st.write(f"Ano: {movies['releaseDate']}")


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

    user_id = st.number_input(
        "Informe o ID do usuário que você deseja vê os filmes assistidos e prevê as recomendações：", value=56)

    col1, col2, col3 = st.columns([2, 1, 2])

    if col2.button("🔮Previsão🔮"):
        df_recommended = filtering.recommend(user_id)
        df_watched_movies = filtering.watched_movies(user_id)

        # Segunda área de interação
        html_assistidos = """
                <div style=padding: 15px;">
                <h3 style="color:white;text-align:center;">✅ Assistidos ✅</h3>
                <h5 style="color:white;text-align:center;">5 mais bem avaliados</h5>
                </div>
            """
        st.markdown(html_assistidos, unsafe_allow_html=True)

        user_watched_movies = df_watched_movies[:5]

        # Percorre a lista de filmes assistidos pelo o usuário
        for i in range(len(user_watched_movies)):
            movies = user_watched_movies.loc[i]
            st.markdown('---')
            form_movie(movies)

        # Terceira área de interação
        html_recomendados = """
                <div style=padding:10px; margin-top:30px;">
                <h3 style="color:white;text-align:center;">👍 Recomendados 👍</h3>
                <h5 style="color:white;text-align:center;">5 mais bem recomendados</h5>
                </div>
            """
        st.markdown(html_recomendados, unsafe_allow_html=True)

        five_recommended = df_recommended[:5]

        # Percorre a lista de filmes recomendados ao usuário
        for i in range(len(five_recommended)):
            movies = five_recommended.loc[i]
            st.markdown('---')
            form_movie(movies)


if __name__ == '__main__':
    main()
