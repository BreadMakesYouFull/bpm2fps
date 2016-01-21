"""
bpm2fps
Match a songs beats to their closest frame.
"""
import math

def closest_frame(time, fps):
    """
    Returns the closest frame (rounding down) at a particular time.
    time - time in seconds
    fps - frames per second
    """
    return math.floor(time * fps)

def bps(bpm):
    """
    Returns beats per second from beats per minute.
    """
    return (1 / 60.0) * bpm
    
def beats_to_frames(bpm, fps, start_time, end_time):
    """
    Returns a list of frames for each beat.
    bpm - beats per minute
    fps - frames per second
    start_time - start time in seconds, can be used to offset beat
    end_time - end time in seconds
    """
    frames = []
    time = start_time
    step = 1 / bps(bpm)
    print(bps(bpm), step)
    while (time < end_time + step):
        frame = closest_frame(time, fps)
        frames.append(frame)
        time += step
    return frames

if __name__ == "__main__":
    print("\n")
    print("bpm2fps Match a songs beats to their closest frame.")
    print("\n")
    bpm = input("Beats per minute (bpm): ")
    fps = input("Frames per second (fps): ")
    start_time = input("Song start time (seconds): ")
    end_time = input("Max song time (seconds): ")
    print("\n")
    frames = beats_to_frames(bpm, fps, start_time, end_time)
    i = 0
    for frame in frames:
        print("beat {} | on frame {} | at {} seconds".format(i, frame, frame * (1.0 / fps)))
        i += 1
    print("\n")
    print("Press enter to quit")
    input()