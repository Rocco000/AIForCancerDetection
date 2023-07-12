import pandas as pd
import os

def normalize_metrics():
    source_file_path=str(input("Inset the path to the file to be normalized:"))
    destination_file_path=os.path.splitext(source_file_path)[0]+'Normalized.csv'
    
    # Load file in a dataframe
    df = pd.read_csv(source_file_path)

    # Select column on which do normalization
    columns= ['sharpness','snr','cnr','contrast']

    # Apply min-max normalization
    for column in columns:
        min_value = df[column].min()
        max_value = df[column].max()
        df[column] = (df[column] - min_value) / (max_value - min_value)

    # Save the normalized file
    df.to_csv(destination_file_path, index=False)


normalize_metrics()