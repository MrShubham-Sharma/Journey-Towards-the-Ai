audit_record = "2026-MAR-SITE_01"

# 1. Extract the Year (First 4 characters)
year = audit_record[:4]

# 2. Extract the Site ID (Last 2 characters)
site_id = audit_record[-2:]

# 3. Clean and convert a status string
status = "   in_progress   "
final_status = status.strip().replace("_", " ").title()

print(f"Record Year: {year} | ID: {site_id}")
print(f"Current Status: {final_status}")