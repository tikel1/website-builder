import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from bs4 import BeautifulSoup
from config import SERVER_PORT

class SiteBuilder:
    def __init__(self, website_root):
        self.website_root = website_root

    def update_image_paths(self):
        """Update all HTML files to use relative image paths"""
        for root, _, files in os.walk(self.website_root):
            for file in files:
                if file.endswith(('.html', '.htm')):
                    file_path = os.path.join(root, file)
                    self._update_single_file(file_path)

    def _update_single_file(self, html_path):
        """Update image paths in a single HTML file"""
        try:
            with open(html_path, "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file, "html.parser")

            modified = False
            for img_tag in soup.find_all("img"):
                if "src" in img_tag.attrs:
                    src = img_tag["src"]
                    if src.startswith("http"):
                        local_path = os.path.basename(src)
                        img_tag["src"] = local_path
                        modified = True

            if modified:
                with open(html_path, "w", encoding="utf-8") as file:
                    file.write(str(soup))

        except Exception as e:
            print(f"Error processing {html_path}: {e}")

    def serve(self):
        """Start local server"""
        server_address = ('', 8000)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        print(f"Serving website at http://localhost:8000")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.server_close() 