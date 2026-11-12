# AI & ML Journey

A structured, hands-on learning repository documenting the progression from **Python fundamentals** and **Object-Oriented Programming (OOP)** to **Data Structures & Algorithms (DSA)**, **numerical computing with NumPy**, **exploratory data analysis with Pandas & Matplotlib**, and **real-world data cleaning workflows** in Jupyter Notebooks.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Module Breakdown](#module-breakdown)
  - [1. Python Fundamentals](#1-python-fundamentals)
  - [2. Object-Oriented Programming (`OOP/`)](#2-object-oriented-programming-oop)
  - [3. Data Structures & Algorithms (`DSA/`)](#3-data-structures--algorithms-dsa)
  - [4. Numerical Computing (`Numpy/`)](#4-numerical-computing-numpy)
  - [5. Data Analysis (`Pandas/`)](#5-data-analysis-pandas)
  - [6. Data Cleaning Notebooks (`Data Cleaning/`)](#6-data-cleaning-notebooks-data-cleaning)
- [Tech Stack & Dependencies](#tech-stack--dependencies)
- [Getting Started](#getting-started)
- [Datasets & Git Tracking Notes](#datasets--git-tracking-notes)

---

## Project Overview

This repository serves as a personal study archive and reference codebase for building foundational skills required for Artificial Intelligence and Machine Learning:

- **Core Python**: Variables, data types, operators, strings, collections, control flow, functions, and recursion.
- **Software Design**: Classes, constructors, encapsulation, properties, static methods, and inheritance.
- **Problem Solving**: Recursive algorithms (factorial, Fibonacci, Tribonacci).
- **Scientific Computing**: Multi-dimensional arrays, broadcasting, vectorization, slicing, filtering, and aggregations with NumPy.
- **Data Manipulation & Cleaning**: Inspecting, filtering, transforming, deduplicating, visualizing, and exporting real-world CSV datasets using Pandas and Matplotlib.

---

## Repository Structure

```text
.
├── Introduction/           # First Python scripts and external package usage
├── ChapterTwo/             # Variables, data types, operators, type casting, input
├── ChapterThree/           # Strings, slicing, and string methods
├── ChapterFour/            # Lists and tuples
├── ChapterFive/            # Dictionaries and sets
├── ChapterSix/             # Conditional statements and logical/relational operators
├── ChapterSeven/           # Loops (for, while) and loop control (break, continue)
├── ChapterEight/           # Functions and recursion exercises
├── OOP/                    # Object-Oriented Programming concepts in Python
├── DSA/                    # Recursion and basic data structure exercises
├── Numpy/                  # NumPy arrays, broadcasting, math, and filtering
├── Pandas/                 # Exploratory data analysis with IPL dataset
├── Data Cleaning/          # End-to-end data cleaning Jupyter notebooks
├── pyproject.toml          # Project metadata and core dependencies
├── uv.lock                 # Lockfile managed by uv
└── .gitignore              # Git ignore rules (excludes *.csv)
```

---

## Module Breakdown

### 1. Python Fundamentals

Organized into introductory scripts and progressive chapters:

| Directory | Files | Topics Covered |
| :--- | :--- | :--- |
| `Introduction/` | `HelloWorld.py`, `Jokes.py` | Basic `print()` output and importing external packages (`pyjokes`) |
| `ChapterTwo/` | `Variables.py`, `Datatypes.py`, `Operators.py`, `TypeCasting.py`, `InputFunction.py` | Integers, floats, strings, booleans, `None`, arithmetic/assignment/comparison/logical operators, type conversion, and `input()` |
| `ChapterThree/` | `Strings.py`, `Functions.py` | String slicing (`[start:end]`) and built-in string methods (`len`, `startswith`, `endswith`, `capitalize`) |
| `ChapterFour/` | `Lists.py`, `tuple.py` | Mutable lists (`append`, `sort`, `reverse`) vs. immutable tuples (`count`, `index`) |
| `ChapterFive/` | `Dictionary.py`, `DictionaryMethods.py`, `Set.py`, `SetMethods.py` | Key-value mappings (`keys`, `values`, `items`, `update`) and unique unordered sets (`add`) |
| `ChapterSix/` | `Conditions.py`, `RelationalOperators.py`, `LogicalOperators.py` | `if`/`elif`/`else` branching, relational comparisons (`==`, `!=`, `<`, `>`), and boolean logic (`and`) |
| `ChapterSeven/` | `ForLoop.py`, `WhileLoop.py`, `BreakandContinue.py` | `range()` iteration, `while` loops, early exit with `break`, and skipping iterations with `continue` |
| `ChapterEight/` | `Functions.py`, `Recursion.py`, `Sum_with_recursion.py` | Custom functions, recursive factorial, and recursive sum of natural numbers |

---

### 2. Object-Oriented Programming (`OOP/`)

Covers Python's OOP paradigm and class mechanics:

| File | Concept Demonstrated |
| :--- | :--- |
| `Class.py` | Defining a class with class attributes and instantiating objects |
| `Constractor.py` | Initializing object state with `__init__` |
| `Self_parameter.py` | Instance methods and how `self` binds to the calling instance |
| `Static_methods.py` | Class-level utility methods using the `@staticmethod` decorator |
| `Getter_setter.py` | Encapsulating attributes with `@property` and `@<attr>.setter` |
| `Inheritance.py` | Single inheritance and calling parent constructors via `super()` |
| `Multiple_inheritance.py` | Inheriting from multiple parent classes (`Programmer(Employee, Coder)`) |
| `Private_attributes_and_methods.py` | Name mangling with double underscores (`__attribute`, `__method`) |

---

### 3. Data Structures & Algorithms (`DSA/`)

Introductory algorithm and recursion practice:

| File | Description |
| :--- | :--- |
| `Lists.py` | Basic list indexing and element access |
| `Recursion1.py` | Printing numbers from `1` to `n` recursively |
| `Factorial.py` | Recursive factorial calculation (`fact(n)`) |
| `Fibo.py` | Recursive Fibonacci sequence (`fibo(n)`) |
| `Tribo.py` | Recursive Tribonacci sequence (`tribo(n)`) |

---

### 4. Numerical Computing (`Numpy/`)

Hands-on scripts exploring NumPy's `ndarray` and vectorized operations:

| File | Topics Covered |
| :--- | :--- |
| `Version_check.py` | Checking the installed NumPy version |
| `Multidimentional_array.py` | Creating `0D`, `1D`, `2D`, and `3D` arrays; inspecting `.ndim`, `.shape`, and multi-axis indexing |
| `Dtypes.py` | Explicit data types (`np.str_`, `<U6`), `.dtype`, and memory footprint (`.nbytes`) |
| `NumPy_functions.py` | Array initialization with `np.zeros()` |
| `Reshape.py` | Changing dimensions with `.reshape()` (including `-1` inferred dimensions) |
| `Slicing.py` | 2D row and column slicing (`array[start:end:step]`) |
| `Scalar_arithmetics.py` | Element-wise scalar operations (`+`, `-`, `*`, `/`, `**`) |
| `Multiply_array.py` | Vectorized array multiplication vs. Python lists |
| `Broadcasting.py` | Multiplying arrays of compatible shapes (`(1, 4)` and `(4, 1)`) |
| `Vectorized_math_functions.py` | Universal functions such as `np.sqrt()` and `np.round()` |
| `Aggregate_functions.py` | Summary statistics: `np.sum()`, `np.mean()`, `np.std()`, `np.var()` |
| `Filtering.py` | Boolean masking (`<`, `>=`, `&`) and conditional replacement with `np.where()` |
| `Random_num.py` | Random integers, array shuffling, and sampling with `np.random.default_rng()` |

---

### 5. Data Analysis (`Pandas/`)

- **`IPL_analysis.ipynb`** (uses `matches.csv`):
  - DataFrame exploration (`head()`, `tail()`, `shape`, `info()`, `describe()`).
  - Column selection and row slicing via `.iloc`.
  - Single and compound boolean masking (filtering matches by `city` and `date`).
  - Frequency counts (`value_counts()`), duplicate removal (`drop_duplicates(subset=...)`), and grouping (`groupby('city')`).
  - Data visualization with Matplotlib: horizontal bar chart of top match winners and pie chart of toss decisions.

---

### 6. Data Cleaning Notebooks (`Data Cleaning/`)

Practical data cleaning pipelines implemented in Jupyter Notebooks:

1. **`Airbnb_data_analysis.ipynb`** (Dataset: `Airbnb_Open_Data.csv`)
   - Selecting relevant listing columns and dropping unused metadata (`house_rules`, `license`, `id`, etc.).
   - Checking and removing duplicate rows (`duplicated()`, `drop_duplicates()`).
   - Inspecting and dropping missing values (`isna().sum()`, `dropna()`).

2. **`Netflix_data_analysis.ipynb`** (Dataset: `netflix1.csv` → `Cleaned_netfix_data.csv`)
   - Dropping the `rating` column and standardizing column names with `.capitalize()`.
   - Removing duplicate records and missing values.
   - Parsing `Show_id` strings (e.g., stripping the `"s"` prefix) and casting to `int`.
   - Exporting the cleaned dataset to CSV without row indices.

3. **`Zomato_data_analysis.ipynb`** (Dataset: `zomato.csv` → `Cleaned_zomato_data.csv`)
   - Filtering and dropping unnecessary restaurant metadata columns.
   - Normalizing column headers, removing duplicates/nulls, and resetting DataFrame indices.
   - Cleaning string formatting in `Rate` (removing whitespace and replacing `/` with `" out of "`).
   - Encoding binary categorical values in `Online_order` (`"Yes"` → `1`, otherwise `0`).
   - Exporting the processed dataset to CSV.

---

## Tech Stack & Dependencies

- **Python**: `>= 3.14` (configured in `pyproject.toml`)
- **Package Manager**: [`uv`](https://docs.astral.sh/uv/) (`pyproject.toml` & `uv.lock`)
- **Core Dependency** (defined in `pyproject.toml`):
  - `pyjokes >= 0.8.3`
- **Additional Libraries** (used in `Numpy/`, `Pandas/`, and `Data Cleaning/`):
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `jupyter` / `ipykernel` (for running `.ipynb` notebooks)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ShahriarXProxima/AI-ML-Journey.git
cd AI-ML-Journey
```

### 2. Set Up the Environment

Using **uv** (recommended, matches `pyproject.toml` and `uv.lock`):

```bash
uv sync
```

To run the NumPy, Pandas, and Data Cleaning modules, also install the data science packages in your environment:

```bash
uv pip install numpy pandas matplotlib jupyter
```

Or using standard **pip** and **venv**:

```bash
python -m venv .venv
source .venv/bin/activate
pip install pyjokes numpy pandas matplotlib jupyter
```

### 3. Run Scripts & Notebooks

Run any standalone Python script from the project root:

```bash
python Introduction/Jokes.py
python OOP/Inheritance.py
python Numpy/Broadcasting.py
```

Launch Jupyter Notebook (or open the `.ipynb` files directly in VS Code) to explore the Pandas and Data Cleaning workflows:

```bash
jupyter notebook
```

---

## Datasets & Git Tracking Notes

- `.gitignore` excludes `*.csv` (and `Data Cleaning/zomato.csv` explicitly) to avoid committing large or generated CSV files.
- `Data Cleaning/Airbnb_Open_Data.csv` and `Pandas/matches.csv` are currently tracked in the repository and work out of the box.
- To execute `Data Cleaning/Netflix_data_analysis.ipynb` or `Data Cleaning/Zomato_data_analysis.ipynb` locally, place `netflix1.csv` and `zomato.csv` inside the `Data Cleaning/` directory before running the notebooks.
