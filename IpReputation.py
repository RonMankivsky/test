from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv


file = open("hosts.txt","r")
content = file.read().split()
print(content)
results = []
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()


for ip in content :
    try:
        print(ip)
        driver.get("https://scamalytics.com/ip/"+ip)
        score = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[2]")
        content = driver.find_element_by_xpath("/html/body/div[3]/div[3]")


        header = ['score', 'description']
        data = [score.text,content.text]
        results.append(data)
        print(score.text)
        print(content.text)
    except:
        pass

rfile = open('results.csv', 'w', newline='')
dataWriter = csv.writer(rfile, delimiter = ',')
dataWriter.writerow(["Score","Description"])
for result in results:
    try:
        dataWriter.writerow(result)
    except:
        pass

file.close()