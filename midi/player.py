import time
from utils.music import beat_duration, midi_to_freq

def play_melody(melodia, bpm, osc, env):
    for nota, beats in melodia:
        osc.freq = midi_to_freq(nota)
        env.play()
        time.sleep(beat_duration(bpm, beats))