#                 Assignment
# You need to write a program that finds all “.java” or “.cpp” files in a directory, including all sub-directories (and their sub-directories, etc.)
# Recursive Solution: find_java_files(directory_path)/find_cpp_files(directory_path):
# Scan all items in directory_path.
# For each item:
# Base Case 1: If the item is a file and ends with “.java” or “.cpp”, add it to our list.
# Recursive Step: If the item is a directory, recursively call find_java_files(item_path)/find_cpp_files(item_path).
# 3. Return the final list.

#This program will help you to find all the “.java”  files in a directory, including all sub-directories (and their sub-directories, etc.) using recursion.

import os

def find_java_files(directory_path):

    java_files = []

    for item in os.listdir(directory_path):

        item_path = os.path.join(directory_path, item)

        if os.path.isfile(item_path):
            if item.endswith(".java"):
                java_files.append(item_path)

        elif os.path.isdir(item_path):
            java_files.extend(find_java_files(item_path))

    return java_files

directory = input("Enter directory path: ")

java_results = find_java_files(directory)


print("\nJava files found:")
for file in java_results:
    print(file)

