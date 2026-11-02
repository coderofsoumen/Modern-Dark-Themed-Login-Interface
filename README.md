Modern Dark-Themed Tkinter Login Interface
A clean, responsive desktop login window built using Python's native tkinter library. Designed with a modern dark-mode aesthetic (Catppuccin Mocha-inspired palette), rounded entry styling, and built-in keyboard event handling.
Features
 * Modern Dark Palette: Clean contrast using deep slate backgrounds (#1E1E2E, #2A2A3E) and soft pastel accents (#89B4FA).
 * Input Validation: Checks for empty fields and informs the user before processing credentials.
 * Keyboard Shortcut: Bound to the <Return> / Enter key so users can submit the form without clicking the button.
 * Password Masking: Uses the bullet symbol (•) to obscure password input.
 * Native Dialogs: Clear popups for missing fields, authentication success, and login failures using tkinter.messagebox.
 * Zero Third-Party Dependencies: Runs entirely on standard Python 3 installations.
Default Credentials
| Field | Default Value |
|---|---|
| Username | admin |
| Password | 1234 |
Requirements
 * Python 3.x
 * Tkinter (included by default with most standard Python installations on Windows and macOS)
> Linux Users: If tkinter is not installed by default, install it via your package manager:
> sudo apt install python3-tk
> 
> 
Getting Started
 * Save the code as login.py.
 * Run the file from your terminal:
python login.py

Color Palette Reference
| Element | Hex Code | Description |
|---|---|---|
| Window Background | #1E1E2E | Base dark background |
| Card Frame | #2A2A3E | Elevated surface background |
| Primary Accent / Button | #89B4FA | Periwinkle blue focus & action color |
| Button Hover State | #B4BEFE | Lightened active state |
| Primary Text | #CDD6F4 | High-contrast readable text |
| Muted Text / Labels | #BAC2DE / #A6ADC8 | Secondary labels and subtitles |
| Input Border | #45475A | Inactive entry highlight |
File Structure & Logic Overview
 * root: Configures the fixed 420x540 window and disables window resizing.
 * card_frame: Acts as an elevated container providing uniform padding around form controls.
 * handle_login(): Reads the values from username_entry and password_entry, runs conditional validation, and renders appropriate messagebox alerts.
