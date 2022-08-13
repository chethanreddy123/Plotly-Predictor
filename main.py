#Import the required Libraries

import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import requests
import json

# json


# Add a title and intro text
st.title('Predict the future performance of your suppliers :)')
st.subheader('Type in the company name correctly')

# Create file uploader object
selected = st.text_input("", "")
button_clicked = st.button("Click Here to Predict")
print(button_clicked)

# Check to see if a file has been uploaded
if button_clicked:

    url = 'https://new-supur-backend.herokuapp.com/predictionSearch'
    myobj = {"SearchedString" : selected}
    json_object = json.dumps(myobj, indent = 4) 
    x = requests.post(url, data = json_object)
    res = dict(eval(x.text))

    # Create a section for matplotlib figure
    st.header('Predicted Graph of %s'%(selected))

    x = res['Years']
    y = res['Performance']

    df = pd.DataFrame({"Year" : x, "Performance" : y})
    fig = go.Figure()
    fig.add_scattergl(x=df['Year'], y=df['Performance'], line={'color': 'blue'} , 
    name = "Recorded Performance" , text= "Performance")
    fig.add_scattergl(x=df.Year.where(df.Year>2020), y=df['Performance'], line={'color': 'pink'}, 
    name = "Predicted Performance", text = "Predicted Performance")

    fig.update_layout(
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    paper_bgcolor="LightSteelBlue",
    )
    


    
    st.plotly_chart(fig, use_container_width=True)