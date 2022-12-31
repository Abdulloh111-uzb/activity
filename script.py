import os
from datetime import datetime, timedelta

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    with open("file.txt", "a") as f:
        f.write(f"data {date_str}\n")
    
    os.system("git add .")
    os.system(f'git commit --date="{date_str}" -m "commit on {date_str}"')
    
    current_date += timedelta(days=1)