# CLI_synchronizes_two_folders
 A program that synchronizes two folders.


This program is designed to synchronize two folders: a source folder and a replica folder. The program's primary objective is to maintain an exact and complete copy of the source folder in the replica folder. To address this task, you are required to write a Python program.

Key features of the program include:

One-Way Synchronization: The synchronization process is unidirectional, ensuring that after synchronization, the content of the replica folder is modified to precisely match the content of the source folder.

Periodic Synchronization: The program allows for periodic synchronization to ensure that the replica folder stays up to date with any changes in the source folder.

Logging Operations: The program logs all file creation, copying, and removal operations to a designated log file and displays them in the console output for reference and monitoring.

Command Line Arguments: You can specify folder paths, synchronization intervals, and the path to the log file using command line arguments, providing flexibility and customization.

Library Usage: While it is discouraged to use third-party libraries specifically designed for folder synchronization, you are encouraged to leverage external libraries that implement other well-known algorithms. For instance, if you require functionality such as MD5 calculation, it is perfectly acceptable to use third-party or built-in libraries to achieve this.

By implementing this program, you can efficiently synchronize the contents of two folders, keeping the replica folder in sync with changes in the source folder.