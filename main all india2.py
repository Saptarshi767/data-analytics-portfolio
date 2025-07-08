import os
import requests
import pandas as pd
from datetime import datetime, timedelta


def download_excel(date_str):
    url = f"https://meritindia.in/StateWiseDetails/ExportToExcel?StateCode=0&RecordDate={date_str}&DiscomCode=0"
    response = requests.get(url)
    filename = f"data_{date_str.replace(' ', '_')}.xlsx"
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename


def append_data(filename, date_str, main_df):
    df = pd.read_excel(filename)
    df.insert(0, 'Date', date_str)  
    main_df = pd.concat([main_df, df], ignore_index=True)
    return main_df


def automate_download_append():
    end_date = datetime.now().date() 
    start_date = end_date - timedelta(days=30)  
    
    main_df = pd.DataFrame()  

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%d %b %Y")
        filename = download_excel(date_str)
        main_df = append_data(filename, date_str, main_df)
        os.remove(filename)  
        current_date += timedelta(days=1)
    
    save_path = "C:\\Users\\sapta\\OneDrive\\Desktop\\test3.xlsx"
    main_df.to_excel(save_path, index=False)  


automate_download_append()
