# presetting
import requests, re, time, pickle, datetime
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
GC = {
    "number_of_pages_in_bulletin": 99,
    'url_open_market_trade_bulletin': 'http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/17081/index1.html',
    'url_pbc_homepage': 'http://www.pbc.gov.cn/',
    'urls_open_market_trade_announcement': [],
    'request': [],
    'flag_generate_request': True,
    'flag_get_all_announcement_links': False,
    'maximum_request_interval_in_seconds': 0.2,
    'xpath_page_content': '//*[@id="zoom"]',
    "restartpoint": 0
}

# generate request with right cookies and header
if GC[ 'flag_generate_request']:
    def generate_request(GC):
        # open browser
        print('Opening chrome...')
        Browser = webdriver.Chrome()
        Browser.get(GC["url_open_market_trade_bulletin"])
        css_selector = 'body > div.mainw950 > table:nth-child(2) > tbody > tr > td:nth-child(3) > table > tbody > tr > td > table > tbody > tr > td > script'
        WebDriverWait(Browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        print('Completed!')

        # pass cookies and header
        print('Passing cookies and header...')
        Request = requests.Session()
        for cookie in Browser.get_cookies():
            Request.cookies.set(cookie['name'], cookie['value'])
        Request.headers.update({'User-Agent': Browser.execute_script("return navigator.userAgent;")})
        Browser.close()
        print('Completed!')

        # test connection
        print('Testing connection...')
        assert Request.get(GC["url_open_market_trade_bulletin"]).status_code == 200, "Request fail! Please check connection!"
        print('Completed! Connection is good!')
        return Request
    GC["request"] = generate_request(GC)
else:
    with open('GC.pickle', 'rb') as f:
        GC_save = pickle.load(f)
    GC['request'] = GC_save['request']

# get all announcement links and save
if GC['flag_get_all_announcement_links']:
    def extract_announcement_links_in_this_page(GC, url_this_bulletin_page):
        page = GC['request'].get(url_this_bulletin_page)
        assert page.status_code == 200, 'No Conecttion with ' + url_this_bulletin_page
        pattern = '<a href="(/zhengcehuobisi/.*?/index.html)"'
        temp = re.findall(pattern, page.text, re.S)
        extracted_announcement_links = [GC['url_pbc_homepage'][:-1] + element for element in temp]
        output = GC['urls_open_market_trade_announcement'] + extracted_announcement_links
        print(len(extracted_announcement_links),"links added in urls_open_market_trade_announcement.", len(output), "in total.")
        return output
    def extract_all_announcement_links(GC):
        print("Extracting announcement links...")
        for i in range(GC["number_of_pages_in_bulletin"]):
            time.sleep(np.random.uniform() * GC['maximum_request_interval_in_seconds'])
            url_this_bulletin_page = GC['url_open_market_trade_bulletin'][:-6] + str(i+1) + GC['url_open_market_trade_bulletin'][-5:]
            print(i,"/", GC['number_of_pages_in_bulletin'], "of all pages are finished!")
        # unique with original ranking
        temp = set()
        GC['urls_open_market_trade_announcement'] = [x for x in GC['urls_open_market_trade_announcement'] if x not in temp and (temp.add(x) or True)]
        # save file
        file_name = "GC_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".pickle"
        with open(file_name, "wb") as f:
            pickle.dump(GC, f)
        print("Completed!", len(GC['urls_open_market_trade_announcement']), "are saved in", file_name)
    extract_all_announcement_links(GC)
else:
    with open('GC.pickle', 'rb') as f:
        GC_save = pickle.load(f)
    GC['urls_open_market_trade_announcement'] = GC_save['urls_open_market_trade_announcement']

# get all announcement
def process_str(text):
    text = re.sub('\t+', ' ', text)
    text = re.sub('\xa0+', ' ', text)
    text = re.sub('\n+', ' ', text)
    text = re.sub(' +', ' ', text)
    text = text.strip(' ')
    return text
df_output = pd.DataFrame()
num = len(GC['urls_open_market_trade_announcement'])
for i in range(num)[GC["restartpoint"]:]:
    time.sleep(np.random.uniform() * GC['maximum_request_interval_in_seconds'])
    url = GC['urls_open_market_trade_announcement'][i]
    try:
        page = GC["request"].get(url)
        page.encoding = 'utf-8'
        soup = BeautifulSoup(page.text)
        date = soup.find(id="shijian").get_text()
        print(date, i+1, "/", num)
        year = re.findall('\[(\d{4})\]',soup.title.string, re.S)[0]
        code = re.findall('第(\d{1,3})号',soup.title.string, re.S)[0]
        text = process_str(soup.find(id="zoom").get_text())
        data = {
            "日期": [date],
            "年份": [int(year)],
            "编号": [int(code)],
            "正文": [text]
        }
        df_temp = pd.DataFrame(data)
        df_output = pd.concat([df_output,df_temp], axis=0, join="outer")
    except:
        print("Attention! Somthing wrong with range id ", i, url)
        break
df_output["日期"] = pd.to_datetime(df_output["日期"]).dt.date
df_output = df_output.set_index("日期")
df_output = df_output.sort_index(ascending=False)
file_name = "OMO_announcement_pbc_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".xlsx"
df_output.to_excel(file_name)
print("All completed! File saved!")
