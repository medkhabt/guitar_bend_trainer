import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt 
import numpy as np


from note_detection.zcr import frequency_zcr_classic, frequency_zcr_adapted

def dat_file_format(res, file_name=""):
    file = open('experiments/' + file_name + '.dat', 'w')
    if file_name: 
        print("are we here") 
        printer = lambda text: file.write(text + '\n')  
    else : 
        printer = print
    printer("note classic_diff adapter_diff lib_diff first_10_frames_lib_diff freq")
    for v in res:
        printer(f"{v['note']} {v['classic']['diff']:.3f} {v['adapted']['diff']:.3f} {v['lib']['diff']:.3f} {v['lib_1_frame']['diff']:.3f} {v['freq']}")
def print_result(res):      
    for v in res:
        print(f"note : {v['note']} ; classic : value = {v['classic']['value']}, diff = {v['classic']['diff']} ; adapted : value = {v['adapted']['value']} , diff = {v['adapted']['diff'] }");
def main(): 


## Load different notes 
#TODO function relate MIDI to musical anntations and from frequencies to MIDI
    files= {
	'a2' : { 'path': "experiments/audio/A2_s2_01.wav", 'freq': 110.00 } , 
	'b3' : { 'path': "experiments/audio/B3_s5_01.wav", 'freq': 246.94},
	'b4' : { 'path': "experiments/audio/B4_s6_01.wav", 'freq': 493.88},
	'c#6' : { 'path': "experiments/audio/C#6_s6_01.wav", 'freq': 1108.73},
	'c2' : { 'path': "experiments/audio/C2_s1_01.wav", 'freq': 65.41},
	'c3' : { 'path': "experiments/audio/C3_s2_02.wav", 'freq': 130.81},
	'd5' : { 'path': "experiments/audio/D5_s6_01.wav", 'freq': 587.33},
	'e3' : { 'path': "experiments/audio/E3_s3_01.wav", 'freq': 164.81},
	'e4' : { 'path': "experiments/audio/E4_s6_01.wav", 'freq': 329.63},
	'f2' : { 'path': "experiments/audio/F2_s1_01.wav", 'freq': 87.31},
	'g#5' : { 'path': "experiments/audio/G#5_s6_03.wav", 'freq': 830.61 },
	'g3' : { 'path': "experiments/audio/G3_s4_01.wav", 'freq': 196.00 },
	'g2' : { 'path': "experiments/audio/G4_s6_01.wav", 'freq': 98.00},
} 

    res = [];
    for k, v in files.items():  

## graph in dbs 

        sig, sr = librosa.load(v['path'])
##     calculate the freq from zcr classic and adapt. 

        classic_zcr = frequency_zcr_classic(sig, sr)
        adapted_zcr = frequency_zcr_adapted(sig, sr) 
        lib_zcr_vect = librosa.feature.zero_crossing_rate(sig)
        lib_zcr = lib_zcr_vect.mean() 
        first_10_frames_lib_zcr = lib_zcr_vect[0,10] 
        res.append({'note': k, 'freq' : v['freq'] , 'classic' : { 'value' : classic_zcr, 'diff': abs(v['freq'] - classic_zcr)  } , 'adapted' : { 'value' : adapted_zcr, 'diff' :  abs(v['freq'] - adapted_zcr)}, 'lib' : { 'value' : lib_zcr, 'diff' :  abs(v['freq'] - lib_zcr)} , 'lib_1_frame' : { 'value' : first_10_frames_lib_zcr, 'diff' :  abs(v['freq'] - first_frame_lib_zcr)}})
        ## Plotting the waves 
        plt.figure(figsize=(10,7))
        librosa.display.waveshow(sig, alpha=0.5)
        slice_zcr = sig[0:10*2048]
        librosa.display.waveshow(slice_zcr, alpha=0.7, color='r')
        plt.savefig('experiments/waves/' + k) 
    # saving the data 
    dat_file_format(res, "comparing_zcr_methods")
#    dat_file_format(res)
#    print_result(res)
	    
main()

