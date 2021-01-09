# ClimateAI-CAELI 
Hive project as part of Applied AI Essentials

## Problem Statement: 

Solar power will play a major role towards sustainable energy transition. Reliable operation of solar power plants is critical both in terms of power system safety and economics. The use-case we aim to solve here is to improve the operational performance of solar modules enabling focused maintenance and improved efficiency. This is a multi-classification problem using infrared images where our aim is to classify whether a given image belongs to the healthy category or one of the unhealthy ones. 

## Dataset:

https://github.com/RaptorMaps/InfraredSolarModules

## Folder structure:

1. modelTraining: It contains scripts used for model training and saving.

2. prediction: It contains code for predicting the class given a new image.

3. static: style sheet, images and model metadeta for web application.

4. templates: HTML for web application.

5. image: contains any image used either in readme 

6. project-planning: Project Planning and Version Control workflow management.

## Hardware detail:

This project is developed on Windows 10 operating system without any GPU.

## Setup:

### Step 1: Create virtual environment

```
conda create -n hiveProject python=3.6
conda activate hiveProject
```
### Step 2: Install required library to the virtual environment from requirements.txt file.

### Step 3: Train model using CNN notebook in modelTraining folder.

### Step 4: Save the model and other encoding parameters in static/model-metadeta folder for the web application to pick it.

### Step 5: Run app.py to check the application functionality in development.

```
python app.py
```

### Step 6: Create a new app in heroku and push the code to heroku master  



  