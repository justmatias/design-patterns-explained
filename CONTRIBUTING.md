# Contributing to Design Patterns in Python

Thank you for your interest in contributing to this project! Here are some guidelines to help you get started.

## Setting Up the Development Environment

1. **Fork the repository**: Click the "Fork" button at the top right corner of the repository page to create a copy of the repository in your GitHub account.

2. **Clone the repository**: Clone your forked repository to your local machine:

    ```sh
    git clone https://github.com/justmatias/design-patterns-explained.git
    cd design-patterns-explained
    ```

3. **Install uv**: If you don't have uv installed, follow the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

4. **Install dependencies**:

    ```sh
    uv sync --group dev
    ```

5. **Install pre-commit hooks**:

    ```sh
    uv run pre-commit install
    ```

## Running Pre-Commit Hooks

Run all hooks manually at any time with:

```sh
uv run poe format
```

This runs codespell, pyupgrade, ruff, pylint, and mypy across the entire codebase.

## Project Structure

Patterns are organized by category. Each pattern lives in its own folder containing:

```
creational/
├── builder/
│   ├── builder.py       # real-world example
│   ├── conceptual.py    # abstract/generic implementation
│   └── index.md         # documentation page
├── singleton/
│   └── ...
└── prototype/
    └── ...
```

When adding a new pattern, follow the same structure and use `template.md` as a starting point for the documentation page.

## Making Changes

1. **Create a new branch**:

    ```sh
    git checkout -b <branch-name>
    ```

2. **Make your changes** following the project structure above.

3. **Commit your changes** with a descriptive commit message:

    ```sh
    git add .
    git commit -m "Description of the changes"
    ```

4. **Push your changes**:

    ```sh
    git push origin <branch-name>
    ```

5. **Create a pull request**: Go to the original repository and open a pull request with a clear description of your changes.

## Code Style

- Use meaningful variable, function, and class names.
- All hooks must pass (`uv run poe format`) before submitting a pull request.
- Follow the existing pattern structure when adding new patterns.
