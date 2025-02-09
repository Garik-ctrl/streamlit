import streamlit as st
import csv

CSV_soubor="sample_books_data.csv"

st.header("Data Collection Form")
with st.form(key="knihy"):
    title= st.text_input("Název knihy")
    author= st.text_input("Zadej autora")
    genre=st.text_input("Zadej žánr knihy")
    publication_year= st.number_input("Rok publikace", min_value=1000, max_value=2025, step=5)
    rating= st.number_input("zadej hodnocení, nejméně je 1, nejvíce je 5", min_value=1, max_value=5, step=1)
    submit_button=st.form_submit_button("Odeslat")

if submit_button: #submit_button==True:
    if title and author and genre:
        with open(CSV_soubor, mode="a", encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerow([title,author, genre, publication_year, rating])
        st.success("Kniha byla zapsána")
    else:
        st.error("Chybí povinné údaje")

st.header("Zapsané knihy")
with open(CSV_soubor, mode="r", encoding="utf-8") as file:
    reader=csv.reader(file) #přečtení dat
    """
    data=[]
    for radky in reader:
        if any(radky):
            data.append(radky)
    """
    data=[radky for radky in reader if any(radky)]
    st.table(data)


