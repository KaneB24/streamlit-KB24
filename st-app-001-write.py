import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

st.title("Streamlit App practice on Formatting text on Layout")

df=pd.read_csv("data/titanic.csv")

# st.write(df.Sex.value_counts())

# st.dataframe(df.Sex.value_counts(),height=100, width=150)

col1, col2 =st.columns([0.9,0.3])

col2.write(df.Sex.value_counts(),height=100, width=100)

# ax=plt.subplot()

# ax=df.Sex.value_counts().plot(kind='bar',title='Bar Graph')

dc = {"a" : 10 , "b" : 20 , "c" : 30}
fig , ax = plt.subplots()
# ax.scatter(np.arange(5) , np.arange(5) ** 2)
ax=df.Sex.value_counts().plot(kind='bar',title='Titanic Survivors by Gender',color='orange',xlabel="Gender",ylabel="Count")

col1.write(fig)

# st.write(st.altair_chart)

