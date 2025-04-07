#!/usr/bin/python3
import sys
import os

def print_usage():
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)

def get_heap_region(pid):
    """Extract heap memory region from /proc/[pid]/maps"""
    try:
        with open(f"/proc/{pid}/maps", "r") as maps_file:
            for line in maps_file:
                if "[heap]" in line:
                    parts = line.split()
                    addresses = parts[0]
                    perms = parts[1]
                    if "r" in perms and "w" in perms:
                        start, end = addresses.split("-")
                        return int(start, 16), int(end, 16)
    except Exception as e:
        print(f"Error reading heap region: {e}")
        sys.exit(1)
    return None, None

def read_heap(pid, start, end):
    """Read the heap region from /proc/[pid]/mem"""
    try:
        with open(f"/proc/{pid}/mem", "rb") as mem_file:
            mem_file.seek(start)
            return mem_file.read(end - start)
    except Exception as e:
        print(f"Error reading memory: {e}")
        sys.exit(1)

def write_heap(pid, address, data):
    """Write data to a specific memory address"""
    try:
        with open(f"/proc/{pid}/mem", "rb+") as mem_file:
            mem_file.seek(address)
            mem_file.write(data)
    except Exception as e:
        print(f"Error writing to memory: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 4:
        print_usage()

    pid = sys.argv[1]
    search_str = sys.argv[2]
    replace_str = sys.argv[3]

    if len(replace_str) != len(search_str):
        print("Error: search_string and replace_string must be the same length.")
        sys.exit(1)

    # Get heap memory region
    start, end = get_heap_region(pid)
    if not start or not end:
        print("Could not find heap memory region.")
        sys.exit(1)

    # Read heap content
    heap = read_heap(pid, start, end)

    # Find string offset
    index = heap.find(bytes(search_str, "utf-8"))
    if index == -1:
        print("String not found in heap.")
        sys.exit(1)

    # Calculate the exact memory address
    addr = start + index
    print(f"Found '{search_str}' at address {hex(addr)}")

    # Write the new string
    write_heap(pid, addr, bytes(replace_str, "utf-8"))
    print(f"Replaced '{search_str}' with '{replace_str}'")

if __name__ == "__main__":
    main()
