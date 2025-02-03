import requests;
from flask import Flask, request, jsonify;
from flask_cors import CORS;
# http://numbersapi.com/#42
# https://en.wikipedia.org/wiki/Parity_(mathematics)

app = Flask(__name__);
CORS(app);


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_perfect(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num


def is_armstrong(num):
    digits = list(map(int, str(num)))
    power = len(digits)
    return sum(d ** power for d in digits) == num


def get_fun_fact(number):
    url = f"http://numbersapi.com/{number}?json"
    response = requests.get(url)
    return response.json().get("text", "No fun fact available")

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        
        number = request.args.get('number')
        
        if not number.isdigit() and not (number.startswith('-') and number[1:].isdigit()):
            return jsonify({"error": True, "message": "Invalid input. Please provide a valid integer."}), 400
        
        
        number = int(number)
        
        if number < 0:
            return jsonify({"error": True, "message": "Invalid input. The number must be a non-negative integer."}), 400
        
        
        prime = is_prime(number)
        perfect = is_perfect(number)
        armstrong = is_armstrong(number)
        odd_or_even = "odd" if number % 2 != 0 else "even"
        
        
        properties = []
        if armstrong:
            properties.append("armstrong")
        if odd_or_even == "odd":
            properties.append("odd")
        else:
            properties.append("even")
        
        
        digit_sum = sum(int(digit) for digit in str(number))
        
       
        fun_fact = get_fun_fact(number)
        
        
        response = {
            "number": number,
            "is_prime": prime,
            "is_perfect": perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }
        
        return jsonify(response), 200
        
    except ValueError:
        
        return jsonify({"error": True, "message": "Invalid input, please provide a valid integer"}), 400

if __name__ == "__main__":
    app.run(debug=True)
