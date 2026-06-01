import numpy as np
from PIL import Image, ImageDraw
import moviepy.editor as mpy
from race import Team


def create_text_clip(text, duration):
    img = Image.new("RGB", (500, 120), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((20, 40), text, fill=(255, 255, 255))

    return mpy.ImageClip(np.array(img)).set_duration(duration)


def generate_video(group, teams):

    duration = 10

    background = mpy.ColorClip(
        size=(720, 1280),
        color=(20, 120, 20),
        duration=duration
    )

    clips = []

    positions = [200, 400, 600, 800]

    for i, team in enumerate(teams):

        clip = create_text_clip(team, duration)

        clip = clip.set_position(
            lambda t, i=i: (50 + t * 50, positions[i])
        )

        clips.append(clip)

    final = mpy.CompositeVideoClip([background] + clips)

    output = f"{group}_race.mp4"

    final.write_videofile(
        output,
        fps=24,
        codec="libx264"
    )

    return output
