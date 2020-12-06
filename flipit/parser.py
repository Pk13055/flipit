from pathlib import Path

import pandas as pd

def parse_file(file_path: Path) -> pd.DataFrame:
    """Parse a .flip file and validate and generate the format"""
    # TODO: add file parsing and path confirmation
    raw = [_.split(' ') for _ in open(file_path).read().splitlines()]
    data = pd.DataFrame(raw, columns=["frame", "x", "y", "path"])
    return data
