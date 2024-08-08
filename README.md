# bpm2fps

Python script to convert beats per minute to animation frames.

## Requires

* python 3

## Quickstart

Can be installed via pip, or ran directly:

```
# Usage
$ ./bpm2fps.sh --help
usage: cli.py [-h] start end bpm fps
cli.py: error: the following arguments are required: start, end, bpm, fps

# Example
./bpm2fps.sh 0 60 120 24
# Example Result:
# [
#   {
#     "beat": 0,
#     "frame": 0.0,
#     "second": 0.0
#   },
#   {
#     "beat": 1,
#     "frame": 12.0,
#     "second": 0.5
#   },
#   # ...
#   {
#     "beat": 119,
#     "frame": 1428.0,
#     "second": 59.5
#   }
# ]

# Chain with "jq" to get only nearest frames where beats occur:
./bpm2fps.sh 0 10 60 24 | jq '.[]["frame"]'
# Example result:
# 0
# 24
# 48
# 72
# 96
# 120
# 144
# 168
# 192
# 216

```
