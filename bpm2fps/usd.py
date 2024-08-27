"""Output a minute of ball bounce reference.
"""

USD_TEMPLATE = """#usda 1.0
(
    "bpm2fps reference"
    metersPerUnit = 1
    upAxis = "Z"
    startTimeCode = 1
    // One minute of animation, fps * 60
    endTimeCode = {minute}
    framesPerSecond = {fps}
    timeCodesPerSecond = {fps}
)

def Xform "bpm2fps" (
)
{
    def Sphere "bouceEverySecond_{fps}fps" (
    )
    {
        double radius = 0.1
        float3 xformOp:translate.timeSamples = {fps_data}
        // Example at bounce every second at 24 fps:
        // {
        //     1001: (0, 0, 0),
        //     1012: (0, 0, 1),
        //     1024: (0, 0, 0),
        // }
        uniform token[] xformOpOrder = ["xformOp:translate"]
        color3f[] primvars:displayColor = [(1.0, 0.0, 0.0)]  // Red
    }
    def Sphere "bounceEveryBeat_{bpm}bpm" (
    )
    {
        double radius = 0.1
        float3 xformOp:translate.timeSamples = {bpm_data}
        // Example at bounce every beat at 120 bpm 24 fps:
        // {
        //     1001: (0, 0, 0),
        //     1006: (0, 0, 1),
        //     1012: (0, 0, 0),
        //     1018: (0, 0, 1),
        //     1025: (0, 0, 0),
        // }
        uniform token[] xformOpOrder = ["xformOp:translate"]
        color3f[] primvars:displayColor = [(0.0, 0.0, 1.0)]  // Blue
    }
}
"""


def generate(bpm, fps):
    """Generate an extremely basic USD reference file matching bpm fps inputs"""
    half_fps = fps / 2
    frames_per_beat = (fps * 60) / bpm
    half_frames_per_beat = frames_per_beat / 2

    frame = 0
    fps_data = {}
    fps_data[0] = (0, 0, 0)
    fps_data[1] = (0, 0, 0)
    while frame <= (fps * 60):  # one minute
        frame += half_fps
        fps_data[int(frame)] = (0, 0, 1)
        frame += half_fps
        fps_data[int(frame)] = (0, 0, 0)

    frame = 0
    bpm_data = {}
    bpm_data[0] = (1, 0, 0)
    bpm_data[1] = (1, 0, 0)
    while frame <= (fps * 60):  # one minute
        frame += half_frames_per_beat
        bpm_data[int(frame)] = (1, 0, 1)
        frame += half_frames_per_beat
        bpm_data[int(frame)] = (1, 0, 0)

    return (
        USD_TEMPLATE.replace("{minute}", str(fps * 60))
        .replace("{fps}", str(fps))
        .replace("{bpm}", str(bpm))
        .replace("{fps_data}", str(fps_data))
        .replace("{bpm_data}", str(bpm_data))
    )
