# Password Strength Checker

This is a simple Python tool to assess the strength of a password based on several criteria like length, presence of uppercase and lowercase letters, numbers, and special characters. It provides feedback on how strong the password is and offers suggestions for improvement.

Additionally, the tool uses a list of **common passwords** (SecList file) to check if the password is too common and offers feedback to avoid weak, commonly used passwords.

## Features

- **Password Strength Evaluation**: Evaluates whether the password is "Weak", "Moderate", or "Strong".
- **Detailed Feedback**: Gives suggestions to improve password strength (e.g., add numbers, special characters).
- **Common Password Check**: Checks the password against a list of common passwords (SecList file).
- **Easy-to-use GUI**: Built with `Tkinter`, this tool has a user-friendly interface.
- **Password Visibility Toggle**: Allows users to show/hide their password while typing.

## Requirements

- Python 3.x
- Tkinter (included with Python by default)
- A Password file (a list of common passwords) is required for the common password check.

## How to Run

1. Clone the repository or download the `password_strength_checker.py` file.
4. Open a terminal or command prompt, navigate to the directory containing `password_checker.py`.
5. Run the script with the following command:

   ```bash
   python password_checker.py
   ```

## How to Use

1. **Enter your password**: Type the password you want to check in the input field.
2. **Check strength**: Click on the "Check Strength" button to evaluate your password.
3. **View feedback**: The program will provide feedback on whether your password is **Weak**, **Moderate**, or **Strong**, along with suggestions for improvement.
4. **Clear fields**: Click the "Clear" button to reset the fields and start over.

## Notes

- The tool uses the **SecList Password file** (common passwords) to check if the entered password is too commonly used and provides feedback to avoid weak, common passwords.
- Passwords with fewer than 6 characters are considered **Weak**, regardless of complexity.
- The program will display suggestions if certain criteria (like adding numbers, special characters, etc.) are not met.
