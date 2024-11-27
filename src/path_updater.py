import os
import re

def update_paths():
    """
    Met à jour les chemins dans les fichiers pour utiliser la structure existante.
    """
    BASE_DIR = os.path.abspath("/home/ubuntu/prvsnl_cmptbl")
    
    path_mapping = {
        '"//Users/deo_metoyer/Desktop/ONU/EXPR📡📟📡ERPN/visualizations_output"': 'os.path.join(BASE_DIR, "html_viz")',
        '"//Users/deo_metoyer/Desktop/ONU/EXPR��📟📡ERPN/visualizations_output/"': 'os.path.join(BASE_DIR, "html_viz")',
        '"/Users/deo_metoyer/Desktop/ONU/EXPR📡📟📡ERPN/cleaned_final"': 'os.path.join(BASE_DIR, "cleaned_final")'
    }
    
    def process_file(file_path):
        print(f"Processing {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Ajouter les imports nécessaires
        if 'import os' not in content:
            content = 'import os\n' + content
        
        # Définir BASE_DIR si nécessaire
        if 'BASE_DIR = ' not in content:
            base_dir_def = f'\nBASE_DIR = "{BASE_DIR}"\n'
            content = content.replace('import os\n', f'import os{base_dir_def}')
        
        # Mettre à jour les chemins absolus
        for old_path, new_path in path_mapping.items():
            content = content.replace(old_path, new_path)
        
        # Mettre à jour les chemins relatifs des fichiers HTML
        content = re.sub(r'src="([^/]+\.html)"', r'src="html_viz/\1"', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
    
    # Traiter tous les fichiers Python dans src/
    src_dir = os.path.join(BASE_DIR, 'src')
    for file_name in os.listdir(src_dir):
        if file_name.endswith('.py'):
            file_path = os.path.join(src_dir, file_name)
            if file_path != os.path.abspath(__file__):  # Ne pas traiter ce fichier lui-même
                process_file(file_path)

if __name__ == "__main__":
    update_paths()
