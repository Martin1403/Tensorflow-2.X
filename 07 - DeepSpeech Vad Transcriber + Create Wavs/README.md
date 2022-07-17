DeepSpeech Vad Transcribe Audio
===============================
![](img.png)
### Venv:
##### Anaconda3
```
conda env create -f environment.yml

# conda env export > environment.yml
```

### Unpack Scorer:
###### / 
###### apt-get install p7zip-full
```
7za x model/archive/output_graph.scorer.7z.001 -omodel/
```
### Run
###### /
```
python main.py --file text.txt

```

