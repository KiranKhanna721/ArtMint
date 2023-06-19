import openai
import streamlit as st    
import os
import config


def generate_nft_artwork(description):
    prompt = f"Create an NFT artwork based on the description: {description}"
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256X256"
    )
    image_url = response['data'][0]['url']
    return image_url

def app():
    st.header("NFT Art Generation with DALL·E")
    openai.api_key = config.OPENAI_API_KEY 
    description = st.text_input("Description for a image you want to generate")
    artwork = generate_nft_artwork(description)
    st.write(artwork)
    st.image(artwork)
