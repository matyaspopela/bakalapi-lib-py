# Refactor to src-layout for PyPI Compatibility

## Goal
The goal is to refactor the `bakalapi-libs` project to use the standard `src` layout. This ensures that the package is correctly packaged and installed, avoiding common pitfalls with flat layouts (like import ambiguities). This will make the package fully compatible with PyPI and `pip install`.

## Architecture
The project will be restructured as follows:

```text
bakalapi-libs/
├── src/
│   └── bakalapi/
│       ├── __init__.py
│       ├── client.py
│       └── models.py
├── pyproject.toml
├── setup.py (optional, can be kept for legacy compatibility but updated)
├── README.md
└── LICENSE (if applicable)
```

## Changes
1.  **Directory Structure**: Create a `src` directory and move the `bakalapi` package inside it.
2.  **Configuration**: Update `pyproject.toml` to specify `package-dir`.
3.  **Metadata**: Ensure all necessary metadata for PyPI is present and correct in `pyproject.toml`.

## Rationale
Using a `src` layout is a best practice for Python packaging:
-   It prevents the "importing local directory" mistake during testing.
-   It forces you to install the package to test it, ensuring that what you test is what you ship.
-   It is the standard recommended by the Python Packaging Authority (PyPA).
