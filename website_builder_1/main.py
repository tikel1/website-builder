import os
import subprocess
from downloader import WebsiteDownloader
from face_swapper import FaceSwapper
from site_builder import SiteBuilder

def git_commit_and_push(message):
    try:
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', message], check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        print(f"Successfully committed and pushed: {message}")
    except subprocess.CalledProcessError as e:
        print(f"Git operation failed: {e}")

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

    print(f"Website downloaded to: {website_root}")
    
    # Commit original website files
    git_commit_and_push("Add original website files")

    # Step 2: Process images with face swapping
    print("Processing images...")
    swapper = FaceSwapper()
    
    # Create a directory for swapped images
    swapped_images_dir = os.path.join(website_root, 'swapped_images')
    os.makedirs(swapped_images_dir, exist_ok=True)
    
    # Process images and save to swapped_images directory
    swapper.process_directory(website_root, output_dir=swapped_images_dir)
    
    # Commit face-swapped images
    git_commit_and_push("Add face-swapped images")

    # Step 3: Build and serve the site
    print("Building site...")
    builder = SiteBuilder(website_root)
    
    # Create all necessary directories
    os.makedirs(website_root, exist_ok=True)
    
    # Update image paths to use swapped images where available
    builder.update_image_paths(swapped_images_dir)
    
    # Commit final website with replaced images
    git_commit_and_push("Update website with swapped images")

    # Step 4: Serve the website
    print("Starting local server...")
    builder.serve()

if __name__ == "__main__":
    main() 