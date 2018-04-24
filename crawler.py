# -*-coding:utf8-*-
import time
import re
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path="/Users/Xuan/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs")
driver.get("https://reiseauskunft.bahn.de/bin/bhftafel.exe/dn?ld=41166&protocol=https:&seqnr=11&ident=56.011313166.1521551544&rt=1&rtMode=DB-HYBRID&")
data = driver.title
driver.save_screenshot('./google.png')
driver.find_element_by_name("input").send_keys(u"Göttingen")
#driver.find_element_by_name("inputRef").send_keys(u"Göttingen#008000128")
#driver.find_element_by_id("date").send_keys(u"20.03.188")
#driver.find_element_by_id("HFS_time").send_ukeys(u"15:36")
#driver.find_element_by_id("dep").send_keys("dep")
print '1'
#driver.find_element_by_id("prod_0").send_keys("15:36")
driver.find_element_by_name("start").click()
data = driver.title
driver.save_screenshot('./google.png')
print data
time.sleep(5)
pageSource = driver.page_source
with open('./source.html','w') as f:
    f.write(pageSource.encode('ISO-8859-1'))
driver.close()
print 'success'
