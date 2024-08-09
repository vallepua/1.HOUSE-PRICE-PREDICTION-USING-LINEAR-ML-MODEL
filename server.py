# from flask import Flask, request, jsonify
# import util

# app = Flask(__name__)



# @app.route('/get_location_names', methods=['GET'])
# def get_location_names():
#     response = jsonify({
#         'locations': util.get_location_names()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response

# @app.route('/predict_home_price', methods=['GET', 'POST'])
# def predict_home_price():
#     total_sqft = float(request.form['total_sqft'])
#     location = request.form['location']
#     bhk = int(request.form['bhk'])
#     bath = int(request.form['bath'])

#     response = jsonify({
#         'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response

# if __name__ == "__main__":
#     print("Starting Python Flask Server For Home Price Prediction...")
#     util.load_saved_artifacts()
#     app.run() 


from flask import Flask, request, jsonify
import util as util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    try:
        locations = util.get_location_names()
        if locations is None:
            return jsonify({'error': 'Failed to fetch location names'}), 500

        response = jsonify({'locations': locations})
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# @app.route('/predict_home_price', methods=['POST'])
# def predict_home_price():
#     try:
#         # Ensure that the request contains the required form data
#         if 'total_sqft' not in request.form or 'location' not in request.form \
#                 or 'bhk' not in request.form or 'bath' not in request.form:
#             return jsonify({'error': 'Missing required form data'}), 400

#         # Parse form data
#         total_sqft = float(request.form['total_sqft'])
#         location = request.form['location']
#         bhk = int(request.form['bhk'])
#         bath = int(request.form['bath'])

#         # Calculate estimated price
#         estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
#         if estimated_price is None:
#             return jsonify({'error': 'Failed to calculate estimated price'}), 500

#         # Prepare response
#         response = jsonify({'estimated_price': estimated_price})
#         response.headers.add('Access-Control-Allow-Origin', '*')

#         return response
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500 

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == 'POST':
        # Handle POST request
        try:
            total_sqft = float(request.form['total_sqft'])
            location = request.form['location']
            bhk = int(request.form['bhk'])
            bath = int(request.form['bath'])

            estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
            if estimated_price is None:
                return jsonify({'error': 'Failed to calculate estimated price'}), 500

            return jsonify({'estimated_price': estimated_price}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    elif request.method == 'GET':
        # Handle GET request
        # You might handle GET requests differently, depending on your requirements
        return jsonify({'message': 'GET request received for predict_home_price endpoint'}), 200


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
