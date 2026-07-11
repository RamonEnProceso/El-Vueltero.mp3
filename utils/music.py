def beat_duration(bpm=120, beats=4):
    return (60 / bpm) * beats


def midi_to_freq(midi_note):
    return 440.0 * (2 ** ((midi_note - 69) / 12))
