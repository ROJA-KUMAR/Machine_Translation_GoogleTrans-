from googletrans import Translator
from languages import *
import streamlit as st

st.title("Language Translation App")
source_text =st.text_input("Enter the text to translate")
target_language = st.selectbox("select you target language",options=languages)
translate = st.button("Translate")
if translate:
    translator=Translator()
    out = translator.translate(source_text,dest=target_language)
    st.write(out.text)