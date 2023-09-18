```python
import tkinter as tk
from app import MainApp
from constants import APP_TITLE
from utils import format_error_message

def main():
    try:
        root = tk.Tk()
        root.title(APP_TITLE)
        app = MainApp(root)
        root.mainloop()
    except Exception as e:
        print(format_error_message(e))

if __name__ == "__main__":
    main()
```