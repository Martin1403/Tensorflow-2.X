import os
import re
import argparse

from library.vad_audio_transcribe import transcribe

# microphone volume
os.system("pacmd set-source-volume 1 18000")

# paths
metadata_path = "audio/metadata.csv"
audio_folder = "audio/wavs"
model_path = 'model/output_graph.tflite'
scorer_path = 'model/output_graph.scorer'

parser = argparse.ArgumentParser()
parser.add_argument("--text", type=str)
# folders
os.makedirs(audio_folder, exist_ok=True)

if __name__ == '__main__':
    try:
        args = parser.parse_args()
        text = args.text.lower()
        text = re.sub(r"[^\w ']", "", text).strip()
        text = re.sub(" +", " ", text)
        transcribe(model_path, scorer_path, audio_folder, metadata_path, text)
    except KeyboardInterrupt:
        pass
