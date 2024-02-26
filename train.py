# train.py
import logging
from model import train_model
from preprocessing import preprocess_data
from config import MODEL_PARAMS

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def train():
    try:
        logger.info("Starting model training...")
        
        # Preprocess data
        logger.info("Preprocessing data...")
        preprocessed_data = preprocess_data()

        # Train model
        logger.info("Training model...")
        trained_model = train_model(preprocessed_data, MODEL_PARAMS)

        logger.info("Model training completed successfully!")
    
    except Exception as e:
        logger.exception("An error occurred during training: %s", str(e))

if __name__ == "__main__":
    train()
