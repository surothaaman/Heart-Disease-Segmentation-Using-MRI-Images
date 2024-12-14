import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.utils import class_weight

# Example training data (replace with actual data)
training_data = np.random.rand(100, 128, 128, 1)  # 100 grayscale MRI images
training_labels = np.zeros((100, 12))  # 12 classes (adjust as per your actual number of classes)
training_labels[:50, 0] = 1  # First 50 are Healthy
training_labels[50:, 1] = 1  # Next 50 are Myocardial Infarction

# Convert labels to categorical
training_labels = to_categorical(np.argmax(training_labels, axis=1), num_classes=12)

# Compute class weights for imbalanced classes
class_weights = class_weight.compute_class_weight(
    class_weight='balanced', 
    classes=np.unique(np.argmax(training_labels, axis=1)), 
    y=np.argmax(training_labels, axis=1)
)

# Convert class weights to a dictionary
class_weights_dict = dict(enumerate(class_weights))

# Build a simple CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(12, activation='softmax')  # 12 output classes
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model with the class weights
model.fit(training_data, training_labels, epochs=5, batch_size=8, class_weight=class_weights_dict)

# Save the model
model.save('heart_mri_model.h5')
