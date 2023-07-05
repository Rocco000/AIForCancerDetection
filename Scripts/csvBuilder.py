import os
import pandas as pd
import imageMetrics
import csv

#return the name of all files in path and the number of files
def get_image_names(path):
    img_names=list()
    images=os.listdir(path)
    for img in images:
        img_names.append(img)
    return img_names

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


def compute_metrics():
    benign_folder_source_path=str(input("Insert benign folder source path:\n"))
    malignant_folder_source_path=str(input("Insert malignant folder source path:\n"))
    # CSV file path
    analysis_file_name=str(input("Insert analysis file name:"))
    analysis_file_name= os.path.join("Data/",analysis_file_name)

    print("Calculating benign images metrics...")
    names_benign_images=get_image_names(benign_folder_source_path)
    label=0
    bening_rows=imageMetrics.calculate_metrics(benign_folder_source_path,names_benign_images,label)

    print("Calculating malignant images metrics...")
    names_malignant_images=get_image_names(malignant_folder_source_path)
    label=1
    malignant_rows=imageMetrics.calculate_metrics(malignant_folder_source_path,names_malignant_images,label)
    rows=bening_rows+malignant_rows
    return analysis_file_name,rows

analysis_file_name,rows=compute_metrics()
build_csv_file(analysis_file_name,rows)

