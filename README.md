# DeWare Discord Spammer

## 📋 Overview
DeWare Discord Spammer is a Python application designed for automated messaging across multiple Discord channels. This tool provides users with the capability to send messages to various channels simultaneously, making it efficient for notifications and announcements.

## 🔧 Installation
To use this application, you'll need to install the required Python packages. Use the package manager [pip](https://pip.pypa.io/en/stable/) for installation:

```bash
pip install requests 
pip install pyfade 
```

## ✨ Features
- **Multi-Channel Support**: Send messages to multiple Discord channels simultaneously
- **Automated Messaging**: Streamline your communication process with automated message delivery

## 🚀 Executable Creation
To convert the script into a standalone executable:

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Navigate to the project directory in your command prompt and run:
```bash
pyinstaller main.py --onefile --icon=NONE
```

## ⚠️ Important Notice
Please be aware that this is a legacy project that may require updates to function with current versions of its dependencies. The application was developed using an older version of the pyfade library, and compatibility issues may arise. Users with Python development experience are encouraged to review and update the code as needed.
