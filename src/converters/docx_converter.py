import os
import subprocess


"""
Module for DOCX file conversions.

This module provides functions to convert DOCX files to PDF and plain text,
as well as converting plain text to DOCX.
"""

def docx_to_pdf(input_file, output_file):
    """
    Convert a DOCX file to a PDF file using LibreOffice.

    Args:
        input_file (str): Path to the input DOCX file.
        output_file (str): Path to the output PDF file.

    Raises:
        RuntimeError: If the conversion fails.
    """
    libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"
    output_dir = os.path.dirname(os.path.abspath(output_file)) 

    command = [
        libreoffice_path,
        "--headless",
        "--convert-to", "pdf",
        input_file,
        "--outdir", output_dir, 
    ] 

    result = subprocess.run(command, capture_output=True, text=True) #explanation

    if result.returncode != 0:
        raise RuntimeError(f"Error converting DOCX to PDF: {result.stderr}")

    # LibreOffice automatically names the converted file
    # after the input file (example: sample1.docx -> sample1.pdf)
    generated_pdf = os.path.join(
        output_dir,
        os.path.splitext(os.path.basename(input_file))[0] + ".pdf"
    )

    # Rename the generated PDF to match the user's requested output filename
    if generated_pdf != os.path.abspath(output_file):
        os.replace(generated_pdf, output_file)

def docx_to_text(input_file, output_file):
    """
    Convert a DOCX file to plain text using Pandoc.

    Args:
        input_file (str): Path to the input DOCX file.
        output_file (str): Path to the output text file.

    Raises:
        RuntimeError: If the conversion fails.
    """
    pandoc_path = r"C:\Program Files\Pandoc\pandoc.exe"

    command = [
        pandoc_path,
        input_file,
        "-t", "plain",
        "-o", output_file
    ]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Error converting DOCX to text: {result.stderr}")

def text_to_docx(text, output_file):
    """
    Convert plain text to a DOCX file using Pandoc.

    Args:
        text (str): Path to the input plain text file.
        output_file (str): Path to the output DOCX file.

    Raises:
        RuntimeError: If the conversion fails.
    """
    pandoc_path = r"C:\Program Files\Pandoc\pandoc.exe"

    command = [
        pandoc_path,
        text,
        "-t", "docx",
        "-o", output_file
    ]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Error converting text to DOCX: {result.stderr}")