# agent_v2.py
import sys
import os

# --- Add project root and subfolders to Python path ---
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJECT_ROOT)  # For main folder modules
sys.path.append(os.path.join(PROJECT_ROOT, 'custom_parsers'))  # For custom_parsers
sys.path.append(os.path.join(PROJECT_ROOT, 'Backend'))        # For Backend modules

# --- Now you can safely import your local modules ---
from custom_parsers import icici_parser
from bank_detector import detect_bank  # if needed from Backend

# --- Your existing code below ---
def main():
    print("Agent v2 is running...")
    # Example usage
    # data = icici_parser.parse("path_to_sample.pdf")
    # detect_bank(data)

if __name__ == "__main__":
    main()
