import os

def find_and_delete_matching_files():
    """
    Compares files in two directories based on a prefix, identifies matches,
    and offers to delete the matched files from the first directory.
    """
    try:
        # 1. Get folder paths from the user
        folder1_path = input("Enter the path for the first folder (e.g., where 'united_nations.json' is): ").strip()
        folder2_path = input("Enter the path for the second folder (e.g., where 'questions_united_nations.json' is): ").strip()

        # --- Validate folder paths ---
        if not os.path.isdir(folder1_path):
            print(f"\nError: The path for the first folder does not exist or is not a directory.")
            print(f"Path provided: {folder1_path}")
            return
        if not os.path.isdir(folder2_path):
            print(f"\nError: The path for the second folder does not exist or is not a directory.")
            print(f"Path provided: {folder2_path}")
            return
            
        # 2. Get the prefix to remove
        prefix = input("Enter the prefix used in the second folder's files (e.g., 'questions_'): ").strip()

        # 3. Get list of files from both directories
        folder1_files = set(os.listdir(folder1_path))
        folder2_files = os.listdir(folder2_path)

        # 4. Find files in folder1 that have a corresponding prefixed file in folder2
        files_to_delete = []
        print("\n--- Searching for matches ---")
        for file_in_folder2 in folder2_files:
            # Check if the file in folder 2 actually has the specified prefix
            if file_in_folder2.startswith(prefix):
                # Remove the prefix to get the potential original filename
                original_filename = file_in_folder2[len(prefix):]
                
                # Check if this original filename exists in the first folder
                if original_filename in folder1_files:
                    files_to_delete.append(original_filename)
                    print(f"Match found: '{original_filename}' in Folder 1 corresponds to '{file_in_folder2}' in Folder 2.")

        # 5. Ask for confirmation and delete if requested
        if not files_to_delete:
            print("\nNo matching files were found to delete.")
            return

        print("\n--- Deletion Confirmation ---")
        print("The following files are matched and can be deleted from the first folder:")
        for filename in files_to_delete:
            print(f"  - {filename}")
        
        # Ask the user for confirmation
        confirm = input(f"\nDo you want to delete these {len(files_to_delete)} files from '{folder1_path}'? (yes/no): ").lower().strip()

        if confirm == 'yes':
            deleted_count = 0
            print("\n--- Deleting Files ---")
            for filename in files_to_delete:
                file_path_to_delete = os.path.join(folder1_path, filename)
                try:
                    os.remove(file_path_to_delete)
                    print(f"Successfully deleted: {file_path_to_delete}")
                    deleted_count += 1
                except OSError as e:
                    print(f"Error deleting file {file_path_to_delete}: {e}")
            print(f"\nDeletion complete. {deleted_count} files were removed.")
        else:
            print("\nDeletion cancelled. No files were removed.")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    find_and_delete_matching_files()

