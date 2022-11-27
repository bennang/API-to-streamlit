import streamlit as st
import requests

url = "https://api.nasa.gov/planetary/apod?api_key=gayjcpVgykAyvyEFi67eEKNS63sJd8gh8B6UKXcd"

# Access the data
respond = requests.get(url)

# Convert to Dict, get the Title, image url & Description
contents = respond.json()
title = contents['title']
description = contents['explanation']
title = contents['title']
image_url = contents['hdurl']

# Extract the image
image = requests.get(image_url)
image = image.content
with open("apod.jpg", 'wb') as file:
    file.write(image)

# Write to Streamlit
col1, col2, col3 = st.columns([1, 1.5, 1])
st.title(title)
st.image(image)
st.write(description)





