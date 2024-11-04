import os
import subprocess
from downloader import WebsiteDownloader
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

    # Step 2: Build and serve the site (skipping face swapping)
    print("Building site...")
    builder = SiteBuilder(website_root)
    
    # Create all necessary directories
    os.makedirs(website_root, exist_ok=True)
    
    # Commit final website
    git_commit_and_push("Update website structure")

    # Step 3: Serve the website
    print("Starting local server...")
    builder.serve()

if __name__ == "__main__":
    main() 