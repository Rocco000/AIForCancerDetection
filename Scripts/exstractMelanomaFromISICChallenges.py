import csv
import shutil
import os

def get_melanoma_names(path):
    images_names=list()
    # Open the cvs file in read mode
    with open(path, 'r') as file:
        # Create a reader object to read csv file
        reader = csv.reader(file)
        #Skip the first row of csv file
        next(reader)
        for row in reader:
            if row[9]=='melanoma': #row[8] for challenge 2019 and 2018 task 1,2 / row[6] for challenge 2018 task 3 / row[9] for 2020 challenge
                images_names.append(row[0])
    return images_names

def copy_melanoma_images(images_names):
    source_path=str(input("Insert source folder path:"))
    destination_path=str(input("Insert folder path in whitch copy melanoma images:"))
    for image_name in images_names:
        image_path=os.path.join(source_path,image_name+'.jpg')
        shutil.copy(image_path,destination_path)


def get_images_names():
    final_dataset_benign=str(input("Insert final dataset benign folder path: "))
    final_dataset_melanoma=str(input("Insert final dataset melanoma folder path: "))
    
    final_dataset_benign_names=os.listdir(final_dataset_benign)
    final_dataset_melanoma_names=os.listdir(final_dataset_melanoma)
    return final_dataset_benign_names+final_dataset_melanoma_names


def remove_duplicates(images_names):
    isic_challenge_melanoma=str(input("Insert ISIC challenge melanoma path:"))
    isic_challenge_melanoma_images=os.listdir(isic_challenge_melanoma)
    removed_images=list()
    for image_name in images_names:
        if image_name in isic_challenge_melanoma_images:
            removed_images.append({'image name':image_name})
            image_path=os.path.join(isic_challenge_melanoma,image_name)
            os.remove(image_path)
    return removed_images


def build_csv_file(analysis_file_name,rows):
    if len(rows)==0:
        print("There are NO duplicates!")
    else:
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
path=str(input("Insert source path of challenge metadata csv: "))
copy_melanoma_images(get_melanoma_names(path))

#Remove duplicates from ISIC 2019 melanoma images
folder_path=str(input("Insert folder path in which save csv file:"))
file_name=str(input("Insert file name in which store the name of duplicated removed images:"))
path=os.path.join(folder_path,file_name)
build_csv_file(path,remove_duplicates(get_images_names()))