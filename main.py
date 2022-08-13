#Import the required Libraries

import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import requests
import json

# json


# Add a title and intro text
st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')

# Create file uploader object
selected = st.text_input("", "Search...")
button_clicked = st.button("OK")
print(button_clicked)

# Check to see if a file has been uploaded
if button_clicked:

    url = 'https://new-supur-backend.herokuapp.com/predictionSearch'
    myobj = {"SearchedString" : selected}
    json_object = json.dumps(myobj, indent = 4) 
    x = requests.post(url, data = json_object)
    res = dict(eval(x.text))

    # Create a section for matplotlib figure
    st.header('Plot of Data')

    x = res['Years']
    y = res['Performance']

    df = pd.DataFrame({"Year" : x, "Performance" : y})
    fig = go.Figure()
    fig.add_scattergl(x=df['Year'], y=df['Performance'], line={'color': 'black'})
    fig.add_scattergl(x=df.Year.where(df.Year>2020), y=df['Performance'], line={'color': 'red'})

    
    st.plotly_chart(fig, use_container_width=True)