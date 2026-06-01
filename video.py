import random
from PIL import Image, ImageDraw
import numpy as np
import moviepy.editor as mpy
from race import Team


# 🟢 تحويل النص إلى صورة (بديل TextClip)
def create_text_clip(text, duration, size=(500, 120)):
    img = Image.new('RGB', size, color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.text((20, 40), text, fill=(255, 255, 255))

    return mpy.ImageClip(np.array(img)).set_duration(duration)


def generate_video(group, teams):

    players = [Team(t) for t in teams]

    duration = 10

    # 🟢 خلفية الملعب
    background = mpy.ColorClip((720, 1280), color=(20, 120, 20), duration=duration)

    clips = []

    positions = [200, 400, 600, 800]

    # 🟢 حركة الكرات (نصوص بدل TextClip)
    for i, p in enumerate(players):

        speed = p.speed

        clip = create_text_clip(p.name, duration).set_position(
            lambda t, i=i, s=speed: (50 + t * s, positions[i])
        )

        clips.append(clip)

    # 🟢 دمج المشهد
    final = mpy.CompositeVideoClip([background] + clips)

    # 🟢 تحديد الفائزين
    players.sort(key=lambda x: x.distance, reverse=True)
    winners = players[:2]

    result_text = f"{group} QUALIFIED: {winners[0].name} & {winners[1].name}"

    txt = create_text_clip(result_text, duration).set_position("center")

    final = mpy.CompositeVideoClip([final, txt])

    # 🟢 حفظ الفيديو
    output = f"output/{group}_race.mp4"
    final.write_videofile(output, fps=24)

    return output
