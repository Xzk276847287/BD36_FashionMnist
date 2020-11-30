# BD36_FashionMnist
[![standard-readme compliant](https://img.shields.io/badge/Build%20by-python-brightgreen.svg?style=flat-square)](https://www.docker.com/)

This repository contains:

1.The main program of this project.

2.A demo video.mp4 file for how does it run in docker.

3.A Readme.txt for my instructor.

## Table of Contents
- [Background](#Background)
- [Main program](#Main-program)
- [Run by flask](#Run-by-flask)
  - [Install](#Install)
- [Run by docker](#Run-by-docker)

## Background

This project is written by python, and you can run this project by both flask and docker

To see more information about flask, see the [flask](https://flask.palletsprojects.com/en/1.1.x/)

To see more information about docker, see the [docker](https://docs.docker.com/)

## Main program

To see the main program of this project, see the [app](app/)

## Run by flask

To run this project by flask in your localhost, use this code:

```sh
> $env:FLASK_APP = "app.py"
> python -m flask run
 * Running on http://127.0.0.1:5000/
```

### Install

This project many packages. Go check them out if you don't have them locally installed.

```sh
> pip install flask
> pip install tensorflow
> pip install keras
> pip install Flask
> pip install Pillow
> pip install numpy
> pip install opencv-python
> pip install pymongo
> pip install dnspython
```

## Run by docker

To run this project by docker in your localhost, use this code:
```sh
> docker build -t fashion_mnist .
> docker run -d -p 80:80 fashion_mnist
 * Running on http://127.0.0.1/
 ```
