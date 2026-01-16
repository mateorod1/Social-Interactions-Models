import kagglehub

# Dataset de Vuelos:
# Link: https://www.kaggle.com/datasets/mahoora00135/flights
path = kagglehub.dataset_download("mahoora00135/flights")

print("Path to dataset files:", path)

# Dataset de Logistica:
# Link: https://www.kaggle.com/datasets/pushpitkamboj/logistics-data-containing-real-world-data?select=incom2024_delay_variable_description.csv
path = kagglehub.dataset_download("pushpitkamboj/logistics-data-containing-real-world-data")

print("Path to dataset files:", path)
