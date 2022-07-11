DeepSpeech Vad Transcribe Audio
===============================

### Venv:
##### Anaconda3
```
conda env export > environment.yml
conda env create -f environment.yml
```

### Unpack Scorer:
###### / 
###### apt-get install p7zip-full
```
7za x model/archive/output_graph.scorer.7z.001 -omodel/
```
### Run
###### /
```bash
python library/vad_audio_transcribe.py
```