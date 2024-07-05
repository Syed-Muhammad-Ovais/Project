import streamlit as st
import pandas as pd

# Title and text content display
st.title("Text Display")
st.write("Write content")
st.text("Text content...")
st.markdown("# Markdown content")
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.title("Title content")
st.header("Header content")
st.subheader("Sub header content")
st.code("[i for i in range(1,10)]")

# Data display section
st.title("Data Display")
df = pd.DataFrame({
    "Col1": [1, 2, 3],
    "Col2": ['a', 'b', 'c']
})
st.write(df)
st.table(df)
st.json(df.to_dict())
st.metric('My metric', 42, 2)

# Media display section
st.title("Display Media")
st.video("https://youtu.be/_OVnXw2ldog?si=2qsVAd3WdTUAlRVH")

