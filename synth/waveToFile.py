import numpy as np
from scipy.io import wavfile
from sineOscillator import SineOscillator

def wave_to_file(wav, wav2=None, fname="temp.wav", amp=0.5, sample_rate=44100):
    wav = np.array(wav)
    wav = np.int16(wav * amp * (2**15 - 1))
    
    if wav2 is not None:
        wav2 = np.array(wav2)
        wav2 = np.int16(wav2 * amp * (2 ** 15 - 1))
        wav = np.stack([wav, wav2]).T
    
    wavfile.write(fname, sample_rate, wav)




osc = SineOscillator(440)
osc._initialize_osc()
osc.freq = 440


samples = [next(osc) for i in range(44100 * 4)]



print("Saving")
wave_to_file(samples)
print("Saved")
