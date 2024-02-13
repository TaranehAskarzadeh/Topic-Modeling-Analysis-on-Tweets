# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:16:12 2024

@author: Taraneh
"""

import json
import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

# Function to load data from a JSONL file
def load_data(file_path):
    tweets = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            tweets.append(tweet['text'])  
    return tweets

# Function to preprocess text
def preprocess_texts(texts):
    stop_words = stopwords.words('english')
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]


file_paths = [
    r'C:\Users\Taraneh\OneDrive - North Dakota University System\Desktop\New folder (3)\TweetData_JSONL_Starting2020_04_01_To2020_04_30_Retrieved27082020_By1133.jsonl',
    r'C:\Users\Taraneh\OneDrive - North Dakota University System\Desktop\New folder (3)\TweetData_JSONL_Starting2020_05_01_To2020_05_31_Retrieved27082020_By1136.jsonl',
    r'C:\Users\Taraneh\OneDrive - North Dakota University System\Desktop\New folder (3)\TweetData_JSONL_Starting2020_06_01_To2020_06_30_Retrieved27082020_By1137.jsonl',
    r'C:\Users\Taraneh\OneDrive - North Dakota University System\Desktop\New folder (3)\TweetData_JSONL_Starting2020_07_01_To2020_07_31_Retrieved27082020_By1138.jsonl',
    r'C:\Users\Taraneh\OneDrive - North Dakota University System\Desktop\New folder (3)\TweetData_JSONL_Starting2020_08_01_To2020_08_27_Retrieved27082020_By1139.jsonl'
]

tweets = []
for file_path in file_paths:
    tweets.extend(load_data(file_path))

preprocessed_texts = preprocess_texts(tweets)

# Create Dictionary and Corpus
id2word = corpora.Dictionary(preprocessed_texts)
corpus = [id2word.doc2bow(text) for text in preprocessed_texts]

# Parameters for LDA
num_topics = 3
alpha = 0.01
eta = 0.01
passes = 50

# Train LDA model
lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=num_topics,
                                       random_state=100,
                                       chunksize=100,
                                       passes=passes,
                                       alpha=alpha,
                                       eta=eta)

# Compute Coherence Score
coherence_model_lda = CoherenceModel(model=lda_model, texts=preprocessed_texts, dictionary=id2word, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score:', coherence_lda)

# Explore the topics
for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))
