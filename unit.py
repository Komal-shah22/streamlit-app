import streamlit as st
import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyCGWvA8m5WNtGOQVkD6fELMq-k585-W7PI")

st.markdown("""
    <style>
        .main { background-color: #f4f4f4; }
        .stButton button {
            background-color: #4CAF50 !important;
            color: white !important;
            font-size: 18px !important;
            padding: 10px 24px !important;
            border-radius: 8px !important;
        }
        .stTextInput, .stNumberInput, .stSelectbox {
            font-size: 16px !important;
        }
        .stSuccess {
            background-color: #d4edda !important;
            color: #155724 !important;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

def convert_units(amount: float, from_unit: str, to_unit: str) -> str:
    """Google Gemini API se unit conversion perform kare."""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        query = f"Convert {amount} {from_unit} to {to_unit}"
        response = model.generate_content(query)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

st.markdown("<h1 style='text-align: center; color: #2c3e50;'>🔄 Unit Converter</h1>", unsafe_allow_html=True)

unit_categories = {
    "📏 Length": ["meters", "kilometers", "miles", "feet", "inches", "centimeters"],
    "⚖️ Weight": ["grams", "kilograms", "pounds", "ounces"],
    "🌡️ Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "🍶 Volume": ["liters", "milliliters", "gallons", "cups"],
    "💱 Currency": ["USD", "EUR", "GBP", "PKR", "INR", "AED", "CAD", "AUD", "JPY"],
    "💾 Data Storage": ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes", "petabytes"]
}

category = st.selectbox("📌 Select a Category", list(unit_categories.keys()))

col1, col2 = st.columns(2)
from_unit = col1.selectbox("🔄 Convert From", unit_categories[category])
to_unit = col2.selectbox("➡️ Convert To", unit_categories[category])

amount = st.number_input("✍️ Enter Value", min_value=0.0, step=0.1)

if st.button("🚀 Convert Now"):
    if amount > 0:
        with st.spinner("🔄 Processing... Please wait!"):
            time.sleep(1) 
            result = convert_units(amount, from_unit, to_unit)
            if "❌ Error" in result:
                st.error(result)
            else:
                st.success(f"✅ {amount} {from_unit} = {result}")
    else:
        st.warning("⚠️ Please enter a value greater than 0.")







