# Program: Hospital Patient Record Finder

def find_patients(records, illness):
    """Finds all patients having the given disease."""
    return [rec["Name"] for rec in records if rec["Disease"].lower() == illness.lower()]

# Example run
patient_data = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_for = "Flu"
matches = find_patients(patient_data, search_for)
print(f"Patients suffering from {search_for}: {matches}")
