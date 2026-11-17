"""Command line entry point for nattergrooms4r_kit."""
import argparse

from .core import Nattergrooms4rTool


def main(argv=None):
    parser = argparse.ArgumentParser(description="csv numeric summary")
    parser.add_argument("path")
    parser.add_argument("--column")
    args = parser.parse_args(argv)
    for name, stats in Nattergrooms4rTool().summarize(args.path, args.column).items():
        print(f"{name}: n={stats['n']} min={stats['min']} max={stats['max']} mean={stats['mean']}")
    return 0
