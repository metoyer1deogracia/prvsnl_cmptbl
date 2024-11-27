import os
import sys
from typing import List, Callable

class AutomationStep:
    def __init__(self, name: str, function: Callable, description: str):
        self.name = name
        self.function = function
        self.description = description

def run_automation():
    """
    Script principal qui exécute toutes les étapes d'automatisation dans le bon ordre.
    """
    BASE_DIR = "/home/ubuntu/prvsnl_cmptbl"
    
    def execute_steps(steps: List[AutomationStep]) -> None:
        """Exécute une série d'étapes d'automatisation avec gestion des erreurs."""
        for i, step in enumerate(steps, 1):
            print(f"\n[{i}/{len(steps)}] {step.name}")
            print(f"Description: {step.description}")
            try:
                step.function()
                print(f"✓ {step.name} completed successfully")
            except Exception as e:
                print(f"✗ Error in {step.name}: {str(e)}")
                if input("Continue with next step? (y/n): ").lower() != 'y':
                    sys.exit(1)
    
    # Import des autres scripts
    from file_structure_organizer import organize_project_structure
    from path_updater import update_paths
    from powerbi_generator import create_powerbi_template
    
    # Définition des étapes
    steps = [
        AutomationStep(
            "Project Structure Organization",
            organize_project_structure,
            "Creates and organizes project directories"
        ),
        AutomationStep(
            "Path Updates",
            update_paths,
            "Updates all file paths to match new structure"
        ),
        AutomationStep(
            "PowerBI Template Generation",
            create_powerbi_template,
            "Creates PowerBI dashboard template"
        )
    ]
    
    # Exécution
    print("Starting automation process...")
    execute_steps(steps)
    print("\nAutomation completed!")
    print("\nNext steps:")
    print("1. Review the generated PowerBI.html in html_viz/")
    print("2. Verify all visualizations are loading correctly")
    print("3. Check path updates in Python files")

if __name__ == "__main__":
    run_automation()
