import os
import re
import argparse

from library.utilities import bold_line
from library.vad_audio_transcribe import transcribe
import warnings

warnings.filterwarnings(action="ignore")
# microphone volume
os.system("pacmd set-source-volume 1 18000")

# paths
metadata_path = "audio/metadata.csv"
audio_folder = "audio/wavs"
model_path = 'model/output_graph.tflite'
scorer_path = 'model/output_graph.scorer'

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, default="text.txt", help="File path")
# folders
os.makedirs(audio_folder, exist_ok=True)

if __name__ == '__main__':
    try:
        args = parser.parse_args()
        transcribe(args.file, model_path, scorer_path, audio_folder, metadata_path)

    except KeyboardInterrupt:
        print("\n")
        bold_line(t="END", n=41)
