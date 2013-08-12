::for /F "eol=c tokens=1" %%i in (%1) do "C:\Program Files\Mozilla Firefox\firefox.exe" %%i
::for /F "eol=c tokens=1" %%i in (%1) do "C:\Program Files\Google\Chrome\Application\chrome.exe"  --no-startup-window --silent-launch %%i
for /F "eol=c tokens=1" %%i in (%1) do "C:\Program Files\Google\Chrome\Application\chrome.exe" %%i
