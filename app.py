from flask import Flask, jsonify
from flask_restx import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

@api.route('/hello/')
class HelloWorld(Resource):
    def get(self):
        return "Hello World"
      
        

@app.route('/monitor', methods=['GET'])
def get_data():
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
    
if __name__ == '__main__':
    app.run(debug=True)
