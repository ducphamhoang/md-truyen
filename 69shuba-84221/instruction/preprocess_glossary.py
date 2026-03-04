import csv
import re
import os

def preprocess_text(text_content, glossary_path):
    """
    Preprocesses text by replacing Chinese terms with Vietnamese equivalents from a glossary.
    Uses 'Longest Match First' to prevent shorter terms from corrupting longer ones.
    """
    if not os.path.exists(glossary_path):
        print(f"Error: Glossary not found at {glossary_path}")
        return text_content

    # 1. Load Glossary
    glossary = []
    with open(glossary_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            original = row['Original'].strip()
            vietnamese = row['Vietnamese'].strip()
            if original and vietnamese:
                glossary.append((original, vietnamese))

    # 2. Sort by length of Chinese 'Original' descending
    # This is the "Longest Match First" rule
    glossary.sort(key=lambda x: len(x[0]), reverse=True)

    # 3. Perform Cleaning and Replacement
    processed_lines = []
    lines = text_content.splitlines()
    
    for line in lines:
        stripped_line = line.strip()
        # Skip metadata and separator lines
        if stripped_line.startswith('#') or stripped_line.startswith('='):
            continue
        # Skip empty lines at the very beginning if any, but keep structure later
        if not stripped_line and not processed_lines:
            continue
            
        current_line = line
        for cn_term, vn_term in glossary:
            current_line = current_line.replace(cn_term, vn_term)
        processed_lines.append(current_line)

    return "\n".join(processed_lines)

if __name__ == "__main__":
    # Example usage for testing
    import sys
    
    # Configuration
    GLOSSARY_FILE = "master_glossary.csv"
    
    # Check if paths are provided via command line
    input_file = sys.argv[1] if len(sys.argv) > 1 else None
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output_preprocessed.txt"
    
    if input_file:
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Execute pre-processing
            # Assuming script is in the same dir as glossary for this example
            script_dir = os.path.dirname(os.path.abspath(__file__))
            glossary_abs_path = os.path.join(script_dir, GLOSSARY_FILE)
            
            new_content = preprocess_text(content, glossary_abs_path)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"Successfully preprocessed: {input_file} -> {output_file}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Usage: python preprocess_glossary.py <input_file_path> <output_file_path>")
