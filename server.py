from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/get_pokemon/<pokemon_name>')
def get_pokemon(pokemon_name):

    pokeapi_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(pokeapi_url)

    if response.status_code == 200:

        pokemon_data = response.json()

        return jsonify({'name': pokemon_data['name'], 'height': pokemon_data['height']})
    else:
        return jsonify({'error': 'Pokemon not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
