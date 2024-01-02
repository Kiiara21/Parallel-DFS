import requests
import threading

server_url = 'http://localhost:5000'

# num_pokemons = int(input("Enter the number of Pokemons: "))

# def fetch_pokemons_concurrently():
#     threads = []
#     num_clients = 2

#     for _ in range(num_clients):
#         thread = threading.Thread(target=get_pokemons_info, args=(num_pokemons,))
#         thread.start()
#         threads.append(thread)

#     for thread in threads:
#         thread.join()


def get_pokemons_info(num_pokemons):
    response = requests.get(f'{server_url}/get_pokemons/{num_pokemons}')

    if response.status_code == 200:
        data = response.json()
        pokemons = data.get('pokemons', [])
        for pokemon in pokemons:
            print(f"Name: {pokemon['name']}, URL: {pokemon['url']}")
    else:
        print(f"Error: {response.json().get('error', 'Unknown error')}")


def get_pokemon_info(pokemon_name):
    response = requests.get(f'{server_url}/get_pokemon/{pokemon_name}')

    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name']}, Height: {data['height']}")
        return data
    else:
        print(f"Error: {response.json().get('error', 'Unknown error')}")
        return None


#  we define some arbitrary adjacent Pokemons
def get_adjacent_pokemons(pokemon_name):
    adjacent_pokemons = {
        'pikachu': ['charmander', 'squirtle'],
        'charmander': ['bulbasaur'],
        'squirtle': ['bulbasaur', 'ivysaur'],
        'ivysaur': ['bulbasaur'],
        'bulbasaur': ['ivysaur','charizard'],
        'charizard': ['eevee'],
        'eevee': ['metapod']
    }
    
    return adjacent_pokemons.get(pokemon_name, [])


def dfs(current_path, target_pokemon):
    current_pokemon = current_path[-1]
    
    if(current_pokemon == target_pokemon):
        return current_path
    
    for neighbor in get_adjacent_pokemons(current_pokemon):
        if neighbor not in current_path:
            neighbor_info = get_pokemon_info(neighbor)
            result = dfs(current_path + [neighbor_info['name']], target_pokemon)
            if result: return result
            
    return None 

if __name__ == "__main__":
    start_pokemon = 'pikachu'
    target_pokemon = 'charizard'

    # Perform DFS to find the target Pokemon
    result_path = dfs([start_pokemon], target_pokemon)

    if result_path:
        print(f"Found a path to {target_pokemon}: {result_path}")
    else:
        print(f"Could not find a path to {target_pokemon}")