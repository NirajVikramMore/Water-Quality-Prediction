import joblib
import streamlit as st
from datetime import date

model = joblib.load('model.pkl')


st.set_page_config(
    page_title = 'Water Quality Prediction',
    layout = 'wide'
)


st.title('Water Quality Prediction')


ph = st.number_input("Ph",min_value=0.00,max_value=14.00)
hardness = st.number_input("Hardness",min_value=117.12,max_value=276.39)
solids = st.number_input('Solids',min_value=320.94,max_value=44831.86)
chloramines = st.number_input('Chloramines',min_value=3.14,max_value=11.09)
sulfate = st.number_input('Sulfate',min_value=267.15,max_value=400.32)
conductivity =  st.number_input('Conductivity',min_value=191.64,max_value=655.87)
organic_carbon = st.number_input('Organic Carbon',min_value=5.32,max_value=23.29)
trihalomethanes = st.number_input('Trihalomethanes',min_value=26.61,max_value=106.69)
turbidity = st.number_input('Turbidity',min_value=1.84,max_value=6.09)

year = date.today().year

if st.button('Predict'):
    predictions = model.predict([[
        ph,
        hardness,
        solids,
        chloramines,
        sulfate,
        conductivity,
        organic_carbon,
        trihalomethanes,
        turbidity
    ]])

    output = int(predictions[0])

    if output == 1:
        st.write('Current Year : ',year)
        st.write("The water with given details is pure and potable enough to drink and meets the federal standards for domestic consumption.")
    else:
        st.write('Current Year : ', year)
        st.write("The water with specified details is impure, contaminated and non-potable. It may not be suitable for domestic consumption.")
