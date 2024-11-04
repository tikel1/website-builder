import os
import shutil

class WebsiteDownloader:
    def __init__(self):
        self.website_root = os.path.join(os.path.dirname(__file__), 'downloads', 'www.fcashdod.co.il')

    def get_website_root(self):
        return self.website_root

    def download(self):
        """Create local website structure"""
        try:
            # Clear and recreate the website directory
            if os.path.exists(self.website_root):
                shutil.rmtree(self.website_root)
            
            # Create main directory and subdirectories
            os.makedirs(self.website_root)
            os.makedirs(os.path.join(self.website_root, 'images'))
            os.makedirs(os.path.join(self.website_root, 'css'))
            os.makedirs(os.path.join(self.website_root, 'js'))
            
            # Create a basic index.html
            index_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Local Website</title>
                <style>
                    .image-grid {
                        display: grid;
                        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
                        gap: 1rem;
                        padding: 1rem;
                    }
                    .image-grid img {
                        width: 100%;
                        height: auto;
                    }
                </style>
            </head>
            <body>
                <div class="image-grid" id="imageContainer">
                    <!-- Images will be added here dynamically -->
                </div>
                <script>
                    // Add your JavaScript here if needed
                </script>
            </body>
            </html>
            """
            
            with open(os.path.join(self.website_root, 'index.html'), 'w') as f:
                f.write(index_html)
            
            print(f"Created local website structure at: {self.website_root}")
            return True
            
        except Exception as e:
            print(f"Error creating website structure: {e}")
            return False