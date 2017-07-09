import selenium
from selenium import webdriver
from Q.employeesSignIn import Dtech

test1 = webdriver.Firefox()

test1.get("http://dareebatech.com/company/register")

checkBox = test1.find_element_by_css_selector("div.checkbox:nth-child(1) > label:nth-child(1) > span:nth-child(2) > span:nth-child(1)")

checkBox.click()

def findCheckBoxSelected(x):
    return x.is_enabled()

print (findCheckBoxSelected(checkBox))

if findCheckBoxSelected(checkBox) == False:
    checkBox.click()
    print("we did it")
else: 
    print ("should be selected")


Dtech.close()

