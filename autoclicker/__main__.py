import tkinter as tk
from tkinter import messagebox, font
import threading
import time
import pyautogui
import random
import tkinter.ttk as ttk

# Global flags
running = False
blink_on = True

# ASCII Art 
HACKER_ASCII = """
╔══════════════════════════════════════════════════════╗
║   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ║
║       ╔═╗╔═╗╦╔═    ╔╦╗╔═╗╔═╗╔╦╗╦═╗╔═╗╦ ╦╔═╗╦═╗       ║
║       ╠═╣╠╣ ╠╩╗     ║║║╣ ╚═╗ ║ ╠╦╝║ ║╚╦╝║╣ ╠╦╝       ║
║       ╩ ╩╚  ╩ ╩    ═╩╝╚═╝╚═╝ ╩ ╩╚═╚═╝ ╩ ╚═╝╩╚═       ║
║   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ║
║              [[ AFK DESTROYER 9000 ]]                ║
║        << AUTOMATED TARGETING SYSTEM v2.1 >>         ║
╚══════════════════════════════════════════════════════╝
"""

def matrix_rain():
    """Create matrix-like rain effect in status"""
    chars = "█▀▄▌▐░▒▓■□▢▣▤▥▦▧▨▩▪▫▬▭▮▯▰▱▲▼◄►◆◇○●◐◑◒◓◔◕"
    prefixes = ["EXECUTING:", "TARGETING:", "PROCESSING:", "DEPLOYING:", "SCANNING:"]
    while running:
        prefix = random.choice(prefixes)
        rain = ''.join(random.choice(chars) for _ in range(25))
        status_label.config(text=f"{prefix} {rain}")
        time.sleep(0.08)
        root.update()

def blink_elements():
    """Create blinking effect for UI elements"""
    global blink_on
    while True:
        blink_on = not blink_on
        color = "lime" if blink_on else "green4"
        try:
            title_label.config(fg=color)
            if not running:
                status_label.config(fg=color)
        except:
            break
        time.sleep(0.7)

def cyber_countdown(seconds):
    """Display a cyber-styled countdown"""
    for i in range(seconds, 0, -1):
        status = f"SYSTEM BOOT SEQUENCE: {i}"
        padding = "=" * (40 - len(status))
        status_label.config(text=f"[{status}{padding}]", fg="yellow")
        root.update()
        time.sleep(0.2)
        status_label.config(text=f"<{status}{padding}>", fg="yellow")
        root.update()
        time.sleep(0.2)
        status_label.config(text=f"({status}{padding})", fg="yellow")
        root.update()
        time.sleep(0.6)

def clicker(delay, clicks, button, x, y):
    curr_click = 0
    matrix_thread = threading.Thread(target=matrix_rain, daemon=True)
    matrix_thread.start()
    
    while running:
        if clicks and curr_click >= clicks:
            break
        if x is not None and y is not None:
            pyautogui.click(x, y, button=button)
        else:
            pyautogui.click(button=button)
        curr_click += 1
        time.sleep(delay)
    stop_clicking()

def start_clicking():
    global running, t
    
    # Get delay from field
    try:
        delay = float(delay_entry.get())
    except ValueError:
        messagebox.showerror("SYSTEM ERROR", "Delay must be a valid number (seconds).")
        return

    # Number of clicks
    clicks_str = clicks_entry.get().strip()
    if clicks_str:
        try:
            clicks_num = int(clicks_str)
            if clicks_num <= 0:
                clicks_num = None
        except ValueError:
            messagebox.showerror("SYSTEM ERROR", "Number of clicks must be a positive integer.")
            return
    else:
        clicks_num = None

    button = button_var.get()
    if button not in ['left', 'right', 'middle']:
        button = 'left'

    # Coordinates
    x_str = x_entry.get().strip()
    y_str = y_entry.get().strip()
    if x_str and y_str:
        try:
            x_coord = float(x_str)
            y_coord = float(y_str)
        except ValueError:
            messagebox.showerror("SYSTEM ERROR", "Coordinates must be numeric.")
            return
    else:
        x_coord, y_coord = None, None

    try:
        start_delay_val = float(start_delay_entry.get())
    except ValueError:
        start_delay_val = 0

    if not running:
        running = True
        if start_delay_val > 0:
            cyber_countdown(int(start_delay_val))
        status_label.config(text="|| TARGET ACQUIRED - EXECUTING ATTACK PROTOCOL ||", fg="red")
        t = threading.Thread(target=clicker, args=(delay, clicks_num, button, x_coord, y_coord), daemon=True)
        t.start()

def stop_clicking():
    global running
    running = False
    status_label.config(text="<< SYSTEM DISENGAGED - AWAITING NEW TARGET >>", fg="orange")

# Setup the main GUI window
root = tk.Tk()
root.title("AFK DESTROYER 9000 - CYBER WARFARE EDITION")
root.configure(bg="black")

# Custom font for more tech feel
default_font = ("Courier New", 12, "bold")
title_font = ("Courier New", 14, "bold")

# Title with ASCII art
title_label = tk.Label(root, text=HACKER_ASCII, bg="black", fg="lime", font=("Courier New", 10))
title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Frame for all controls with a green border
main_frame = tk.Frame(root, bg="black", bd=2, relief="ridge", highlightbackground="lime", highlightthickness=2)
main_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

# Delay field
delay_label = tk.Label(main_frame, text="ATTACK INTERVAL (sec):", bg="black", fg="lime", font=default_font)
delay_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
delay_entry = tk.Entry(main_frame, bg="grey10", fg="lime", insertbackground="lime", font=default_font)
delay_entry.insert(0, "1.0")
delay_entry.grid(row=0, column=1, padx=5, pady=5)

# Number of clicks field
clicks_label = tk.Label(main_frame, text="STRIKE COUNT:", bg="black", fg="lime", font=default_font)
clicks_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
clicks_entry = tk.Entry(main_frame, bg="grey10", fg="lime", insertbackground="lime", font=default_font)
clicks_entry.grid(row=1, column=1, padx=5, pady=5)

# Button type dropdown
button_label = tk.Label(main_frame, text="ATTACK VECTOR:", bg="black", fg="lime", font=default_font)
button_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
button_var = tk.StringVar(value="left")
button_options = tk.OptionMenu(main_frame, button_var, "left", "right", "middle")
button_options.config(bg="grey10", fg="lime", font=default_font, highlightbackground="black", activebackground="grey20")
button_options.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Coordinates
coord_label = tk.Label(main_frame, text="TARGET COORDINATES [X:Y]:", bg="black", fg="lime", font=default_font)
coord_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
coord_frame = tk.Frame(main_frame, bg="black")
coord_frame.grid(row=3, column=1, padx=5, pady=5)
x_entry = tk.Entry(coord_frame, width=8, bg="grey10", fg="lime", insertbackground="lime", font=default_font)
x_entry.pack(side="left", padx=(0,5))
y_entry = tk.Entry(coord_frame, width=8, bg="grey10", fg="lime", insertbackground="lime", font=default_font)
y_entry.pack(side="left")

# Start Delay field
start_delay_label = tk.Label(main_frame, text="DEPLOYMENT DELAY (sec):", bg="black", fg="lime", font=default_font)
start_delay_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
start_delay_entry = tk.Entry(main_frame, bg="grey10", fg="lime", insertbackground="lime", font=default_font)
start_delay_entry.insert(0, "3")
start_delay_entry.grid(row=4, column=1, padx=5, pady=5)

# Status display with "tech" border
status_frame = tk.Frame(root, bg="black", bd=2, relief="ridge", highlightbackground="lime", highlightthickness=1)
status_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
status_label = tk.Label(status_frame, text="SYSTEM READY - AWAITING DEPLOYMENT", bg="black", fg="orange", font=default_font)
status_label.pack(pady=5)

# Control buttons frame
button_frame = tk.Frame(root, bg="black")
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

# Create custom style for buttons
style = ttk.Style()
style.theme_use('default')  # Use default theme as base

# Configure the button styles with more specific options
style.configure('Cyber.TButton',
                font=default_font,
                foreground='lime',
                background='black',
                borderwidth=0,
                relief='flat',
                padding=5)
style.map('Cyber.TButton',
          foreground=[('active', 'green'), ('pressed', 'green4')],
          background=[('active', 'black'), ('pressed', 'black')],
          relief=[('pressed', 'flat'), ('!pressed', 'flat')])

style.configure('Cyber.Danger.TButton',
                font=default_font,
                foreground='red',
                background='black',
                borderwidth=0,
                relief='flat',
                padding=5)
style.map('Cyber.Danger.TButton',
          foreground=[('active', 'darkred'), ('pressed', '#8B0000')],
          background=[('active', 'black'), ('pressed', 'black')],
          relief=[('pressed', 'flat'), ('!pressed', 'flat')])

# Override default button layout to remove border
style.layout('Cyber.TButton', [
    ('Button.padding', {'children': [
        ('Button.label', {'sticky': 'nswe'})
    ], 'sticky': 'nswe'})
])
style.layout('Cyber.Danger.TButton', [
    ('Button.padding', {'children': [
        ('Button.label', {'sticky': 'nswe'})
    ], 'sticky': 'nswe'})
])

# Styled buttons
start_button = ttk.Button(button_frame, text="[ ENGAGE ]", command=start_clicking, 
                         style='Cyber.TButton', width=12)
start_button.pack(side="left", padx=5)

stop_button = ttk.Button(button_frame, text="[ ABORT ]", command=stop_clicking,
                        style='Cyber.Danger.TButton', width=12)
stop_button.pack(side="left", padx=5)

quit_button = ttk.Button(button_frame, text="[ TERMINATE ]", command=root.quit,
                        style='Cyber.Danger.TButton', width=14)
quit_button.pack(side="left", padx=5)

# Start blinking thread
blink_thread = threading.Thread(target=blink_elements, daemon=True)
blink_thread.start()

# Add system initialization message
def show_boot_sequence():
    messages = [
        "INITIALIZING CYBER WARFARE PROTOCOLS...",
        "LOADING TARGETING ALGORITHMS...",
        "CALIBRATING CLICK MATRICES...",
        "ESTABLISHING TACTICAL INTERFACE...",
        "SYSTEM READY FOR DEPLOYMENT"
    ]
    for msg in messages:
        status_label.config(text=msg, fg="lime")
        root.update()
        time.sleep(0.5)
    status_label.config(text="<< TACTICAL SYSTEM ARMED - AWAITING ORDERS >>", fg="orange")

# Show boot sequence after window is ready
root.after(500, show_boot_sequence)

# Center window on screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

root.mainloop() 