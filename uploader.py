import requests

def upload_to_filepress(file_path):
    url = "https://api.filepress.store/upload"
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    response.raise_for_status()
    json_data = response.json()
    return json_data['data']['file']['url']
