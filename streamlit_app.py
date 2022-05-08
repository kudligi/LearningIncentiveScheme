import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

threshold = st.slider("Time involvement", 0, 100, 5)

def time_val(x):
  m = 100 / threshold
  if x >= threshold:
    return 100
  return m * x

vec_time_val = np.vectorize(time_val)

time_x = np.arange(100)

time_source = pd.DataFrame({
  'time' : time_x,
  'time_score' : vec_time_val(time_x)
})

st.line_chart(time_source)

with plt.xkcd():
  fig = plt.figure()
  ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
  ax.spines.right.set_color('none')
  ax.spines.top.set_color('none')
#   ax.set_xticks([])
#   ax.set_yticks([])
#   ax.set_ylim([-30, 10])

  data = vec_time_val

#   ax.annotate(
#   'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
#   xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

  ax.plot(data)

  ax.set_xlabel('time')
  ax.set_ylabel('time score')
  fig.text(
  0.5, 0.05,
  '"Stove Ownership" from xkcd by Randall Munroe',
  ha='center')
  
  st.pyplot(fig)
  

"""
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write("Here's our first attempt at using data to create a table:")
st.write(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

if st.checkbox('Show dataframe'):
    chart_data2 = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data2
    
    
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)



left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
    'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
"""
