# File Hashing – Drag & Drop Application

|<img width="1280" height="640" alt="fileHashing" src="https://github.com/user-attachments/assets/f6b4b6b7-6291-4875-859c-a82112efe680" />|
|---|

A professional desktop tool for instantly calculating cryptographic hashes (MD5, SHA-1, SHA-256, SHA-512) of any file via drag & drop.  
Efficient, secure, and ready for everyday use by IT professionals and end users alike.

<br>

---

<br>

## Features

- **Intuitive Drag & Drop:**  
  Simply drag any file onto the app window to compute its hash values.
- **Multiple Hash Algorithms:**  
  Calculates and displays MD5, SHA-1, SHA-256, and SHA-512 checksums.
- **Modern UI:**  
  Clean dark theme for optimal readability and focus.
- **Immediate Results:**  
  All hash values are displayed instantly upon dropping a file.
- **Robust Error Handling:**  
  Invalid file drops are clearly flagged.

<br>

---

<br>

## Installation

1. **Clone this repository:**
2. 
    ```yarn
    git clone https://github.com/your-username/file-hashing-dragndrop.git
    cd file-hashing-dragndrop
    ```
    
3. **Install dependencies:**  
    Python 3.8+ required.
   
    ```yarn
    pip install tkinterdnd2
    ```
    
    > `tkinter` is included in most standard Python installations.

5. **Run the application:**
6. 
    ```yarn
    python app.py
    ```

<br>

---

<br>

## Usage

- Launch the application.
- Drag and drop any file from your file explorer onto the application window.
- Instantly view MD5, SHA-1, SHA-256, and SHA-512 hash results.

![screenshot example](assets/screenshot.png) <!-- Replace with your screenshot path if available -->

---

## Typical Use Cases

- Verifying file integrity after downloads or transfers.
- Detecting duplicates or changes for cybersecurity purposes.
- Generating cryptographic checksums for compliance and documentation.
- Supporting IT security, software distribution, or forensics workflows.

<br>

---

<br>

## System Requirements

- Python 3.8+
- tkinter (Standard library)
- tkinterdnd2

Works on Windows, macOS, and most Linux distributions.

<br>

---

<br>

## Security Notice

All hash calculations are performed locally on your device.  
No file data is ever transmitted or stored externally.

<br>

---

<br>

## License

This project is licensed under the MIT License.  
See MIT [LICENSE](LICENSE) for details.

---
