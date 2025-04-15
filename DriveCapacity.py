# DriveCapacity.py
# Adam Morehouse
# 14 April 2025
# CSC333 Hard Drive Capacity Calculator

# Get inputs with nice prompts and make sure they’re valid
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Gotta be a positive number, try again!")
            else:
                return value
        except ValueError:
            print("That’s not a number, dude! Try again.")

# Main program
def main():
    print("Let's figure out your hard drive's size!")
    
    # Get all inputs
    platters = get_positive_int("How many platters? ")
    surfaces = get_positive_int("How many surfaces per platter? ")
    tracks = get_positive_int("How many tracks per surface? ")
    sectors = get_positive_int("How many sectors per track? ")
    bytes = get_positive_int("How many bytes per sector? ")
    
    # Calculate total bytes
    total_bytes = platters * surfaces * tracks * sectors * bytes
    # We multiply all inputs to get the full drive size
    
    # Convert to KB, MB, GB, TB (using 1024 for binary units)
    kb = total_bytes / 1024.0
    mb = kb / 1024.0
    gb = mb / 1024.0
    tb = gb / 1024.0
    # Each step divides by 1024 to switch units
    
    # Find smallest unit > 1.0, check from largest to smallest
    if tb >= 1.0:
        print(f"Drive size: {tb:.1f} TB")
    elif gb >= 1.0:
        print(f"Drive size: {gb:.1f} GB")
    elif mb >= 1.0:
        print(f"Drive size: {mb:.1f} MB")
    elif kb >= 1.0:
        print(f"Drive size: {kb:.1f} KB")
    else:
        print(f"Drive size: {total_bytes:.1f} bytes")
    # Print first unit that’s 1 or more, with one decimal

if __name__ == "__main__":
    main()