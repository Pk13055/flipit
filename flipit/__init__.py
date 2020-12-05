from pathlib import Path
from typing import Tuple

from .parser import parse_file
from .generator import ClipGen


class FlipIt(object):
    """FlipIt Compiler

        The compiler is responsible for parsing the flip file and applying
        the image merging logic necessary to generate an animated video sequence
    """

    def __init__(self, frame_rate: int, dims: Tuple[int, int]):
        """Initialize a Flipbook compiler for video generation"""
        self.frame_rate = frame_rate
        self.height, self.width = dims

    @staticmethod
    def generate(input_path: Path, output_path: Path) -> bool:
        """Generate the video writers for each I/O pair"""
        flip_data = parse_file(input_path)
        generator = ClipGen(flip_data, output_path)
        return generator.generate_clip()

