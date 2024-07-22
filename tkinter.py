import tkinter as tk

def count_lines():
    num_lines = text_box.index('end-1c').split('.')[0]  # Get total number of lines
    line_numbers.config(state=tk.NORMAL)
    line_numbers.delete('1.0', tk.END)
    for line in range(1, int(num_lines) + 1):
        line_numbers.insert(tk.END, f'{line}\n')
    line_numbers.config(state=tk.DISABLED)

window = tk.Tk()
window.configure(background="#545454")
window.title("Roblox Cheat Loader")

# Top frame for top_text labels
top_frame = tk.Frame(master=window, height=30, width=100, bg="#424242")
top_frame.grid(row=0, column=0, columnspan=3, sticky="ew")

# Labels in the top_frame
top_text1 = tk.Label(master=top_frame, text="0x Exploit", height=2, fg="white", bg="#424242")
top_text1.grid(row=0, column=0, padx=(10, 0), sticky="w")

top_text2 = tk.Label(master=top_frame, text="Uninjected", fg="white", bg="#424242")
top_text2.grid(row=0, column=1, padx=20)

top_text3 = tk.Label(master=top_frame, text="Numbers :3", fg="white", bg="#424242")
top_text3.grid(row=0, column=2, padx=40)

top_text4 = tk.Label(master=top_frame, text="Version: UwU", fg="white", bg="#424242")
top_text4.grid(row=0, column=3, padx=(0, 320), sticky="e")

# Buttons and their frames
inject_frame = tk.Frame(master=window, height=10, width=40, bg="#545454")
inject_frame.grid(row=2, column=0, sticky="w")

inject_button = tk.Button(master=inject_frame, text="Inject", width=6, height=1, fg="white", bg="#424242")
inject_button.pack(pady=0, padx=10)

settings_frame = tk.Frame(master=window, height=10, width=40, bg="#545454")
settings_frame.grid(row=3, column=0, sticky="w")

settings_button = tk.Button(master=settings_frame, text="Settings", width=6, height=1, fg="white", bg="#424242")
settings_button.pack(pady=5, padx=10)

refresh_frame = tk.Frame(master=window, bg="#545454")
refresh_frame.grid(row=4, column=0, sticky="w")

refresh_button = tk.Button(master=refresh_frame, text="Refresh", width=6, height=1, fg="white", bg="#424242")
refresh_button.pack(pady=5, padx=10)

execute_frame = tk.Frame(master=window, bg="#545454")
execute_frame.grid(row=5, column=0, sticky="w")

execute_button = tk.Button(master=execute_frame, text="Execute", width=6, height=1, fg="white", bg="#424242")
execute_button.pack(pady=5, padx=10)

load_frame = tk.Frame(master=window, bg="#545454")
load_frame.grid(row=6, column=0, sticky="w")

load_button = tk.Button(master=load_frame, text="Load", width=6, height=1, fg="white", bg="#424242")
load_button.pack(pady=5, padx=10)

# The Text Box
text_box = tk.Text(fg="white", bg="black")
text_box.grid(row=1, rowspan=6, column=2, columnspan=3, sticky="nsew")

# Line number widget
line_numbers = tk.Text(window, width=4, bg="#333333", fg="white", bd=0, padx=4, wrap=tk.NONE)
line_numbers.grid(row=1, rowspan=6, column=5, sticky="ns")

# Count lines and update line numbers
count_lines()

window.mainloop()
