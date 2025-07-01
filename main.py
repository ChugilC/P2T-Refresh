from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth
import argparse
from tests import test_update_emails

load_dotenv()
FUSION_USERNAME = os.getenv("FUSION_USERNAME")
FUSION_PASSWORD = os.getenv("FUSION_PASSWORD")
FUSION_URL = os.getenv("FUSION_URL")

url = f"{FUSION_URL}/hcmRestApi/resources/latest/emps?limit=1"


try:
    response = requests.get(url, auth=HTTPBasicAuth(FUSION_USERNAME, FUSION_PASSWORD))

    if response.status_code == 200:
        print("✅ Connection successful! You are authenticated.")
    elif response.status_code == 401:
        print("❌ Unauthorized. Check your username/password.")
    else:
        print(f"⚠️ Something went wrong. Status Code: {response.status_code}")
        print(response.text)

except Exception as e:
    print("❌ Error occurred:", e)



test_map = {
    "update_emails": test_update_emails.run,
    # Add more as needed
}

parser = argparse.ArgumentParser()
parser.add_argument("--test", help="Test case to run", choices=test_map.keys())
args = parser.parse_args()

if args.test:
    test_map[args.test]()
else:
    print("Please provide a test to run using --test option")
