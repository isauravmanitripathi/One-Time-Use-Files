import os
import fnmatch

def is_code_file(filename):
    """
    Check if a file is likely to contain code based on its extension.
    """
    code_extensions = [
        '*.py', '*.js', '*.jsx', '*.ts', '*.tsx', '*.java', '*.c', '*.cpp', 
        '*.cc', '*.cxx', '*.h', '*.hpp', '*.cs', '*.php', '*.rb', '*.go', 
        '*.rs', '*.swift', '*.kt', '*.scala', '*.r', '*.m', '*.mm', 
        '*.pl', '*.sh', '*.bash', '*.zsh', '*.fish', '*.ps1', '*.bat', 
        '*.cmd', '*.vb', '*.vbs', '*.asm', '*.s', '*.sql', '*.html', 
        '*.htm', '*.css', '*.scss', '*.sass', '*.less', '*.xml', '*.json', 
        '*.yaml', '*.yml', '*.toml', '*.ini', '*.cfg', '*.conf', 
        '*.dockerfile', '*.makefile', '*.cmake', '*.gradle', '*.maven',
        '*.lua', '*.dart', '*.elm', '*.ex', '*.exs', '*.clj', '*.cljs',
        '*.f', '*.f90', '*.f95', '*.jl', '*.nim', '*.zig'
    ]
    
    # Check if filename matches any code extension pattern
    return any(fnmatch.fnmatch(filename.lower(), pattern) for pattern in code_extensions)

def read_file_safely(filepath):
    """
    Attempt to read a file with multiple encoding strategies.
    """
    encodings = ['utf-8', 'utf-16', 'latin-1', 'cp1252']
    
    for encoding in encodings:
        try:
            with open(filepath, 'r', encoding=encoding) as file:
                return file.read()
        except (UnicodeDecodeError, UnicodeError):
            continue
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return None
    
    print(f"Could not decode file: {filepath}")
    return None

def extract_code_from_folder(folder_path, output_file='combined_code.txt'):
    """
    Recursively read through a folder, extract code from files, 
    and combine them into one text file.
    """
    
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return
    
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a directory.")
        return
    
    code_files = []
    
    # Walk through all subdirectories and files
    for root, dirs, files in os.walk(folder_path):
        # Skip common non-code directories
        dirs[:] = [d for d in dirs if d not in ['.git', '.svn', 'node_modules', '__pycache__', '.vscode', '.idea', 'build', 'dist', 'target']]
        
        for file in files:
            if is_code_file(file):
                filepath = os.path.join(root, file)
                code_files.append(filepath)
    
    if not code_files:
        print(f"No code files found in '{folder_path}'")
        return
    
    print(f"Found {len(code_files)} code files. Processing...")
    
    # Write combined code to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(f"=== COMBINED CODE FROM: {os.path.abspath(folder_path)} ===\n")
            outfile.write(f"Generated on: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            outfile.write(f"Total files processed: {len(code_files)}\n")
            outfile.write("="*80 + "\n\n")
            
            processed_count = 0
            
            for filepath in sorted(code_files):
                relative_path = os.path.relpath(filepath, folder_path)
                
                # Write file header
                outfile.write(f"\n{'='*60}\n")
                outfile.write(f"FILE: {relative_path}\n")
                outfile.write(f"FULL PATH: {filepath}\n")
                outfile.write(f"{'='*60}\n\n")
                
                # Read and write file content
                content = read_file_safely(filepath)
                if content is not None:
                    outfile.write(content)
                    processed_count += 1
                    if not content.endswith('\n'):
                        outfile.write('\n')
                else:
                    outfile.write("<!-- Could not read this file -->\n")
                
                outfile.write(f"\n{'='*60}\n")
                outfile.write(f"END OF FILE: {relative_path}\n")
                outfile.write(f"{'='*60}\n\n")
            
            # Write summary at the end
            outfile.write(f"\n{'='*80}\n")
            outfile.write(f"SUMMARY: Successfully processed {processed_count} out of {len(code_files)} files\n")
            outfile.write(f"{'='*80}\n")
        
        print(f"✓ Successfully created '{output_file}' with {processed_count} code files!")
        print(f"✓ Output file location: {os.path.abspath(output_file)}")
        
    except Exception as e:
        print(f"Error writing to output file: {e}")

def main():
    """
    Main function to get user input and run the code extraction.
    """
    print("Code Extractor and Combiner")
    print("-" * 30)
    
    # Get folder path from user
    folder_path = input("Enter the path to the folder: ").strip()
    
    # Remove quotes if user wrapped path in quotes
    if folder_path.startswith('"') and folder_path.endswith('"'):
        folder_path = folder_path[1:-1]
    elif folder_path.startswith("'") and folder_path.endswith("'"):
        folder_path = folder_path[1:-1]
    
    # Get output filename (optional)
    output_file = input("Enter output filename (press Enter for 'combined_code.txt'): ").strip()
    if not output_file:
        output_file = 'combined_code.txt'
    
    # Ensure output file has .txt extension
    if not output_file.endswith('.txt'):
        output_file += '.txt'
    
    print(f"\nProcessing folder: {folder_path}")
    print(f"Output file: {output_file}\n")
    
    extract_code_from_folder(folder_path, output_file)

if __name__ == "__main__":
    main()