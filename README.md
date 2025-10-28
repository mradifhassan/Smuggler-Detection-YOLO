# Smuggler-Detection-YOLO

A simple object detection ML model based on small training focused on detecting smuggler.

## Table of Contents
- [Overview](#overview)
- [Prerequisties](#prerequisties)
- [Build & Run Instructions](#build--run-instructions)
  
## Overview
This repository showcases custom object detection using the YOLOv8-Nano model, fine-tuned to identify and localize one class: Smuggler. The project demonstrates the complete machine learning workflow, from custom data preparation and model training on a small, self-collected dataset to real-time live inference using a webcam stream. It serves as a strong proof-of-concept for deploying lightweight, high-speed object detection models on low-power devices.
## Prerequisties
| **Component**      | **Requirement**                          | **Notes**                                                                                            |
|--------------------|------------------------------------------|------------------------------------------------------------------------------------------------------|
| Operating System   | Linux (Ubuntu 20.04+ Recommended)        | The environment used for project development and scripting.                                          |
| Python             | Python 3.8+                              | Developed using Python 3.13.5.                                                                       |
| PyTorch            | 2.0+ (CPU or GPU version)                | The fundamental deep learning library.                                                               |
| Ultralytics        | 8.0+                                     | The official framework for YOLOv8.                                                                   |
| OpenCV             | Latest version                           | Required for real-time video stream processing.                                                      |
| Hardware           | GPU/iGPU (NVIDIA/AMD) Strongly advised   | Training is computationally intensive; CPU training is possible but extremely slow.                  |
| Anaconda           | Strongly recommended                     | Used for creating isolated Python environments (conda create -n yolo_pen_env).                       |
|                    |                                          | This prevents dependency conflicts with other projects.                                              |
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Build & Run Instructions

First of all, we need to setup our environment in our desktop so that we can work. So, we need anaconda to install. Go to the official website of anaconda (https://www.anaconda.com/download) and download it. Then launch your terminal and write `conda activate` if you are on Linux, if you are on windows, you might see conda prompt from menu. Now your desktop environment has been set up. Now follow the commands below-
```bash
# Creating environment for yolo which is a framework of python.
conda create --name yolo-env1 python=3.13 -y

# Install ultralytics library which contains YOLO framework.
pip install ultralytics

# This will launch your desired working environment.
conda activate yolo-env1

# Install PyTorch engine for running and processing mathematical and computational tasks. if you have only cpu.
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Now install label-studio exactly what we are going to do training and labeling our object by naming classes
pip install label-studio

# Launch label-studio
label-studio start
````
Now our task is to labeling up our datasets by label-studio; after labeling, download as `YOLO format` where every images and their train dataset will exist in corresponding order. Make sure to keep all of the datasets as corresponding, otherwise training will be terminated or not work. If they aren't in corresponding order or if you just see any suffix infront of the name of your images or `txt` file, use this bash command to make them corresponding order-

````bash

# Check how many images are there in your folder
ls -l | wc -l

# Renaming for ascending order
n=1
for file in $(ls -v *.jpg); do
    new_name=$(printf "%03d.jpg" "$n")
    mv -i "$file" "$new_name"
    n=$((n + 1))
done

# If the corresponding txt format trained datasets contains suffix, then use this command
for filename in *.txt; do
    new_name=$(echo "$filename" | sed -E 's/^[^0-9]*([0-9].*)\.txt$/\1\.txt/')
    if [ "$filename" != "$new_name" ]; then
        mv "$filename" "$new_name"
    fi
done
````
Now if everything is done, now you are ready to train the mode

````bash

# Run from your PyCharm terminal
python3 train_yolo.py
````

Once you finished training properly, you are ready to test. There are several options to test, from your camera/webcams attached with your device, testing from `mp4` file from your device or directly accessing camera to another device like Smartphone or tablets where requires a software named `Ip Camera` which allows you to connect your device with another device by your ip address under same network (like your WiFi, Cellular data) 

````bash
# Running from webcam/camera
yolo predict model='/home/username/Smuggler Detection/runs/detect/border_security_cpu_v1/weights/best.pt' source=0 show=True

# Running from device's folder
yolo predict model='runs/detect/border_security_cpu_v1/weights/best.pt' source='/home/username/Downloads/video.mp4' show=True

# Accessing from another device using ip address
yolo predict model='/home/username/Smuggler Detection/runs/detect/border_security_cpu_v1/weights/best.pt' source="http://192.168.XXX.XX:8080/video" show=True

````

In order to access from another device by using ip address, Download `Ip Camera`, click start server from top right three dot, it will show a interface of a camera, click more and copy the ip address like this format `192.168.XXX.XX`. Now add this here 
