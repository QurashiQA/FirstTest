from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
 
 
Dtech = webdriver.Firefox()

Dtech.get("http://www.dareebatech.com")

failuer = []

def employeeSignInPageLoading ():
    result = Dtech.find_element_by_css_selector("a.btn:nth-child(3)")
    result.click()
        
    try:
        assert "dareebatech.com/individual/login" in Dtech.current_url 
    except:
        failuer.append("error 1")
        
    if failuer.__len__() >1:
        print (failuer)
    else:
        print ("No Errors")
    


def employeeLogInEmail():
    email = Dtech.find_element_by_id("email")
    email.send_keys("qurshi@qurshi.com")
    
    password = Dtech.find_element_by_id("password")
    password.send_keys("this is my password")
    
    enter = Dtech.find_element_by_css_selector(".btn")    
    enter.click()
    
    try:
        
        assert ("incorrect" in source == True)
    except:
        failuer.append("error 2")
        

employeeSignInPageLoading()

employeeLogInEmail()

print (failuer)
source =[""]
source.append(Dtech.page_source)

Dtech.close()