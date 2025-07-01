from utils.fusion_api import fusion_get, fusion_patch

def run():
    print("Running: Update Emails Test")

    response = fusion_get("/hcmRestApi/resources/latest/emps?limit=2")
    employees = response.json().get("items", [])

    for emp in employees:
        emp_id = emp["PersonId"]
        new_email = f"test_user_{emp_id}@example.com"
        patch_resp = fusion_patch(f"/hcmRestApi/resources/latest/emps/{emp_id}", {
            "WorkEmail": new_email
        })
        if patch_resp.status_code == 200:
            print(f"✅ Updated email for ID {emp_id}")
        else:
            print(f"❌ Failed to update ID {emp_id}")
