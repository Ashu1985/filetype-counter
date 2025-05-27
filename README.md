# 📁 Filetype Counter

**Filetype Counter** is a simple and extensible Python CLI tool to count files in a directory and its subdirectories — either as a total count or grouped by file extensions.

Ideal for quickly understanding file distribution in large folders.

---

## 🔧 Installation (Local Development)

Clone the repository and install it as a CLI tool:

git clone https://github.com/Ashu1985/filetype-counter.git
cd filetype-counter
Use setup_env.bat/setup_env.sh to setup base env

## 🚀 Usage
The tool accepts two arguments:

-groupby:

Use Extension to count files by type (extension)

Use None to count total files

-FolderPath:
Path to the folder you want to analyze

## 📌 Example 1 — Count Total Files

filecounter -groupby None -FolderPath "C:\MyFolder\Files"

### Sample Output:

Total files in 'C:\MyFolder\Files': 18093

## 📌 Example 2 — Count Files Grouped by Extension

filecounter -groupby Extension -FolderPath "C:\MyFolder\Files"

### Sample Output:

📂 File counts by extension in 'C:\MyFolder\Files':

.jpeg:   24  

.jpg:     9  

.xlsx:    1  

.zip:     1  

NO_EXT:   1

## 🧠 Features
Recursively counts files in nested subfolders

Supports Windows and Unix-style paths

Handles quoted or unquoted folder paths

Can be packaged as a .whl, .exe, or published on PyPI (future-ready)

## 📄 License
This project is licensed under the MIT License.


