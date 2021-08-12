'''
Title: Automation File Sorter
Author: Naeem Patel
Date: 2021-08-11
Software Link: https://github.com/mayfled/File_sorter
'''

import os
import sys
from typing import List

FILENAME_LENGTH = 20


def split_into_components(filename: str) -> List[str]:
    # Will work only if the length of the filename is == FILENAME_LENGTH
    if len(filename) != FILENAME_LENGTH:
        return []

    type = filename[0:2]
    three_digit_code = filename[2:5]
    # Skipping the dot in between
    dd = filename[6:8]
    mm = filename[8:10]
    yy = filename[10:12]
    remaining = filename[12:]

    return [type, three_digit_code, dd, mm, yy, remaining]


def create_dirs(yy: str, mm: str, dd: str, type: str, prev_path: str) -> str:
    """
    Creates the directories if they're not already there, in the order defined above in the docstring
    And then returns the relative path to folder it's currently in which would be `prev_path/yy/mm/dd/type`
    """
    if not os.path.isdir(yy):
        os.mkdir(yy)
    os.chdir(yy)
    if not os.path.isdir(mm):
        os.mkdir(mm)
    os.chdir(mm)
    if not os.path.isdir(dd):
        os.mkdir(dd)
    os.chdir(dd)
    if not os.path.isdir(type):
        os.mkdir(type)
    os.chdir(type)

    current_path = os.path.relpath(os.getcwd(), prev_path)

    # Moving back to the original directory
    os.chdir(prev_path)

    return current_path


def move_file(src: str, dest: str) -> None:
    """
    Moves a file from src to dest
    """
    os.rename(os.path.abspath(src), os.path.abspath(dest))


def main(dir_to_search: str) -> None:
    total_count = 0
    success_count = 0
    failure_count = 0

    # Moving into the directory to search, so we can later move with respect to relative paths
    os.chdir(dir_to_search)

    for file in os.listdir():
        if os.path.isfile(file):
            try:
                segments = split_into_components(file)
                total_count += 1

                # If the length of the file is != 20, segments = []
                if len(segments) == 0:
                    print("%s was not moved" % file)
                    continue

                # Extracting the variables required
                type, three_digit_code, dd, mm, yy, remaining = segments

                # Creates the necessary directories if they're not already there
                dest_folder = create_dirs(
                    yy, mm, dd, type, os.getcwd())

                # Creates relative paths for src and destination
                src_path = os.path.join(".", file)
                dest_path = os.path.join(".", dest_folder, file)

                move_file(src_path, dest_path)
                print("%s moved successfully to %s" % (file, dest_path))

                success_count += 1

            # If there's an exception we say that the file failed
            except Exception as e:
                print("%s failed" % file)
                print("Error:", e)
                failure_count += 1

    # Final Stats
    print("\nTotal files: %d\nSuccess: %d\nFailed: %d" %
          (total_count, success_count, failure_count))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python organize.py <directory>")
        exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Error: Invalid Directory")
        exit(1)

    main(directory)
