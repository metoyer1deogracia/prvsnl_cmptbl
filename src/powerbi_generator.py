import os

def create_powerbi_template():
    """
    Crée un template HTML pour PowerBI avec une structure améliorée.
    """
    BASE_DIR = "/home/ubuntu/prvsnl_cmptbl"
    
    template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PowerBI Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        :root {
            --primary-color: #2C3E50;
            --secondary-color: #3498DB;
            --accent-color: #4EC9B0;
            --background-color: #B3CEE2;
            --text-color: #1E2A38;
        }
        
        body {
            margin: 0;
            padding: 0;
            font-family: 'Sora', sans-serif;
            background-color: var(--background-color);
        }
        
        .dashboard-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        
        .visualization-card {
            background: white;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .visualization-card iframe {
            width: 100%;
            height: 400px;
            border: none;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <!-- Service Hierarchy -->
        <div class="visualization-card">
            <h3>Service Architecture</h3>
            <iframe src="html_viz/service_hierarchy.html"></iframe>
        </div>
        
        <!-- Cost Analysis -->
        <div class="visualization-card">
            <h3>Cost Analysis</h3>
            <iframe src="html_viz/cost_hierarchy.html"></iframe>
        </div>
        
        <!-- Financial Flows -->
        <div class="visualization-card">
            <h3>Financial Flows</h3>
            <iframe src="html_viz/flux_financiers_enhanced.html"></iframe>
        </div>
        
        <!-- Subsidies Analysis -->
        <div class="visualization-card">
            <h3>Subsidies Analysis</h3>
            <iframe src="html_viz/subsidies_heatmap_Code APE_Source Principale.html"></iframe>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Ajuster la hauteur des iframes en fonction du contenu
            const resizeIframes = () => {
                document.querySelectorAll('iframe').forEach(iframe => {
                    iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
                });
            };
            
            // Attendre le chargement complet des iframes
            window.addEventListener('load', resizeIframes);
            window.addEventListener('resize', resizeIframes);
        });
    </script>
</body>
</html>"""
    
    # Créer le fichier PowerBI.html
    output_path = os.path.join(BASE_DIR, 'html_viz', 'PowerBI.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    print(f"Created PowerBI template at: {output_path}")

if __name__ == "__main__":
    create_powerbi_template()
