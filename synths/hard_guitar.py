from pyo import *
from utils.test_synth import test_synth

def hard_guitar():
    env = Adsr(
        attack=0.005,
        decay=0.15,
        sustain=0.7,
        release=0.5,
        dur=1.2,
        mul=0.35
    )

    osc = SuperSaw(
        freq=220,
        detune=0.3,
        bal=0.6,
        mul=env
    )

    dist = Disto(
        osc,
        drive=0.75,
        slope=0.85,
    )
    
    dist = Compress(
        dist,
        thresh=-20,
        ratio=4,
        risetime=0.01,
        falltime=0.15
    )

    dist = Sig(dist, mul=3.5)

    filt = ButLP(
        dist,
        freq=3200
    )
    
    filt = Chorus(filt, depth= 0.1, feedback=0.5)
    
    filt = WGVerb(filt, bal=0.2, cutoff=5000, mul=2, add=0.9)
    
    dist = Compress(
        dist,
        thresh=-40,
        ratio=1,
        risetime=0.01,
        falltime=0.15
    )
    
    return env, osc, filt

if __name__ == "__main__":
    test_synth(hard_guitar)