import os
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = load_model('heart_mri_model.h5')

# Function to process the uploaded MRI image
def process_image(img_path):
    img = Image.open(img_path).convert('L')  # Convert image to grayscale
    img = img.resize((128, 128))  # Resize to match the input shape of the model
    img_array = np.expand_dims(np.array(img), axis=0)  # Add batch dimension
    img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension
    img_array = img_array / 255.0  # Normalize the image
    return img_array

# Route to handle image upload and prediction
@app.route('/', methods=['GET', 'POST'])
def upload_and_predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']
        
        if file.filename == '':
            return "No selected file"
        
        if file:
            # Save the uploaded file to the 'uploads' folder
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)

            # Process the image and make predictions
            img = process_image(file_path)
            predictions = model.predict(img)

            # Debugging: Log predictions for analysis
            print(f"Predictions: {predictions}")  # Log the predicted probabilities

            # Assuming the model outputs a probability for each class
            predicted_class = np.argmax(predictions[0])
            confidence = float(np.max(predictions[0]))

            # Map the class index to a disease label
            disease_labels = [
                'Normal', 'Healthy', 'Myocardial Infarction', 'Coronary Artery Disease',
                'Arrhythmias', 'Heart Failure', 'Heart Valve Disease', 'Cardiomyopathy',
                'Congenital Heart Defects', 'Pericarditis', 'Aortic Disease', 
                'Chronic Ischemic Heart Disease'
            ]
            result = disease_labels[predicted_class]

            # Map result to CSS class for styling
            result_class = {
                'Normal': 'Healthy', 'Healthy': 'Healthy',
                'Myocardial Infarction': 'Myocardial',
                'Coronary Artery Disease': 'Coronary',
                'Arrhythmias': 'Arrhythmias',
                'Heart Failure': 'HeartFailure',
                'Heart Valve Disease': 'HeartValve',
                'Cardiomyopathy': 'Cardiomyopathy',
                'Congenital Heart Defects': 'Congenital',
                'Pericarditis': 'Pericarditis',
                'Aortic Disease': 'Aortic',
                'Chronic Ischemic Heart Disease': 'ChronicIschemic'
            }.get(result, 'Unknown')

            return render_template('result.html', 
                                   image_url=f'/uploads/{file.filename}',
                                   predicted_class=result, 
                                   confidence=round(confidence * 100, 2),  # Display confidence as percentage
                                   result_class=result_class)

    return '''
    <!doctype html>
    <title>Upload MRI Image</title>
    <h1>Upload MRI Image for Prediction</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''

# Route to load and predict from images in train, val, and test folders
@app.route('/test_images')
def test_images():
    # Specify paths to the image folders
    folders = ['train_data', 'val_data', 'test_data']  # Ensure these folders exist
    results = {}
    
    for folder in folders:
        folder_path = os.path.join('uploads', folder)
        if not os.path.exists(folder_path):
            continue
        
        # Collect results for each image in the folder
        results[folder] = []
        for filename in os.listdir(folder_path):
            if filename.endswith(('.png', '.jpg', '.jpeg')):  # Check for image file types
                img_path = os.path.join(folder_path, filename)
                img = process_image(img_path)
                predictions = model.predict(img)

                # Log predictions for each image
                predicted_class = np.argmax(predictions[0])
                confidence = float(np.max(predictions[0])) * 100  # Convert to percentage
                disease_labels = [
                    'Normal', 'Healthy', 'Myocardial Infarction', 'Coronary Artery Disease',
                    'Arrhythmias', 'Heart Failure', 'Heart Valve Disease', 'Cardiomyopathy',
                    'Congenital Heart Defects', 'Pericarditis', 'Aortic Disease', 
                    'Chronic Ischemic Heart Disease'
                ]
                result = disease_labels[predicted_class]
                
                results[folder].append({
                    'filename': filename,
                    'predicted_class': result,
                    'confidence': round(confidence, 2)  # Round confidence for display
                })
    
    return render_template('upload.html', results=results)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    # Create train, val, and test folders if they do not exist
    for folder in ['train_data', 'val_data', 'test_data']:  # Correcting folder names
        os.makedirs(os.path.join('uploads', folder), exist_ok=True)
    app.run(debug=True)
