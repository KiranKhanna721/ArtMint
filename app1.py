import streamlit as st     
import requests
from PIL import Image


def app():
    st.header("Mint an Omnichain NFT to Opensea")
    st.write("Input file for your NFT mint. It should be an image file of typr jpg/png/jpeg")
    filePath = st.file_uploader("Upload an image",type=["jpg", "jpeg", "png"])
    st.write("Name of your NFT")
    name = st.text_input("Enter name of your NFT")
    st.write("Description of your NFT")
    description = st.text_input("Enter the description of your NFT")
    st.write("Wallet addres that NFT will be minted to - optional. If empty, the NFT will be in the default Verbwire wallet.")
    recipientAddress  = st.text_input("Enter the wallet addres that NFT will be minted")
    allowPlatformToOperateToken = st.selectbox("Select", ["true","false"])
    st.write("Data to be minted in your NFT.")
    st.write("TTo make your minted data viewable as an attribute on Opensea, your input your data should be in the form - [{trait_type:TraitType1 value:TraitValue1}  {trait_type:TraitType2 value:TraitValue2}]. Note: If you do not care about viewing your NFT attributes on OpenSea you do not have to conform to this format.")
    data = st.text_input("Enter data to be minted in your NFT.")
    st.write("Blockchain on which NFT will be minted")
    chain = st.selectbox("Select blockchain on which NFT will be minted", ["goerli","bsc-testnet","fuji","mumbai", "arbitrum-goerli","ethereum","optimism-goerli","fantom-testnet","bsc","avalanche","polygon","arbitrum","optimism","fantom"])
    if not filePath:
        st.warning("Please upload you file.")
    if not name:
        st.warning("Please enter your name.")
    if not description:
        st.warning("Please enter your description.")
    if not chain:
        st.warning("Please select you chain.")
    else:
        submit_button = st.button("Submit")
        if submit_button:
            url = "https://api.verbwire.com/v1/nft/mint/quickMintFromFile"
            image = Image.open(filePath)
            file_extension = filePath.type.split("/")[-1]
            save_location = "1."+file_extension
            image.save(save_location)
            files = {"filePath": (save_location, open(save_location, "rb"), "image/"+file_extension)}
            payload = {
                "allowPlatformToOperateToken": allowPlatformToOperateToken,
                "chain": chain,
                "name": name,
                "recipientAddress": recipientAddress,
                "data": data,
                "description": description
                
            }
            headers = {
                "accept": "application/json",
                "X-API-Key": "sk_live_69db9c79-e3c0-4467-a77b-8c143e304c9c"
            }
            response = requests.post(url, data=payload, files=files, headers=headers)
            st.write(response.text)