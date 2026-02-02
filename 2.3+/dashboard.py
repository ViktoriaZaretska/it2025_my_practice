import streamlit as st
import sqlite3
import pandas as pd

DB_NAME = "ias.db"


def load_data(query):
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


# --- Інтерфейс ---
st.title("Інформаційно-аналітична система реагування на інциденти")

st.subheader("Таблиця ресурсів")
resources_df = load_data("SELECT * FROM resources;")
st.dataframe(resources_df)

st.subheader("Розподіл ресурсів за статусом")
status_counts = resources_df["status"].value_counts()
st.bar_chart(status_counts)

st.subheader("Таблиця інцидентів")
incidents_df = load_data("SELECT * FROM incidents;")
st.dataframe(incidents_df)
