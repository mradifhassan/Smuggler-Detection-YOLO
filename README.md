# Smuggler-Detection-YOLO

A simple object detection ML model based on small training focused on detecting smuggler.

## Table of Contents
- [Overview](#overview)
- [Prerequisties](#prerequisties)
- [Build & Run Instructions](#build--&--run--instructions)

## Overview
This repository showcases custom object detection using the YOLOv8-Nano model, fine-tuned to identify and localize two distinct classes: Pens and Pencils. The project demonstrates the complete machine learning workflow, from custom data preparation and model training on a small, self-collected dataset to real-time live inference using a webcam stream. It serves as a strong proof-of-concept for deploying lightweight, high-speed object detection models on low-power devices.
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

First of all, we need to setup our environment in our desktop so that we can work. So, we need anaconda to install. Go to the official website of anaconda (https://www.anaconda.com/download) and download it. Then launch your terminal and write `conda activate` if you are on Linux, if you are on windows. you might see conda prompt from menu. Now your desktop environment has been set up. Now follow the commands below-
```bash
# Creating environment for yolo which is a framework of `python`
conda create --name yolo-env1 python=3.13 -y

# This will launch your desired working environment.
conda activate yolo-env1 
