# Folder Size in Gigabytes

This script calculates the size of a folder (including all subfolders and files) in gigabytes (GB).

## Usage

```bash
python get_folder_size_gb.py /path/to/your/folder
```

### Output

The script will print the total size of the specified folder in GB, for example:

```
Size of '/path/to/your/folder': 1.2345 GB
```

## Requirements

- Python 3.x

## Notes

- The script uses only the standard library (`os`, `sys`).
- It recursively walks through all subdirectories and sums up the sizes of all files.

## License

MIT License
