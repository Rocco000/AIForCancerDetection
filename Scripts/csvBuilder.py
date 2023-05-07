import os
import pandas as pd
import imageMetrics

#return the name of all files in path
def get_image_names(path):
    with os.scandir(path) as images:
        img_names= list()
        for img in images:
            img_names.append(img.name)
    return img_names

def create_csv_file(img_name, path, sharpness, labels):
    rows = {"image_name": img_name, "path": path, "sharpness": sharpness, "diagnosis": labels}
    # Create a pandas DataFrame from the data
    df = pd.DataFrame(rows)
    print(df)

    #Create csv file
    df.to_csv("../Datasets/Dataset2/analysis2.csv")


list_names1 = get_image_names('../Datasets/Dataset2/melanoma')
list_sharpness1 = imageMetrics.calculate_sharpness('../Datasets/Dataset2/melanoma', list_names1)
label = [1]*70
path = ["../Datasets/Dataset2/melanoma"]*70

list_names0 = get_image_names('../Datasets/Dataset2/naevus')
list_sharpness0 = imageMetrics.calculate_sharpness('../Datasets/Dataset2/naevus', list_names0)
app = [0]*100
app2 = ["../Datasets/Dataset2/naevus"]*100

label = label + app
path = path +app2
list_img_name = list_names1 + list_names0
list_img_sharpness = list_sharpness1 + list_sharpness0

print(list_img_name)

create_csv_file(list_img_name, path, list_img_sharpness, label)

