import os
import re
import sys

from colorama import Fore, Style, Back
from nltk.translate.bleu_score import sentence_bleu


def compute_bleu(candidate, reference, gram=1):
    candidate = candidate.split(" ")
    reference = [reference.split(" ")]
    weights = [0, 0, 0, 0]
    weights[gram - 1] = 1
    """
    print(candidate)
    print(reference)
    print(weights)
    """
    return sentence_bleu(reference, candidate, weights=weights)


def bold_line(t="START", n=20):
    print(
        f"{Back.LIGHTWHITE_EX}{' ' * n}{Fore.BLACK}{t}{' ' * n}{Style.RESET_ALL}"
    )


def bold_text(mode="SPEAK", text=""):
    print(
        f"{Fore.GREEN if mode == 'SPEAK' else Fore.BLUE}{mode}: {Style.RESET_ALL}{text}"
    )


line_count = 0


def read_text(path):
    global line_count
    with open(path, "r", encoding="utf-8") as file:
        lines = [line for line in file.read().splitlines()]
        try:
            line = lines[line_count]
            line_count += 1
            return line
        except IndexError:
            bold_line(t="END", n=41)
            sys.exit(1)


def counter(num=1, length=3):
    """Counter etc. 0001, 0002
    Attributes:
    num (int) integer etc. 1 ==> 0001
        length (int) length of counter etc. 3 ==> 001
    Return:
        (str) etc. 0001
    """
    number = '0' * length + str(num)
    number = number[len(number)-length:]
    return number


def load_audio_number(meta):
    if not os.path.isfile(meta):
        with open(meta, "w", encoding="utf-8") as file:
            file.close()

    with open(meta, "r", encoding="utf-8") as file:
        line_number = len([line for line in file.read().splitlines()])
    return counter(line_number + 1, 4)


def save_audio_data(meta, name, text, transcript):
    with open(meta, "a", encoding="utf-8") as file:
        bleu = compute_bleu(transcript, text, gram=1)
        file.writelines(f"{name}|{text}|{transcript}|{bleu}\n")


def filter_text(text):
    text = text.lower()
    text = re.sub(r"’m", r"'m", text)
    text = re.sub(r"’s", r"'s", text)
    text = re.sub(r"’t", r"'t", text)
    text = re.sub(r"’clock", r"'clock", text)
    text = re.sub(r"’re", r"'re", text)
    text = re.sub(r"’ve", r"'ve", text)
    text = re.sub(r"[^\w ']", "", text)     # a-z'

    text = re.sub(" +", " ", text)          # "  " -> " "
    return text.strip()
