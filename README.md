# CLI_synchronizes_two_folders
A program that synchronizes two folders.

This program is designed to synchronize two folders: a source folder and a replica folder. The program's primary objective is to maintain an exact and complete copy of the source folder in the replica folder. To address this task, you are required to write a Python program.

Key features of the program include:

- **One-Way Synchronization:** The synchronization process is unidirectional, ensuring that after synchronization, the content of the replica folder is modified to precisely match the content of the source folder.

- **Periodic Synchronization:** The program allows for periodic synchronization to ensure that the replica folder stays up to date with any changes in the source folder.

- **Logging Operations:** The program logs all file creation, copying, and removal operations to a designated log file and displays them in the console output for reference and monitoring.

- **Command Line Arguments:** You can specify folder paths, synchronization intervals, and the path to the log file using command line arguments, providing flexibility and customization.

By implementing this program, you can efficiently synchronize the contents of two folders, keeping the replica folder in sync with changes in the source folder.

## Usage

To use the program, you can run it from the command line with the following options:

- `-s` or `--source`: Specify the source folder.
- `-o` or `--output`: Specify the output folder (replica). (Optional; default is "<source_folder>_copy")
- `-i` or `--interval`: Specify the synchronization interval in seconds. (Optional; default is 40 seconds)
- `-l` or `--log`: Specify the path to the log file. (Optional; default is "<source_folder>.log")

### Examples

1. Synchronize the 'source_folder' with default output folder and log file:

```python main.py -s source_folder```

2. Synchronize the 'source_folder' with a custom output folder and log file:

```python main.py -s source_folder -o custom_output -l custom_log.log```

3. Synchronize the 'source_folder' with a custom synchronization interval (e.g., 60 seconds):

```python main.py -s source_folder -i 60```

**Author:** Ivan Shkvyr
**Date:** 2023/10/11
