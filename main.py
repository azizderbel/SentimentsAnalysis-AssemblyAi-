from api import *
from yt_extractor import *
import json
import matplotlib.pyplot as plt

def extract_insights():
    with open("output_sentiments.json", "r") as f:
        data = json.load(f)
    
    positives = []
    negatives = []
    neutrals = []
    for result in data:
        text = result["text"]
        if result["sentiment"] == "POSITIVE":
            positives.append(text)
        elif result["sentiment"] == "NEGATIVE":
            negatives.append(text)
        else:
            neutrals.append(text)
        
    n_pos = len(positives)
    n_neg  = len(negatives)
    n_neut = len(neutrals)

    #print("Num positives:", n_pos)
    #print("Num negatives:", n_neg)
    #print("Num neutrals:", n_neut)

    return n_pos,n_neut,n_neg

def save_video_sentiments(url):
    audio_url = get_audio_url(get_video(url))
    if(save_transcript(audio_url,title='output',sentiment_analysis=True)):
        print('transcription and sentiment analysis done')

save_video_sentiments("https://www.youtube.com/watch?v=K62cKysma_s")

def plot_stats():
    n_pos,n_neu,n_neg = extract_insights()
    labels = 'Positve feedback', 'Neutral feedback', 'Negative feedback'
    sizes = [n_pos, n_neu, n_neg]
    explode = (0.1, 0, 0)
    plt.subplots()
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    plt.title('iPhone 14 Pro Max youtube review')

plot_stats()

plt.show()