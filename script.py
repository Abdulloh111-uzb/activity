import os
from datetime import datetime, timedelta

start_date = datetime(2025, 1, 1)
end_date = datetime(2026, 4, 1)

current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d 12:00:00")
    
    with open("file.txt", "a") as f:
        f.write(date_str + "\n")
    
    os.system("git add .")
    os.system(f'git commit --date="{date_str}" -m "commit {date_str}"')
    
    current_date += timedelta(days=1)