# run_tests.py
# Adam Morehouse
# 14 April 2025
# Runs tests for CSC333 Hard Drive Capacity Calculator, saves to test_results.txt

import subprocess
import os

# Test cases with corrected expected values based on actual byte calculations
tests = [
    {
        "name": "Test 1: Tiny Drive",
        "inputs": ["1", "1", "1", "1", "512"],
        "expected": "Drive size: 512.0 bytes"
    },
    {
        "name": "Test 2: Small Drive",
        "inputs": ["1", "2", "1000", "100", "512"],
        "expected": "Drive size: 97.7 MB"
    },
    {
        "name": "Test 3: Medium Drive",
        "inputs": ["2", "2", "5000", "500", "4096"],
        "expected": "Drive size: 38.1 GB"
    },
    {
        "name": "Test 4: Our Multi-TB Drive",
        "inputs": ["6", "2", "500000", "2000", "4096"],
        "expected": "Drive size: 44.7 TB"
    },
    {
        "name": "Test 5: Huge Drive",
        "inputs": ["8", "2", "1000000", "3000", "4096"],
        "expected": "Drive size: 178.8 TB"
    },
    {
        "name": "Test 6: Minimal Inputs",
        "inputs": ["1", "1", "1", "1", "1"],
        "expected": "Drive size: 1.0 bytes"
    },
    {
        "name": "Test 7: High Sectors",
        "inputs": ["4", "2", "10000", "10000", "512"],
        "expected": "Drive size: 381.5 GB"
    }
]

# Check for main program existence
def check_file():
    if not os.path.exists("DriveCapacity.py"):
        print("🚫 Missing DriveCapacity.py!")
        return False
    return True

# Run individual test case
def run_test(test):
    print(f"🔧 Running {test['name']}...")
    try:
        result = subprocess.run(
            ["python", "DriveCapacity.py"],
            input="\n".join(test["inputs"]),
            capture_output=True,
            text=True,
            timeout=10
        )
        output = result.stdout
        if result.stderr:
            output += "\nErrors:\n" + result.stderr
        return output.strip()
    except subprocess.TimeoutExpired:
        return f"{test['name']} took too long!"
    except Exception as e:
        return f"{test['name']} crashed: {str(e)}"

# Main test runner
def main():
    if not check_file():
        print("💥 Can't continue — fix missing file.")
        return

    with open("test_results.txt", "w") as f:
        f.write("CSC333 Hard Drive Capacity Test Results\n")
        f.write("Adam Morehouse\n")
        f.write("14 April 2025\n\n")

        for test in tests:
            f.write(f"--- {test['name']} ---\n")
            f.write(f"Inputs: Platters={test['inputs'][0]}, Surfaces={test['inputs'][1]}, "
                    f"Tracks={test['inputs'][2]}, Sectors={test['inputs'][3]}, Bytes={test['inputs'][4]}\n")
            f.write(f"Expected Output: {test['expected']}\n\n")

            output = run_test(test)
            f.write(f"Actual Output:\n{output}\n\n")

            if test["expected"] in output:
                f.write("[PASS] Result: PASS\n")
            else:
                f.write("[FAIL] Result: FAIL\n")
                f.write("WARNING: Output did not match expected.\n")

            f.write("=" * 60 + "\n\n")

    print("✅ All tests complete! See test_results.txt for results.")

if __name__ == "__main__":
    main()
