#!/usr/bin/env python3
# coding: utf-8
"""
    :brief: Code to compile .flip files into
            video clips
    :author: pk13055
"""
import argparse
import os
from pathlib import Path
from typing import List

from flipit import FlipIt


def collect_args() -> argparse.Namespace:
    """Collect cli arguments"""
    parser = argparse.ArgumentParser(description="""
                                     FlipIt - Flipbook compiler

                                     # TODO: add description here
                                     """)
    parser.add_argument("-f", "--framerate", type=int, default=3,
                        help="frame rate of the output video")
    parser.add_argument("--height", type=int, default=1000,
                        help="height of the output clip")
    parser.add_argument("--width", type=int, default=1000,
                        help="width of the output clip")

    parser.add_argument("-i", "--input", dest="inputs", action="append",
                        help="Input .flip file(s)")
    parser.add_argument("-o", "--output", dest="outputs", action="append",
                        help="output .avi file(s)")

    args = parser.parse_args()
    return args


def main():
    args = collect_args()
    fc = FlipIt(args.framerate, (args.height, args.width))
    for _input, _output in zip(args.inputs, args.outputs):
        input = Path(_input)
        output = Path(_output)
        fc.generate(input, output)


if __name__ == "__main__":
    main()

