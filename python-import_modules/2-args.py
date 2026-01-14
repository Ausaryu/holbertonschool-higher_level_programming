#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argv = sys.argv
argc = len(sys.argv) - 1

if argc == 0:
    print("arguments.")
else:
    print(f"{argc} arguments:")
    for i in range(1, argc + 1):
        print(f"{i}: {argv[i]}")
