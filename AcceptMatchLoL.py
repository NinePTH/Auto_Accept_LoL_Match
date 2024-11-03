import pyautogui
import time
import tkinter as tk
import threading

# Global variables to control the process
accepted = False
running = False

# Function to print a message (for testing button bind)
def print_something():
    print('Button bind working!')

# Function to search and click the "Accept" button
def autoAccept():
    global accepted, running
    running = True  # Set the flag to start the process
    while not accepted and running:
        res = pyautogui.locateOnScreen("LoLAcceptButton.png", confidence=0.9)
        if res is not None:
            print("Found at:")
            print(res)
            acceptButton = pyautogui.center(res)
            pyautogui.moveTo(acceptButton)
            pyautogui.click()
            accepted = True
        else:
            print("Button not found, retrying...")
            time.sleep(1)
    print("Process stopped.")

# Function to start the process in a separate thread
def start_autoAccept():
    global thread
    thread = threading.Thread(target=autoAccept)
    thread.start()

# Function to stop the process
def stop_autoAccept():
    global running
    running = False  # Set the flag to False to stop the loop

# Setting up the GUI
app = tk.Tk()
app.title('Auto Accept LoL Match')

# Start and Stop buttons
start_button = tk.Button(text='Start', command=start_autoAccept)
start_button.pack()

stop_button = tk.Button(text='Stop', command=stop_autoAccept)
stop_button.pack()

app.mainloop()
