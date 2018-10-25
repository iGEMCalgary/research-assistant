from .webScraper import Parser
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
from nltk.probability import FreqDist
import numpy
import re

## Text summarization algorithm based off of Luhn's algorithm for automatic text analysis ##


class Summarizer:
    N = 100  # Number of words to consider
    CLUSTER_THRESHOLD = 5  # Distance between words to consider
    TOP_SENTENCES = 5  # Number of sentences to return for a "top n" summary

    ## Driver for text summary ##
    def summarize(self, text):
        summary = self.summarizeText(text)
        return summary

    ## Driver for statistical summary methods ##
    def summarizeText(self, txt):

        normalizedSentences = [s for s in nltk.tokenize.sent_tokenize(txt)]
        # normalizedSentences = self.stripNewLines(sentences)

        if len(normalizedSentences) == 0:
            return dict([('Success', False), ('Description', '')])

        words = [w.lower() for sentence in normalizedSentences for w in
                 nltk.tokenize.word_tokenize(sentence)]

        fdist = nltk.FreqDist(words)
        stopwords = nltk.corpus.stopwords.words('english')
        top_n_words = [w[0] for w in fdist.items()
                       if w[0] not in stopwords][:self.N]

        scoredSentences = self.scoreSentences(normalizedSentences, top_n_words)

        # Summarization Approach 1:
        # Filter out nonsignificant sentences by using the average score plus a
        # fraction of the std dev as a filter
        # if len(scoredSentences) > 0:
        avg = numpy.mean([s[1] for s in scoredSentences])
        std = numpy.std([s[1] for s in scoredSentences])
        mean_scored = [(sent_idx, score) for (sent_idx, score) in scoredSentences
                       if score > avg + 0.5 * std]

        meanSummary = ''

        for (idx, score) in mean_scored:
            meanSummary += ' ' + \
                normalizedSentences[idx][:1].capitalize(
                ) + normalizedSentences[idx][1:]

        return dict([('Success', True), ('MeanDescription', meanSummary[1:])])

    ## Strips new lines from text ##
    def stripNewLines(self, sentences):
        normalizedSentences = []
        sentences = [s.lower() for s in sentences]

        for s in sentences:
            s = re.sub(r'[^\x00-\x7f]', r'', s)
            if '\n' in s:
                s = s.replace('\n', ' ')
                while '  ' in s:
                    s = s.replace('  ', ' ')

            if not 'page discussion view source history teams log in' in s and ('loading menubar' not in s and (not re.search(r'^team:\w+', s))):
                normalizedSentences.append(s)

        return normalizedSentences

    ## Scores each sentence in the text by important word ##
    ## position and frequency.										    ##
    def scoreSentences(self, sentences, important_words):
        scores = []
        sentence_idx = -1

        for s in [nltk.tokenize.word_tokenize(s) for s in sentences]:
            sentence_idx += 1
            word_idx = []

            for w in important_words:
                try:
                    # Compute an index for where any important words occur in the sentence
                    word_idx.append(s.index(w))
                except ValueError:
                    pass

            word_idx.sort()

            # Check for sentences that contain no important words
            if len(word_idx) == 0:
                continue

            # Using word index, compute clusters by using a max distance threshold
            # for any two consecutive words

            clusters = []
            cluster = [word_idx[0]]
            i = 1
            while i < len(word_idx):
                if word_idx[i] - word_idx[i - 1] < self.CLUSTER_THRESHOLD:
                    cluster.append(word_idx[i])
                else:
                    clusters.append(cluster[:])
                    cluster = [word_idx[i]]
                i += 1
            clusters.append(cluster)

            # Score each cluster. The max score for any given cluster is the score
            # for the sentence

            max_cluster_score = 0
            for c in clusters:
                significant_words_in_cluster = len(c)
                total_words_in_cluster = c[-1] - c[0] + 1
                score = 1.0 * significant_words_in_cluster \
                    * significant_words_in_cluster / total_words_in_cluster

                if score > max_cluster_score:
                    max_cluster_score = score

            scores.append((sentence_idx, score))

        return scores
