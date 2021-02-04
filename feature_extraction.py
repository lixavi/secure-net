import numpy as np
import pandas as pd

def extract_basic_features(data):
    """
    Extracts basic statistical features from network traffic data.
    
    Args:
    - data (DataFrame): Preprocessed network traffic data.
    
    Returns:
    - features (DataFrame): Extracted features.
    """
    features = pd.DataFrame()
    
    # Basic statistical features
    features['mean_packet_length'] = data.groupby('source_ip')['packet_length'].mean()
    features['std_packet_length'] = data.groupby('source_ip')['packet_length'].std()
    features['total_packets_sent'] = data.groupby('source_ip').size()
    
    return features

def extract_time_based_features(data):
    """
    Extracts time-based features from network traffic data.
    
    Args:
    - data (DataFrame): Preprocessed network traffic data.
    
    Returns:
    - features (DataFrame): Extracted features.
    """
    features = pd.DataFrame()
    
    # Time-based features
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    features['hour_of_day'] = data['timestamp'].dt.hour
    features['day_of_week'] = data['timestamp'].dt.dayofweek
    
    return features

def extract_frequency_features(data):
    """
    Extracts frequency-based features from network traffic data.
    
    Args:
    - data (DataFrame): Preprocessed network traffic data.
    
    Returns:
    - features (DataFrame): Extracted features.
    """
    features = pd.DataFrame()
    
    # Frequency-based features
    features['unique_destinations'] = data.groupby('source_ip')['destination_ip'].nunique()
    features['unique_ports'] = data.groupby('source_ip')['destination_port'].nunique()
    
    return features

def extract_features(data):
    """
    Extracts various features from network traffic data.
    
    Args:
    - data (DataFrame): Preprocessed network traffic data.
    
    Returns:
    - features (DataFrame): Extracted features.
    """
    basic_features = extract_basic_features(data)
    time_features = extract_time_based_features(data)
    frequency_features = extract_frequency_features(data)
    
    # Combine all features
    features = pd.concat([basic_features, time_features, frequency_features], axis=1)
    
    return features
