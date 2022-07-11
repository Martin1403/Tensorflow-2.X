import os


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


def save_audio_data(meta, name, text, transcribed):
    with open(meta, "a", encoding="utf-8") as file:
        file.writelines(f"{name}|{text}|{transcribed}\n")
