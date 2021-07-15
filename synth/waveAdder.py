from sineOscillator import SineOscillator
from triangleOscillator import TriangleOscillator
from sawToothOscillator import SawtoothOscillator
from squareOscillator import SquareOscillator


class WaveAdder:
    def __init__(self, *oscillators):
        self.oscillators = oscillators
        self.n = len(oscillators)
    
    def __iter__(self):
        [iter(osc) for osc in self.oscillators]
        return self
    
    def __next__(self):
        return sum(next(osc) for osc in self.oscillators) / self.n


import numpy as np
from scipy.io import wavfile
from sineOscillator import SineOscillator

def wave_to_file(wav, wav2=None, fname="temp.wav", amp=1, sample_rate=44100):
    wav = np.array(wav)
    wav = np.int16(wav * amp * (2**15 - 1))
    
    if wav2 is not None:
        wav2 = np.array(wav2)
        wav2 = np.int16(wav2 * amp * (2 ** 15 - 1))
        wav = np.stack([wav, wav2]).T
    
    wavfile.write(fname, sample_rate, wav)


gen = WaveAdder(
    SineOscillator(freq=440),
    TriangleOscillator(freq=220, amp=0.8),
    SawtoothOscillator(freq=110, amp=0.6),
    SquareOscillator(freq=55, amp=0.4),
)

iter(gen)
wav = [next(gen) for _ in range(44100 * 4)] # 4 Seconds
wave_to_file(wav, fname="prelude_one.wav")