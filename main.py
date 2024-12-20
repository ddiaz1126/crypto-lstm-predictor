from datetime import datetime
from data_ingestion import fetch_and_save_stock_data
from data_transforming import fetch_and_process_stock_data
from modeling import predict_stock_diff

def main():
    # Define file paths dynamically
    today = datetime.today().strftime('%Y-%m-%d')
    ingestion_output = f"data_ingested/ETH_USD_{today}.csv"
    transformation_output = f"data_transformed/last_5_close_diff_{today}.npy"
    modeling_output = f"modeling_predictions/predicted_close_diff_{today}.npy"
    model_path = "model_pipeline.joblib"

    # Run ETL steps
    print("Running ETL Step 1: Data Ingestion...")
    fetch_and_save_stock_data(
        symbol="ETH-USD",
        period="1mo",
        interval="1d",
        output_path=ingestion_output
    )
    print("Data Ingestion completed.\n")

    print("Running ETL Step 2: Data Transformation...")
    fetch_and_process_stock_data(
        input_path=ingestion_output,
        output_path=transformation_output,
        look_back=5
    )
    print("Data Transformation completed.\n")

    print("Running ETL Step 3: Modeling...")
    predict_stock_diff(
        input_path=transformation_output,
        model_path=model_path,
        output_path=modeling_output
    )
    print("Modeling completed.\n")

if __name__ == "__main__":
    main()