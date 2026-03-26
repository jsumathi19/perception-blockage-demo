import re
import os
os.listdir()
from pathlib import Path

# Read files
base_dir = Path(__file__).resolve().parent

file_path = base_dir / "../requirements/L2_sw_requirements.md"
with open(file_path.resolve()) as f:
    l2_data = f.read()
#print(l2_data)

file_path = base_dir / "../requirements/traceability_matrix.md"
with open(file_path.resolve()) as f:
    trace_data = f.read()
#print(trace_data)

file_path = base_dir / "kpi_definition.md"
with open(file_path.resolve()) as f:
    kpi_data = f.read()

# Extract L2 IDs
l2_ids = re.findall(r"(L2_[A-Z_0-9]+)", l2_data)

# Extract mappings
mapped_l2 = re.findall(r"(L2_[A-Z_0-9]+)", trace_data)

# Extract KPI links
kpi_links = re.findall(r"Linked to: (L2_[A-Z_0-9]+)", kpi_data)

print("🔍 TRACEABILITY CHECK\n")

for l2 in set(l2_ids):
    print(f"Checking {l2}...")

    if l2 not in mapped_l2:
        print(f"❌ Missing in traceability matrix")

    if l2 not in kpi_links:
        print(f"❌ Missing KPI linkage")

    else:
        print("✅ Fully traced")

    print("-" * 30)