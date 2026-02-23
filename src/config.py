import os 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_DIR, 'data', 'raw')
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed')
LIVE_LOG_PATH = os.path.join(BASE_DIR, 'live_logs', 'incoming.log')
MODEL_PATH = os.path.join(BASE_DIR, 'models')
BATCH_SIZE = 100
ANOMALY_PROBABILITY = 0.05
LOG_DELAY = 0.05
LOG_LEVEL_WEIGHTS = {
    'INFO': 70,
    'WARNING': 20,
    'ERROR': 8,
    'CRITICAL': 2
}


