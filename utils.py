# utils.py
import logging
import os
import pandas as pd

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Args:
    - file_path (str): Path to the CSV file.
    
    Returns:
    - data (DataFrame): Loaded data as a pandas DataFrame.
    """
    try:
        logger.info("Loading data from file: %s", file_path)
        data = pd.read_csv(file_path)
        logger.info("Data loaded successfully!")
        return data
    except Exception as e:
        logger.exception("An error occurred while loading data: %s", str(e))
        return None

def create_directory(directory):
    """
    Create a directory if it does not exist.
    
    Args:
    - directory (str): Path to the directory.
    """
    try:
        if not os.path.exists(directory):
            logger.info("Creating directory: %s", directory)
            os.makedirs(directory)
            logger.info("Directory created successfully!")
    except Exception as e:
        logger.exception("An error occurred while creating directory: %s", str(e))

def save_model(model, file_path):
    """
    Save a trained model to a file.
    
    Args:
    - model: Trained model object.
    - file_path (str): Path to save the model file.
    """
    try:
        logger.info("Saving model to file: %s", file_path)
        model.save(file_path)
        logger.info("Model saved successfully!")
    except Exception as e:
        logger.exception("An error occurred while saving model: %s", str(e))
