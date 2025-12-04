## 📝 EXE Metadata Reader (Windows)

A simple Python tool that extracts version and metadata information from any Windows `.exe` file.<br>
It uses win32api (from pywin32) to read the embedded version info and displays fields like:

- Company Name
- File Description
- File Version
- Product Name
- Product Version
- Original Filename
- Internal Name

Useful for forensics, malware analysis, software auditing, or simply identifying unknown executables.

## 📦 Requirements
-Python version
`Python 3.0+`

- Required package pywin32:
`pip install pywin32`

## ▶️ How to Use
- Double click or Run the script from CMD:
`python exe_info_reader.py`

- You will be prompted to enter the full path to an executable:<br>
`Enter a full path to a Windows executable (.exe)`<br>
`Path to EXE: C:\Users\You\Desktop\program.exe`
