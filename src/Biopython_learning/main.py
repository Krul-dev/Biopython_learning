#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-08-01
Description: 
"""
from pathlib import Path

# This assumes you're running the notebook or IPython session from the project root
PROJECT_ROOT = Path().resolve()
DATA_DIR = PROJECT_ROOT / "data"


def main():
    print(PROJECT_ROOT, "is the project root directory.")
    print(DATA_DIR, "is the data directory.")


if __name__ == "__main__":
    main()
