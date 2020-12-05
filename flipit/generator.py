"""
    :brief: Engine actually calculates the logic and combination of the
    images into the appropriate sequence
"""
from pathlib import Path
from typing import Dict

import cv2


class ClipGen(object):
    """Logic and sequence generator"""

    def __init__(self, flip_data: Dict, output_path: Path):
        """Initialize the engine with data and output path"""
        self.data = flip_data
        self.to_write = output_path

    def generate_clip(self) -> bool:
        """Generate the clip based on language definiton"""
        # TODO: add generation logic
        print(cv2.__version__, self.data)
        return True

