import json
import subprocess
import os


def render_video(
    a_roll_path,
    broll_dir,
    timeline_path,
    output_path
):
    """
    Render final video using FFmpeg based on timeline.json
    """

    if not os.path.exists(timeline_path):
        raise FileNotFoundError("timeline.json not found")

    with open(timeline_path, "r", encoding="utf-8") as f:
        timeline = json.load(f)

    ffmpeg_cmd = ["ffmpeg", "-y", "-i", a_roll_path]

    filter_commands = []
    input_index = 1

    for ins in timeline.get("insertions", []):
        broll_path = os.path.join(broll_dir, f"{ins['broll_id']}.mp4")

        if not os.path.exists(broll_path):
            print(f"Skipping missing B-roll: {broll_path}")
            continue

        ffmpeg_cmd.extend(["-i", broll_path])

        start = ins["start_sec"]
        duration = ins["duration_sec"]
        end = start + duration

        filter_commands.append(
            f"[{input_index}:v]scale=iw:ih,trim=0:{duration},setpts=PTS+{start}/TB[b{input_index}];"
            f"[0:v][b{input_index}]overlay=enable='between(t,{start},{end})'"
        )

        input_index += 1

    if not filter_commands:
        raise ValueError("No B-roll insertions found in timeline.json")

    ffmpeg_cmd.extend([
        "-filter_complex", ";".join(filter_commands),
        "-map", "0:a?",
        "-c:v", "libx264",
        "-c:a", "aac",
        output_path
    ])

    subprocess.run(ffmpeg_cmd, check=True)
