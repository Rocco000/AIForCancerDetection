import matplotlib.pyplot as plt
import pandas as pd

#Define dataframe for dataset1
dataset1_analysis_file_path='Data\Dataset1\Dataset1CleanedAnalysisNormalized.csv'
df_dataset1 = pd.read_csv(dataset1_analysis_file_path)

#Define dataframe for dataset2
dataset2_analysis_file_path='Data\Dataset2\Dataset2CleanedAnalysisNormalized.csv'
df_dataset2 = pd.read_csv(dataset2_analysis_file_path)

#Define dataframe for ISIC 2018
ISIC2018_analysis_file_path='Data\ISIC2018\ISIC2018MelanomaCleanedAnalysisNormalized.csv'
df_ISIC2018 = pd.read_csv(ISIC2018_analysis_file_path)

#Define dataframe for ISIC 2019
ISIC2019_analysis_file_path='Data\ISIC2019\ISIC2019MelanomaCleanedAnalysisNormalized.csv'
df_ISIC2019 = pd.read_csv(ISIC2019_analysis_file_path)

#Define dataframe for ISIC 2020
ISIC2020_analysis_file_path='Data\ISIC2020\ISIC2020MelanomaCleanedAnalysisNormalized.csv'
df_ISIC2020 = pd.read_csv(ISIC2020_analysis_file_path)

#Define dataframe for related project dataset
related_project_file_path='Data\DatasetReladProject\RelatedProjectCleanedAnalysisNormalized.csv'
df_related_project=pd.read_csv(related_project_file_path)



def plot_sharpness():
    plt.boxplot([df_dataset1['sharpness'],df_dataset2['sharpness'],df_ISIC2018['sharpness'],df_ISIC2019['sharpness'],df_ISIC2020['sharpness'],df_related_project['sharpness']]) 

    labels=['Dataset1','Dataset2','ISIC2018','ISIC2019','ISIC2020','RelatedProject']

    plt.title('Sharpness values')
    # Impostazione delle etichette sull'asse x
    plt.xticks(range(1, len(labels) + 1), labels)
    # Aggiunta di etichette
    plt.ylabel('Values')    
    plt.savefig('Data/DataQuality/sharpness.png')
    # Visualizzazione del boxplot
    plt.show()


def plot_brightness():
    plt.boxplot([df_dataset1['brightness'],df_dataset2['brightness'],df_ISIC2018['brightness'],df_ISIC2019['brightness'],df_ISIC2020['brightness'],df_related_project['brightness']]) 

    labels=['Dataset1','Dataset2','ISIC2018','ISIC2019','ISIC2020','RelatedProject']

    plt.title('Brightness values')
    # Impostazione delle etichette sull'asse x
    plt.xticks(range(1, len(labels) + 1), labels)
    # Aggiunta di etichette
    plt.ylabel('Values')    
    plt.savefig('Data/DataQuality/brightness.png')
    # Visualizzazione del boxplot
    plt.show()


def plot_snr():
    plt.boxplot([df_dataset1['snr'],df_dataset2['snr'],df_ISIC2018['snr'],df_ISIC2019['snr'],df_ISIC2020['snr'],df_related_project['snr']]) 

    labels=['Dataset1','Dataset2','ISIC2018','ISIC2019','ISIC2020','RelatedProject']

    plt.title('SNR values')
    # Impostazione delle etichette sull'asse x
    plt.xticks(range(1, len(labels) + 1), labels)
    # Aggiunta di etichette
    plt.ylabel('Values')    
    plt.savefig('Data/DataQuality/snr.png')
    # Visualizzazione del boxplot
    plt.show()


def plot_cnr():
    plt.boxplot([df_dataset1['cnr'],df_dataset2['cnr'],df_ISIC2018['cnr'],df_ISIC2019['cnr'],df_ISIC2020['cnr'],df_related_project['cnr']]) 

    labels=['Dataset1','Dataset2','ISIC2018','ISIC2019','ISIC2020','RelatedProject']

    plt.title('CNR values')
    # Impostazione delle etichette sull'asse x
    plt.xticks(range(1, len(labels) + 1), labels)
    # Aggiunta di etichette
    plt.ylabel('Values')    
    plt.savefig('Data/DataQuality/cnr.png')
    # Visualizzazione del boxplot
    plt.show()


def plot_contrast():
    plt.boxplot([df_dataset1['contrast'],df_dataset2['contrast'],df_ISIC2018['contrast'],df_ISIC2019['contrast'],df_ISIC2020['contrast'],df_related_project['contrast']]) 

    labels=['Dataset1','Dataset2','ISIC2018','ISIC2019','ISIC2020','RelatedProject']

    plt.title('Contrast values')
    # Impostazione delle etichette sull'asse x
    plt.xticks(range(1, len(labels) + 1), labels)
    # Aggiunta di etichette
    plt.ylabel('Values')    
    plt.savefig('Data/DataQuality/contrast.png')
    # Visualizzazione del boxplot
    plt.show()


def plot_RMS_contrast():
    plt.boxplot([df_dataset1['rms contrast'],df_dataset2['rms contrast'],df_ISIC2018['rms contrast'],df_ISIC2019['rms contrast'],df_ISIC2020['rms contrast'],df_related_project['rms contrast']]) 

    labels=['Dataset1','Dataset2','ISIC2018','ISIC2019','ISIC2020','RelatedProject']

    plt.title('RMS Contrast values')
    # Impostazione delle etichette sull'asse x
    plt.xticks(range(1, len(labels) + 1), labels)
    # Aggiunta di etichette
    plt.ylabel('Values')    
    plt.savefig('Data/DataQuality/rmsContrast.png')
    # Visualizzazione del boxplot
    plt.show()



plot_sharpness()
plot_brightness()
plot_snr()
plot_cnr()
plot_contrast()
plot_RMS_contrast()