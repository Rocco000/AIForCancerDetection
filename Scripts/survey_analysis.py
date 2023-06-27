import pandas as pd
import matplotlib.pyplot as plt

def read_survey_csv(path):
    csv_file = pd.read_csv(path)
    column_counts = csv_file['What is your job?'].value_counts()
    
    plt.figure(figsize=(13, 4))
    column_counts.plot(kind='barh')
    plt.xlabel('Occurence')
    plt.ylabel('Jobs')
    plt.title('Participants job')
    
    plt.set_yticklabels([label.replace(' ', '\n') for label in labels])

    plt.show()

read_survey_csv("../Datasets/SurveyAnlysisOutput.csv")