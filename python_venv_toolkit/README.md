# Python Virtual Environment Setup Toolkit

This toolkit helps you manage Python environments and dependencies in a structured way, with a simple menu interface.

## Included Files

- `setup.bat`: Windows batch script to:
  1. Detect installed Python versions
  2. Let you choose one to create a `.venv`
  3. Export `requirements.txt` without version numbers (using `pipreqs`)
  4. Install from `requirements.txt`

- `setup.sh`: Linux (Kubuntu) Bash script with the same functionality.

## Usage

### Windows

1. Double-click or run `setup.bat` in a command prompt.
2. Follow the menu instructions.

### Linux

1. Make the script executable:
   ```bash
   chmod +x setup.sh
   ```
2. Run the script:
   ```bash
   ./setup.sh
   ```

## Dependencies

Both scripts use `pipreqs` to generate `requirements.txt`:
- If not installed, the scripts will automatically install it inside the virtual environment.

## Notes

- Version numbers are excluded in `requirements.txt` (for portability).
- Scripts assume a project structure where all `.py` files are in the same folder or subfolders.
