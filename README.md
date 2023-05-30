# unicode-sheriff

Unicode Sheriff is a powerful tool designed to help you clean up pesky, broken Unicode characters in your text files. It provides an efficient and user-friendly solution for handling encoding issues and ensuring your text files are free from invalid or corrupted Unicode sequences.

## Features

- Detects and fixes invalid UTF-8 sequences in text files.
- Provides options for automatic error fixing or interactive confirmation.
- Supports bulk processing of multiple files and directories.
- Offers the ability to overwrite existing files or create new fixed versions.
- Includes a helpful progress indicator and detailed error reporting.

## Usage

To use Unicode Sheriff, follow these steps:

1. Install Python 3 on your system if you haven't already.

2. Clone the repository or download the `unicode-sheriff.py` script.

3. Open a terminal or command prompt and navigate to the directory containing the `unicode-sheriff.py` script.

4. Run the following command to clean up a single file:


```
python unicode-sheriff.py [file_path]
```

Replace `[file_path]` with the path to the file you want to process.

5. Run the following command to clean up all text files in a directory (including subdirectories):

```
python unicode-sheriff.py [directory_path]
```

Replace `[directory_path]` with the path to the directory you want to process.

6. Use the available options to customize the cleaning process:
- `--auto`: Automatically fix all errors without confirmation.
- `--overwrite`: Overwrite existing files with the fixed versions.
- `--moveold`: Create a directory named "old" in the text source directory and move the old versions there.

7. Sit back and let Unicode Sheriff do its magic! The tool will analyze the text files, identify any invalid Unicode sequences, and provide options for fixing or confirming the changes.

8. Once the process is complete, Unicode Sheriff will generate fixed versions of the files, ensuring your text files are now free from broken Unicode characters.

## Contribution

Unicode Sheriff is an open-source project, and contributions are welcome! If you encounter any issues, have suggestions for improvements, or want to contribute code, please feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/FlyingFathead/unicode-sheriff).

## License

Unicode Sheriff is released under the [MIT License](LICENSE).


