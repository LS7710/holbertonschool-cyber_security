#!/usr/bin/python3
"""
Reads and modifies the heap of a running process by replacing a given string.
Usage: read_write_heap.py pid search_string replace_string
"""

import sys
import os

def usage():
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)

def read_heap(pid):
    """Reads the heap memory range from /proc/[pid]/maps"""
    try:
        with open(f"/proc/{pid}/maps", 'r') as maps_file:
            for line in maps_file:
                if "[heap]" in line:
                    parts = line.split()
                    addr_range = parts[0]
                    return addr_range
    except Exception as e:
        print(f"Error reading /proc/{pid}/maps: {e}")
        sys.exit(1)
    print("Heap not found in memory maps.")
    sys.exit(1)

def replace_in_heap(pid, search_str, replace_str):
    """Find and replace a string in the heap of a given process."""
    heap_range = read_heap(pid)
    start_str, end_str = heap_range.split('-')
    start = int(start_str, 16)
    end = int(end_str, 16)

    try:
        with open(f"/proc/{pid}/mem", 'rb+') as mem_file:
            mem_file.seek(start)
            heap_data = mem_file.read(end - start)

            offset = heap_data.find(search_str.encode())
            if offset == -1:
                print(f"'{search_str}' not found in heap.")
                return

            print(f"Found '{search_str}' at offset {hex(start + offset)}")

            mem_file.seek(start + offset)

            # Only write up to the original length
            if len(replace_str) > len(search_str):
                print("Error: replacement string is longer than search string.")
                sys.exit(1)

            # Pad with null bytes if needed
            replace_bytes = replace_str.encode().ljust(len(search_str), b'\x00')
            mem_file.write(replace_bytes)
            print(f"Replaced '{search_str}' with '{replace_str}' in heap memory.")

    except PermissionError:
        print("Permission denied. Try running the script with sudo.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: process does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Error accessing memory: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 4:
        usage()

    pid, search_str, replace_str = sys.argv[1:]
    if not pid.isdigit():
        usage()

    replace_in_heap(pid, search_str, replace_str)

if __name__ == "__main__":
    main()
