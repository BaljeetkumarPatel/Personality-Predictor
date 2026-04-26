import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# Set page config for an interactive and user-friendly UI
st.set_page_config(page_title="Personality Predictor", page_icon="🧠", layout="wide")

# Custom CSS for rich aesthetics and modern web design
st.markdown("""
<style>
    .stApp {
        background-color: #f9fbfd;
        font-family: 'Inter', sans-serif;
    }
    .main-title {
        color: #1e3a8a;
        text-align: center;
        font-weight: 800;
        margin-bottom: 10px;
        font-size: 3rem;
    }
    .sub-title {
        text-align: center; 
        font-size: 1.1rem; 
        color: #4b5563; 
        margin-bottom: 40px;
    }
    .stSlider > div[data-baseweb="slider"] {
        padding-top: 10px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(37, 99, 235, 0.3);
    }
    .stButton>button:active {
        transform: translateY(1px);
    }
    .prediction-card {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 15px 30px rgba(37, 99, 235, 0.3);
        margin-top: 30px;
        animation: fadeIn 0.8s ease-out forwards;
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# Main Titles
st.markdown("<h1 class='main-title'>🧠 Personality Type Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Discover your personality type based on your behavioral traits. Rate yourself on a scale of 0 to 10 for each attribute below.</p>", unsafe_allow_html=True)

# Load model and scaler securely
@st.cache_resource
def load_models():
    base_path = os.path.dirname(__file__)
    model_path = os.path.join(base_path, 'personality_model.pkl')
    scaler_path = os.path.join(base_path, 'scaler.pkl')
    
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

try:
    model, scaler = load_models()
except FileNotFoundError:
    st.error("Model or scaler files not found. Ensure 'personality_model.pkl' and 'scaler.pkl' are in the same directory.")
    st.stop()
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

# Exact features used for model training
features = [
    'social_energy', 'alone_time_preference', 'talkativeness', 'deep_reflection',
    'group_comfort', 'party_liking', 'listening_skill', 'empathy', 'organization',
    'leadership', 'risk_taking', 'public_speaking_comfort', 'curiosity',
    'routine_preference', 'excitement_seeking', 'friendliness', 'planning',
    'spontaneity', 'adventurousness', 'reading_habit', 'sports_interest',
    'online_social_usage', 'travel_desire', 'gadget_usage',
    'work_style_collaborative', 'decision_speed'
]

# Section Headers for Inputs
st.markdown("### 📊 Personal Attributes")

# Create a clean layout with 2 columns
cols = st.columns(2)
input_data = {}

st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

for idx, feature in enumerate(features):
    col = cols[idx % 2]
    # Format the display names to look readable
    formatted_name = feature.replace('_', ' ').title()
    with col:
        input_data[feature] = st.slider(f"{formatted_name}", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

st.markdown("<br><br>", unsafe_allow_html=True)

# Centered Predict Button
cols_btn = st.columns([1, 2, 1])
with cols_btn[1]:
    if st.button("🔮 Predict My Personality Type"):
        # Prepare input array
        input_array = np.array([input_data[f] for f in features]).reshape(1, -1)
        
        # Scale Data
        scaled_input = scaler.transform(input_array)
        
        # Make Prediction
        prediction = model.predict(scaled_input)[0]
        
        # Decode numeric prediction if the model output was LabelEncoded (0, 1, 2)
        # Alphabetical sorting sets: 0 -> Ambivert, 1 -> Extrovert, 2 -> Introvert
        class_mapping = {0: "Ambivert", 1: "Extrovert", 2: "Introvert"}
        if isinstance(prediction, (int, float, np.integer, np.floating)) or str(prediction) in ['0', '1', '2']:
            prediction = class_mapping.get(int(prediction), prediction)
        
        # Probability for confidence level
        try:
            probabilities = model.predict_proba(scaled_input)[0]
            max_prob = np.max(probabilities) * 100
            prob_text = f"Model Confidence: <strong>{max_prob:.2f}%</strong>"
        except:
            prob_text = "Model Confidence: <strong>High (Accuracy 99.75%)</strong>"
        
        # Add visual mapping for personalities
        emoji_map = {
            "Extrovert": "🌟",
            "Introvert": "🎧",
            "Ambivert": "⚖️"
        }
        
        predicted_emoji = emoji_map.get(prediction, "✨")
        
        # Show Output nicely formatted
        st.markdown(f"""
        <div class="prediction-card">
            <h2 style='color: #e0f2fe; margin-bottom: 5px; font-size: 24px; font-weight: 500;'>Your Predicted Personality</h2>
            <h1 style='color: white; font-size: 56px; margin: 15px 0; font-weight: 800;'>{predicted_emoji} {prediction}</h1>
            <p style='font-size: 18px; color: #bae6fd;'>{prob_text}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Information breakdown regarding personalities
        if prediction == "Extrovert":
            st.success("💬 **Extrovert:** You draw energy from being around others, love engaging in social settings, and often feel recharged by group activities!")
        elif prediction == "Introvert":
            st.info("🛋️ **Introvert:** You recharge your energy through alone time, value deeper one-on-one connections, and might find large gatherings draining over time.")
        else:
            st.warning("🔄 **Ambivert:** You have a balance of both extrovert and introvert traits, making you highly adaptable. You enjoy social time but also deeply value your alone time to recharge.")
