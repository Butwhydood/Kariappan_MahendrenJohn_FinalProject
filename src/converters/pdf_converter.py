"""
Module for PDF file conversions.

This module provides functions to convert PDF files to DOCX and plain text.
"""
import os
import subprocess
from docx import Document
from pdf2docx import Converter
import fitz  # PyMuPDF

def pdf_to_docx(input_file, output_file):
    """
    Convert a PDF file to a DOCX file.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path to the output DOCX file.
    """
    cv = Converter(input_file) 
    cv.convert(output_file)
    cv.close()

def pdf_to_text(input_file, output_file):
    """
    Extract text from a PDF file and save it as plain text.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path to the output text file.
    """
    doc = fitz.open(input_file) 
    text = ""
    for page in doc:
        text += page.get_text()
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)