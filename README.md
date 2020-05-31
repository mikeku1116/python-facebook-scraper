# python-facebook-scraper #

## 專案介紹 ##

本專案結合Python的Selenium及BeautifulSoup套件，開發爬取Facebook粉絲專頁文章標題的動態網頁爬蟲，其中使用的Selenium Webdriver為ChromeDriver 83.0.4103.39，可以搭配[[Python爬蟲教學]整合Python Selenium及BeautifulSoup實現動態網頁爬蟲(https://www.learncodewithmike.com/2020/05/python-selenium-scraper.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，開啟專案中的config.py檔案，輸入登入的Facebook「電子郵件」及「密碼」後，即可利用以下的指令執行網頁爬蟲：

`$ python app.py`

## 執行結果 ##

執行結果將會印出Learn Code With Mike粉絲專頁的文章標題，像以下的範例：

![Alt text](https://1.bp.blogspot.com/-LuamcfotjWQ/XtNW5ep-IGI/AAAAAAAAClU/osnHim0Ppxs1r5LxjWZ9gcSpvKZ1FoChwCK4BGAsYHg/python_selenium.PNG "Optional title")
