import time
import psutil
import pygetwindow as gw
from pywinauto import Application
import subprocess
from plyer import notification
import re

def close_video_call_window(window_title):
    try:
        video_call_windows = gw.getWindowsWithTitle(window_title)
        for video_call_window in video_call_windows:
            if video_call_window != None:
                video_call_window.close()
                print(f"{window_title} window closed.")
    except Exception as e:
        print(f"Error: {str(e)}")

def close_zoom_app():
    for process in psutil.process_iter():
        try:
            if process.name().lower() == "zoom.exe":
                process.terminate()
                print("Zoom application closed.")
        except Exception as e:
            print(f"Error: {str(e)}")
def close_meet_browser_window(browser_name, browser_title, window_title):
    try:
        browser_windows = gw.getWindowsWithTitle(browser_title)
        for browser_window in browser_windows:
            match = re.search(r"Meet - ([a-zA-Z0-9-]+)$", browser_window.title)
            if match:
                meet_id = match.group(1)
                browser_window.close()
                print(f"Google Meet {meet_id} in {browser_name} browser closed.")
                time.sleep(2)  # Add a delay after closing the browser window
                break
    except Exception as e:
        print(f"Error: {str(e)}")

def reopen_zoom():
    subprocess.Popen(r"C:\Users\Tom\AppData\Roaming\Zoom\bin\Zoom.exe")
    print("Zoom application reopened.")

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Video Call Manager",
        timeout=5
    )

def main():
    video_call_check_interval = 1
    reminder_duration = 20
    time_to_wait = 30
    reopen_delay = 20

    zoom_window_title = 'Zoom Meeting'
    google_meet_title = 'Meet - '

    browsers = [
    {"name": "Firefox", "title": "Mozilla Firefox"},
    {"name": "Brave", "title": "Brave"}
]


    while True:
        elapsed_time = 0
        while True:
            video_call_windows = gw.getWindowsWithTitle(zoom_window_title) + [win for win in gw.getAllWindows() if "Meet - " in win.title]
            if video_call_windows:
                print("Video call window detected.")
                break
            else:
                time.sleep(video_call_check_interval)
                elapsed_time += video_call_check_interval
                print(f"Waiting for video call window... (elapsed time: {elapsed_time} seconds)")

        print(f"Waiting for {reminder_duration/60} minutes before reminding to close the video call...")
        time.sleep(reminder_duration)

        send_notification("Reminder", "Please close the video call.")
        print("Reminder: Please close the video call.")
        print(f"Waiting for an additional {time_to_wait/60 - reminder_duration/60} minutes before closing the video call window...")
        time.sleep(time_to_wait - reminder_duration)

        # Add this line to check for video call windows after waiting
        video_call_windows = gw.getWindowsWithTitle(zoom_window_title) + [win for win in gw.getAllWindows() if "Meet - " in win.title]

        if video_call_windows:
            zoom_windows = gw.getWindowsWithTitle(zoom_window_title)
            google_meet_windows = gw.getWindowsWithTitle(google_meet_title)

            if zoom_windows:
                close_video_call_window(zoom_window_title)
                close_zoom_app()
                send_notification("Too much video chat", "Please email instead.")
                print("Too much video chat, please email.")
                time.sleep(reopen_delay)
                reopen_zoom()
            elif google_meet_windows:
                close_video_call_window(google_meet_title)
                for browser in browsers:
                    close_meet_browser_window(browser['name'], browser['title'], google_meet_title)
                send_notification("Too much video chat", "Please email instead.")
                print("Too much video chat, please email.")
            else:
                # Add a check for manually closed Zoom application
                zoom_process = None
                for process in psutil.process_iter():
                    if process.name().lower() == "zoom.exe":
                        zoom_process = process
                        break

                if zoom_process is None:
                    print("Zoom application was closed manually.")
                    reopen_zoom()

        # Add this line to update the video_call_windows variable
        video_call_windows = gw.getWindowsWithTitle(zoom_window_title) + [win for win in gw.getAllWindows() if "Meet - " in win.title]

if __name__ == "__main__":
    main()