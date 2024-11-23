# Django Boot

A highly customizable Django starter template designed to streamline development and ensure consistency across projects. This template includes pre-configured tools for code formatting, linting, and project management.

## Features

- **Django Best Practices**: A clean and reusable structure to kickstart your Django projects.
- **Code Formatting and Linting**:
  - [Black](https://black.readthedocs.io): Enforces consistent Python code formatting.
  - [isort](https://pycqa.github.io/isort/): Automatically sorts Python imports.
  - [Flake8](https://flake8.pycqa.org): Checks your code for style guide compliance.
- **Pre-commit Hooks**:
  - Automatically format and lint your code before every commit.
- **Makefile**: Simplifies common tasks like installing dependencies, running the server, and setting up pre-commit hooks.
- **Dynamic Project Name Handling**: Automatically replaces placeholders like `{{ project_name }}` during project creation.

---

## Quick Start

Clone the template repository:

```bash
git clone https://github.com/your-username/django-starter-template.git
```

Use the template to create your Django project:

```
django-admin startproject my_project --template=/path/to/django-starter-template
```

Navigate to your new project:

```
cd my_project
```

Install dependencies:

```
make install
make runserver
make install-hooks
```

---

## How to Use

### Makefile Commands

The Makefile provides shortcuts for common tasks:

- make install - Installs all dependencies.
- make runserver - Starts the Django development server.
- make install-hooks - Installs pre-commit hooks.
- make lint - Lints the code using Flake8.
- make format - Formats code using Black and isort.

## Pre-configured Tools

- Black and isort ensure that your code is consistently formatted.
- Flake8 catches potential issues early in the development process.
- Pre-commit Hooks enforce code quality checks on every commit.

---

## File Structure

Here’s an overview of the template structure:

```
{{ project_name }}/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── ...
├── manage.py
├── requirements.txt
├── .pre-commit-config.yaml
├── pyproject.toml
├── Makefile
├── README.md
└── setup.cfg
```

---

## Contributing

Contributions are welcome! If you’d like to improve this template:

- Fork the repository.
- Create a new branch:

```
git checkout -b feature/my-feature
```

- Make your changes and test thoroughly.
- Submit a pull request.

---

## License

This project is licensed under the MIT License.
