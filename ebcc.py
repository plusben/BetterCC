import subprocess
import pyautogui
import pygetwindow as gw
import time

cc_launcher_path = "C:\\CCLauncher-Client-3\\CCLauncher_Client_3.0.exe"

def close_cc_launcher():
    window_title = "Titel des cc-launcher Fensters"
    windows = gw.getWindowsWithTitle(window_title)

    if windows:
        for window in windows:
            if window.isActive == False:
                window.activate()
            window.close()
        time.sleep(2)  # Wartet, damit das Fenster sicher geschlossen wird

def open_and_login():
    subprocess.Popen(cc_launcher_path)
    time.sleep(10)  # Wartet, damit das Programm starten kann

    pyautogui.click(x=1000, y=330)
    pyautogui.write('XXXXX')
    pyautogui.click(x=1000, y=390)
    pyautogui.write('XXXXX')
    pyautogui.click(x=1150, y=450)

def run_continuously(interval):
    while True:
        close_cc_launcher()
        open_and_login()
        time.sleep(interval)  # Wartet eine bestimmte Zeit bis zum nächsten Zyklus

# Setzt das Intervall in Sekunden, z.B. 7200 Sekunden für 2 Stunden
interval = 7200
run_continuously(interval)
