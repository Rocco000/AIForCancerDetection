import csv
import shutil
import os

def get_melanoma_names():
    images_names=list()
    # Open the cvs file in read mode
    with open('Data\challenge-2019-training_metadata_2023-07-06.csv', 'r') as file:
        # Create a reader object to read csv file
        reader = csv.reader(file)
        #Skip the first row of csv file
        next(reader)
        for row in reader:
            if row[8]=='melanoma':
                images_names.append(row[0])
    return images_names

def copy_melanoma_images(images_names):
    source_path=str(input("Insert source folder path:"))
    destination_path=str(input("Insert folder path in whitch copy melanoma images:"))
    for image_name in images_names:
        image_path=os.path.join(source_path,image_name+'.jpg')
        shutil.copy(image_path,destination_path)


def get_images_names():
    dataset2_benign=str(input("Insert dataset2 benign folder path: "))
    dataset2_melanoma=str(input("Insert dataset2 melanoma folder path: "))
    dataset2_carcinoma=str(input("Insert dataset2 carcinoma folder path: "))
    dataset2_bowen=str(input("Insert dataset2 Bowen ect. folder path: "))
    dataset3_benign=str(input("Inset dataset3 benign folder path: "))
    dataset3_melanoma=str(input("Insert dataset3 melanoma folder path: "))
    
    dataset2_benign_names=os.listdir(dataset2_benign)
    dataset2_melanoma_names=os.listdir(dataset2_melanoma)
    dataset2_carcinoma_names=os.listdir(dataset2_carcinoma)
    dataset2_bowen_names=os.listdir(dataset2_bowen)
    dataset3_benign_names=os.listdir(dataset3_benign)
    dataset3_melanoma_names=os.listdir(dataset3_melanoma)
    return dataset2_benign_names+dataset2_melanoma_names+dataset2_carcinoma_names+dataset2_bowen_names+dataset3_benign_names+dataset3_melanoma_names


def remove_duplicates(images_names):
    isic_2019_melanoma=str(input("Insert ISIC 2019 melanoma path:"))
    isic_2019_melanoma_images=os.listdir(isic_2019_melanoma)
    removed_images=list()
    for image_name in images_names:
        if image_name in isic_2019_melanoma_images:
            removed_images.append({'image name':image_name})
            image_path=os.path.join(isic_2019_melanoma,image_name)
            os.remove(image_path)
    return removed_images


def build_csv_file(analysis_file_name,rows):
    # Open CSV file in write mode
    print("Writing csv file...")
    with open(analysis_file_name, 'w', newline='') as csv_file:
        # CReate a writer CSV
        writer = csv.DictWriter(csv_file, fieldnames=rows[0].keys())
        # Write header
        writer.writeheader()
        # Write data
        writer.writerows(rows)



#Copy melanoma images from ISIC 2019 dataset
#copy_melanoma_images(get_melanoma_names())

#Remove duplicates from ISIC 2019 melanoma images
build_csv_file('Data/ISIC2019MelanomaDuplicates.csv',remove_duplicates(get_images_names()))