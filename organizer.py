import os
import shutil


def organize_folder(folder_path):
    # Define categories
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Music": [".mp3", ".wav", ".aac"],
        "Code" : [".py",".html", ".css",".js"],
        "Others": []
    }

    # Loop through files
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Get file extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Find which category it belongs to
        moved = False
        for category, extensions in categories.items():
            if file_ext in extensions:
                # Create category folder if not exists
                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)

                # Move file
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved {filename} to {category}")
                moved = True
                break

        if not moved:
            # Move to Others
            others_folder = os.path.join(folder_path, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved {filename} to Others")


# Run the script
folder = input("Enter the folder path to organize: ")
organize_folder(folder)
print("Done! Your folder is now organized.")