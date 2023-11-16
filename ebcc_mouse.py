import subprocess
import pyautogui
import pygetwindow as gw
import time
import json
from datetime import datetime

cc_launcher_path = "C:\\CCLauncher-Client-3\\CCLauncher_Client_3.0.exe"
config_file_path = "config.json"

def load_config():
    with open(config_file_path, 'r') as file:
        return json.load(file)

config = load_config()

def close_cc_launcher():
    window_title = "CC Launcher 3.0"
    confirmation_window_title = "Bestätigung"  # Titel des Bestätigungsfensters
    windows = gw.getWindowsWithTitle(window_title)

    if windows:
        for window in windows:
            if not window.isActive:
                window.activate()
            window.close()
            time.sleep(2)  # Wartet, damit das Fenster sicher geschlossen wird

            # Überprüfen, ob das Bestätigungsfenster erscheint
            confirmation_windows = gw.getWindowsWithTitle(confirmation_window_title)
            if confirmation_windows:
                confirmation_window = confirmation_windows[0]
                confirmation_window.activate()
                time.sleep(2)  # Warten, bis das Fenster aktiv ist

                # Klicken Sie auf die Bestätigungsschaltfläche
                # Ersetzen Sie diese Koordinaten mit den tatsächlichen Koordinaten der Schaltfläche in Ihrem Bestätigungsfenster
                pyautogui.click(x=1000, y=500)

def open_and_login(username, password):
    subprocess.Popen(cc_launcher_path)
    time.sleep(10)

    login_window = gw.getWindowsWithTitle("Login")
    if login_window:
        login_window[0].activate()
        time.sleep(2)

        pyautogui.click(x=1000, y=330)
        pyautogui.write(username)
        pyautogui.click(x=1000, y=390)
        pyautogui.write(password)
        pyautogui.click(x=1150, y=450)
    else:
        print("Login-Fenster wurde nicht gefunden.")

def run_continuously(interval, start_time, end_time):
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))

    while True:
        current_time = datetime.now()
        if start_hour <= current_time.hour < end_hour or (current_time.hour == end_hour and current_time.minute < end_minute):
            close_cc_launcher()
            open_and_login(config['username'], config['password'])
            time.sleep(interval)
        else:
            time.sleep(60)  # Überprüft jede Minute, ob der Zeitplan erreicht ist

run_continuously(config['interval'], config['start_time'], config['end_time'])
