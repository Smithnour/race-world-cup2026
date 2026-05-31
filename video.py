import random
from moviepy.editor import *
from race import Team

def generate_video(group, teams):

    players = [Team(t) for t in teams]

    duration = 10

    background = ColorClip((720, 1280), color=(20, 120, 20), duration=duration)

    clips = []

    positions = [200, 400, 600, 800]

    for i, p in enumerate(players):

        speed = p.speed

        clip = TextClip(
            p.name,
            fontsize=50,
            color='white'
        ).set_position(lambda t, i=i, s=speed: (50 + t * s, positions[i])).set_duration(duration)

        clips.append(clip)

    final = CompositeVideoClip([background] + clips)

    players.sort(key=lambda x: x.distance, reverse=True)
    winners = players[:2]

    txt = TextClip(
        f"{group} QUALIFIED: {winners[0].name} & {winners[1].name}",
        fontsize=45,
        color='yellow'
    ).set_duration(duration).set_position("center")

    final = CompositeVideoClip([final, txt])

    output = f"output/{group}_race.mp4"
    final.write_videofile(output, fps=24)

    return output
