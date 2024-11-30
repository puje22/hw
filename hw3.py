import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import datetime

def last_page_v2(page):
    driver = webdriver.Chrome() 
    today = datetime.date.today()
    date_first = today
    #page = 15 
    
    main_page = f"https://www.unegui.mn/l-hdlh/l-hdlh-zarna/oron-suuts-zarna/?page={page}&ordering=newest"

    while date_first >= today:
        driver.get(main_page)  
        ads = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div[1]")  # Find all ads
                                              
        
        date_label = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[4]/div[1]/div[1]").text
                                                    #"/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[4]/div[1]/div[1]"
        if "Өчигдөр" in date_label:  
            return f"Өчигдрийн зар эндээс эхэлж байна. хуудас: {page}"

        elif "Өнөөдөр" in date_label:  
            # upper = page + (page) // 2
            upper = page + 10
            low = page  

            while low <= upper:
                mid = (low + upper) // 2  
                main_page = f"https://www.unegui.mn/l-hdlh/l-hdlh-zarna/oron-suuts-zarna/?page={mid}&ordering=newest"
                driver.get(main_page)  

                ads = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div[1]")
                                                     #/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[4]/div[1]/div[1]
                
                date_label = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[4]/div[1]/div[1]").text
                                                            #/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[4]/div[1]/div[1]
                if "Өнөөдөр" in date_label:  
                    low = mid + 1  
                elif "Өчигдөр" in date_label:  
                    upper = mid - 1  
                    return f"Өчигдрийн зар эндээс эхэлж байна. хуудас: {mid}"


print(last_page_v2(20))