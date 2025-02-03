# ClassNumber
# NumberClass
A number classification application

# Number Classification API
A simple API that classifies a number and provides a fun fact.
It takes a number and returns an interesting mathematical property and a fun fact.
The endpoint accepts a GET request at /api/classify-number?number=371. The number is extracted from the query parameter.
The Functions in the code are:
        is_prime(): this checks if the number is prime.
        is_perfect(): this checks if the number is perfect.
        is_armstrong(): this checks if the number is Armstrong.
        get_fun_fact(): this requests the Numbers API to get a fun fact about the number.
The:
Properties are based on the calculations, the properties list is populated (Armstrong, odd/even).
Error Handling: If the input is not a valid integer, a 400 error is returned with a message.
Response: Returns a JSON object with the properties, digit sum, and fun fact about the number.

To Test the API Locally, Run the Flask app using this command in the terminal of vs-code: python app.py

The API will be available in the browser at: http://127.0.0.1:5000/api/classify-number?number=371

## The Programming Languages and Technologies
-- Python 3.x

-- Flask 
## Numbers API from these sources:
-- http://numbersapi.com/#42

-- https://en.wikipedia.org/wiki/Parity_(mathematics)

## Installation
To clone the repository, in your git bash type: git clone https://github.com/KathleenCode/NumberClass.git

Lastly, to install dependencies: pip install -r requirements.txt


