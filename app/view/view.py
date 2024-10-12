import tkinter as tk
from tkinter import scrolledtext

class View:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("English Text Summarizer")
        self.window.configure(bg="#f0f0f0")

        tk.Label(self.window, text="URL:", bg="#f0f0f0", fg="#333333", font=("Arial", 12)).pack(padx=10, pady=5, anchor="w")
        self.url_entry = tk.Entry(self.window, width=100, bg="#ffffff", fg="#000000", font=("Arial", 12))
        self.url_entry.pack(padx=10, pady=5, fill=tk.X)

        self.submit_button = tk.Button(self.window, text="Submit", bg="#4CAF50", fg="white", font=("Arial", 12))
        self.submit_button.pack(padx=10, pady=10, fill=tk.X)

        self.loading_label = tk.Label(self.window, text="Still loading please wait..!😘", bg="#f0f0f0", fg="#4CAF50", font=("Arial", 20))
        self.loading_label.pack_forget()

        self.scroll_text = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, width=80, height=20, bg="#ffffff", fg="#000000", font=("Arial", 12))
        self.scroll_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.save_button = tk.Button(self.window, text="Save to Database", bg="#007BFF", fg="white", font=("Arial", 12))
        self.save_button.pack(padx=10, pady=10, fill=tk.X)
        self.save_button.config(state=tk.DISABLED)

    def get_url(self):
        return self.url_entry.get()

    def display_summary(self, summary_text):
        self.scroll_text.delete(1.0, tk.END)
        self.scroll_text.insert(tk.END, summary_text)

    def show_loading(self):
        self.loading_label.pack()

    def hide_loading(self):
        self.loading_label.pack_forget()

    def set_submit_command(self, command):
        self.submit_button.config(command=command)

    def set_save_command(self, command):
        self.save_button.config(command=command)

    def get_summary_text(self):
        return self.scroll_text.get(1.0, tk.END).strip()

    def run(self):
        self.window.mainloop()
