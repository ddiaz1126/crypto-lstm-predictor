# LSTM Crypto Predictor
This repository contains a Long Short-Term Memory (LSTM) model pipeline for predicted the difference between Closed Prices on a daily basis. The project is divided into several components, including training, ETL processes, and post-analysis of daily predictions.

## Project Structure:

## Prerequisites 
### 1. Python 3.12 or above
### 2. Docker (containerization)
### Optional if running locally: pip install -r requirments.txt

## Setup (locally)
### 1. Clone the repository
### 2. Install dependencies (pip install -r requirments.txt)
### 3. Run script: /python main.py 

## Docker Setup
### 1. Build the Docker image: docker build -t lstm-predictor .
### 2. Run the Docker container: docker run -it --name crypto-lstm-container crypto-lstm-predictor
### 3. Stoping: docker stop crypto-lstm-container
### 4. Removing: docker rm crypto-lstm-container
