import subprocess
import pyautogui
import pygetwindow as gw
import time

cc_launcher_path = "C:\\CCLauncher-Client-3\\CCLauncher_Client_3.0.exe"

def close_cc_launcher():
    # Ändern Sie diesen Text zum Namen des Fensters des cc-launchers
    window_title = "CC Launcher 3.0"
    windows = gw.getWindowsWithTitle(window_title)

    if windows:
        for window in windows:
            if window.isActive == False:
                window.activate()
            window.close()
        time.sleep(2)  # Wartet, damit das Fenster sicher geschlossen wird

def open_and_login():
    # Startet den cc-launcher
    subprocess.Popen(cc_launcher_path)
    time.sleep(10)  # Wartet, damit das Programm starten kann

    # Führt den Login-Prozess durch
    pyautogui.click(x=1000, y=330)  # Klickt auf das Benutzernamen-Feld
    pyautogui.write('XXXXXXXX')  # Gibt den Benutzernamen ein
    pyautogui.click(x=1000, y=390)  # Klickt auf das Passwort-Feld
    pyautogui.write('XXXXXXXX')  # Gibt das Passwort ein
    pyautogui.click(x=1150, y=450)  # Klickt auf den Login-Button

# Schließt den cc-launcher, falls er geöffnet ist, und startet ihn neu
close_cc_launcher()
open_and_login()
