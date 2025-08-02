import json


def load_keys(url="/Users/vilourenco/Documents/GitHub/azure-ai-engineer/keys/keys.json"):
    """Load keys from a JSON file."""
    try:
        with open(url) as f:
            keys = json.load(f)
        return keys
    except FileNotFoundError:
        print("Keys file not found. Please ensure the path is correct.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON from keys file.")
        return None
