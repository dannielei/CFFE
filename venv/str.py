from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pyquery import PyQuery as pq
from datetime import datetime

browser=webdriver.Chrome()
wait=WebDriverWait(browser, 5)

def search():
    try:
        browser.get('http://www.cffex.com.cn/jysgg/index.html')
    except TimeoutException:
        return search()

def next_page():
    try:
        date_str2 = get_products()
        date_str3 = datetime.strptime('2018-02-12', "%Y-%m-%d")
        if date_str2 > date_str3:
            next = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.news_content.content > div.content_main.clearFloat > div.common_main_right > div > div.paging > div > a.other_a.paging_other_a')))
            next.click()
            sleep(2)
            get_products()
            return True


    except:
        return False

def get_products():
    html=browser.page_source
    doc=pq(html)
    items=doc('.clearFloat>li').items()
    for item in items:
        product={
            'href':item.find('.list_a_text ').attr('href'),
            'title': item.find('[href]').text(),
            'date': item.find('.time.comparetime').text()
        }
        print(product)
    str=product['date']
    date_str = datetime.strptime(str, "%Y-%m-%d")
    return date_str

def main():
    search()
    sleep(2)
    get_products()
    # str = product['date']
    # date_str = datetime.strptime(str, "%Y-%m-%d")
    # print('click next page: 1')
    for i in range(2,10):
        check = next_page()
        if not check:
            break
        print('click next page: {}'.format(i))


if __name__ == '__main__':
    main()
