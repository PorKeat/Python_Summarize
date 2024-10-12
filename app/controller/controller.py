import threading
from tkinter import messagebox
from app.model.model import Model
from app.view.view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

        self.view.set_submit_command(self.on_submit)
        self.view.set_save_command(self.on_save)

    def on_submit(self):
        url = self.view.get_url()
        self.view.show_loading()
        self.view.submit_button.config(state="disabled")

        thread = threading.Thread(target=self.fetch_and_display_summary, args=(url,))
        thread.start()

    def fetch_and_display_summary(self, url):
        try:
            summary = self.model.fetch_and_summarize(url)
            self.view.display_summary(summary)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.view.hide_loading()
            self.view.submit_button.config(state="normal")
            self.view.save_button.config(state="normal")

    def on_save(self):
        url = self.view.get_url()
        summary_text = self.view.get_summary_text()

        if summary_text:
            success = self.model.save_summary(url, summary_text)
            if success:
                messagebox.showinfo("Success", "Summary saved to database!")
            else:
                messagebox.showerror("Error", "Failed to save summary to database.")
        else:
            messagebox.showwarning("Warning", "No summary to save.")

    def run(self):
        self.view.run()
        self.model.close_connection()
