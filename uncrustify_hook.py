#!python3
import re
import subprocess
import sys

def get_uncrustify_version():
    result = subprocess.run(['uncrustify', '--version'], capture_output=True, text=True)
    match = re.search(r'uncrustify[ -](\d+\.\d+)', result.stdout, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return None

def run_uncrustify_with_passes(max_passes, uncrustify_arguments):
    passes = 0
    changes = 1

    while passes < max_passes and changes != 0:
        print(f"Pass passes {passes}<{max_passes}")
        result = subprocess.run(['uncrustify'] + uncrustify_arguments, capture_output=True, text=True)
        changes = result.returncode
        print(f"{result!r}")
        passes += 1

def main():
    version = get_uncrustify_version()
    if version is None:
        print("Failed to detect uncrustify version.")
        sys.exit(1)

    args = sys.argv[1:]
    max_passes = 10
    uncrustify_args = []

    config_file = False

    i = 0
    while i < len(args):
        arg = args[i]
        i += 1
        if version < 3.00:
            if arg.startswith('--max-passes='):
                max_passes = int(arg.split('=')[1])
                continue
            elif arg == '--max-passes':
                max_passes = int(args[i])
                i += 1  # Skip the next argument
                continue
        if arg in ['--replace', '--no-backup', '-q']:
            continue

        if arg in ['-c', '--config']:
            config_file = True
        uncrustify_args.append(arg)

    uncrustify_args = ["--replace", "--no-backup","-q"] + uncrustify_args
    if config_file is False:
        uncrustify_args = ['-c', 'uncrustify.cfg'] + uncrustify_args

    print(f"{uncrustify_args!r}")
    if version >= 3.00:
        subprocess.run(['uncrustify'] + uncrustify_args)
    else:
        run_uncrustify_with_passes(max_passes, uncrustify_args)

if __name__ == "__main__":
    main()
