# LSTM Crypto Predictor
This repository contains a Long Short-Term Memory (LSTM) model pipeline for predicted the difference between Closed Prices on a daily basis. The project is divided into several components, including training, ETL processes, and post-analysis of daily predictions.

## Prerequisites 
##### 1. Python 3.12 or above
##### 2. Docker (containerization)
##### Optional if running locally: pip install -r requirments.txt

## Setup (locally)
##### 1. Clone the repository
##### 2. Install dependencies (pip install -r requirments.txt)
##### 3. Run script: /python main.py 

## Docker Setup
##### 1. Build the Docker image: docker build -t lstm-predictor .
##### 2. Run the Docker container: docker run -it --name crypto-lstm-container crypto-lstm-predictor
##### 3. Stoping: docker stop crypto-lstm-container
##### 4. Removing: docker rm crypto-lstm-container


## Project Structure
#### **model_training folder**: 
Contains training scripts and model input files.
#### **'data_ingestion','data_transformed','modeling_predictions' folders**:
Contain CSV/Numpy files generated during the ETL process.
#### **'data_ingestion.py', 'data_transformation.py', 'modeling.py' files:
These are the three ETL Scripts.
### **'main.py' script**:
Handles the orchestration and execution of the ETL process.
### **model_predictions_analysis.ipynb** Notebook**:
Post Analysis of daily predictions for 4 days. 

