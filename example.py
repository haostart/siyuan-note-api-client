from siyuan_client import SiyuanClient

def main():
    # 创建客户端实例
    client = SiyuanClient()

    # 获取笔记本列表
    notebooks = client.list_notebooks()
    print("笔记本列表:", notebooks)

    # 如果有笔记本，获取第一个笔记本的文档
    if notebooks and 'data' in notebooks and notebooks['data']['notebooks']:
        first_notebook_id = notebooks['data']['notebooks'][0]['id']
        documents = client.get_notebook_documents(first_notebook_id)
        print("文档列表:", documents)

    # 搜索文档
    search_results = client.search_documents("Python")
    print("搜索结果:", search_results)

if __name__ == '__main__':
    main()