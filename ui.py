```python
import tkinter as tk
from constants import APP_TITLE
from utils import format_error_message

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(APP_TITLE)
        self.geometry("800x600")

class ControlPanel(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack(side="left", fill="both", expand=True)

        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.start_button.pack(side="top")

        self.stop_button = tk.Button(self, text="Stop", command=self.stop)
        self.stop_button.pack(side="top")

    def start(self):
        pass

    def stop(self):
        pass

class ImageViewer(tk.Label):
    def __init__(self, parent):
        tk.Label.__init__(self, parent)
        self.pack(side="right", fill="both", expand=True)

    def update_image(self, image_path):
        try:
            image = tk.PhotoImage(file=image_path)
            self.config(image=image)
            self.image = image
        except Exception as e:
            self.config(text=format_error_message(e))
```
