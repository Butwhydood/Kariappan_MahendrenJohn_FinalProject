import os
import sys
import tempfile
import shutil
import zipfile
from converters.pdf_converter import pdf_to_docx, pdf_to_text
from converters.docx_converter import docx_to_text, docx_to_pdf, text_to_docx
from converters.excel_converter import convert_excel
from converters.image_converter import convert_image


"""
Main module for the File Converter CLI.

This module serves as the entry point for the application. It defines supported file formats,
conversion mappings, and functions for single and bulk file conversions.
"""

IMAGE_FORMATS = {"jpg", "jpeg", "png", "bmp", "gif", "tiff", "webp", "svg", "ico", "heic", "raw", "psd", "ai", "eps", "indd", "cdr", "pdf"}

CONVERSION_LEGEND = {
    "pdf": {
        "docx": pdf_to_docx,
        "txt": pdf_to_text,
        "xlsx": convert_excel,
        "csv": convert_excel
    },
    "docx": {
        "txt": docx_to_text,
        "pdf": docx_to_pdf
    },
    "txt": {
        "docx": text_to_docx
    },
    "xlsx": {
        "csv": convert_excel,
        "pdf": convert_excel,
    },
    "csv": {
        "xlsx": convert_excel,
        "pdf": convert_excel
    }
}

def get_extension(filename): 
    """
    Extract the file extension from a given filename.

    Args:
        filename (str): The name of the file.

    Returns:
        str: The file extension in lowercase without the leading dot.
    """
    return os.path.splitext(filename)[1][1:].lower() 

def convert_file(input_file, output_file):
    """
    Convert a single file from one format to another.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        FileExistsError: If the output file already exists.
        ValueError: If the conversion is not supported.
    """
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found.")

    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    input_ext = get_extension(input_file)
    output_ext = get_extension(output_file)

    # Ensure the output file name matches the desired extension
    if not output_file.endswith(f".{output_ext}"):
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(output_dir, f"{base_name}.{output_ext}")

    if os.path.exists(output_file):
        raise FileExistsError(f"Output file '{output_file}' already exists.")

    if input_ext in IMAGE_FORMATS and output_ext in IMAGE_FORMATS: 
        convert_image(input_file, output_file)
        return 

    try:
        conversion_func = CONVERSION_LEGEND[input_ext][output_ext]
    except KeyError:
        raise ValueError(f"Conversion from '{input_ext}' to '{output_ext}' is not supported.")

    conversion_func(input_file, output_file)

def bulk_convert(input_folder, target_ext):
    """
    Convert all files in a specified input folder to a target file extension.

    Args:
        input_folder (str): Path to the input folder.
        target_ext (str): The target file extension.

    Returns:
        list: A list of paths to the converted files.
    """
    files = [
        f for f in os.listdir(input_folder)
        if os.path.isfile(os.path.join(input_folder, f)) and get_extension(f) in CONVERSION_LEGEND
    ]

    # Check for file type consistency
    file_extensions = {get_extension(f) for f in files}
    if len(file_extensions) > 1:
        print("Warning: Multiple file types detected in the folder.")
        for ext in file_extensions:
            if ext not in CONVERSION_LEGEND:
                print(f"Skipping unsupported file type: {ext}")
                files = [f for f in files if get_extension(f) != ext]

        proceed = input("Proceed with conversion for supported file types? (yes/no): ").strip().lower()
        if proceed != "yes":
            print("Conversion aborted.")
            return

    temp_output_dir = tempfile.mkdtemp()

    converted_files = []

    for filename in files:
        input_path = os.path.join(input_folder, filename)
        if not os.path.exists(input_path):
            print(f"File not found: {input_path}. Skipping.")
            continue
        name_without_ext = ".".join(filename.split(".")[:-1])
        output_filename = f"{name_without_ext}.{target_ext}"
        output_path = os.path.join(temp_output_dir, output_filename)

        try:
            convert_file(input_path, output_path)
            converted_files.append(output_path)
        except Exception as e:
            print(f"Skipping '{input_path}' due to error: {e}")
        
    if not converted_files:
        print("No files were converted.")
        shutil.rmtree(temp_output_dir)
        return

    zip_name = f"{os.path.basename(input_folder)}_{target_ext}.zip"
    zip_path = os.path.join(os.getcwd(), zip_name)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file_path in converted_files:
            if not os.path.exists(file_path):
                print(f"Warning: File '{file_path}' not found. Skipping.")
                continue
            zipf.write(file_path, os.path.basename(file_path))

    print(f"All converted files have been zipped into '{zip_path}'.")
    shutil.rmtree(temp_output_dir)

def main():
    if len(sys.argv) < 2: 
        print("Usage: python main.py <input_file> <output_file>")
        sys.exit(1)

    if sys.argv[1].lower() == "bulk":
        if len(sys.argv) != 4:
            print("Usage for bulk conversion: python main.py bulk <input_folder> <target_extension>")
            sys.exit(1)
        input_folder = sys.argv[2]
        target_ext = sys.argv[3].lower()
        bulk_convert(input_folder, target_ext)
        return
    

    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        convert_file(input_file, output_file)
    except FileNotFoundError as e:
        print(f"[File Error]: {e}")
        sys.exit(1)
    except FileExistsError as e:
        print(f"[File Error]: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"[Conversion Error]: {e}")
        sys.exit(1) 
    except Exception as e:
        print(f"[Unexpected Error]: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
