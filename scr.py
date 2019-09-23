
from selenium import webdriver
# browser=webdriver.Firefox(executable_path = "/home/moha/projects/isai/gecko/geckodriver")
# browser.get('https://www.exploit-db.com/exploits/44298')
# cve = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div[2]/h6/a")
# print(cve.text)
# cve.close()

class CVE:
    def __init__(self,  ed):
        self.ed = ed
    def find(self):
        browser=webdriver.Firefox(executable_path = "/home/moha/projects/isai/gecko/geckodriver")
        browser.get('https://www.exploit-db.com/exploits/' + str(self.ed))
        cve = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div[2]/h6/a")
        self.cve = cve.text
        print(self.cve)
        browser.close()
        return cve