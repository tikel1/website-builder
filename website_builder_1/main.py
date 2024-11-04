import os
from downloader import WebsiteDownloader
from face_swapper import FaceSwapper
from site_builder import SiteBuilder

def main():
    # Step 1: Download website
    print("Downloading website...")
    downloader = WebsiteDownloader()
    success = downloader.download()
    
    if not success:
        print("Failed to download website")
        return
        
    website_root = downloader.get_website_root()
    if not os.path.exists(website_root):
        print(f"Error: Website was not downloaded. Directory does not exist: {website_root}")
        return
        
    # Check if the directory has any content
    if not os.listdir(website_root):
        print(f"Error: Website directory is empty: {website_root}")
        return

    print(f"Website root exists: {os.path.exists(website_root)}")
    print(f"Website root absolute path: {os.path.abspath(website_root)}")
    print(f"Website downloaded to: {website_root}")

    # Step 2: Process images with face swapping
    print("Processing images...")
    swapper = FaceSwapper()
    swapper.process_directory(website_root)

    # Step 3: Build and serve the site
    print("Building site...")
    builder = SiteBuilder(website_root)
    
    # Create all necessary directories
    os.makedirs(website_root, exist_ok=True)
    
    builder.update_image_paths()

    # Step 4: Serve the website
    print("Starting local server...")
    builder.serve()

if __name__ == "__main__":
    main() 