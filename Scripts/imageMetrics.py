import cv2
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

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

def calculate_SNR(images_paths):
    images_snr=list()
    for image_path in images_paths:
        #Obtain the ROI ad the background of the image
        roi,background=compute_segmentation(image_path)

        #Remove zeros from ROI and background
        roi=remove_zero(roi)
        background=remove_zero(background)

        #Calculate means and standard deviation of ROI
        mean_roi = np.mean(roi)
        std_dev_roi = np.std(roi)

        #Calculate and standard deviation of background
        std_dev_background = np.std(background)
        
        #Calculate the noise of the image
        noise = np.sqrt(std_dev_roi**2 + std_dev_background**2)

        # Calculate the signal-to-noise ratio (SNR)
        snr = mean_roi / noise #SNR=average ROI singnal/noise 
        images_snr.append(snr)

    return images_snr

def calculate_RMS_contrast(images_paths):
    images_RMS_contrast=list()
    for image_path in images_paths:
        # Load the image
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Normalize the image
        normalized_image = image.astype(float) / 255.0

        # Calculate the mean of the normalized image
        mean = np.mean(normalized_image)

        # Calculate the squared difference between each pixel and the mean
        squared_diff = np.square(normalized_image - mean)

        # Calculate the mean squared difference
        mean_squared_diff = np.mean(squared_diff)

        # Calculate the RMS contrast
        rms_contrast = np.sqrt(mean_squared_diff)
        images_RMS_contrast.append(rms_contrast)
    return images_RMS_contrast

def compute_segmentation(image_path):
    #Load the image
    image=cv2.imread(image_path)

    # Converts the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Applies Otsu thresholding to obtain threshold values
    _, threshold = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Calculates the mask of the area with higher contrast
    contrast_mask = cv2.bitwise_not(threshold)

    # Extracts the area with higher contrast from the original image
    roi = cv2.bitwise_and(image, image, mask=contrast_mask)

    # Extracts the remaining part of the image
    background = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(contrast_mask))

    #Show the segmentation
    cv2.imshow('ROI', roi)
    cv2.imshow('Back', background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Converts ROI and background in grayscale
    roi=cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    background=cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
    
    return roi, background


def calculate_CNR(images_paths):
    #List containing CNR values of images
    images_CNR=list()
    #List containing contrast between ROI and background of images
    images_contrast=list()
    for image_path in images_paths:
        #Obtain the ROI ad the background of the image
        roi,background=compute_segmentation(image_path)

        #Remove zeros from ROI and background
        roi=remove_zero(roi)
        background=remove_zero(background)

        #Calculate means and standard deviation of ROI
        mean_roi = np.mean(roi)
        std_dev_roi = np.std(roi)

        #Calculate mean and standard deviation of background
        mean_background = np.mean(background)
        std_dev_background = np.std(background)

        #Calculate the contrast
        contrast = abs(mean_roi - mean_background)

        #Calculate the noise of the image
        noise = np.sqrt(std_dev_roi**2 + std_dev_background**2)

        #Calculate the CNR
        cnr = contrast / noise
        images_CNR.append(cnr)
        images_contrast.append(contrast)
    return images_CNR,images_contrast


def measure_image_brightness(image_path):
    #Load the image
    image=cv2.imread(image_path)

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    # Extract the V channel
    v_channel = hsv_image[:,:,2]

    # Calculate the average brightness
    average_brightness = np.mean(v_channel)
    
    # Normalize the average brightness to the range [0, 1]
    normalized_brightness = average_brightness / 255.0

    return normalized_brightness


def remove_zero(image):
    height,width=image.shape[:2]
    nonzero_pixels=list()
    for i in range (height):
        for j in range (width):
            if image[i,j]!=0:
                nonzero_pixels.append(image[i,j])
    return nonzero_pixels




image_path='Data\Dataset2\ISIC_0024349.jpg'     
print("SNR: ",calculate_SNR([image_path]))
print("RMS: ",calculate_RMS_contrast([image_path]))
images_CNR,images_contrats=calculate_CNR([image_path])
print("CNR: ", images_CNR)
print("Contrast between ROI and background: ", images_contrats)
print("Image brightness: ",measure_image_brightness(image_path))

