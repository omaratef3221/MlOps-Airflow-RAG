import streamlit as st
import pandas as pd
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from scripts.perform_search import perform_search
import warnings
warnings.filterwarnings('ignore')

# Load data and FAISS index
csv_path = './data/raw_movies.csv'
data = pd.read_csv(csv_path)

st.title("RAG System - Movie Search")
query = st.text_input("Enter your query:")

if query:
    indices, distances = perform_search(query)
    results = data.iloc[indices[0]].reset_index()
    st.write(results)
