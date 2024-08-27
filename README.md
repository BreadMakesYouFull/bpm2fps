# bpm2fps

Match song beats to their closest frame for animation.

* Utility to convert beats per minute to animation frames.
* Data export to CSV or JSON.
* USD export for bouncing ball reference.
* Also available as cli / python utility

[https://github.com/BreadMakesYouFull/bpm2fps](https://github.com/BreadMakesYouFull/bpm2fps)

## Preview

![GUI](https://raw.githubusercontent.com/BreadMakesYouFull/bpm2fps/main/preview_gui.gif)

![Exported USD reference](https://raw.githubusercontent.com/BreadMakesYouFull/bpm2fps/main/preview_usd.gif)

## Install

Requires:

* python 3
* pyside6 (gui)

```
# Install
pip install bpm2fps[gui]

# ... or install without GUI
pip install bpm2fps
```

## GUI

```
# Launch GUI
bpm2fps
```

## Command line


### Usage

```
./bpm2fps.sh --help
usage: cli.py [-h] [-s START] [-e END] [-b BPM] [-f FPS]

bpm2fps - Match song beats to their closest frame.

options:
  -h, --help            show this help message and exit
  -s START, --start START
                        Start time (seconds).
  -e END, --end END     End time (seconds)
  -b BPM, --bpm BPM     Beats per minute
  -f FPS, --fps FPS     Frames per second
```

### Example
```
./bpm2fps.sh --bpm 120
# Result:
[
  {
    "beat": 0,
    "frame": 0.0,
    "second": 0.0
  },
  {
    "beat": 1,
    "frame": 12.0,
    "second": 0.5
  },
  {
    "beat": 2,
    "frame": 24.0,
    "second": 1.0
  },
  # ... and so on
]
```

Example chained with ``jq`` to get only beat frames:
```
./bpm2fps.sh --bpm 120 | jq '.[]["frame"]'
# Result:
0
12
24
36
48
60
72
84
96
108
```
