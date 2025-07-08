import os
import pandas as pd
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download_excel(date_str, state_code, download_dir):
    url = f"https://meritindia.in/StateWiseDetails/ExportToExcel?StateCode={state_code}&RecordDate={date_str}&DiscomCode=0"
    
   
    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": download_dir}
    chrome_options.add_experimental_option("prefs", prefs)
    
    
    service = Service('path_to_chromedriver')  
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
   
    driver.get(url)
    
  
    filename = f"data_{state_code}_{date_str.replace(' ', '_')}.xlsx"
    filepath = os.path.join(download_dir, filename)
    WebDriverWait(driver, 30).until(lambda d: os.path.exists(filepath))
    
    driver.quit()
    return filepath


def append_data(filepath, date_str, main_df):
    df = pd.read_excel(filepath)
    df.insert(0, 'Date', date_str)  
    main_df = pd.concat([main_df, df], ignore_index=True)
    return main_df


def automate_download_append(start_date_str, end_date_str, state_code, save_path, download_dir):
    start_date = datetime.strptime(start_date_str, "%d %b %Y")
    end_date = datetime.strptime(end_date_str, "%d %b %Y")
    delta = timedelta(days=1)
    
    main_df = pd.DataFrame()  

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%d %b %Y")
        try:
            filepath = download_excel(date_str, state_code, download_dir)
            main_df = append_data(filepath, date_str, main_df)
            os.remove(filepath)  
        except Exception as e:
            print(f"Skipping date {date_str} due to error: {e}")
        current_date += delta
    
    main_df.to_excel(save_path, index=False)  


start_date_str = "10 Jun 2024"
end_date_str = "13 Jun 2024"


state_code = "RJ"


download_dir = "C:\\Users\\sapta\\Downloads"


save_path = "C:\\Users\\sapta\\OneDrive\\Desktop\\test3.xlsx"


automate_download_append(start_date_str, end_date_str, state_code, save_path, download_dir)
