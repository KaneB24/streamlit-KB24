import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title(":orange[Demo Streamlit App to understand Charting]")

tit_df=pd.read_csv("data/titanic.csv")

df=pd.DataFrame(np.random.rand(10,2),columns=["Price","Diff"])

st.markdown("*Streamlit* is **really** ***cool***.")

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.write(df)

# st.write(tit_df.Sex.value_counts())

st.line_chart(tit_df.Sex.value_counts())

st.area_chart(df,x="Diff")