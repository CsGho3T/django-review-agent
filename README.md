# Django Review Agent

A static code review agent for Django projects with security-focused analysis capabilities.
Django Review Agent is a developer tool designed to analyze Django projects, detect common security issues, and provide actionable code review findings.

The project is currently under active development.

---

## Overview

Reviewing backend code manually can be time-consuming and error-prone.

This project aims to build an automated review system that understands Django project structures and performs security-focused analysis using static code analysis techniques.

The agent scans a Django project, builds an internal representation of the project, applies review rules, and generates structured findings.

---

## Current Features

### Project Analysis
- Detect Django projects automatically
- Scan project files
- Locate Django settings files
- Detect URL configurations
- Discover installed applications

### Static Code Analysis
- Python AST based analysis
- Parse Python source files without executing code
- Extract configuration values from Django settings

### Security Review Rules

Currently implemented security checks:

- Django DEBUG mode enabled detection
- Hardcoded SECRET_KEY detection
- Empty ALLOWED_HOSTS detection

More security rules will be added in future versions.

---

## Architecture

The project follows a modular architecture:


djreview/
│
├── engine/
│ ├── scanner.py
│ ├── parser.py
│ ├── ast_visitor.py
│ ├── settings_reader.py
│ ├── reviewer.py
│ └── finding_factory.py
│
├── workspace/
│ ├── loader.py
│ └── workspace.py
│
├── models/
│ ├── project.py
│ └── finding.py
│
├── rules/
│ ├── base_rule.py
│ └── security/
│ ├── debug_mode.py
│ ├── secret_key.py
│ └── allowed_hosts.py
│
└── reports/


---

## How It Works

The review pipeline:


Django Project
|
v
Workspace Loader
|
v
Project Scanner
|
v
Project Mapper
|
v
Rule Engine
|
v
Findings
|
v
Reports


---

## Example Output

Example security finding:


Title:
Debug mode enabled

Severity:
HIGH

Category:
SECURITY

Description:
Django DEBUG is enabled. This can expose sensitive information.

Recommendation:
Set DEBUG=False in production.

File:
settings.py


---

## Technologies

- Python
- Django
- Abstract Syntax Tree (AST)
- Static Code Analysis
- Object-Oriented Programming
- Git / GitHub

---

## Development Goals

Future improvements:

- More Django security rules
- AI-assisted code review
- Integration with LLM providers
- GitHub repository analysis
- Automated review reports
- Code quality analysis
- Performance suggestions

---

## Project Status

🚧 Currently under active development.

The goal is to create an intelligent Django code review assistant capable of analyzing real-world Django applications and providing professional review feedback.

---

## Author

Mehdi Ebrahimi

GitHub:
https://github.com/CsGho3T
