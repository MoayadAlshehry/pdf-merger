# pdf-merger

A fast and simple CLI tool for merging multiple PDF files into one. 

## Features
- Merge multiple PDF files into a single output
- Specify output filename
- Reorder pages
- Extract specific page ranges from PDFs
- Simple drag-and-drop style usage (pass files as arguments)

## Installation
```bash
pip install -r requirements.txt
```

## Usage
Merge all pages of `file1.pdf` and `file2.pdf` into `merged.pdf` (default):
```bash
python main.py file1.pdf file2.pdf
```

Specify an output file:
```bash
python main.py -o output.pdf file1.pdf file2.pdf
```

Extract specific page ranges:
```bash
python main.py file1.pdf:1-3,5 file2.pdf
```
*(The above command takes pages 1, 2, 3, and 5 from file1.pdf and all pages from file2.pdf)*

## Technologies
- Python
- PyPDF2
