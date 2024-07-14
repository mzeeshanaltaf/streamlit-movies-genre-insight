# Import libraries
import streamlit as st

# --- PAGE SETUP ---
movie_page = st.Page(
    "views/movie.py",
    title="Movie Explorer",
    icon=":material/movie:",
    default=True,
)
about_page = st.Page(
    "views/about.py",
    title="About",
    icon=":material/info:",
)

pg = st.navigation({
    "Home": [movie_page],
    "About": [about_page],
                    })

pg.run()
