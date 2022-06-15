import tensorflow as tf
import numpy as np
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt



def to_html(text):
    return "<var style=''><h3>{}<h3> </var>".format(text)


def one_hot(x, title="One-hot Label", figsize=(5, 1)):
    plt.figure(figsize=figsize)
    sns.set(font_scale=1.5)
    sns.heatmap(x, annot=True, cbar=False)
    plt.title(title)
    plt.axis("off")
    plt.show()


callbacks = []
class MyCallback(tf.keras.callbacks.Callback):
    
    def on_epoch_end(self, epoch, logs={}):
        global callbacks
        loss = logs.get('loss')
        callbacks.append(logs)
        if loss < 0.0005:
            self.model.stop_training = True
    def on_train_end(self, logs=None):
        global callbacks
        plt.figure(figsize=(8, 5))
        sns.lineplot(data=pd.DataFrame({k: v for k, v in zip(callbacks[0].keys(), np.array([list(i.values()) for i in callbacks]).T)}))
        callbacks = []
        plt.xlabel("Epochs")
        plt.ylabel("Loss/Acc")
        plt.title("Model score")
        plt.show()

def word_cloud(paragraph: str) -> None:
    """
    paragraph: str ('Example text.')
    """
    stopword_list = set(STOPWORDS)

    word_cloud = WordCloud(width=550, height=550,
                           background_color='white',
                           stopwords=stopword_list,
                           min_font_size=10).generate(paragraph)

    plt.figure(figsize = (8, 6))
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()
    

def hist_plot(X, t="", x="", y="") -> None:
    """
    X: (object) Data to plot.
    """
    plt.figure(figsize=(5, 5))
    sns.histplot(X)
    plt.title(t)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show
    
def pie_plot(data, labels):
    """
    data: list
    labels: list
    """
    colors = sns.color_palette('pastel')[0:5]
    sns.set(font_scale=1.5)
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
    plt.show()