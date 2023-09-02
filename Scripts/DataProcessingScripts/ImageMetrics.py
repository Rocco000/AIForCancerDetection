import cv2
import numpy as np
import os


def calculate_sharpness(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Compute the Laplacian of the image
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    # Compute the variance of the Laplacian (sharpness)
    sharpness = np.var(laplacian)
    return sharpness

def calculate_SNR(roi):
    #Calculate means and standard deviation of ROI
    mean_roi = np.mean(roi)
    std_dev_roi = np.std(roi)

    # Calculate the signal-to-noise ratio (SNR)
    snr = mean_roi / std_dev_roi

    return snr

def calculate_RMS_contrast(image):
    #Convert the image in grayscale
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
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
    return rms_contrast

def compute_segmentation(image):
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
    """ cv2.imshow('ROI', roi)
    cv2.imshow('Back', background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""

    #Converts ROI and background in grayscale
    roi=cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    background=cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
    
    return roi, background


def calculate_CNR(roi,background):
    #Calculate means and standard deviation of ROI
    mean_roi = np.mean(roi)
    std_dev_roi = np.std(roi)

    #Calculate mean of background
    mean_background = np.mean(background)

    #Calculate the contrast
    contrast = abs(mean_roi - mean_background)

    #Calculate the CNR
    cnr = contrast / std_dev_roi
    return cnr,contrast


def calculate_brightness(image):
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


def calculate_metrics(partial_path,images_names,label):
    images_metrics=list()
    for image_name in images_names:
        image_path= os.path.join(partial_path,image_name)
        image=cv2.imread(image_path)
        sharpness=calculate_sharpness(image)
        rms_contrast=calculate_RMS_contrast(image)
        brightness=calculate_brightness(image)
        #Obtain the ROI ad the background of the image
        roi,background=compute_segmentation(image)
        #Remove zeros from ROI and background
        roi=remove_zero(roi)
        background=remove_zero(background)
        snr=calculate_SNR(roi)
        cnr,contrast=calculate_CNR(roi,background)
        image_metrics={'image name':image_name,'sharpness':sharpness,'brightness':brightness,'snr':snr,'cnr':cnr,'contrast':contrast,'rms contrast': rms_contrast,'label':label}
        images_metrics.append(image_metrics)
        print(image_metrics)
    return images_metrics

