"""
This module provides a folder synchronization utility.

This module defines a command-line utility for synchronizing the contents of a
source folder with an output folder. It allows you to specify the
source folder, output folder, synchronization interval, and log file path as
command-line arguments. The utility periodically checks for changes in the
source folder and updates the output folder accordingly. It also logs the copy
actions.

Usage:
    python main.py -s <source_folder> -o <output_folder> -i <interval>
      -l <log_file>

Examples:
    1. Synchronize the 'source_folder' with default output folder and log file:
       python main.py -s source_folder

    2. Synchronize the 'source_folder' with a custom output folder and log file:
       python main.py -s source_folder -o custom_output -l custom_log.log

    3. Synchronize the 'source_folder' with a custom synchronization interval
       (e.g., 60 seconds):
       python main.py -s source_folder -i 60

Author: Ivan Shkvyr
Date: 2023/10/11
"""

import asyncio
import argparse
from logging.handlers import RotatingFileHandler
import logging
from pathlib import Path
from shutil import copyfile, copytree, rmtree
import os


def main_parser():
    """
    Parse command line arguments and set default values for source, output,
    interval, and logging file.

    This function parses the command line arguments using argparse and sets
    default values for source, output, interval, and logging file if they are
    not provided by the user.

    Returns:
        Tuple[Path, Path, int, Path]: A tuple containing the source folder,
        output folder, synchronization interval (in seconds), and the path to
        the log file.
    """
    parser = argparse.ArgumentParser(description="Synchronizes folders")
    parser.add_argument("--source", "-s", help="Source folder", required=True)
    parser.add_argument("--output", "-o", help="Output folder")
    parser.add_argument(
        "--interval",
        "-i",
        help="Synchronization interval,in seconds, default is 40 seconds",
        default=40,
    )
    parser.add_argument("--loggingfile", "-l", help="Log file path")

    args = vars(parser.parse_args())

    source = args.get("source")
    output = args.get("output")
    interval = args.get("interval")
    loggingfile = args.get("loggingfile")

    # Setting default values if not provided.
    output = output or (source + "_copy")
    loggingfile = loggingfile or (source + ".log")

    loggingfile = Path(loggingfile)
    base_folder = Path(source)
    output_folder = Path(output)
    interval = int(interval)

    output_folder.mkdir(parents=True, exist_ok=True)

    return base_folder, output_folder, interval, loggingfile


def grabs_folder(path: Path):
    """
    Get a list of files and directories in the specified folder.

    This function returns a list of files and directories found in the
    specified folder.

    Parameters:
        path (Path): The path to the folder to scan.

    Returns:
        List[Path]: A list of Path objects representing files and directories
        in the folder.
    """
    files_in_base_folder = []
    for el in path.iterdir():
        files_in_base_folder.append(el)
    return files_in_base_folder


async def copy_file(base_path: Path, out_path: Path):
    """
    Copy a file or directory from the source folder to the output folder.

    This function copies a file or directory from the source folder to the
    output folder. It logs the action and handles exceptions if the copy
    operation fails.

    Parameters:
        base_path (Path): The path to the source file or directory.
        out_path (Path): The path to the output folder.

    Returns:
        None
    """
    if base_path.is_file():
        try:
            copyfile(base_path, out_path / base_path.name)
            logging.info("Copied: %s", base_path)
        except OSError as err:
            logging.error(err)
    if base_path.is_dir():
        try:
            copytree(base_path, out_path / base_path.name)
            logging.info("Copied: %s", base_path)
        except OSError as err:
            logging.error(err)


async def main():
    """
    Synchronize folders at regular intervals.

    This is the main function of the program. It configures logging, parses
    command line arguments, and synchronizes the source folder with the output
    folder at regular intervals. It clears the output folder before each
    synchronization and logs the copy actions.

    Returns:
        None
    """
    # Logger configuration
    log_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    console_handler.setLevel(logging.INFO)
    root_logger.addHandler(console_handler)

    base_folder, output_folder, interval, loggingfile = main_parser()

    # Setting up a file log handler
    file_handler = RotatingFileHandler(
                                       loggingfile,
                                       maxBytes=1024000,
                                       backupCount=3,
                                      )
    file_handler.setFormatter(log_format)
    root_logger.addHandler(file_handler)

    while True:
        files_in_base_folder = grabs_folder(base_folder)

        # Clearing the replica folder if there are files present.
        for file_1 in os.scandir(output_folder):
            if file_1.is_file():
                os.remove(file_1.path)
            elif file_1.is_dir():
                rmtree(file_1.path)

        await asyncio.gather(
            *(
                copy_file(file_need_to_copy, output_folder)
                for file_need_to_copy in files_in_base_folder
            )
        )

        # Delay before the next iteration (in seconds)
        await asyncio.sleep(interval)


if __name__ == "__main__":
    asyncio.run(main())
