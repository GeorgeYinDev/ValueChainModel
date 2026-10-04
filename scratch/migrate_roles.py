import os
import glob
import re

def migrate_roles():
    for filepath in glob.glob("roles/*.md"):
        with open(filepath, "r") as f:
            content = f.read()

        if content.startswith("---"):
            continue # already migrated

        id_match = re.search(r"\*\*Role ID\*\*: `(.*?)`", content)
        name_match = re.search(r"# Role Definition: (.*)", content)
        dept_match = re.search(r"\*\*Department\*\*: (.*)", content)
        reports_to_match = re.search(r"\*\*Reports To\*\*: (.*)", content)
        
        limit_match = re.search(r"\$([0-9,]+)", content)
        
        r_id = id_match.group(1) if id_match else os.path.basename(filepath).replace('.md', '')
        r_name = name_match.group(1).strip() if name_match else ""
        r_dept = dept_match.group(1).strip() if dept_match else ""
        
        limit_val = 0.0
        if "Unlimited" in content:
            limit_val = 999999999.0
        elif limit_match:
            limit_val = float(limit_match.group(1).replace(",", ""))

        if "role_general_ledger_accountant" in r_id:
            limit_val = 10000.0
        elif "role_category_manager" in r_id:
            limit_val = 500000.0
        elif "role_procurement_specialist" in r_id:
            limit_val = 50000.0
        elif "role_finance_controller" in r_id:
            limit_val = 999999999.0
        elif "role_warehouse_supervisor" in r_id:
            limit_val = 0.0
        elif "role_sales_ops_specialist" in r_id:
            limit_val = 250000.0
        elif "role_credit_manager" in r_id:
            limit_val = 250000.0

        yaml = f"""---
id: {r_id}
type: role
name: "{r_name}"
department: "{r_dept}"
approval_limit_usd: {limit_val}
---
"""
        with open(filepath, "w") as f:
            f.write(yaml + content)
            print(f"Migrated {r_id}")

if __name__ == "__main__":
    migrate_roles()
