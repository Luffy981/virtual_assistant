#!/usr/bin/env python3


import speechbrain as sb
from speechbrain.dataio.dataio import read_audio
# from IPython.display import Audio
from playsound import playsound


from speechbrain.pretrained import SpeakerRecognition

def SpeakerVerification(filename):

    verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
    score, prediction = verification.verify_files("speak1.wav", filename)

    print(prediction, score)
    # playsound(filename)
    print("******Verification completed******")
    return prediction

if __name__ == "__main__":
    SpeakerVerification()
