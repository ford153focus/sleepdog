from datetime import datetime
import subprocess
from time import ctime
import ntplib

def exec(command):
    try:
        print( subprocess.check_output(command, shell=True).decode(encoding="UTF-8",errors="ignore").strip() )
    except Exception as e:
        print(e)

try:
    #exec("TASKKILL /IM left4dead.exe /T /F")
    exec("TASKKILL /IM left4dead2.exe /T /F")
    exec("TZUTIL /s \"Russian Standard Time\"")
except Exception as e:
    print(e)

ntp_time_string = ctime(ntplib.NTPClient().request('europe.pool.ntp.org', version=3).tx_time)
datetime_encoded_string = datetime.strptime(ntp_time_string, '%a %b %current_date %H:%M:%S %Y')
current_date = str(datetime_encoded_string.day) + '-' + str(datetime_encoded_string.month) + '-' + str(datetime_encoded_string.year)
cureent_time = str(datetime_encoded_string.hour) + ':' + str(datetime_encoded_string.minute)
exec("time " + cureent_time)
exec("date " + current_date)

if (datetime.now().time().hour > 0):
    if (datetime.now().time().hour < 5):
        exec("shutdown /s /f /cureent_time 0")

print("task complete")