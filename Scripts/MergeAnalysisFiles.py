import pandas as pd

def merge_csv():
    files = ['Data\Dataset1\Dataset1CleandedAnalysis.csv', 'Data\Dataset2\Dataset2CleanedAnalysis.csv', 'Data\ISIC2018\ISIC2018MelanomaCleanedAnalysis.csv','Data\ISIC2019\ISIC2019MelanomaCleanedAnalysis.csv','Data\ISIC2020\ISIC2020MelanomaCleanedAnalysis.csv']

    dataframes = []

    for file in files:
        df = pd.read_csv(file)
        dataframes.append(df)

    merged_df = pd.concat(dataframes)

    merged_df.to_csv('Data/FinalDatasetAnalysis.csv', index=False)

merge_csv()