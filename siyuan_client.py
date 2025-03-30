import os
import requests
from dotenv import load_dotenv

load_dotenv()

class SiyuanClient:
    def __init__(self):
        self.api_token = os.getenv('SIYUAN_API_TOKEN')
        self.server_url = os.getenv('SIYUAN_SERVER_URL', 'http://localhost:6806')
        self.headers = {
            'Authorization': f'Token {self.api_token}',
            'Content-Type': 'application/json'
        }

    def list_notebooks(self):
        """获取所有笔记本列表"""
        url = f'{self.server_url}/api/notebook/listNotebooks'
        response = requests.post(url, headers=self.headers)
        return response.json()

    def get_notebook_documents(self, notebook_id):
        """获取指定笔记本的文档列表"""
        url = f'{self.server_url}/api/notebook/getNotebookConf'
        payload = {"notebook": notebook_id}
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()

    def search_documents(self, keyword):
        """搜索文档"""
        url = f'{self.server_url}/api/search/searchDocs'
        payload = {"k": keyword}
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()

if __name__ == '__main__':
    client = SiyuanClient()
    print("笔记本列表:", client.list_notebooks())