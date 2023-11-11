# Import necessary modules and classes from Flask and Flask-Restx
from flask_restx import Resource, Namespace, reqparse
from flask import jsonify

# Import the 'requests' library for making HTTP requests
import requests

# Import the 'SchemaBuilder' class from the 'genson' module
from genson import SchemaBuilder

# Create a Namespace named 'ns'
ns = Namespace('')

# Define a request parser for the '/execute' route
parser = reqparse.RequestParser()
parser.add_argument('config', type=str, required=True, help='Please choose a configuration', location='json')

# Define a resource class for the '/monitor' route
@ns.route("/monitor")
class Monitor(Resource):
    def get(self):
        try:
            # Make a request to the external API for monitoring data
            external_api_url = 'http://host.docker.internal:2011/meta/get_perception'
            response = requests.get(external_api_url)

            # Check if the request to the external API was successful
            if response.status_code == 200:
                data = response.json()

                # Check if data is not empty and return the first dictionary in the list
                if data:
                    return jsonify(data[0])
                else:
                    return jsonify({'error': 'No data received from the external API'}), 500
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

# Define a resource class for the '/execute' route
@ns.route("/execute")
class Execute(Resource):
    @ns.expect(parser)  # Apply the parser to expect request data
    def put(self):
        try:
            # Parse the request body
            args = parser.parse_args()

            # Get the config from the parsed data
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

# Define a resource class for the '/adaptation_options' route
@ns.route("/adaptation_options")
class Adaptation(Resource):
    def get(self):
        try:
            # Make a request to the external API for adaptation options
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

# Define a resource class for the '/monitor_schema' route
@ns.route("/monitor_schema")
class MonitorSchema(Resource):
    def get(self):
        try:
            # Make a request to the external API for monitoring data
            external_api_url = 'http://host.docker.internal:2011/meta/get_perception'
            response = requests.get(external_api_url)

            # Check if the request to the external API was successful
            if response.status_code == 200:
                data = response.json()

                # Generate JSON schema from the received JSON response
                builder = SchemaBuilder()
                builder.add_object(data)
                schema = builder.to_schema()

                # Move 'type' and 'properties' keys up a level if 'items' key exists
                if 'items' in schema:
                    schema['type'] = schema['items']['type']
                    schema['properties'] = schema['items']['properties']
                    del schema['items']

                # Return the generated schema
                return jsonify(schema)
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

# Define a resource class for the '/execute_schema' route
@ns.route("/execute_schema")
class ExecuteSchema(Resource):
    def get(self):
        try:
            # Make a request to the external API for execution schema
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
                return jsonify(schema)
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

# Define a resource class for the '/adaptation_options_schema' route
@ns.route("/adaptation_options_schema")
class AdaptationOptionsSchema(Resource):
    def get(self):
        try:
            # Make a request to the external API for adaptation options schema
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
                return jsonify(schema)
            else:
                return jsonify({'error': 'Failed to fetch data from the external API'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500
