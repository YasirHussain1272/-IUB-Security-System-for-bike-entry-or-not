import streamlit as st
import cv2
import joblib
import numpy as np
from skimage.feature import hog
from PIL import Image

# Load the trained models and label encoder
svm_classifier = joblib.load('svm_model.pkl')
random_forest_classifier = joblib.load('random_forest_model_1.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Function to extract HOG features from an image
def extract_hog_features(image):
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    hog_features, hog_image = hog(gray_image, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True)
    return hog_features

# Function for predicting new images
def predict_image(image, model):
    image = image.resize((128, 128))
    features = extract_hog_features(image)
    features = features.reshape(1, -1)
    
    prediction = model.predict(features)
    label = label_encoder.inverse_transform(prediction)[0]
    return label

# Streamlit app
st.set_page_config(layout="wide")

# Set background image
background_image = Image.open("bg.jpg")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{background_image}');
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for model selection
with st.sidebar:
    st.title("Model Selection")
    model_option = st.selectbox(
        "Select a model",
        ("SVM", "Random Forest")
    )

    st.title("Upload Image")
    uploaded_file = st.file_uploader("Upload an image of the bike", type=["jpg", "jpeg", "png"])

# Main content area
st.title("IUB GateGuard: Vehicle Access System🚴")
st.markdown("<h3 style='text-align: center; font-size: 20px;'>Certificate in AI(Deep Embeded)</h3>", unsafe_allow_html=True)

# Display project authors
st.header("Authors")
st.image("image.png")


if uploaded_file is not None:
    # Read the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=False, width=600)
    
    # Map model option to classifier
    model = svm_classifier if model_option == "SVM" else random_forest_classifier
    
    # Make prediction
    label = predict_image(image, model)
    if label == 'bikes_with_stickers':
        st.markdown("<h2 style='color: green;'>✅ Vehicle permitted for campus entry: Sticker Affixed.</h2>", unsafe_allow_html=True)
    elif label == 'bikes_without_stickers':
        st.markdown("<h2 style='color: red;'>🚫 Unauthorized Vehicle Entry: Sticker Required for Campus Access.</h2>", unsafe_allow_html=True)
