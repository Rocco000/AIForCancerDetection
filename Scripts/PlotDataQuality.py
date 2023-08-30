import matplotlib.pyplot as plt
import pandas as pd
import csv

#Define dataframe for uncleaned dataset metics
dataset_uncleaned_file_path='Data\FinalDatasetUnleandedAnalysis.csv'
df_uncleaned = pd.read_csv(dataset_uncleaned_file_path)

#Define dataframe for cleaned dataset metrics
dataset_cleaned_file_path='Data\FinalDatasetCleandedAnalysis.csv'
df_cleaned = pd.read_csv(dataset_cleaned_file_path)

#Define dataframe for related project dataset
related_project_file_path='Data\DatasetReladProject\RelatedProjectUncleanedAnalysis.csv'
df_related_project=pd.read_csv(related_project_file_path)

csv_path='Data\DataQuality\ImageMetrics.csv'
with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['metric','data type','min','max','standard deviation','mean','median'])


def plot_sharpness():
    with open(csv_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['sharpness','uncleaned',df_uncleaned['sharpness'].min(),df_uncleaned['sharpness'].max(),df_uncleaned['sharpness'].std(),df_uncleaned['sharpness'].mean(),df_uncleaned['sharpness'].median()])
        writer.writerow(['sharpness','cleaned',df_cleaned['sharpness'].min(),df_cleaned['sharpness'].max(),df_cleaned['sharpness'].std(),df_cleaned['sharpness'].mean(),df_cleaned['sharpness'].median()])

    plt.figure(figsize=(11, 6))
    plt.suptitle('Sharpness')
    plt.subplot(1, 2, 1)
    plt.boxplot([df_uncleaned['sharpness'],df_cleaned['sharpness']]) 
    labels=['Uncleaned images','Cleaned images']
    plt.title('Compairson uncleaned/cleaned data')
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.ylabel('Values')

    plt.subplot(1, 2, 2)
    plt.boxplot([df_cleaned['sharpness'],df_related_project['sharpness']]) 
    labels=['Our dataset','Existing dataset']
    plt.title('Comparison of our data with the existing ones')
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.ylabel('Values')
    plt.savefig('Data\DataQuality\sharpness.png')
    plt.show()


def plot_brightness():
    with open(csv_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['brightness','uncleaned',df_uncleaned['brightness'].min(),df_uncleaned['brightness'].max(),df_uncleaned['brightness'].std(),df_uncleaned['brightness'].mean(),df_uncleaned['brightness'].median()])
        writer.writerow(['brightness','cleaned',df_cleaned['brightness'].min(),df_cleaned['brightness'].max(),df_cleaned['brightness'].std(),df_cleaned['brightness'].mean(),df_cleaned['brightness'].median()])
    
    plt.figure(figsize=(11, 6))
    plt.suptitle('Brightness')
    plt.subplot(1, 2, 1)
    plt.boxplot([df_uncleaned['brightness'],df_cleaned['brightness']]) 
    labels=['Uncleaned images','Cleaned images']
    plt.title('Compairson uncleaned/cleaned data')
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.ylabel('Values')

    plt.subplot(1, 2, 2)
    plt.boxplot([df_cleaned['brightness'],df_related_project['brightness']]) 
    labels=['Our dataset','Existing dataset']
    plt.title('Comparison of our data with the existing ones')
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.ylabel('Values')
    plt.savefig('Data/DataQuality/brightness.png')
    plt.show()


def plot_snr():
    with open(csv_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['snr','uncleaned',df_uncleaned['snr'].min(),df_uncleaned['snr'].max(),df_uncleaned['snr'].std(),df_uncleaned['snr'].mean(),df_uncleaned['snr'].median()])
        writer.writerow(['snr','cleaned',df_cleaned['snr'].min(),df_cleaned['snr'].max(),df_cleaned['snr'].std(),df_cleaned['snr'].mean(),df_cleaned['snr'].median()])

    plt.figure(figsize=(11, 6))
    plt.suptitle('SNR')
    plt.subplot(1, 2, 1)
    plt.boxplot([df_uncleaned['snr'],df_cleaned['snr']]) 
    labels=['Uncleaned images','Cleaned images']
    plt.title('Compairson uncleaned/cleaned data')
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.ylabel('Values')

    plt.subplot(1, 2, 2)
    plt.boxplot([df_cleaned['snr'],df_related_project['snr']]) 
    labels=['Our dataset','Existing dataset']
    plt.title('Comparison of our data with the existing ones')
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.ylabel('Values')
    plt.savefig('Data\DataQuality\snr.png')
    plt.show()


def plot_cnr():
    with open(csv_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['cnr','uncleaned',df_uncleaned['cnr'].min(),df_uncleaned['cnr'].max(),df_uncleaned['cnr'].std(),df_uncleaned['cnr'].mean(),df_uncleaned['cnr'].median()])
        writer.writerow(['cnr','cleaned',df_cleaned['cnr'].min(),df_cleaned['cnr'].max(),df_cleaned['cnr'].std(),df_cleaned['cnr'].mean(),df_cleaned['cnr'].median()])

    plt.figure(figsize=(11, 6))
    plt.suptitle('CNR')
    plt.subplot(1, 2, 1)
    plt.boxplot([df_uncleaned['cnr'],df_cleaned['cnr']]) 
    labels=['Uncleaned images','Cleaned images']
    plt.title('Compairson uncleaned/cleaned data')
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.ylabel('Values')

    plt.subplot(1, 2, 2)
    plt.boxplot([df_cleaned['cnr'],df_related_project['cnr']]) 
    labels=['Our dataset','Existing dataset']
    plt.title('Comparison of our data with the existing ones')
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.ylabel('Values')
    plt.savefig('Data\DataQuality\cnr.png')
    plt.show()


def plot_contrast():
    with open(csv_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['contrast','uncleaned',df_uncleaned['contrast'].min(),df_uncleaned['contrast'].max(),df_uncleaned['contrast'].std(),df_uncleaned['contrast'].mean(),df_uncleaned['contrast'].median()])
        writer.writerow(['contrast','cleaned',df_cleaned['contrast'].min(),df_cleaned['contrast'].max(),df_cleaned['contrast'].std(),df_cleaned['contrast'].mean(),df_cleaned['contrast'].median()])

    plt.figure(figsize=(11, 6))
    plt.suptitle('Contrast')
    plt.subplot(1, 2, 1)
    plt.boxplot([df_uncleaned['contrast'],df_cleaned['contrast']]) 
    labels=['Uncleaned images','Cleaned images']
    plt.title('Compairson uncleaned/cleaned data')
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.ylabel('Values')

    plt.subplot(1, 2, 2)
    plt.boxplot([df_cleaned['contrast'],df_related_project['contrast']]) 
    labels=['Our dataset','Existing dataset']
    plt.title('Comparison of our data with the existing ones')
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.ylabel('Values')
    plt.savefig('Data\DataQuality\contrast.png')
    plt.show()


def plot_RMS_contrast():
    with open(csv_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['rms contrast','uncleaned',df_uncleaned['rms contrast'].min(),df_uncleaned['rms contrast'].max(),df_uncleaned['rms contrast'].std(),df_uncleaned['rms contrast'].mean(),df_uncleaned['rms contrast'].median()])
        writer.writerow(['rms contrast','cleaned',df_cleaned['rms contrast'].min(),df_cleaned['rms contrast'].max(),df_cleaned['rms contrast'].std(),df_cleaned['rms contrast'].mean(),df_cleaned['rms contrast'].median()])

    plt.figure(figsize=(11, 6))
    plt.suptitle('RMS Contrast')
    plt.subplot(1, 2, 1)
    plt.boxplot([df_uncleaned['rms contrast'],df_cleaned['rms contrast']]) 
    labels=['Uncleaned images','Cleaned images']
    plt.title('Compairson uncleaned/cleaned data')
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.ylabel('Values')

    plt.subplot(1, 2, 2)
    plt.boxplot([df_cleaned['rms contrast'],df_related_project['rms contrast']]) 
    labels=['Our dataset','Existing dataset']
    plt.title('Comparison of our data with the existing ones')
    plt.xticks(range(1, len(labels) + 1), labels)
    plt.ylabel('Values')
    plt.savefig('Data/DataQuality/rmsContrast.png')
    plt.show()


plot_sharpness()
plot_brightness()
plot_snr()
plot_cnr()
plot_contrast()
plot_RMS_contrast()