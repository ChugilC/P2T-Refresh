from dotenv import load_dotenv
import os

load_dotenv()
FUSION_USERNAME = os.getenv("FUSION_USERNAME")
FUSION_PASSWORD = os.getenv("FUSION_PASSWORD")
FUSION_URL = os.getenv("FUSION_URL")
