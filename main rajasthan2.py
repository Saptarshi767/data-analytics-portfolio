import os
import requests
import pandas as pd
from datetime import datetime, timedelta


def download_excel(date_str, state_code):
    url = f"https://meritindia.in/StateWiseDetails/ExportToExcel?StateCode={state_code}&RecordDate={date_str}&DiscomCode=0"
    response = requests.get(url)
    filename = f"data_{state_code}_{date_str.replace(' ', '_')}.xlsx"
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename


def append_data(filename, date_str, main_df):
    df = pd.read_excel(filename)
    df.insert(0, 'Date', date_str)  
    main_df = pd.concat([main_df, df], ignore_index=True)
    return main_df


def automate_download_append(start_date_str, end_date_str, state_code, save_path):
    start_date = datetime.strptime(start_date_str, "%d %b %Y")
    end_date = datetime.strptime(end_date_str, "%d %b %Y")
    delta = timedelta(days=1)
    
    main_df = pd.DataFrame()  

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%d %b %Y")
        filename = download_excel(date_str, state_code)
        main_df = append_data(filename, date_str, main_df)
        os.remove(filename)  
        current_date += delta
    
    main_df.to_excel(save_path, index=False)  

start_date_str = "9 Jun 2024"
end_date_str = "10 Jun 2024"


state_code = "RJ"


save_path = "C:\\Users\\sapta\\OneDrive\\Desktop\\test4.xlsx"


automate_download_append(start_date_str, end_date_str, state_code, save_path)
