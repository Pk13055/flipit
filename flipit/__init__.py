from pathlib import Path
from typing import Tuple

import cv2
import pandas as pd
import numpy as np


from .parser import parse_file


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
    def add_object(canvas: np.array, data_dir: Path, details: pd.Series) -> np.array:
        file_path = data_dir / Path(details.path)
        obj = cv2.imread(str(file_path)).astype('uint8')
        x = int(details.x)
        y = int(details.y)
        _h, _w, _ch = obj.shape
        canvas[x:x+_h, y:y+_w] = obj
        return canvas

    def generate(self, input_path: Path, output_path: Path) -> bool:
        """Generate the video writers for each I/O pair"""
        self.data = parse_file(input_path)
        self.data.frame = pd.to_numeric(self.data.frame)
        self.canvas = 255 * np.ones((self.height, self.width, 3)).astype('uint8')
        data_path = input_path.parent
        # TODO: add more codecs
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(str(output_path), fourcc, self.frame_rate, (1000,1000))
        for frame_id, objects in self.data.groupby('frame'):
            # TODO make vectorized :(
            canvas = self.canvas.copy()
            for index, row in objects.iterrows():
                try:
                    canvas = self.add_object(canvas, data_path, row)
                    print(f"[info] generating frame {frame_id}")
                except Exception as e:
                    print(f"[error] could not generate frame {frame_id} | {e}")
            out.write(canvas)
        out.release()
        return True
