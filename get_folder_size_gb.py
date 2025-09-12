import os
import sys

def get_folder_size_bytes(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size

def bytes_to_gb(size_bytes):
    return size_bytes / (1024 ** 3)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_folder_size_gb.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        sys.exit(1)

    size_bytes = get_folder_size_bytes(folder_path)
    size_gb = bytes_to_gb(size_bytes)
    print(f"Size of '{folder_path}': {size_gb:.4f} GB")
