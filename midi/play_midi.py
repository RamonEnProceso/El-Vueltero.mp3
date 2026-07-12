from mido import MidiFile, bpm2tempo, tick2second
from utils.music import beat_duration, midi_to_freq
import time

demo_mid=MidiFile("midi/demo/demo.mid")

def play_midi(midiPath, bpm, osc, env):
    
    midi=MidiFile(midiPath)
    tempo= None
    
    for track in midi.tracks:
        for msg in track:
            if msg.is_meta:
                if msg.type == "set_tempo":
                    tempo = msg.tempo
                continue
            if bpm is not None:
                tempo_actual = bpm2tempo(bpm)
            else:
                tempo_actual = tempo
                
            segundos = tick2second(
                msg.time,
                midi.ticks_per_beat,
                tempo_actual
            )

            time.sleep(segundos)

            if msg.type == "note_on" and msg.velocity > 0:
                osc.freq = midi_to_freq(msg.note)
                env.play()

            elif msg.type == "note_off":
                pass