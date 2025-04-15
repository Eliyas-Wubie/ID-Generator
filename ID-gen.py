import json
import os
from datetime import datetime

# Define the filename for storing the IDs
filename = './last_ids.json'

def load_last_ids():
    """Load the last IDs from the JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}

def save_last_ids(last_ids):
    """Save the last IDs to the JSON file."""
    with open(filename, 'w') as f:
        json.dump(last_ids, f, indent=4)

def generate_id(last_number):
    """Generate a new ID given the last ID number."""
    new_id_number = last_number + 1
    hex_id = f"INC-{new_id_number:06X}"  # Format the number as hexadecimal with zero-padded 6 digits
    return hex_id, new_id_number

def main():
    last_ids = load_last_ids()
    today = datetime.now().date().isoformat()

    # Get the last number for today; if not found, start from 0
    last_number = last_ids.get(today, -1)

    # Generate a new ID
    new_id, new_last_number = generate_id(last_number)

    # Update the last number for today
    last_ids[today] = new_last_number

    # Save back to JSON
    save_last_ids(last_ids)

    print(f"Generated ID: {new_id}")

if __name__ == "__main__":
    main()