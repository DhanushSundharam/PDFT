import streamlit as st
from PyPDF2 import PdfReader
from translate import Translator
from langdetect import detect

def translate_text(text, target_language):
    try:
        translator = Translator(to_lang=target_language)
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        return None

def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        return None

def main():
    st.set_page_config(page_title="PDF Translator", page_icon=":globe_with_meridians:")
    st.header("PDF Translator")

    pdf_file = st.file_uploader("Upload PDF file", type=["pdf"])

    if pdf_file:
        pdf_text = ""
        pdf_reader = PdfReader(pdf_file)

        for page in pdf_reader.pages:
            pdf_text += page.extract_text()

        source_language = detect_language(pdf_text)

        if source_language:
            st.write(f"Detected Source Language: {source_language}")

            target_language = st.selectbox("Select Target Language:", ["en", "fr", "es", "de", "it", "ja","ta"])

            if st.button("Translate"):
                translated_text = translate_text(pdf_text, target_language)

                if translated_text:
                    st.subheader("Translated Text:")
                    st.write(translated_text)
                else:
                    st.warning("Translation failed. Please try again.")
            else:
                st.warning("Click the 'Translate' button to perform the translation.")
        else:
            st.warning("Language detection failed. Please check the input text.")

if __name__ == "__main__":
    main()
