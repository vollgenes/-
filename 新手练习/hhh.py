import time
import requests
url = 'http://www.zfcg.sh.gov.cn/portal/category'
now_time = int(time.time())
data = {'pageNo': 1, 'pageSize': 100, 'categoryCode': "ZcyAnnouncement1", '_t': now_time}
headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Length': '79',
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': '_zcy_log_client_uuid=8fa87f60-dc6b-11ee-9415-37ece01e1492',
            'DNT': '1',
            'Host': 'www.zfcg.sh.gov.cn',
            'Origin': 'http://www.zfcg.sh.gov.cn',
            'Referer': 'http://www.zfcg.sh.gov.cn/site/category?parentId=137027&childrenCode=ZcyAnnouncement&utm=site.site-PC-39928.959-pc-websitegroup-navBar-front.8.8fa91ba0dc6b11ee941537ece01e1492',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
            'X-Requested-With': 'XMLHttpRequest'
        }
json_data = requests.post(url, headers=headers, verify=False, data=data).json()
print(json_data)
