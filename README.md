# File Converter CLI

The File Converter CLI is a command-line tool designed to convert files between various formats, including PDF, DOCX, TXT, images, Excel files, and more. This tool is built using Python and supports bulk conversion as well as single file conversion.

## Features
- Convert between PDF, DOCX, and TXT formats.
- Convert images between various formats (e.g., JPG to PNG).
- Convert Excel files to CSV and vice versa.
- Bulk conversion of files in a folder.
- Extensible design for adding new converters.

## Prerequisites
- Python 3.14 or higher installed on your system.
- Install the required dependencies using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## Usage

### Single File Conversion
To convert a single file, use the `convert_file` function in the `main.py` script. Run the script from the command line as follows:

```bash
python main.py <input_file> <output_file>
```

Example:
```bash
python main.py input.pdf output.docx
```
https://github.com/Butwhydood/Kariappan_MahendrenJohn_FinalProject/blob/78f294712a840517b16ccfb1b264214ae98d9e47/data/exampleforreadme1.png

This will convert `input.pdf` to `output.docx`.

### Bulk Conversion
To convert all supported files in a folder to a specific format, use the `bulk_convert` function. Run the script as follows:

```bash
python main.py <input_folder> <target_extension>
```

Example:
```bash
python main.py Tobeconverted txt
```
https://github.com/Butwhydood/Kariappan_MahendrenJohn_FinalProject/blob/f86999c34d9f1ccc95de8a1dccf88e3fa871b8e6/data/exampleforreadme2.png

This will convert all supported files in the `Tobeconverted` folder to the TXT format.

### Supported Conversions
The supported conversions are defined in the `CONVERSION_LEGEND` dictionary in `main.py`. Here are some examples:
- PDF to DOCX, TXT, EPUB, XLSX, CSV
- DOCX to TXT, PDF
- TXT to DOCX
- XLSX to CSV, PDF
- CSV to XLSX, PDF
- Image formats (e.g., JPG to PNG, BMP to TIFF)

### Adding New Converters
To add support for new file formats, create a new converter script in the `converters/` folder and update the `CONVERSION_LEGEND` dictionary in `main.py`.

## Error Handling
- If the input file does not exist, a `FileNotFoundError` will be raised.
- If the output file already exists, a `FileExistsError` will be raised.
- Unsupported conversions will raise a `ValueError`.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.
