def strip_punctuation(word):
    new = ''
    for w in word:
        if w in punctuation_chars:
            new += w.replace(w, '')
        else:
            new += w
    return new

def get_pos(sentence):
    sentence = sentence.lower()
    sentence = strip_punctuation(sentence)
    sentence = sentence.split()
    count_pos = 0
    for word in sentence:
        if word in positive_words:
            count_pos = count_pos + 1
    return count_pos

def get_neg(sentence):
    sentence = sentence.lower()
    sentence = strip_punctuation(sentence)
    sentence = sentence.split()
    count_pos = 0
    for word in sentence:
        if word in negative_words:
            count_pos = count_pos + 1
    return count_pos

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

ft = open('project_twitter_data.csv')
lines = ft.readlines()
fr = open('resulting_data.csv', 'w')
fr.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
fr.write('\n')
for line in lines[1:]:
    count = line.strip().split(',')
    Number_of_Retweets = int(count[1])
    Number_of_Replies =  int(count[2])
    Positive_Score = get_pos(','.join(count))
    Negative_Score =  get_neg(','.join(count))
    Net_Score = Positive_Score - Negative_Score
    fr.write('{},{},{},{},{}'.format(Number_of_Retweets, Number_of_Replies, Positive_Score, Negative_Score, Net_Score))
    fr.write('\n')

fr.close()
ft.close()
