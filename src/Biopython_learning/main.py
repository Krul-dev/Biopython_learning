#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-08-01
Description: 
"""
from pathlib import Path
from Bio import SeqIO

# This assumes you're running the notebook or IPython session from the project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"


def main():
    fasta_file_path = DATA_DIR / "ls_orchid.fasta"
    sequences = SeqIO.parse(fasta_file_path, "fasta")
    for record in sequences:
        print(f"ID: {record.id}, Length: {len(record.seq)}")
        print(f"Description: {record.description}")
        # Print first 50 characters of the sequence
        print(f"Sequence: {record.seq}")


if __name__ == "__main__":
    main()
