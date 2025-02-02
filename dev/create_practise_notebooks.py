import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell

# Path to your notebooks directory
notebooks_path = (
    "/Users/vamsi_mbmax/Library/CloudStorage/OneDrive-Personal/"
    "01_vam_PROJECTS/LEARNING/proj_Productivity/dev_proj_Productivity/"
    "practise_prod_python_tools/notebooks"
)

# Dictionary with section keys and list of tool descriptions
sections = {
    "beginner_python_content": [
        "args kwargs - Function Arguments",
        "comprehensions - Awesome One-Liners",
        "decorators - Expressive Functions",
        "lambda - Expressive Functions",
        "recursion - Rephrasing Complexity",
        "virtualenv - Environments Matter"
    ],
    "tools_that_check_python_code": [
        "black - Format Your Code",
        "flake8 - Check Your Style",
        "pre-commit - Prevent Bad Commits",
        "pyinstrument - Measure Slow Code",
        "pytest - Intro to Testing",
        "pytest tricks - Utilities for Pytest"
    ],
    "scikit_learn_related": [
        "bad labels - And how to find them",
        "human learn - Rule-Based Systems",
        "partial_fit - Batches of ML",
        "scikit dummy - Smart Benchmark",
        "scikit learn - Overview Starts Here",
        "scikit meta - Extra Model Behavior",
        "scikit metrics - Measurement Matters",
        "scikit prep - Preprocess Data",
        "scikit save - Re-Use Models Safely"
    ],
    "jupyter_tools": [
        "ipywidgets - UI on Jupyter",
        "jupyter lab - Happy Notebooks",
        "pigeon - Simple Labeling"
    ],
    "visualization": [
        "altair - Interactive Plots",
        "hiplot - Parallel Coordinates",
        "ipywidgets - UI on Jupyter",
        "marimo - Reactive Notebooks",
        "matplot gif - Quick GIFs",
        "matplotlib - Quick Plots",
        "streamlit - Interactive Demos"
    ],
    "cool_command_line_tools": [
        "cookiecutter - Automate Boilerplate",
        "cool cli - Joy in the Terminal",
        "entr - Repeat on Change",
        "makefiles - Not War",
        "ngrok - Quick Demo Tunnels",
        "pyinstrument - Measure Slow Code",
        "rich - Great Terminal Output",
        "typer - Make Grand CLIs"
    ],
    "web_development": [
        "fastapi - Fast Web Stuff",
        "locust - Web Stress Tests",
        "ngrok - Quick Demo Tunnels",
        "playwright - Web Tests, End to End",
        "tailwind - CSS Made Easier"
    ]
}

# Ensure the notebooks directory exists
os.makedirs(notebooks_path, exist_ok=True)

# Loop through each section and create a notebook file with markdown headers
for section, tools in sections.items():
    nb = new_notebook()
    for tool in tools:
        # Create a markdown cell with a level 2 header for the tool
        cell = new_markdown_cell("## " + tool)
        nb.cells.append(cell)

    # Build the file name: practise_<section_name>.ipynb
    filename = f"practise_{section}.ipynb"
    filepath = os.path.join(notebooks_path, filename)

    # Write the notebook to file
    with open(filepath, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    print(f"Created {filepath}")
