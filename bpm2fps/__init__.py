"""bpm2fps - Match a songs beats to their closest frame.
"""


def frame_at_time(time: float, fps: float = 24.0) -> int:
    """
    Returns the closest frame (rounding down) at a particular time.

    Args:
        time (float): Time in seconds.
        fps (float): Frames per second. Default: ``24.0``.

    Returns:
        int: frame at time
    """
    return time * fps


def bps(bpm: float) -> float:
    """Convert beats per minute to per second.

    Args:
        bpm (float): Beats per minute.

    Returns:
        float: Beats per second.
    """
    return (1.0 / 60.0) * bpm


def frange(start: float, stop: float, step: float = 1.0):
    """Produces a sequence of floats from start (inclusive).

    Args:
        start (float): range start
        stop (float): range end
        step (float, optional): range step. Default: ``1.0``.

    Yields:
        float: range values.
    """
    value = start
    while value < stop:
        yield value
        value += step


def beats_to_frames(
    start: float, stop: float, bpm: float = 60.0, fps: float = 24.0
) -> tuple[float]:
    """Get clostest frames for each beat in a time range.

    Args:
        start (float): Start time in seconds.
        stop (float, optional): End time in seconds.
        bpm (float, optional): Beats per minute. Default ``60``.
        fps (float, optional): Frames per second. Default: ``24``.

    Returns:
        tuple[float, ...]: Frames for each beat.
    """
    return (frame_at_time(time, fps) for time in frange(start, stop, 1 / bps(bpm)))


def beats_to_frames_data(
    start: float, stop: float, bpm: float = 60.0, fps: float = 24.0
) -> tuple[dict[str, float]]:
    """Get clostest frame datafor each beat in a time range.

    Args:
        start (float): Start time in seconds.
        stop (float, optional): End time in seconds.
        bpm (float, optional): Beats per minute. Default ``60``.
        fps (float, optional): Frames per second. Default: ``24``.

    Returns:
        tuple[float, ...]: Frames for each beat.
    """
    return [
        {"beat": i, "frame": frame, "second": frame * (1.0 / fps)}
        for (i, frame) in enumerate(beats_to_frames(start, stop, bpm, fps))
    ]
