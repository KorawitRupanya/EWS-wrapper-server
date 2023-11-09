from flask_restx import Resource, Namespace 
from flask import jsonify, request
import requests

ns = Namespace("ews")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"hello": "restx"}

@ns.route("/monitor")
class Monitor(Resource):
    def get(self):
        try:
            # Make a request to the external API
            external_api_url = 'http://localhost:2011/meta/get_perception'
            response = requests.get(external_api_url)

            # Check if the request to the external API was successful
            if response.status_code == 200:
                data = response.json()
                return jsonify(data)  # Return the JSON response from the external API
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500


@ns.route("/execute")
class Execute(Resource):
    def put(self):
        try:
            # Get the JSON data from the request body
            request_data = request.get_json()

            if not request_data:
                return jsonify({'error': 'Invalid JSON data in the request'}), 400

            # Make a POST request to the external API with the JSON data
            external_api_url = 'http://localhost:2011/meta/set_config'
            response = requests.post(external_api_url, json=request_data)

            # Check if the request to the external API was successful
            if response.status_code == 200:
                return 200
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500        
        


@ns.route("/adaptation_options")
class Adaptation(Resource):
    def get(self):
        try:
            # Make a request to the external API
            external_api_url = 'http://localhost:2011/meta/get_all_configs'
            response = requests.get(external_api_url)

            # Check if the request to the external API was successful
            if response.status_code == 200:
                data = response.json()
                return jsonify(data)  # Return the JSON response from the external API
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500            
