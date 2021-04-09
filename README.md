# Turing 2.3.5 House Price Predictions

## Introduction

This is a final project of 2.3 module. I created a Flask app that predicts house price in Boston and hosted it in Heroku.

## Usage

In order to receive a prediction a POST request should be made to `https://turing235.herokuapp.com/predict`
Input should be in JSON format and should include a list of dictionaries that contain features data.
A sample input should look like this:

`{
    "inputs": [
        {
            "CRIM": 0.145,
            "ZN": 12.5,
            "INDUS": 7.87,
            "CHAS": 0,
            "NOX": 0.524,
            "RM": 6.17,
            "AGE": 96.1,
            "DIS": 5.95,
            "RAD": 5,
            "TAX": 311,
            "PTRATIO": 15.2,
            "B1000": 397,
            "LSTAT": 19.1
        }
    ]
}`

## Contact
Feel free to contact me here [@arnoldasjan](https://github.com/arnoldasjan/) for questions or just chat :)

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)