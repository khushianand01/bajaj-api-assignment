from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])

        user_id = "khushi_anand_28082004"
        email = "khushi28anand@gmail.com"
        roll_number = "2210993804"

        # Initialize lists and variables
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        alphabet_chars = ""

        # Process each item in the input data array
        for item in data:
            if item.isalpha():
                alphabets.append(item.upper())
                alphabet_chars += item
            elif item.isnumeric():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))
                total_sum += num
            else:
                special_characters.append(item)

        # Create the concatenated string [cite: 16]
        reversed_alphabets = alphabet_chars[::-1]
        concat_string = ""
        for i, char in enumerate(reversed_alphabets):
            if i % 2 == 0:
                concat_string += char.lower()
            else:
                concat_string += char.upper()

        # Prepare the final response object
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }
        
        # Send the response with a 200 OK status code [cite: 32]
        return jsonify(response), 200

    except Exception as e:
        # Handle any potential errors
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)