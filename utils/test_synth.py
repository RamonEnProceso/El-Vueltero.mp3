from pyo import *
from utils.music import midi_to_freq
from midi.play_midi import play_midi

def test_synth(synth):
    s = Server(sr=44100, buffersize=1024, duplex=0)
    s.setOutputDevice(1)
    s.boot()
    s.start()

    env, osc, filt = synth()
    filt.out()

    play_midi("midi/demo/demo.mid", bpm=None, osc=osc, env=env)

    while True:
        entrada = input("Nota MIDI (ej. 40=Mi grave, 45=La, 'q' para salir): ")
        if entrada.lower() == "q":
                break
        try:
            midi = int(entrada)
            osc.freq = midi_to_freq(midi)
            env.play()
        except ValueError:
            print("Ingresá un número MIDI válido o 'q'")