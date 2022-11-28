# Garbage Classification Model

Final project for McGill AI Society Intro to ML Bootcamp by Karl, Tofic, and Tristan.

Training data retieved from [Kaggle](https://www.kaggle.com/datasets/mostafaabla/garbage-classification).

## Project Description

This is a web app that classifies images into 12 different categories of materials commonly found in the garbage. The classification is done with RESNET in Tensorflow and the backend is built with Flask while the frontend is done with Vue and Tailwind.

## Running the app

Currently the backend server URLs in the frontend are hardcoded to localhost, port 5000. Flask defaults to port 5000.

To setup the backend, initiate a python virtual environment if desired. Run `pip install -r requirements.txt` inside `backend` to install all required packages.

Then, start the server with `flask run`.

To setup the frontend, navigate to the `frontend` folder and run `yarn install` to install all packages. Then run `yarn serve` to start at the webserver. All commands can also be done with `npm`.