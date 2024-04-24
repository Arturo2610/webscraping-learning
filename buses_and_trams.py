import requests
import json

def fetch_data_from_api(api_url):
    response = requests.get(api_url, headers={"Cache-Control": "no-cache"})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from the API. Status code: {response.status_code}")
        return None

def save_data_to_file(data, file_path):
    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def main():
    api_url = "https://api.um.warszawa.pl/api/action/busestrams_get/?resource_id=f2e5503e927d-4ad3-9500-4ab9e55deb59&apikey=e12d532a-cc5a-4f38-accb-b7ab9edb9e07&type=2"
    data = fetch_data_from_api(api_url)

    if data is not None:
        file_path = "buses_and_trams.json"
        save_data_to_file(data, file_path)
        print("Data saved to buses_and_trams.txt successfully.")
    else:
        print("Data not saved due to API error.")

if __name__ == "__main__":
    main()
