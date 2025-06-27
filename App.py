import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('diamond_price_model.pkl')

st.title("Diamond Price Predictor")

# Input fields
carat = st.number_input('Carat', min_value=0.0, max_value=5.0, step=0.01)
depth = st.number_input('Depth', min_value=50.0, max_value=70.0, step=0.1)
table = st.number_input('Table', min_value=50.0, max_value=70.0, step=0.1)
x = st.number_input('X (Length)', min_value=0.0, step=0.1)
y = st.number_input('Y (Width)', min_value=0.0, step=0.1)
z = st.number_input('Z (Height)', min_value=0.0, step=0.1)

# Categorical inputs
cut = st.selectbox('Cut', ['Fair', 'Good', 'Ideal', 'Premium', 'Very Good'])
color = st.selectbox('Color', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
clarity = st.selectbox('Clarity', ['I1', 'SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2', 'IF'])

# Generate one-hot encoded input in same order as training
def encode_inputs(cut, color, clarity):
    cut_vals = ['Fair', 'Good', 'Ideal', 'Premium', 'Very Good']
    color_vals = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
    clarity_vals = ['I1', 'IF', 'SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2']
    
    cut_encoded = [1 if c == cut else 0 for c in cut_vals]
    color_encoded = [1 if c == color else 0 for c in color_vals]
    clarity_encoded = [1 if c == clarity else 0 for c in clarity_vals]
    
    return cut_encoded + color_encoded + clarity_encoded

# Predict
if st.button('Predict Price'):
    size = x * y * z
    features = [carat, depth, table, x, y, z, size] + encode_inputs(cut, color, clarity)
    price = model.predict([features])[0]
    st.success(f"Estimated Diamond Price: ${price:,.2f}")
