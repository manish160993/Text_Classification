
import os
import math


def getDocs(hamPath, spamPath):
    train_ham = os.listdir(hamPath)
    train_spam = os.listdir(spamPath)
    ham = []
    spam = []
    for file in train_ham:
        with open(hamPath + '/' + file, 'r', encoding="Latin-1") as myfile:
            data = myfile.read().replace('\n', ' ')
        ham.append(data)
    for files in train_spam:
        with open(spamPath + '/' + files, 'r', encoding="Latin-1") as myfile:
            data1 = myfile.read().replace('\n', ' ')
        spam.append(data1)
    return ham, spam

def NBtrainModel(C, D):
    v = set()
    for entry in D[0]:
        word_list = entry.split(" ")
        v.update(set(word_list))
    for entry2 in D[1]:
        word_list2 = entry2.split(" ")
        v.update(set(word_list2))

    n = len(D[0]) + len(D[1])
    prior = {}
    text = {}
    t = {}
    condProb = {}
    s_sum = {}
    for c in C:
        if c == 'ham':
            Nc = len(D[0])
        else:
            Nc = len(D[1])

        prior[c] = Nc / n
        text[c] = mixTextClass(D, c)
        s = 0
        for token in v:
            t[c + '.' + token] = uniqueCount(text[c], token)
            s = s + uniqueCount(text[c], token)
        sum = 0
        for token in v:
            sum = sum + t[c + '.' + token] + 1
        denominator = sum
        s_sum[c] = denominator
        for token in v:
            condProb[c + '.' + token] = (t[c + '.' + token] + 1) / denominator
    return v, prior, condProb, s_sum


'''
uniqueCount function counts the frequency of occurence of a given token in a given text
'''


def uniqueCount(text, token):
    text_words = text.split(" ")
    count = 0
    for w in text_words:
        if w == token:
            count = count + 1
    return count

'''
this function does what it's name suggests for given document tuple D and class c
'''


def mixTextClass(D, c):
    text = ''
    if c == 'ham':
        for docs in D[0]:
            text = text + docs + " "
        return text
    else:
        for docs in D[1]:
            text = text + docs + " "
        return text


'''
this function applies multinomial naive bayes to test document located at location = d
'''


def applyMultinomialNB(C, v, prior, condProb, d, s_sum):
    global docsSpam
    global docsHam
    data = d
    score = {}
    updateFromData = extractTokensFromDoc(v, data, condProb, s_sum)
    w = updateFromData[0]
    smoothedCondProb = updateFromData[1]
    for c in C:
        score[c] = math.log10(prior[c])
        for token in w:
            score[c] = score[c] + math.log10(smoothedCondProb[c + '.' + token])
    # print(score)
    if score['ham'] >= score['spam']:
        # print("The document belongs to class ham")
        docsHam = docsHam + 1
    else:
        # print("The document belongs to class spam")
        docsSpam = docsSpam + 1


'''
sub function of testing function called applyMultinomialNB
'''


def extractTokensFromDoc(v, data, condProb, s_sum):
    # result[0] is tokens obtained from splitting data
    vocabLen = len(v)
    vocabData = set(data.split(" "))
    # result[1] is a dictionary containing smoothed cond prob for items having zero frequency in the vocabulary v

    for token in vocabData:
        token_ham = 'ham.' + token
        token_spam = 'spam.' + token
        if token_ham not in condProb.keys():
            condProb[token_ham] = 1 / (s_sum['ham'] + vocabLen)
        if token_spam not in condProb.keys():
            condProb[token_spam] = 1 / (s_sum['spam'] + vocabLen)

    return vocabData, condProb


'''
main function for testing of documents in a folder given by directory folder given by path
'''


def test_NB(C, res, path_folder):
    global docsHam
    global docsSpam
    D = getDocs(path_folder + '\ham', path_folder + '\spam')
    # D[0] is a list of documents in folder ham, D[1] is a list of data of documents in folder spam
    for doc in D[0]:
        applyMultinomialNB(C, res[0], res[1], res[2], doc, res[3])
    accuracyHam=str((docsHam / len(D[0])) * 100)
    print('Accuracy for test set documents in ham folder: ' + accuracyHam + "%")
    docsSpam = 0
    docsHam = 0
    for doc in D[1]:
        applyMultinomialNB(C, res[0], res[1], res[2], doc, res[3])
    accuracySpam=str((docsSpam / len(D[1])) * 100)
    print('Accuracy for test set documents in spam folder: ' + accuracySpam  + "%")
    #accuracy = ((docsHam / len(D[0])) + (docsSpam / len(D[1]))) * 100
    #accuracy=(double(accuracyHam)+double(accuracySpam))/2
    print("The accuracy is: " + str(accuracy))


if __name__ == '__main__':
    trainHam = r'C:\Users\manis\Desktop\Github\Text_Classification\Naive\train\ham'
    trainSpam = r'C:\Users\manis\Desktop\Github\Text_Classification\Naive\train\spam'
    docsSpam = 0
    docsHam = 0
    C = ['ham', 'spam']
    Dict = getDocs(trainHam, trainSpam)
    res = NBtrainModel(C, Dict)
    testPath = r'C:\Users\manis\Desktop\Github\Text_Classification\Naive\test'
    test_NB(C, res, testPath)

