import os
import sys
import argparse
from PyPDF2 import PdfReader, PdfWriter

DEFAULT_OUTPUT = "merged.pdf"

def parse_ranges(ranges_str, total_pages):
    pages = []
    for part in ranges_str.split(','):
        if '-' in part:
            start, end = part.split('-')
            start = int(start) - 1 if start else 0
            end = int(end) if end else total_pages
            pages.extend(range(start, end))
        else:
            pages.append(int(part) - 1)
    return pages

def main():
    parser = argparse.ArgumentParser(description="Merge multiple PDF files into one.")
    parser.add_argument("files", nargs="+", help="PDF files to merge. Format: file.pdf or file.pdf:1-3,5")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="Output filename")
    
    args = parser.parse_args()
    
    writer = PdfWriter()
    print("\033[94m Starting PDF merge...\033[0m")
    
    try:
        for item in args.files:
            filepath = item
            pages_str = None
            
            if not os.path.exists(filepath):
                if ':' in item:
                    possible_file, _, possible_pages = item.rpartition(':')
                    if os.path.exists(possible_file):
                        filepath = possible_file
                        pages_str = possible_pages
            
            if not os.path.exists(filepath):
                print(f"\033[91m Error: File not found -> {filepath}\033[0m")
                sys.exit(1)
                
            reader = PdfReader(filepath)
            total = len(reader.pages)
            
            if pages_str:
                pages_to_add = parse_ranges(pages_str, total)
                print(f" Adding {filepath} (pages: {pages_str})")
            else:
                pages_to_add = range(total)
                print(f" Adding {filepath} (all {total} pages)")
                
            for p in pages_to_add:
                writer.add_page(reader.pages[p])
                
        with open(args.output, "wb") as f:
            writer.write(f)
            
        print(f"\033[92m Successfully merged into {args.output}\033[0m")
        
    except Exception as e:
        print(f"\033[91m An error occurred: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
