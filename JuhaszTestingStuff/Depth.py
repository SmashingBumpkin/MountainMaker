import numpy as np
import torch
from transformers import AutoImageProcessor, AutoModelForDepthEstimation
from torch import Tensor

import cv2
import matplotlib.pyplot as plt
import open3d as o3d

import os
import random
from pathlib import Path

images = []
num_samples = 1


#pathToImage = "/0.jpg"
#input_img = cv2.imread(pathToImage)
#input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
#images.append(input_img)

valid_images_folder = "C:/WorkingSets/3D/OriginalImages"
drawing_images_folder = "C:/WorkingSets/3D/DepthImages"



processor = AutoImageProcessor.from_pretrained("LiheYoung/depth-anything-large-hf")
model = AutoModelForDepthEstimation.from_pretrained("LiheYoung/depth-anything-large-hf").to("cuda")
#print(model.config)



def ConvertAllImagesToDepthImages():
    # Loop through each file in the input folder
    for filename in os.listdir(valid_images_folder):
        # Check if the file is an image (you can add more image formats if needed)
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Load the image
            image_path = os.path.join(valid_images_folder, filename)

            # Load the image using cv2.imread
            #image = PostProcesser.GetImageFromPath(image_path)
            image = cv2.imread(image_path)

            # Check if the image is loaded successfully
            if image is not None:

                #image = cv2.resize(image, (250,250))
                # Process the image as needed
                depth_img = ConvertImageToDepthImage(image)
                
                # Construct the output path using raw string literals or forward slashes
                output_path = os.path.join(drawing_images_folder, f"Processed_{filename}")
                
                # Save the processed image to the output folder
                cv2.imwrite(output_path, depth_img)
                
                print(f"Saved {filename} to {output_path}")
            else:
                print(f"Failed to load {filename}")


'''
for i in range(num_samples):
    pathToImage = "C:/WorkingSets/3D/Images/"+str(i)+".jpg"
    input_img = cv2.imread(pathToImage)
    input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
    #print(input_img.shape)

    images.append(input_img)
'''



def ConvertImageToDepthImage(img):
    input = processor(images=img, return_tensors="pt").to("cuda")

    with torch.no_grad():
        outputs = model(**input)
        depth = outputs.predicted_depth
    
    depth = depth.squeeze().cpu().numpy()
    return depth

def plot_samples():
    for i in range(num_samples):
        fig, axs = plt.subplots(1, 2)
        axs[0].imshow(samples[i][0])
        axs[0].set_title("Original Image")
        axs[1].imshow(samples[i][1])
        axs[1].set_title("Depth Image")
        plt.show()

#plot_samples()

ConvertAllImagesToDepthImages()