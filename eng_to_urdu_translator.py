import streamlit as st
from googletrans import Translator

# Page settings
st.set_page_config(page_title="English to Urdu Translator", layout="centered")
st.title("English to Urdu Translator")
st.markdown("Type your English text below and get the Urdu translation instantly!")

# Input box
text = st.text_area("Enter English Text Here", height=150)

# Translate
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some English text first.")
    else:
        with st.spinner("Translating..."):
            translator = Translator()
            translated = translator.translate(text, dest='ur')
            st.success("Translation Successful!")
            st.subheader("Urdu Translation")
            st.markdown(f"{translated.text}")




st.markdown("---")
