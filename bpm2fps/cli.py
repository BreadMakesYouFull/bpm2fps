"""bpm2fps - Match a songs beats to their closest frame.
"""

from . import beats_to_frames_data

import argparse
import json


def get_parser():
    """Returns: Argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(
        description=__doc__
    )
    parser.add_argument(
        "start",
        help=(
            "Start time (seconds). "
            "Can be used to offset beats."
        ),
        type=float,
    )
    parser.add_argument(
        "end",
        help="End time (seconds)",
        type=float,
    )
    parser.add_argument(
        "bpm",
        help="Beats per minute",
        type=float,
        default=60.0
    )
    parser.add_argument(
        "fps",
        help="Frames per second",
        type=float,
        default=24.0
    )
    return parser

def main():
    """Main entry point
    """
    args = get_parser().parse_args()
    data = beats_to_frames_data(
        args.start,
        args.end,
        args.bpm,
        args.fps
    )
    json_data = json.dumps(data, indent=2)
    print(json_data)


if __name__ == "__main__":
    main()
