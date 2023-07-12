import cv2
import os

#return the name of all files in path and the number of files
def get_image_names(path):
    img_names=list()
    images=os.listdir(path)
    for img in images:
        img_names.append(img)
    return img_names


def resize_images(source_partial_path, images_names,destination_partial_path):
    for image_name in images_names:
        source_image_path= os.path.join(source_partial_path,image_name)
        image=cv2.imread(source_image_path)
        image=cv2.resize(image, (600,450))
        destination_image_path= os.path.join(destination_partial_path,image_name)
        cv2.imwrite(destination_image_path,image)


#benign_folder_source_path=str(input("Insert benign folder source path:\n"))
malignant_folder_source_path=str(input("Insert malignant folder source path:\n"))
#benign_folder_destination_path=str(input("Insert benign folder destination path:\n"))
malignant_folder_destination_path=str(input("Insert malignant folder destination path:\n"))
"""benign_images_names=get_image_names(benign_folder_source_path)
print("Resizing benign images...")
resize_images(benign_folder_source_path,benign_images_names,benign_folder_destination_path)"""
malignant_images_names=get_image_names(malignant_folder_source_path)
print("Resizing malignant images...")
resize_images(malignant_folder_source_path,malignant_images_names,malignant_folder_destination_path)