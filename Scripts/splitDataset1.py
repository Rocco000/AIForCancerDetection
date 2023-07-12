import csv
import shutil
import os

def get_samples():
    images=list()
    # Open the cvs file in read mode
    with open('Data/HAM10000_metadata.csv', 'r') as file:
        # Create a reader object to read csv file
        reader = csv.reader(file)
        #Skip the first row of csv file
        next(reader)
        for row in reader:
            image={'image_name':row[1]+'.jpg','diagnosis':row[2]}
            images.append(image)
    return images


def split_dataset(images):
    source_directory_path=str(input("Insert folder source path: "))
    benign_destination_directory_path=str(input("Insert benign folder destination path: "))
    melanoma_destination_directory_path=str(input("Insert melanoma folder destination path: "))
    carcinoma_destination_directory_path=str(input("Insert carcinoma folder destination path: "))
    intraephiterial_carcinoma_bowel_desease_destination_directory_path=str(input("Insert bowel etc. folder destination path: "))
    print("Splitting dataset...")
    for image in images:
        image_path=os.path.join(source_directory_path,image['image_name'])
        if image['diagnosis']=='akiec':
            shutil.move(image_path, intraephiterial_carcinoma_bowel_desease_destination_directory_path)
        elif image['diagnosis']=='bcc':
            shutil.move(image_path,carcinoma_destination_directory_path)
        elif image['diagnosis']=='mel':
            shutil.move(image_path,melanoma_destination_directory_path)
        else:
            shutil.move(image_path,benign_destination_directory_path)
    print("Splitting done")
            

split_dataset(get_samples())
