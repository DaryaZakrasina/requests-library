from pprint import pprint
import requests

token = "***"

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": disk_file_path, "overwrite": "true"}
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
        response = requests.get(upload_url, headers = headers, params = params)
        return response.json()
    def upload(self,disk_file_path, file_path):
        self.file = file_path
        link_dict = self.get_upload_link(disk_file_path = disk_file_path)
        href = link_dict.get("href", "")
        response = requests.put(href, data = open(file_path, 'rb'))

uploader = YaUploader(token)
uploader.get_upload_link('ALPHA concensus_cryo.pdf')
uploader.upload('ALPHA concensus_cryo.pdf', r"C:\Users\darya\OneDrive\Рабочий стол\курсы эмбриологов\витрификация\ALPHA concensus_cryo.pdf")