import streamlit as st
from Screape import (scrape_website, split_dom_content, clean_body_content, extract_body_content)
from parse import parse_with_ollama

st.header("IA")
st.title("Site para resumir sites")
url = st.text_input("Digite a URL do site: ")

if st.button("Resumir site"):
    st.write("Resumindo site...")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_body_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_body_content

    with st.expander("Ver conteúdo do site"):
        st.text_area("Conteúdo Site", cleaned_body_content, height=300)


if "dom_content" in st.session_state:
    parse_description = st.text_area("Descreva que informação quer extrair do site: ")

    if st.button("Extrair informação"):
        if parse_description:
            st.write("Extraindo conteúdo...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)