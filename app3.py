import streamlit as st     
import requests


def app():
    st.header("NFT collection has been indexed on this platform.")
    search = st.text_input("Enter Search value")
    submit_button = st.button("Submit")
    if submit_button:
        if not search:
            st.write("Top Collection in Opensea for Ethereum")
            url = "https://api.verbwire.com/v1/nft/data/collections/all?chain=ethereum&limit=25&page=1&sortField=rank&sortInterval=allTime&sortDirection=ASC"
            headers = {
                "accept": "application/json",
                "X-API-Key": st.secrets["api_key"]
                }
            response = requests.get(url, headers=headers)
            st.write(response.text)
        else:
            st.write("Searched NFT collections")
            url1 = "https://api.verbwire.com/v1/nft/data/collections/search?searchString="+search+"&limit=25&page=1&sortField=rank&sortInterval=allTime&sortDirection=ASC"
            headers = {
                "accept": "application/json",
                "X-API-Key": "sk_live_69db9c79-e3c0-4467-a77b-8c143e304c9c"
            }
            response1 = requests.get(url1, headers=headers)
            st.write(response1.text)
