# vader sentiment analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# initialize vader sentiment analyzer
analyser = SentimentIntensityAnalyzer()


def clean_text(text):
    # correct spelling, remove stop words and punctuations
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = [w.lower() for w in word_tokens if not w in stop_words and w.isalpha()]
    return ' '.join(filtered_sentence)


def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score

def get_sentiment(text):
    # clean text
    text = clean_text(text)
    # get sentiment score
    score = sentiment_analyzer_scores(text)
    # return sentiment
    return score
