"""bpm2fps - Match song beats to their closest frame.
"""

from . import beats_to_frames_data

import argparse
import json


def get_parser():
    """Returns: Argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-s", "--start", help="Start time (seconds).", type=float, default=0.0
    )
    parser.add_argument(
        "-e", "--end", help="End time (seconds)", type=float, default=60.0
    )
    parser.add_argument(
        "-b",
        "--bpm",
        help="Beats per minute",
        type=float,
    )
    parser.add_argument(
        "-f", "--fps", help="Frames per second", type=float, default=24.0
    )
    return parser


def main():
    """Main entry point"""
    parser = get_parser()
    args = parser.parse_args()
    if args.bpm:
        data = beats_to_frames_data(args.start, args.end, args.bpm, args.fps)
        json_data = json.dumps(data, indent=2)
        print(json_data)
    else:
        try:
            from . import gui

            gui.main()
        except ImportError:
            parser.print_help()


if __name__ == "__main__":
    main()
