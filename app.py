import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import hashlib
import os

class HashingApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Hashing")
        self.geometry("600x420")
        self.configure(bg="#23272e")

        self.label_info = tk.Label(self, text="Drag & drop a file here", bg="#23272e", fg="#56c7ff", font=("Segoe UI", 16, "bold"))
        self.label_info.pack(pady=25)

        self.drop_area = tk.Label(self, text="🗂️ Drop your file here", bg="#303542", fg="#c1c1c1", width=60, height=6, font=("Segoe UI", 13, "bold"), relief="groove", borderwidth=3)
        self.drop_area.pack(pady=10)
        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind('<<Drop>>', self.handle_drop)

        self.result_frame = tk.Frame(self, bg="#23272e")
        self.result_frame.pack(pady=10, fill="both", expand=True)

        self.result_labels = {}

        for algo in ["MD5", "SHA1", "SHA256", "SHA512"]:
            lbl = tk.Label(self.result_frame, text=f"{algo}:", anchor="w", bg="#23272e", fg="#eee", font=("Consolas", 11))
            lbl.pack(fill="x", padx=30, pady=2)
            self.result_labels[algo] = lbl

    def handle_drop(self, event):
        file_path = event.data.strip("{}")
        if not os.path.isfile(file_path):
            self.label_info.config(text="Invalid file!", fg="#ff5151")
            return

        self.label_info.config(text=os.path.basename(file_path), fg="#56c7ff")
        hashes = self.calculate_hashes(file_path)
        for algo, value in hashes.items():
            self.result_labels[algo].config(text=f"{algo}: {value}")

    def calculate_hashes(self, file_path):
        hash_algos = {
            "MD5": hashlib.md5(),
            "SHA1": hashlib.sha1(),
            "SHA256": hashlib.sha256(),
            "SHA512": hashlib.sha512()
        }
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                for h in hash_algos.values():
                    h.update(chunk)
        return {name: h.hexdigest() for name, h in hash_algos.items()}

if __name__ == "__main__":
    try:
        from tkinterdnd2 import TkinterDnD
    except ImportError:
        print("Please run: pip install tkinterdnd2")
        exit(1)

    app = HashingApp()
    app.mainloop()
