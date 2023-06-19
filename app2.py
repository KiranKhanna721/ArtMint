import streamlit as st     
import requests
from PIL import Image


def app():
    st.header("Understanding holdings of a particular wallet of NFT on Opensea")
    st.write("walletAddress")
    walletAddress = st.text_input("Enter name of your walletAddress")
    st.write("Blockchain to search")
    chain = st.selectbox("Select blockchain", ["ethereum"])
    submit_button = st.button("Submit")
    if submit_button:
        if not walletAddress:
            st.warning("Please enter your wallet address.")
        else:
            url = "https://api.verbwire.com/v1/nft/data/owned?walletAddress="+walletAddress+"&chain=ethereum"
            headers = {
                "accept": "application/json",
                "X-API-Key": st.secrets["api_key"]
            }
            response = requests.get(url, headers=headers)
            st.write("Get all NFTs owned by a wallet address")
            st.write(response.text)
            st.write("-------------------------------------------------------------------------------------------")
            st.write("Get all NFTs created by a wallet address")
            url1 = "https://api.verbwire.com/v1/nft/data/created?walletAddress="+walletAddress+"&chain=ethereum"
            response1 = requests.get(url1, headers=headers)
            st.write(response1.text)
            st.write("-------------------------------------------------------------------------------------------")
            st.write("Get all transactions by a wallet address")
            url2 = "https://api.verbwire.com/v1/nft/data/transactions?walletAddress="+walletAddress+"&chain=ethereum"
            response2 = requests.get(url2, headers=headers)
            st.write(response2.text)
