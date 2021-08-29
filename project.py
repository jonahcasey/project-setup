from selenium import webdriver

url = "https://github.com/"
browser = webdriver.chrome()
browser.get(url)
browser.find_element_by_xpath("/html/body/div[1]/header/div[6]/details/details-menu/a[1]").click