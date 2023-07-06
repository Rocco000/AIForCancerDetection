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


copy_melanoma_images(get_melanoma_names())