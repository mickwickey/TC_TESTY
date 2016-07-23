from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\Mick\\Desktop\\Seleniump\\chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml')
time.sleep(5) # Let the user actually see something!ffl