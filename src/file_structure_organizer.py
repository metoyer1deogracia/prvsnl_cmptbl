import os
import shutil

def organize_project_structure():
    """
    Organise la structure des fichiers du projet en créant les dossiers nécessaires
    et en déplaçant les fichiers vers les bons emplacements.
    """
    # Définition de la structure
    BASE_DIR = "/home/ubuntu/prvsnl_cmptbl"
    STRUCTURE = {
        'html_viz': ['*.html'],
        'data': ['*.csv'],
        'src': ['*.py', '*.ipynb'],
        'static': ['*.svg', '*.png', '*.jpg']
    }
    
    def create_directories():
        for directory in STRUCTURE.keys():
            dir_path = os.path.join(BASE_DIR, directory)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                print(f"Created directory: {directory}")
    
    def move_files():
        for directory, patterns in STRUCTURE.items():
            dir_path = os.path.join(BASE_DIR, directory)
            for pattern in patterns:
                extension = pattern[1:]  # Remove the *
                for file in os.listdir(BASE_DIR):
                    if file.endswith(extension):
                        src = os.path.join(BASE_DIR, file)
                        dst = os.path.join(dir_path, file)
                        if os.path.isfile(src) and not os.path.samefile(os.path.dirname(src), dir_path):
                            shutil.move(src, dst)
                            print(f"Moved {file} to {directory}/")

    # Exécution
    print("Starting project organization...")
    create_directories()
    move_files()
    print("Project organization completed!")

if __name__ == "__main__":
    organize_project_structure()
