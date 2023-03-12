import os
import json

from googleapiclient.discovery import build


class Channel():
    """
    Инициализация данных, id канала
    """
    def __init__(self, id_channel):
        self.id_channel = id_channel
        api_key: str = os.getenv('API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=api_key)


    def print_info(self):
        """
        Функция вывода информации о канале по его id
        :return:
        """
        channel = self.youtube.channels().list(id=self.id_channel, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))