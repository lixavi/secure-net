# main.py
import logging
from config import MODEL_PARAMS, DATA_PATH
from preprocessing import preprocess_data
from model import train_model
from evaluate import evaluate_model
from predict import predict_anomalies
from visualize import visualize_results

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("Starting SecureNet...")
        
        # Preprocess data
        logger.info("Preprocessing data...")
        preprocessed_data = preprocess_data(DATA_PATH)

        # Train model
        logger.info("Training model...")
        trained_model = train_model(preprocessed_data, MODEL_PARAMS)

        # Evaluate model
        logger.info("Evaluating model...")
        evaluation_results = evaluate_model(trained_model, preprocessed_data)

        # Predict anomalies
        logger.info("Predicting anomalies...")
        anomalies = predict_anomalies(trained_model, preprocessed_data)

        # Visualize results
        logger.info("Visualizing results...")
        visualize_results(evaluation_results, anomalies)

        logger.info("SecureNet completed successfully!")
    
    except Exception as e:
        logger.exception("An error occurred: %s", str(e))

if __name__ == "__main__":
    main()
