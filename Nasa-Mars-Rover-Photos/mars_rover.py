import requests

def get_rover_photos(api_key, rover_name, sol):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover_name}/photos"
    params = {
        'sol': sol,  # Martian sol (a Martian day) - an integer
        'api_key': api_key
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if 'errors' in data.keys():
            print(data['errors'])
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        data = None
    return data

def display_rover_photos(data):
    if data:
        if "photos" in data:
            for index, photo in enumerate(data["photos"], 1):
                print("Item NO: ", index)
                print("Image URL:", photo["img_src"])
                print("Earth Date:", photo["earth_date"])
                print("Rover:", photo["rover"]["name"])
                print("Camera:", photo["camera"]["full_name"])
                print("-" * 50)
            print("number_of_photos: ", len(data['photos']))
        else:
            print("Error:", data["errors"])

def main():
    api_key = "your api key"
    rover_name = "curiosity"  # Available options: curiosity, opportunity, perseverance, spirit
    sol = 1000  # Martian sol (day) to retrieve photos from
    rover_photos_data = get_rover_photos(api_key, rover_name, sol)
    display_rover_photos(rover_photos_data)

if __name__ == "__main__":
    main()