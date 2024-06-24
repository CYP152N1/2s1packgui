import tkinter as tk
from tkinter import ttk
import logging
from datetime import datetime

# Dictionary to manage button states
button_state = {}
# Dictionary to manage container names
container_names = {1: 'Container 1', 2: 'Container 2', 3: 'Container 3'}
# Dictionary to manage container statuses
container_status = {1: False, 2: False, 3: False}

# Global variable to manage mounted state
gonio = False
mounted_button = None

# Global variable to manage hold state
hold = False
held_button = None

# Variable to store the default button color
default_bg = None

# Logging setup
log_filename = datetime.now().strftime("%y%m%d_sample.log")
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s: %(message)s', datefmt='%H%M')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s: %(message)s', datefmt='%H%M')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# Setup the log textbox
def setup_log_textbox(tab):
    log_textbox = tk.Text(tab, height=5, state='disabled')
    log_textbox.grid(row=18, column=0, columnspan=3, sticky='nsew')
    scrollbar = tk.Scrollbar(tab, command=log_textbox.yview)
    scrollbar.grid(row=18, column=3, sticky='nsew')
    log_textbox['yscrollcommand'] = scrollbar.set
    return log_textbox

def log_message(message):
    logging.info(message)
    log_textbox_load.config(state='normal')
    log_textbox_mount.config(state='normal')
    log_textbox_move.config(state='normal')
    timestamp = datetime.now().strftime("%H%M")
    log_textbox_load.insert(tk.END, f"{timestamp}: {message}\n")
    log_textbox_mount.insert(tk.END, f"{timestamp}: {message}\n")
    log_textbox_move.insert(tk.END, f"{timestamp}: {message}\n")
    log_textbox_load.config(state='disabled')
    log_textbox_mount.config(state='disabled')
    log_textbox_move.config(state='disabled')

def button_callback_load(button_name):
    global default_bg
    col = int(button_name.split('-')[0])
    if container_status[col]:
        if button_state[button_name] == 'default':
            log_message(f"{button_name} is loaded")
            button_state[button_name] = 'loaded'
        elif button_state[button_name] == 'loaded':
            log_message(f"{button_name} is unloaded")
            button_state[button_name] = 'default'
    update_buttons()

def button_callback_mount(button_name):
    global default_bg, mounted_button, gonio
    col = int(button_name.split('-')[0])
    if hold:
        log_message(f"{held_button} has been held on check, {button_name} cannot be treated.")
        return
    if container_status[col]:
        if gonio is False:
            if button_state[button_name] == 'loaded':
                log_message(f"{button_name} is mounted")
                button_state[button_name] = 'mounted'
                mounted_button = button_name
                gonio = True
            elif button_state[button_name] == 'default':
                log_message(f"{button_name} has not been loaded")
        elif gonio is True:
            if button_state[button_name] == 'mounted':
                log_message(f"{button_name} is unmounted")
                button_state[button_name] = 'loaded'
                mounted_button = None
                gonio = False
            elif button_state[button_name] == 'default':
                log_message(f"{mounted_button} was unmounted and moved to {button_name}")
                button_state[mounted_button] = 'default'
                button_state[button_name] = 'loaded'
                mounted_button = button_name
                gonio = False
            elif button_state[button_name] == 'loaded':
                log_message("other sample has been still mounted on gonio")
    update_buttons()

def button_callback_move(button_name):
    global default_bg, hold, held_button
    col = int(button_name.split('-')[0])
    if container_status[col]:
        if hold is False:
            if button_state[button_name] == 'loaded':
                log_message(f"{button_name} is held")
                button_state[button_name] = 'held'
                held_button = button_name
                hold = True
            elif button_state[button_name] == 'default':
                log_message(f"{button_name} has not been loaded")
            elif button_state[button_name] == 'mounted':
                log_message(f"{button_name} has been mounted on gonio")
        elif hold is True:
            if button_state[button_name] == 'held':
                log_message(f"{button_name} is released")
                button_state[button_name] = 'loaded'
                held_button = None
                hold = False
            elif button_state[button_name] == 'default':
                log_message(f"{held_button} is moved to {button_name}")
                button_state[held_button] = 'default'
                button_state[button_name] = 'loaded'
                held_button = None
                hold = False
            elif button_state[button_name] == 'mounted':
                log_message(f"{button_name} has been mounted on gonio")
            elif button_state[button_name] == 'loaded':
                log_message(f"{button_name} has been loaded. {held_button} cannot move to {button_name}")
    update_buttons()

def create_buttons(frame, mode):
    global default_bg
    for col in range(3):
        # Create container status button
        container_button = tk.Button(
            frame,
            text=f"Enable {col+1}",
            width=15,
            height=2,
            command=lambda c=col+1: toggle_container(c),
            state='normal' if mode == 'load' else 'disabled'
        )
        if default_bg is None:
            default_bg = container_button.cget('bg')  # Get the default color
        container_button.grid(row=0, column=col, padx=5, pady=5)
        container_button._col = col + 1

        # Create entry for container name
        container_name_var = tk.StringVar(value=container_names[col+1])
        if mode == 'load':
            entry = tk.Entry(frame, textvariable=container_name_var, width=15)
            entry.bind("<FocusOut>", lambda e, col=col+1: update_container_name(e, col))
        else:
            entry = tk.Entry(frame, textvariable=container_name_var, width=15, state='readonly')
        entry.grid(row=1, column=col, padx=5, pady=5)

        for row in range(16):
            # Create button name
            button_name = f"{col+1}-{row+1:02d}"
            if button_name not in button_state:
                button_state[button_name] = 'default'

            # Create button
            button = tk.Button(
                frame,
                text=button_name,
                width=10,
                height=2,
                command=lambda bn=button_name, m=mode: button_callback(bn, m),
                state='normal' if container_status[col+1] else 'disabled'
            )
            button.grid(row=row+2, column=col, padx=5, pady=5)  # Shift down by 2 rows for the entry and container button
            button._name = button_name
            button._mode = mode
            update_button_color(button, button_name)

def toggle_container(col):
    container_status[col] = not container_status[col]
    log_message(f"Container {col} enabled: {container_status[col]}")
    update_buttons()
    # Set button enabled/disabled based on updated status
    for widget in notebook.winfo_children():
        for subwidget in widget.winfo_children():
            if isinstance(subwidget, tk.Button):
                if hasattr(subwidget, '_name'):
                    button_name = subwidget._name
                    try:
                        if int(button_name.split('-')[0]) == col:
                            subwidget.config(state='normal' if container_status[col] else 'disabled')
                    except ValueError:
                        continue
                elif hasattr(subwidget, '_col'):
                    subwidget.config(bg='light green' if container_status[subwidget._col] else default_bg)

def update_container_name(event, col):
    container_names[col] = event.widget.get()
    log_message(f"Container {col} name updated to: {container_names[col]}")
    update_buttons()

def button_callback(button_name, mode):
    if mode == 'load':
        button_callback_load(button_name)
    elif mode == 'mount':
        button_callback_mount(button_name)
    elif mode == 'move':
        button_callback_move(button_name)

def update_buttons():
    for widget in notebook.winfo_children():
        for subwidget in widget.winfo_children():
            if isinstance(subwidget, tk.Button):
                if hasattr(subwidget, '_name'):
                    button_name = subwidget._name
                    try:
                        col = int(button_name.split('-')[0])
                        update_button_color(subwidget, button_name)
                    except ValueError:
                        continue
                elif hasattr(subwidget, '_col'):
                    subwidget.config(bg='light green' if container_status[subwidget._col] else default_bg)

def update_button_color(button, button_name):
    if button_state[button_name] == 'default':
        button.config(bg=default_bg)
    elif button_state[button_name] == 'loaded':
        button.config(bg='light blue')
    elif button_state[button_name] == 'mounted':
        button.config(bg='red')
    elif button_state[button_name] == 'held':
        button.config(bg='yellow')

# Create the main window
root = tk.Tk()
root.title("Storage Container Management System")

# Create the notebook widget
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Create Load tab
load_frame = ttk.Frame(notebook)
notebook.add(load_frame, text='Load')
create_buttons(load_frame, 'load')

# Create Mount tab
mount_frame = ttk.Frame(notebook)
notebook.add(mount_frame, text='Mount')
create_buttons(mount_frame, 'mount')

# Create Move tab
move_frame = ttk.Frame(notebook)
notebook.add(move_frame, text='Move')
create_buttons(move_frame, 'move')

# Create log textboxes
log_textbox_load = setup_log_textbox(load_frame)
log_textbox_mount = setup_log_textbox(mount_frame)
log_textbox_move = setup_log_textbox(move_frame)

# Run the GUI
root.mainloop()

