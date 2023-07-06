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
    source_directory_path='D:/datasets/dataset2/HAM10000_images'
    benign_destination_directory_path='D:/datasets/dataset2/bening'
    melanoma_destination_directory_path='D:/datasets/dataset2/melanoma'
    carcinoma_destination_directory_path='D:/datasets/dataset2/carcinoma'
    intraephiterial_carcinoma_bowel_desease_destination_directory_path='D:/datasets/dataset2/intraepithelial_carcinoma&Bowen_disease'
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
