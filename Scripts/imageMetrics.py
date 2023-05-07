import cv2
import numpy as np
import os
import pandas as pd

def calculate_blur(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Compute the Laplacian of the image
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    # Compute the variance of the Laplacian
    variance = np.var(laplacian)
    return variance
    
def calculate_sharpness(partial_path, images):
    list_of_sharpness= list()
    for image in images:
        path= os.path.join(partial_path,image)
        # Load the image
        img = cv2.imread(path)
        # Calculate the image sharpness
        sharpness = calculate_blur(img)
        #Store the sharpness
        list_of_sharpness.append(sharpness)
    return list_of_sharpness