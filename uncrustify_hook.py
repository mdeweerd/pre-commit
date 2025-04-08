import re
import subprocess
import sys

def get_uncrustify_version():
    result = subprocess.run(['uncrustify', '--version'], capture_output=True, text=True)
    match = re.search(r'uncrustify (\d+\.\d+)', result.stdout)
    if match:
        return float(match.group(1))
    return None

def run_uncrustify_with_passes(max_passes, files):
    passes = 0
    changes = 1

    while passes < max_passes and changes != 0:
        result = subprocess.run(['uncrustify', '-c', 'uncrustify.cfg'] + files, capture_output=True, text=True)
        changes = result.returncode
        passes += 1

def main():
    version = get_uncrustify_version()
    if version is None:
        print("Failed to detect uncrustify version.")
        sys.exit(1)

    files = sys.argv[1:]

    if version >= 3.00:
        subprocess.run(['uncrustify', '--max-passes=10', '-c', 'uncrustify.cfg'] + files)
    else:
        run_uncrustify_with_passes(10, files)

if __name__ == "__main__":
    main()
