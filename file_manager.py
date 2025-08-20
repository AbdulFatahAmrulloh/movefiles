import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')  # supaya print aman di Windows

def organizer_files(main_folder): #jangan lupa buat folder Images, Audio, Documents, Archives, dan Executables
    extension_folders = {
        '.gif': 'Images',
        '.jpeg': 'Images',
        '.jpg': 'Images',
        '.png': 'Images',
        '.svg': 'Images',
        '.mp3': 'Audio',
        '.ogg': 'Audio',
        '.wav': 'Audio',
        '.mp4': 'Video',
        '.avi': 'Video',
        '.mov': 'Video',
        '.pdf': 'Documents',
        '.txt': 'Documents',
        '.docx': 'Documents',
        '.xlsx': 'Documents',
        '.pptx': 'Documents',
        '.zip': 'Archives',
        '.rar': 'Archives',
        '.tar': 'Archives',
        '.exe': 'Executables',
        '.bat': 'Executables',
        '.sh': 'Executables',
    }

    existing_folders = []

    for item in os.listdir(main_folder):
        item_path = os.path.join(main_folder, item)
        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            ext = ext.lower()

            if ext in extension_folders:
                target_folder = extension_folders[ext]

                if target_folder.lower() not in existing_folders:
                    os.makedirs(os.path.join(main_folder, target_folder), exist_ok=True)
                    existing_folders.append(target_folder.lower())

                shutil.move(item_path, os.path.join(main_folder, target_folder, item))
                print(f"Moved {item} -> {target_folder}")
            else:
                print(f"Skipping {repr(item)} (no folder mapping)")

main_folder_path = r"D:\ASUS\Downloads" #perbarui ini ke folder anda
organizer_files(main_folder_path)
