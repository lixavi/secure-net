# config.py
MODEL_PARAMS = {
    "hidden_layers": [64, 32],     # Number of units in each hidden layer
    "activation": "relu",           # Activation function for hidden layers
    "optimizer": "adam",            # Optimizer algorithm
    "epochs": 10,                   # Number of training epochs
    "batch_size": 32                # Batch size for training
}

DATA_PATH = "data/network_traffic.csv"  # Path to the dataset

# Additional configuration settings
LOG_PATH = "logs/securenet.log"         # Path to the log file
VISUALIZATION_FORMAT = "pdf"            # Format for saving visualization results
