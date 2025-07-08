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


def automate_download_append(start_date_str, end_date_str, save_path):
    start_date = datetime.strptime(start_date_str, "%d %b %Y")
    end_date = datetime.strptime(end_date_str, "%d %b %Y")
    delta = timedelta(days=1)
    
    main_df = pd.DataFrame()  

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%d %b %Y")
        filename = download_excel(date_str)
        main_df = append_data(filename, date_str, main_df)
        os.remove(filename) 
        current_date += delta
    
    main_df.to_excel(save_path, index=False)  


start_date_str = "1 Jun 2024"
end_date_str = "3 Jun 2024"


save_path = "C:\\Users\\sapta\\OneDrive\\Desktop\\test3.xlsx"


automate_download_append(start_date_str, end_date_str, save_path)
print("Sheet updated")