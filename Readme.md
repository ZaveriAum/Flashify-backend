# Flashify-backend

[![Flask](https://img.shields.io/badge/Flask-2.2.3-blue)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 🚀 Features

- Feature 1: Create Flashcards in folders manually.
- Feature 2: Create Flashcards using ai based on topic or text.
- Feature 3: Interact with the flashcards using ai.

---

## 📂 Project Structure

```plaintext
📦 Flashify-backend
├── controllers/         # Handles HTTP requests and defines logic for API endpoints
├── decorators/          # Custom decorators for reusable functionalities like authentication
├── migrations/          # Database migration files managed by Flask-Migrate
├── models/              # Defines database models and schema
├── routes/              # Organizes API route definitions
├── services/            # Business logic and service layer for modular functionality
├── utils/               # Utility functions and helpers used across the project
├── venv/                # Virtual environment for managing project-specific Python dependencies
├── .gitignore           # Specifies files and directories to be ignored by Git
├── app.py               # Entry point for the Flask app
├── config.py            # Configuration settings and environment variables
├── requirements.txt     # Python dependencies for the project
└── README.md            # Project documentation
```

## 🛠️ Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.9 or higher
- pip (Python package manager)
- Virtual environment tools (venv or virtualenv)

### Setup Instructions

#### Clone the repository:

```bash
git clone https://github.com/ZaveriAum/Flashify-backend.git
cd Flashify-backend
```

#### Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

#### Install the required dependencies:

```bash
pip install -r requirements.txt
```

#### Create a config.py file or set them directly in your shell: from the given example.config.py

```bash
flask run
```
