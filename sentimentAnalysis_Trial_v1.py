import nltk
from nltk.corpus import opinion_lexicon

# Download the opinion lexicon
nltk.download('opinion_lexicon')


# Positive and negative words
positive_words = set(opinion_lexicon.positive())
negative_words = set(opinion_lexicon.negative())


# The text to be analyzed
text = "I hate you"


# Split the text into words
words = text.split()


# Initialize counters
positive_count = 0
negative_count = 0


# Count the number of positive and negative words
for word in words:
    if word in positive_words:
        positive_count += 1
    elif word in negative_words:
        negative_count += 1
				
				
# Calculate the overall sentiment score
sentiment_score = positive_count - negative_count



# Determine the overall sentiment
if sentiment_score > 0:
    print("Positive sentiment")
elif sentiment_score < 0:
    print("Negative sentiment")
else:
    print("Neutral sentiment")
