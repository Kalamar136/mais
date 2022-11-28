# Garbage Classification Model

Final project for McGill AI Society Intro to ML Bootcamp by Karl, Tofic, and Tristan.

Training data retieved from [Kaggle](https://www.kaggle.com/datasets/mostafaabla/garbage-classification).

## Project Description

This is a web app that classifies images into 12 different categories of materials commonly found in the garbage. The classification is done with RESNET in Tensorflow and the backend is built with Flask while the frontend is done with Vue and Tailwind.

## Running the app

Currently the frontend URLs are hardcoded to an azure server. Change the address that the frontend queries to whereever your flask backend will be booted up.

Then, install all requirements for the app. Launch the app with `flask run` in the `backend` directory.

Launch the frontend from the `frontend` directory with `yarn run serve` after doing a `yarn install` to get all prerequesites.