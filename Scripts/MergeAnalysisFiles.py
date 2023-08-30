import pandas as pd

def merge_csv():
    cleaned_files = ['Data\Dataset1\Dataset1CleanedAnalysis.csv', 'Data\Dataset2\Dataset2CleanedAnalysis.csv', 'Data\ISIC2018\ISIC2018MelanomaCleanedAnalysis.csv','Data\ISIC2019\ISIC2019MelanomaCleanedAnalysis.csv','Data\ISIC2020\ISIC2020MelanomaCleanedAnalysis.csv']
    uncleaned_files=['Data\Dataset1\Dataset1UncleanedAnalysis.csv', 'Data\Dataset2\Dataset2UncleanedAnalysis.csv', 'Data\ISIC2018\ISIC2018MelanomaUncleanedAnalysis.csv','Data\ISIC2019\ISIC2019MelanomaUncleanedAnalysis.csv','Data\ISIC2020\ISIC2020MelanomaUncleanedAnalysis.csv']

    dataframes = []

    for file in cleaned_files:
        df = pd.read_csv(file)
        dataframes.append(df)

    merged_df = pd.concat(dataframes)
    merged_df.to_csv('Data/FinalDatasetCleandedAnalysis.csv', index=False)

    dataframes.clear()

    for file in uncleaned_files:
        df = pd.read_csv(file)
        dataframes.append(df)

    merged_df = pd.concat(dataframes)
    merged_df.to_csv('Data/FinalDatasetUnleandedAnalysis.csv', index=False)

merge_csv()