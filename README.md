# 🧮 Hard Drive Capacity Calculator

**Author:** Adam Morehouse  
**Course:** CSC333 - Computer Organization  
**Date:** April 14, 2025  

This project calculates the storage capacity of a hard drive based on user-provided physical specifications such as platters, surfaces, tracks, sectors, and bytes per sector. It also includes a test automation script to validate the calculations across a variety of configurations — from tiny drives to multi-terabyte monsters.

---

## 📜 Description

The program prompts the user for:

- Number of **platters**
- **Surfaces per platter**
- **Tracks per surface**
- **Sectors per track**
- **Bytes per sector**

It then calculates the total size of the hard drive in **bytes**, **KB**, **MB**, **GB**, and **TB**, and displays the smallest unit greater than or equal to 1.0 (rounded to 1 decimal place). This simulates how modern high-capacity drives are calculated based on physical density, not just platter count.

---

## 🚀 How to Use

```bash
python DriveCapacity.py
```

You'll be prompted to enter five values. Afterward, the calculated drive capacity will be shown in the most appropriate unit.

Example:

```
How many platters? 6
How many surfaces per platter? 2
How many tracks per surface? 500000
How many sectors per track? 2000
How many bytes per sector? 4096
Drive size: 44.7 TB
```

---

## 🔍 Example Test Cases

To validate the program, a test script `run_tests.py` is provided. It feeds sample inputs automatically and compares the output to the expected drive size. This makes it easy to verify that the calculator handles various input sizes correctly.

### Run the tests:

```bash
python run_tests.py
```

### Output:

Results are saved to `test_results.txt`, and each test includes:

- Input parameters
- Expected output
- Actual output
- PASS/FAIL status

---

## 📊 Sample Test Scenarios

| Test | Platters | Surfaces | Tracks | Sectors | Bytes | Expected Size |
|------|----------|----------|--------|---------|--------|----------------|
| Tiny | 1        | 1        | 1      | 1       | 512    | 512.0 bytes    |
| Small| 1        | 2        | 1000   | 100     | 512    | 97.7 MB        |
| Medium| 2       | 2        | 5000   | 500     | 4096   | 38.1 GB        |
| Large| 6        | 2        | 500000 | 2000    | 4096   | 44.7 TB        |
| Huge | 8        | 2        | 1000000| 3000    | 4096   | 178.8 TB       |

---

## 🧪 Files Included

| File | Description |
|------|-------------|
| `DriveCapacity.py` | Main calculator script |
| `run_tests.py`     | Automated test runner |
| `test_results.txt` | Test output results |
| `README.md`        | This file |

---

## 📌 Notes

- The calculator uses **base-2 units (1024)** for conversions.
- Input validation ensures all values are positive integers.
- Handles output formatting and proper unit display (e.g., MB, GB, TB).

---

## 📘 License

This project is provided for academic use under the [MIT License](LICENSE). Feel free to fork, reuse, or expand it.

---

## 🙌 Credits

Developed by Adam Morehouse as part of SUNY Plattsburgh's CSC333 coursework.
