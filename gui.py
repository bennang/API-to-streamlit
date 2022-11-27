import streamlit as st
from main import image, description

st.set_page_config(layout='wide')

col1, col2, col3 = st.columns([0.75, 1.5, 0.75])

with col2:
    st.header("Astronomy Picture of the Day")
    st.image(image)
    st.text("Description")
    st.write(description)



