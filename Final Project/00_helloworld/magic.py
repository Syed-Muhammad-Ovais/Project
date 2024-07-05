import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Display the document title and some markdown text
st.markdown('''
# This is the document title

This is some _markdown_.
''')

# Create and display a dataframe
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': list('abc')})
st.write(df)  # 👈 Draw the dataframe

# Display a string and the value of a variable
x = 100
st.write('x', x)  # 👈 Draw the string 'x' and then the value of x

# Create and display a histogram using Matplotlib
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=30)
st.pyplot(fig)  # 👈 Draw a Matplotlib chart

# Display another markdown title
st.markdown('# Pakistan zinda bad')

# Display the document title and some markdown text again
st.markdown('''
# This is the document title

This is some _markdown_.
''')
