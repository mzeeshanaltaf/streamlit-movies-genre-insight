import streamlit as st

st.subheader('About')
with st.expander('Application'):
    st.markdown(''' Discover top performing Movie Genres of past years.''')
with st.expander('Technologies Used'):
    st.markdown(''' 
    * Pandas -- For Data wrangling
    * Altair -- For Chart plotting
    * Streamlit -- For application Front End
    ''')
with st.expander('Contact'):
    st.markdown(''' Any Queries: Contact [Zeeshan Altaf](mailto:zeeshan.altaf@gmail.com)''')
with st.expander('Source Code'):
    st.markdown(''' Source code: [GitHub](https://github.com/mzeeshanaltaf/)''')
with st.expander('Reference'):
    st.markdown(''' 
    * Movies data is taken from: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
    * This is an adapted version of following application: [GitHub](https://github.com/dataprofessor/movies-explorer)
    ''')
