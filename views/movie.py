# Import libraries
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
page_title = "Genre Insight"
page_icon = "📊"
st.set_page_config(page_title=page_title, page_icon=page_icon)
st.title(f'📊 {page_title}')
st.write(':blue[***Discover Top Performing Movie Genres***]')
st.write(" This app shows a simple demonstration of an interactive movie data explorer that allow users to adjust "
         "parameter through interactive widgets and observe the intuitive visualization in real-time.")
st.info('🛈 Data Source: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)')
st.info('🛈 This app is an adapted version of following application: '
        '[GitHub](https://github.com/dataprofessor/movies-explorer)')

# Load data - Read CSV into a Pandas DataFrame
df = pd.read_csv('movies_genres_summary.csv')
df.year = df.year.astype('int')

# Genres selection - Create dropdown menu for genre selection
genres_list = df.genre.unique()
st.subheader('Select Genres:')
genres_selection = st.multiselect('Select genres', genres_list,
                                  ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'],
                                  label_visibility='collapsed')

# Year selection - Create slider for year range selection
st.subheader('Select Duration:')
year_selection = st.slider('Select year duration', 1984, 2017, (2000, 2017), label_visibility='collapsed')
year_selection_list = list(np.arange(year_selection[0], year_selection[1] + 1))

# Subset data - Filter DataFrame based on selections
df_selection = df[df.genre.isin(genres_selection) & df['year'].isin(year_selection_list)]
reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)
reshaped_df = reshaped_df.sort_values(by='year', ascending=False)

st.subheader('Movies Data')
# Editable DataFrame - Allow users to make live edits to the DataFrame
df_editor = st.data_editor(reshaped_df, height=212, use_container_width=True,
                           column_config={"year": st.column_config.TextColumn("Year")},
                           num_rows="dynamic")

# Data preparation - Prepare data for charting
df_chart = pd.melt(df_editor.reset_index(), id_vars='year', var_name='genre', value_name='gross')

st.subheader('Visualization')
# Display line chart
chart = alt.Chart(df_chart).mark_line().encode(
    x=alt.X('year:N', title='Year'),
    y=alt.Y('gross:Q', title='Gross earnings ($)'),
    color='genre:N'
).properties(height=320)
st.altair_chart(chart, use_container_width=True)
