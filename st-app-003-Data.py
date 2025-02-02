import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.image(
    "https://logowik.com/content/uploads/images/celanese-corporation1904.jpg",
    width=300
)

st.title(":orange[Demo Streamlit App to understand Data Formatting]")



df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")