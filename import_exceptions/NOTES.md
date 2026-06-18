# NOTES

## pip Workflow

1. Created a virtual environment using `python -m venv venv`
2. Activated the environment using `venv\Scripts\activate`
3. Installed requests using `pip install requests`
4. Generated requirements.txt using `pip freeze > requirements.txt`

## uv Workflow

1. Created a virtual environment using `uv venv`
2. Activated the environment using `.venv\Scripts\activate`
3. Installed requests using `uv pip install requests`
4. Generated requirements.txt

## Comparison

* Both pip and uv manage Python packages and dependencies.
* pip is the traditional package manager included with Python.
* uv performs environment creation and package installation much faster.
* uv is compatible with existing Python packages and workflows.
