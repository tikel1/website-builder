import os
import requests
from PIL import Image
from config import REMAKER_API_KEY, SOURCE_FACE_PATH

class FaceSwapper:
    def __init__(self):
        self.api_key = REMAKER_API_KEY
        self.source_face = SOURCE_FACE_PATH
        self.api_url = "https://remaker.ai/api/v1/face-swap"

    def swap_face(self, target_image_path):
        """Swap faces in the target image using Remaker AI API"""
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            with open(self.source_face, "rb") as source_file, \
                 open(target_image_path, "rb") as target_file:
                
                files = {
                    "source_image": source_file,
                    "target_image": target_file
                }
                
                response = requests.post(
                    self.api_url,
                    headers=headers,
                    files=files
                )
                
                if response.status_code == 200:
                    # Save the swapped image
                    with open(target_image_path, "wb") as f:
                        f.write(response.content)
                    return True
                else:
                    print(f"Face swap failed: {response.text}")
                    return False
                    
        except Exception as e:
            print(f"Error during face swap: {e}")
            return False

    def process_directory(self, directory):
        """Process all images in a directory"""
        image_extensions = {'.jpg', '.jpeg', '.png'}
        
        for root, _, files in os.walk(directory):
            for file in files:
                if os.path.splitext(file)[1].lower() in image_extensions:
                    image_path = os.path.join(root, file)
                    self.swap_face(image_path) 