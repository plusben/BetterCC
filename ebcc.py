import subprocess
import pyautogui
import pygetwindow as gw
import time

cc_launcher_path = "C:\\CCLauncher-Client-3\\CCLauncher_Client_3.0.exe"
login_window_title = "Login"  # Ändern Sie dies zum exakten Titel des Login-Fensters

def close_cc_launcher():
    window_title = "CC Launcher 3.0"
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

    # Findet und aktiviert das Login-Fenster
    login_window = gw.getWindowsWithTitle(login_window_title)
    if login_window:
        login_window[0].activate()
        time.sleep(2)  # Wartet, bis das Fenster aktiv ist

        # Hier erfolgen die Eingaben
        pyautogui.click(x=1000, y=330)
        pyautogui.write('Benutzername')  # Ersetzen Sie dies mit dem tatsächlichen Benutzernamen
        pyautogui.click(x=1000, y=390)
        pyautogui.write('Passwort')  # Ersetzen Sie dies mit dem tatsächlichen Passwort
        pyautogui.click(x=1150, y=450)
    else:
        print("Login-Fenster wurde nicht gefunden.")

def run_continuously(interval):
    while True:
        close_cc_launcher()
        open_and_login()
        time.sleep(interval)  # Wartet eine bestimmte Zeit bis zum nächsten Zyklus

interval = 7200  # 2 Stunden
run_continuously(interval)
