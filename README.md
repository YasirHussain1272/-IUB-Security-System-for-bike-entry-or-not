# IUB GateGuard: Vehicle Access System

## Overview
The **IUB GateGuard: Vehicle Access System** is an application designed to determine if a bike is permitted entry onto campus based on the presence of a sticker. Using machine learning models, the app efficiently classifies images of bikes and provides an access decision.

## Key Components:

### 1. Model Loading
- The application loads pre-trained machine learning models (SVM and Random Forest) and a label encoder using the `joblib` library.
- These models are responsible for the image classification tasks.

### 2. Feature Extraction
- The app uses **Histogram of Oriented Gradients (HOG)** to extract features from uploaded bike images.
- HOG helps identify the structural characteristics of the images, aiding in the classification process.

### 3. Image Prediction
- Users can upload images of bikes through the interface.
- The application resizes the uploaded image, extracts HOG features, and uses either the SVM or Random Forest model to predict if the bike has a sticker.

### 4. User Interface
- Built using **Streamlit**, the app offers a clean and intuitive interface:
  - **Sidebar**: Allows users to select a machine learning model (SVM or Random Forest) and upload an image.
  - **Main Content Area**: Displays the app title, authors, uploaded image, and the prediction result.

### 5. Prediction Results
- After the image is uploaded, the app provides feedback based on the model’s prediction:
  - **Green Message**: Indicates the bike is permitted for campus entry if classified as having a sticker.
  - **Red Message**: Warns that the bike requires a sticker for entry if classified as not having a sticker.

## Conclusion
This application demonstrates a real-world use case for image classification through machine learning, particularly in vehicle access control. Its user-friendly interface allows for quick decision-making regarding bike entry based on the presence of a sticker.

## Sample Application View
![IUB GateGuard: Vehicle Access System](iub%20bike%20enter.png)

## How to Use the Application

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/IUB-GateGuard-Vehicle-Access-System.git

