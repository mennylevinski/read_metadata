import os, sys
import win32api

def read_exe_info(path):
    try:
        info = win32api.GetFileVersionInfo(path, '\\')
        lang, codepage = win32api.GetFileVersionInfo(path, '\\VarFileInfo\\Translation')[0]
        string_file_info = f'\\StringFileInfo\\{lang:04X}{codepage:04X}\\'
        fields = [
            "CompanyName", "FileDescription", "FileVersion",
            "InternalName", "OriginalFilename", "ProductName", "ProductVersion"
        ]
        data = {}
        for field in fields:
            try:
                data[field] = win32api.GetFileVersionInfo(path, string_file_info + field)
            except Exception:
                data[field] = None
        return data
    except Exception as e:
        return {"error": str(e)}

def console_ui():
    print("\nEnter a full path to a Windows executable (.exe).")
    print()

    while True:
        exe_path = input("Path to EXE: ").strip().strip('"')

        # Validate input
        if not exe_path:
            print("\n⚠️ Please enter a file path.")
            continue

        if not os.path.isfile(exe_path):
            print("\n❌ File not found. Try again.")
            continue

        # Try to read metadata
        print("\nReading file metadata...\n")
        meta = read_exe_info(exe_path)

        if "error" in meta:
            print(f"❌ Error: {meta['error']}")
        else:
            print("===== Metadata =====")
            for k, v in meta.items():
                print(f"{k}: {v}")
        
        input("\nPress Enter to exit...")
        break


if __name__ == "__main__":
    console_ui()
