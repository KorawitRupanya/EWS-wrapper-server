from flask_restx import Resource, Namespace, reqparse
from flask import jsonify
import requests
from genson import SchemaBuilder

ns = Namespace('')

# Define the request parser
parser = reqparse.RequestParser()
parser.add_argument('config', type=str, required=True, help='Please choose a configuration', location='json')

@ns.route("/monitor")
class Monitor(Resource):
    def get(self):
        try:
            # Make a request to the external API
            external_api_url = 'http://host.docker.internal:2011/meta/get_perception'
            response = requests.get(external_api_url)

            # Check if the request to the external API was successful
            if response.status_code == 200:
                data = response.json()

                # Convert the list to a dictionary
                data_dict = {'data': data}

                return jsonify(data_dict)  # Return the dictionary response from the external API
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@ns.route("/execute")
class Execute(Resource):
    @ns.expect(parser)  # Apply the parser to expect request data
    def put(self):
        try:
            # Parse the request body
            args = parser.parse_args()

            # Get the config
            config = args['config']

            # Make a POST request to the external API with the parsed data
            external_api_url = 'http://host.docker.internal:2011/meta/set_config'
            response = requests.post(external_api_url, json={'config': config})

            # Check if the request to the external API was successful
            if response.status_code == 200:
                return 'Success', 200
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@ns.route("/adaptation_options")
class Adaptation(Resource):
    def get(self):
        try:
            # Make a request to the external API
            external_api_url = 'http://host.docker.internal:2011/meta/get_all_configs'
            response = requests.get(external_api_url)

            # Check if the request to the external API was successful
            if response.status_code == 200:
                data = response.json()
                return jsonify(data)  # Return the JSON response from the external API
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500            

@ns.route("/monitor_schema")
class MonitorSchema(Resource):
    def get(self):
        try:
            # Make a request to the external API
            external_api_url = 'http://host.docker.internal:2011/meta/get_perception'
            response = requests.get(external_api_url)
            # Check if the request to the external API was successful
            if response.status_code == 200:
                data = response.json()
                # Generate JSON schema from the received JSON response
                builder = SchemaBuilder()
                builder.add_object(data)
                schema = builder.to_schema()
                # Return the generated schema
                return jsonify({'schema': schema})
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@ns.route("/execute_schema")
class ExecuteSchema(Resource):
    def get(self):
        try:
            # Make a request to the external API
            external_api_url = 'http://host.docker.internal:2011/meta/get_config'
            response = requests.get(external_api_url)
            # Check if the request to the external API was successful
            if response.status_code == 200:
                data = response.json()
                # Generate JSON schema from the received JSON response
                builder = SchemaBuilder()
                builder.add_object(data)
                schema = builder.to_schema()
                # Return the generated schema
                return jsonify({'schema': schema})
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500
@ns.route("/adaptation_options_schema")
class MonitorSchema(Resource):
    def get(self):
        try:
            # Make a request to the external API
            external_api_url = 'http://host.docker.internal:2011/meta/get_all_configs'
            response = requests.get(external_api_url)
            # Check if the request to the external API was successful
            if response.status_code == 200:
                data = response.json()
                # Generate JSON schema from the received JSON response
                builder = SchemaBuilder()
                builder.add_object(data)
                schema = builder.to_schema()
                # Return the generated schema
                return jsonify({'schema': schema})
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500