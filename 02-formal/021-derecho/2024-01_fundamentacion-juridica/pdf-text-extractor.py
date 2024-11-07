import PyPDF2
import os
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF
    """
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get the number of pages
            num_pages = len(pdf_reader.pages)
            
            # Initialize a string to store the text
            text = ""
            
            # Extract text from each page
            for page_num in range(num_pages):
                # Get the page object
                page = pdf_reader.pages[page_num]
                
                # Extract text from the page
                text += page.extract_text() + "\n\n"
                
            return text
            
    except Exception as e:
        raise Exception(f"An error occurred while processing {pdf_path}: {str(e)}")

def process_multiple_pdfs():
    """
    Process multiple PDF files from the current directory and save their contents to separate text files.
    """
    # Get current directory
    dir_path = Path.cwd()
    
    # List all PDF files in the current directory
    pdf_files = list(dir_path.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {dir_path}")
        return
        
    # Create an output directory for text files
    output_dir = dir_path / "extracted_text"
    output_dir.mkdir(exist_ok=True)
    
    # Dictionary to store results
    results = {}
    
    # Process each PDF file found
    for pdf_path in pdf_files:
        pdf_name = pdf_path.name
        try:
            # Extract text
            print(f"Processing {pdf_name}...")
            extracted_text = extract_text_from_pdf(pdf_path)
            
            # Create output file name (same name but .txt extension)
            output_file = output_dir / f"{pdf_path.stem}.txt"
            
            # Save to file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(extracted_text)
            
            # Store result
            results[pdf_name] = {
                'status': 'success',
                'output_file': str(output_file)
            }
            
            print(f"Successfully processed {pdf_name}")
            
        except Exception as e:
            results[pdf_name] = {
                'status': 'error',
                'error': str(e)
            }
            print(f"Error processing {pdf_name}: {str(e)}")
    
    return results

if __name__ == "__main__":
    print("Starting PDF processing...")
    
    # First, let's show what files we find
    current_dir = Path.cwd()
    print(f"Looking for PDF files in: {current_dir}")
    
    pdf_files = list(current_dir.glob("*.pdf"))
    print("\nPDF files found:")
    if pdf_files:
        for pdf in pdf_files:
            print(f"- {pdf.name}")
    else:
        print("No PDF files found!")
    
    print("\nProcessing files...")
    results = process_multiple_pdfs()
    
    if results:
        # Print summary
        print("\nProcessing Summary:")
        print("-" * 50)
        for pdf_name, result in results.items():
            status = result['status']
            if status == 'success':
                print(f"{pdf_name}: Success - Output saved to {result['output_file']}")
            else:
                print(f"{pdf_name}: Failed - {result['error']}")
