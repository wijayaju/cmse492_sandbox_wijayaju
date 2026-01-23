# Description:
Workspace for CMSE492 assignments.

# Setup venvi (for traditional Python workflows):
Run the following commands:
```
python -m venv cmse492_env
python -m pip install -r requirements.txt
```

# Setup conda (for scientific computing or if you need non-Python dependencies):
Command to create the environment: `conda env create -f environment.yml`
Command to activate it: `conda activate day03-conda-env`
Command to deactivate it: `conda deactivate`

# Setup uv (recommended for new users)
Command to install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
Command to sync uv to project dependencies: `uv sync`
Command to prepend before any command (to properly utilize the environment): `uv run`

# Project Structure Analysis
* cmse492_env/ - directory for virtual environment
* data/ - directory for datasets
* notebooks/ - directory for Jupyter Notebooks
* notes/ - directory for notes
* requirements.txt - list of packages to install in virtual environment
* src/ - directory for source code

# Analysis
Using sample data, makes a computation and visualization based on it.

Location: `src/simple_analysis.py`

How to run: `python src/simple_analysis.py`

