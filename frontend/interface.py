import filtering
import streamlit as st
import pandas as pd
import sys
import httplib2
sys.path.append("lib")


def form_movie(movies, no_rating=False):

    col_poster, col_info = st.columns([7, 11])

    with col_poster:
        poster_url = str({movies['posterPath']})[2:-2]
        h = httplib2.Http()
        resp = h.request(poster_url, 'HEAD')
        if int(resp[0]['status']) < 400:
            st.image(poster_url, width=220)
        else:
            poster_url = 'https://i.pinimg.com/236x/67/63/15/676315f5a4fa3971f544adaffb793ac6.jpg'
            st.image(poster_url, width=220)

    # Nome filme
    with col_info:
        # Nome filme
        st.subheader(f"{movies['title']}")

        # Avaliação
        if no_rating:
            st.write(f"Avaliação geral: {movies['rating']}")
        else:
            st.write(f"Sua avaliação: {movies['rating']}")

        # Gênero
        st.write(f"Gênero: {movies['genres']}")

        # Lançamento
        st.write(f"Lançamento: {movies['releaseDate']}")

        # Sinopse
        st.write(f"Sinopse: {movies['overview']}")


def main():
    st.set_page_config(layout="centered", page_icon="🎥",
                       page_title="Movies App")

    # Primeira área de interação
    st.title("🎥")
    html_title = """
        <h1 style="color:white;text-align:center;">Filmetragem</h1>
        <h2 style="color:white;text-align:center;">Sistema de Recomendação de Filmes</h2>
    """
    st.title("").markdown(
        html_title, unsafe_allow_html=True)

    html_temp = """
        <div style="padding:10px">
        <h3 style="color:white;text-align:center;">Quem vai assistir? 🤔</h3>
        </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    user_id = st.select_slider(
              "Informe o ID do usuário do qual você deseja ver os filmes assistidos e prever as recomendações：",
              options=filtering.all_users)

    col1, col2, col3 = st.columns([2, 1, 2])

    if col2.button("Previsão 🔮"):
        df_recommended = filtering.recommend(user_id)
        df_watched_movies = filtering.watched_movies(user_id)

        # Segunda área de interação
        html_assistidos = """
                <div style=padding: 15px;">
                <h3 style="color:white;text-align:center;">Assistidos ✅</h3>
                <h5 style="color:white;text-align:center;">7 mais bem avaliados</h5>
                </div>
            """
        st.markdown('---')
        st.markdown(html_assistidos, unsafe_allow_html=True)

        user_watched_movies = df_watched_movies[:7]

        # Percorre a lista de filmes assistidos pelo usuário
        for i in range(len(user_watched_movies)):
            movies = user_watched_movies.loc[i]
            st.markdown('---')
            form_movie(movies)

        # Terceira área de interação
        html_recomendados = """
                <div style=padding:10px; margin-top:30px;">
                <h3 style="color:white;text-align:center;">Recomendados 👍</h3>
                <h5 style="color:white;text-align:center;">7 mais bem recomendados</h5>
                </div>
            """
        st.markdown('---')
        st.markdown(html_recomendados, unsafe_allow_html=True)

        five_recommended = df_recommended[:7]

        # Percorre a lista de filmes recomendados ao usuário
        for i in range(len(five_recommended)):
            movies = five_recommended.loc[i]
            st.markdown('---')
            form_movie(movies, True)


if __name__ == '__main__':
    main()
