# unicode sheriff v1.7

import os
import argparse
import shutil

def print_horizontal_line():
    try:
        columns, _ = os.get_terminal_size(0)
    except OSError:
        columns = 80  # fallback value
    print('-' * columns)

def clean_invalid_utf8(filename, auto, overwrite, move_old):
    with open(filename, 'rb') as f:
        bytes_data = f.read()

    # Decode the bytes to a string, replacing any invalid sequences
    string_data = bytes_data.decode('utf-8', 'replace')

    # Split the string into lines
    lines = string_data.split('\n')

    # Process each line
    error_count = 0
    i = 0
    while i < len(lines):
        if '\ufffd' in lines[i]:
            error_count += lines[i].count('\ufffd')
            if not auto:
                # Show the offending line and ask for confirmation
                print_horizontal_line()
                print(f'Offending line in {filename}:{i+1}:')
                print_horizontal_line()
                print(lines[i])
                print_horizontal_line()
                confirm = input('Do you want to remove the invalid UTF-8 sequence from this line? [(y)es / (n)o / (a)ll] ')
                if confirm.lower() == 'y':
                    # Remove the replacement character from the line
                    lines[i] = lines[i].replace('\ufffd', '')
                    i += 1
                elif confirm.lower() == 'a':
                    # Remove the replacement character from the line and fix all errors in the file
                    lines[i] = lines[i].replace('\ufffd', '')
                    i += 1
                    auto = True
                else:
                    # Move on to the next line without making any changes
                    i += 1
            else:
                # Remove the replacement character from the line
                lines[i] = lines[i].replace('\ufffd', '')
                i += 1
        else:
            i += 1

    if error_count == 0:
        print(f'No errors found in file: {filename}')
        return

    # Join the lines back into a string
    string_data = '\n'.join(lines)

    # Re-encode the string to bytes
    bytes_data = string_data.encode('utf-8')

    # Check if the output file already exists
    fixed_filename = filename.replace('.txt', '_utf8fixed.txt')
    if os.path.exists(fixed_filename) and not overwrite:
        print(f'{fixed_filename} already exists. Skipping...')
        return

    if move_old:
        # Create the 'old' directory if it doesn't exist
        old_dir = os.path.join(os.path.dirname(filename), 'old')
        os.makedirs(old_dir, exist_ok=True)

        # Move the old file to the 'old' directory
        old_filename = os.path.join(old_dir, os.path.basename(filename))
        shutil.move(filename, old_filename)

    # Write the cleaned data to a new file
    with open(fixed_filename, 'wb') as f:
        f.write(bytes_data)
    
    print_horizontal_line()
    print(f'Fixed {error_count} errors in {filename}. Written to: {fixed_filename}')
    if move_old:
        print(f'Old version moved to: {old_filename}')
    print_horizontal_line()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input file or directory')
    parser.add_argument('--auto', action='store_true', help='Automatically fix all errors without confirmation')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing _utf8fixed.txt files')
    parser.add_argument('--moveold', action='store_true', help='Move old versions to the "old" directory')
    args = parser.parse_args()

    if os.path.isdir(args.input):
        # If the input is a directory, process all .txt files in the directory
        for filename in os.listdir(args.input):
            if filename.endswith('.txt') and not filename.endswith('_utf8fixed.txt'):
                clean_invalid_utf8(os.path.join(args.input, filename), args.auto, args.overwrite, args.moveold)
    else:
        # If the input is a file, process the file
        clean_invalid_utf8(args.input, args.auto, args.overwrite, args.moveold)

if __name__ == '__main__':
    main()