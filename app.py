```python
import tkinter as tk
from tkinter import messagebox
from ui import MainWindow, ControlPanel, ImageViewer
from api_integration import get_api_response
from image_generator import generate_image
from constants import APP_TITLE
from utils import format_error_message, save_image

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.main_window = MainWindow(self.root)
        self.control_panel = ControlPanel(self.root, self.generate_image)
        self.image_viewer = ImageViewer(self.root)

    def generate_image(self):
        try:
            response = get_api_response()
            image = generate_image(response)
            self.image_viewer.update_image(image)
        except Exception as e:
            messagebox.showerror("Error", format_error_message(e))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    app.run()
```