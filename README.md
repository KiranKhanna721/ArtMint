# ArtMint

A Streamlit app for creating and exploring NFTs. It generates artwork with DALL·E and mints and browses NFTs through the Verbwire API.

## Features

| Page | File | What it does |
|------|------|--------------|
| NFT mint from Image in OpenSea | `app1.py` | Uploads an image and mints it as an NFT on a chosen blockchain (Goerli, BSC testnet, Mumbai, Ethereum and others) |
| Wallet holdings | `app2.py` | Lists the NFTs a wallet address owns and created |
| NFT collections | `app3.py` | Shows top OpenSea collections or searches collections by name |
| NFT Art Generation with DALL·E | `app4.py` | Generates artwork from a text description with the OpenAI image API |

Sign-up and login are stored in a local SQLite database (`data.db`).

## Configuration

The app reads API keys from Streamlit secrets. Create `.streamlit/secrets.toml`:

```toml
api_key = "YOUR_VERBWIRE_API_KEY"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
```

## Getting started

```bash
pip install -r requirements.txt
streamlit run app.py
```
