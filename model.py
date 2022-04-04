# model.py
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

def build_model(input_shape, output_shape, hidden_layers, activation):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(hidden_layers[0], input_shape=input_shape, activation=activation))
    for units in hidden_layers[1:]:
        model.add(tf.keras.layers.Dense(units, activation=activation))
    model.add(tf.keras.layers.Dense(output_shape, activation='sigmoid'))  # Binary classification
    return model

def train_model(data, model_params):
    # Prepare data for training
    # Example: split into train and test sets
    # X_train, X_test, y_train, y_test = ...

    # Build model
    model = build_model(input_shape=data.shape[1], output_shape=1, **model_params)

    # Compile model
    model.compile(optimizer=model_params["optimizer"], loss="binary_crossentropy", metrics=["accuracy"])

    # Define callbacks
    callbacks = [
        EarlyStopping(patience=3, monitor='val_loss'),  # Stop training if val_loss doesn't improve for 3 epochs
        ModelCheckpoint("models/trained_model.h5", save_best_only=True)  # Save the best model
    ]

    # Train model
    # model.fit(X_train, y_train, epochs=model_params["epochs"], batch_size=model_params["batch_size"], 
    #           validation_data=(X_test, y_test), callbacks=callbacks)
    
    return model
