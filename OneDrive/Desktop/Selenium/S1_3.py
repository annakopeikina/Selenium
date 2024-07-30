from selenium import webdriver
from selenium.webdriver.common.by import By # класс для ожидания наступления события
from selenium.webdriver.support.ui import WebDriverWait # включает проверки, такие как видимость элемента на странице, доступность элемента для клика итд
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
import time
import json

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
driver =webdriver.Chrome(options=chrome_options)

youtube_channel_url = "https://youtube.com/@progliveru/videos"

try:
    driver.get(youtube_channel_url)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))
    page_height = driver.execute_script("return document.documentElement.scrollHeight")
    scroll_pause_time = 2
    while True:
        driver.execute_script("window.scrollTo(0, documentElement.scrollHeight")
        scroll_pause_time = 2
        while True:
            driver.execute_script("window.scrollTo(0, documentElement.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == page_height:
                break
            time.sleep = 5
            page_height = new_height
            
        video_titles_xpath = "//*[@id='video-title-link']"
        metadata_xpath = "//div[@id='metadata-line']/span[1]"
        
        video_titles = driver.find_elements(By.XPATH, video_titles_xpath)
        metadata_elements = driver.find_elements(By.XPATH, metadata_xpath)
        
        video_data = {}
        for i in range(min(len(video_titles), len(metadata_elements))):
            title = video_titles[i].text
            metadata_text = metadata_elements[i].text
            if "•"in metadata_text:
                views, time_ago = metadata_text.split("•")
                
            else:
                views = metadata_text
                time_ago = "Неизвестно"
                
            video_data[title] = {"Просмотры": views.strip(), "Published": time_ago.strip()}
        print(video_data)
        
except Exception as e:
    print("Error:", e)
    
finally:
    driver.quit()
        
        
    