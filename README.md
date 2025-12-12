# Advent of Code

This repository contains my solutions to [Advent of Code](https://adventofcode.com/) challenges. Each challenge consists of two-part problems that cover various algorithmic and computational topics including graph traversal, dynamic programming, string manipulation, and mathematical computations.

## Repository Structure

Each year has its own directory, with individual day folders containing:
- **[Puzzle-Name].py** - Python solution file with descriptive naming based on the puzzle theme
- **Puzzle input data** - Stored in a separate submodule to keep solutions and data organized

## Setup

### Python Virtual Environment Setup

1. Create a virtual environment:
    ```bash
    python -m venv adventofcode
    ```

2. Activate the virtual environment:
    - **Windows:**
      ```bash
      adventofcode\Scripts\activate
      ```
    - **Linux/Mac:**
      ```bash
      source adventofcode/bin/activate
      ```

3. Install the local `aoc_util` package in editable mode:
    ```bash
    pip install -e .
    ```

This installs the package in development mode, allowing you to make changes without reinstalling.