import pandas as pd
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud

#Performe a box plot of its input
def box_plot(data, x_label, y_label, title, image_name):
    data.plot(kind='bar')
    plt.rcParams.update({'font.size': 10})
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig('Data/SurveyResults/'+image_name+'.png')
    plt.show()

def box_plot_horizzontal(answers, x_label, y_label, title):
    data = dict()
    for answer in answers:
        issue_str = str(answer)

        #If the answer contains more then one issue
        if ";" in issue_str:
            list_issues = issue_str.split(";")

            for el in list_issues:
                el = el.strip()

                #If the issue is already in data -> update value
                if el in data:
                    data[el] = data[el]+1
                else:
                    #If the issue is new in data ->insert
                    data[el] = 1
        else:
            issue_str = issue_str.strip()
            if issue_str in data:
                data[issue_str] = data[issue_str]+1
            else:
                data[issue_str] = 1
    
    to_plot = pd.Series(data)
    #Set font size to 14
    plt.rcParams.update({'font.size': 14})
    plt.figure(figsize=(10, 8))
    to_plot.plot(kind='barh')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def cluster_plot(to_plot, title,image_name):
    data = dict()
    for feature in to_plot:
        features_str = str(feature)

        #If the answer contains more then one issue
        if "," in features_str:
            list_features = features_str.split(",")

            for el in list_features:
                el = el.strip()

                #If the issue is already in data -> update value
                if el in data:
                    data[el] = data[el]+1
                else:
                    #If the issue is new in data ->insert
                    data[el] = 1
        else:
            features_str = features_str.strip()
            if features_str in data:
                data[features_str] = data[features_str]+1
            else:
                data[features_str] = 1

    #Define the cluster plot
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(data)
    plt.rcParams.update({'font.size': 10})
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.savefig('Data/SurveyResults/'+image_name+'.png')
    plt.show()

def plot_degree(csv_file):
    degree = csv_file['What kind of degree do you have?']
    box_plot_horizzontal(degree, x_label="Num. answers", y_label="Degree", title="Participants' degree")


#To show the participants' job
def plot_jobs(csv_file):
    column_counts = csv_file['What is your job?'].value_counts()
    
    plt.figure(figsize=(13, 10))
    column_counts.plot(kind='barh')
    plt.xlabel('Num. Answers')
    plt.ylabel('Jobs')
    plt.title('Participants job')
    plt.show()

#To calculate the mean job experience
def job_experience_analysis(csv_file):

    #Take only the csv rows with a digit value
    job_experience = csv_file[csv_file["How many job experience years do you have?"].str.isdigit()]

    #Convert all this values in digit
    job_experience = job_experience["How many job experience years do you have?"].values.astype(int)
    
    #Calculate the mean
    sum = 0
    for experience in job_experience:
        sum = sum + experience
    
    num_rows = csv_file.shape[0]-1 #Get the number of csv rows (-1 to remove the string value)
    print("The mean job experience is: ",sum/num_rows)
    plt.rcParams.update({'font.size': 10})
    # Calculate the counts of each job experience value
    experience_counts = pd.Series(job_experience).value_counts()
    sorted_experience_counts=experience_counts.sort_index()
    box_plot(sorted_experience_counts, "Job experience years", "Num. Answers", "Participants' job experience years", "jobExperience")

def experience_in_dermatology(csv_file):
    exp_dermatology = csv_file["How much experience do you have in dermatology?"].value_counts()
    sorted_exp_dermatology=exp_dermatology.sort_index()
    box_plot(data=sorted_exp_dermatology, x_label="Experience in dermatology", y_label="Num. Answers", title="Experience in dermatology", image_name="experienceInDermatology")

def dermoscopic_image_relevance(csv_file):
    relevance = csv_file["How much does dermoscopic image affect melanoma diagnosis?"].value_counts()
    sorted_relevance=relevance.sort_index()
    box_plot(data=sorted_relevance, x_label="Relevance on diagnosis", y_label="Num. Answers", title="Dermoscopic image relevance on diagnosis",image_name="dermoscopicImageRelevance")

def histological_image_relevance(csv_file):
    relevance = csv_file["How much does histological image affect melanoma diagnosis?"].value_counts()
    sorted_relevance=relevance.sort_index()
    box_plot(data=sorted_relevance, x_label="Relevance on diagnosis", y_label="Num. Answers", title="Histological image relevance on diagnosis",image_name="histologicalImageRelevance")

def diagnosis_reliability_dermoscopic(csv_file):
    relevance = csv_file["If only the dermoscopic image is available, how reliable is the diagnosis?"].value_counts()
    sorted_relevance=relevance.sort_index()
    box_plot(data=sorted_relevance, x_label="Diagnosis reliability", y_label="Num. Answers", title="Diagnosis reliability with only dermoscopic image",image_name="diagnosisReliabilityDermoscopic")

def diagnosis_reliability_histological(csv_file):
    relevance = csv_file["If only the histological image is available, how reliable is the diagnosis?"].value_counts()
    sorted_relevance=relevance.sort_index()
    box_plot(data=sorted_relevance, x_label="Diagnosis reliability", y_label="Num. Answers", title="Diagnosis reliability with only histological image", image_name="diagnosisReliabilityHistological")

def diagnosis_reliability_both(csv_file):
    relevance = csv_file["If I have both the histological and dermoscopic images available, how reliable is the diagnosis?"].value_counts()
    sorted_relevance=relevance.sort_index()
    box_plot(data=sorted_relevance, x_label="Diagnosis reliability", y_label="Num. Answers", title="Diagnosis reliability with both image types", image_name="diagnosisReliabilityBoth")

def dermoscopic_problems(csv_file):
    answers = csv_file["What are the problems that can be encountered when acquiring a dermoscopic image?"]
    box_plot_horizzontal(answers, "Num. Answers", "Problems", "Problems when acquiring a dermoscopic image")

def histological_problems(csv_file):
    answers = csv_file["What are the problems that can be encountered when acquiring a histological image?"]
    answers = answers.dropna()
    box_plot_horizzontal(answers, "Num. Answers", "Problems", "Problems when acquiring a histological image")

def useful_metrics(csv_file):
    answers = csv_file["What are the useful metrics to evaluate a dermoscopic image quality?"] #select only the rows with a no empty value
    box_plot_horizzontal(answers, "Num. Answers", "Metrics", "Useful metrics")

def dermoscopic_features(csv_file):
    features = csv_file['What are the relevant dermoscopic image features on which you focus more?'].dropna()
    cluster_plot(features, "Relevant dermoscopic features","dermoscopicRelevantFeatures")

def histological_features(csv_file):
    features = csv_file['What are the relevant histological image features on which you focus more?'].dropna()
    cluster_plot(features, "Relevant histological features", "histologicalRelevantFeatures")  

def plot_nationality(csv_file):
    nat = csv_file['Nationality']
    box_plot_horizzontal(nat, x_label="Num. answers", y_label="Country", title="Where participants work")

#To conduct an analysis of the survey results
def read_survey_csv(path):
    csv_file = pd.read_csv(path)
    
    plot_degree(csv_file)
    plot_jobs(csv_file)
    job_experience_analysis(csv_file)
    experience_in_dermatology(csv_file)
    dermoscopic_image_relevance(csv_file)
    histological_image_relevance(csv_file)
    diagnosis_reliability_dermoscopic(csv_file)
    diagnosis_reliability_histological(csv_file)
    diagnosis_reliability_both(csv_file)
    dermoscopic_problems(csv_file)
    histological_problems(csv_file)
    useful_metrics(csv_file)
    plot_nationality(csv_file)
    dermoscopic_features(csv_file)
    histological_features(csv_file)


    


#os.chdir("Scripts")
read_survey_csv("Data\SurveyAnlysisOutput.csv")