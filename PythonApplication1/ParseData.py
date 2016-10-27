import json
import pandas as pd
#import matplotlib.pylot as plt
import matplotlib.pyplot as plt
import re

global tweets_data_path 
global tweets_data 
global tweets_file 
global tweets

tweets_data_path = 'data.txt'
tweets_data = []
tweets_file = open(tweets_data_path,'r')
tweets = pd.DataFrame()
def dothis():
#prep the data
  
    #put the data somewhere
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

        #print the lines to see the count
    print (len(tweets_data))
    #word_graph()
    lang_country_graph()

   

#organize the data
#start graphing but throw it into a def cuz things and stuff
def lang_country_graph():
    
  #  tweets = pd.DataFrame()
    #tweets['text'] = map(lambda tweet: tweet['text'],tweets_data)
    #tweets['lang'] = map(lambda tweet: tweet['lang'],tweets_data)
    #tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

    tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))

    tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))

    tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))

    tweets_by_lang = tweets['lang'].value_counts();

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)

    ax.set_xlabel('Languages', fontsize=15)
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.set_title('Top 5 languages',fontsize=15, fontweight='bold')

    tweets_by_lang[:5].plot(ax=ax, kind='bar',color='red')

    tweets_by_country = tweets['country'].value_counts()

    fig, ax = plt.subplots()

    tweets_by_country = tweets['country'].value_counts()

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Countries', fontsize=15)
    ax.set_ylabel('Number of tweets' , fontsize=15)
    ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
    tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
    plt.show()
#end the graph

#lets see all the words in a text
def word_in_text(word, text):
    
    if text == None:
        return False
    word = word.lower()
    text = text.lower() 
    match = re.search(word,text)
    if match:
        return True
    else:
        return False
    #if text == None:
    #    return False
    #word = word.lower()
    #text = text.lower()
    #match = re.search(word,text)
    #if match:
    #    return True
    #else:
    #    return False

def word_graph():
   # tweets['text'] = map(lambda tweet: tweet.get('text', None),tweets_data)

    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)

  #  tweets = pd.DataFrame()
    tweets['pyton'] = tweets['text'].apply(lambda tweet: word_in_text('python',tweet))

    tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript',tweet))

    tweets['ruby'] = tweets['ruby'].apply(lambda tweet: word_in_text('ruby',tweet))
    
    print (tweets['python'].value_counts()[True])
    print (tweets['javascript'].value_counts()[True])
    print (tweets['ruby'].value_counts()[True])


if __name__ == "__main__": dothis()