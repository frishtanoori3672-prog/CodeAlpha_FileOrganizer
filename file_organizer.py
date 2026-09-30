import os
import shutil

# Ask the user for the folder to organize
source_folder = input("Enter the path of the folder: ").strip()

# Check if the folder exists
if not os.path.exists(source_folder):
    print("The folder does not exist.")
else:
    # Create a folder for JPG files
    destination_folder = os.path.join(source_folder, "JPG_Files")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Count moved files
    moved_files = 0

    # Check all files in the source folder
    for file_name in os.listdir(source_folder):

        # Check if the file is a JPG file
        if file_name.lower().endswith(".jpg"):

            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)

            # Make sure it is a file
            if os.path.isfile(source_path):

                # Move the JPG file
                shutil.move(source_path, destination_path)

                moved_files += 1
                print(f"Moved: {file_name}")

    # Show the final result
    print("\nTask completed successfully!")
    print(f"Total JPG files moved: {moved_files}")
    print(f"Files were moved to: {destination_folder}")