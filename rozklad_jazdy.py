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
    api_url = "https://api.um.warszawa.pl/api/action/dbtimetable_get?id=e923fa0e-d96c-43f9-ae6e60518c9f3238&busstopId=7009&busstopNr=01&line=523&apikey=e12d532a-cc5a-4f38-accb-b7ab9edb9e07"
    data = fetch_data_from_api(api_url)

    if data is not None:
        file_path = "rozklad_jazdy.txt"
        save_data_to_file(data, file_path)
        print("Data saved to rozklad_jazdy.txt successfully.")
    else:
        print("Data not saved due to API error.")

if __name__ == "__main__":
    main()
