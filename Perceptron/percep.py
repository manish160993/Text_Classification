import os
import math

# Calculating the weights
def calWeights(ham,spam,N):
    global V
    data = set()
    ham_data = documentGetter(ham)
    for iter in range(len(ham_data)):
        ham_set = set(ham_data[iter].split(" "))
        data = data.union(ham_set)
    spam_data = documentGetter(spam)
    for iter2 in range(len(spam_data)):
        spam_set = set(spam_data[iter2].split(" "))
        data = data.union(spam_set)
    V = ['DummyTextForW[0]']  # since X0 is always one , and the notation starts with words starting X1
    list_data = list(data)
    V.extend(list_data)
    W = [0 for i in range(len(V))] #corresponding weights, beginning with initial weights of zero
    hamX = getDoc(ham)
    spamX = getDoc(spam)
    n=0.1 #take initial step size as 0.01
    for iteration in range(N):
             # for docs in ham folder
             rows = len(hamX)
             t = 0
             for j in range(rows):
                 o = W[0]
                 for i in range(1, len(W)):
                     o = o + (W[i] * hamX[j][i])
                 if o > 0:
                     o = 1
                 else:
                     o = 0
                 for wt in range(len(W)):
                     W[wt]=W[wt]+(n*(t-o)*hamX[j][wt])

             # for docs in spam folder
             rows = len(spamX)
             t = 1
             for k in range(rows):
                 o = W[0]
                 for i in range(1, len(W)):
                     o = o + (W[i] * spamX[k][i])
                 if o > 0:
                     o = 1
                 else:
                     o = 0
                 for wt in range(len(W)):
                     W[wt] = W[wt] + (n * (t - o) * spamX[k][wt])
    return W

'''
documentGetter function gets the documents inside the directory specified by Path
'''
def documentGetter(Path):
    directory = os.listdir(Path)
    files = []
    for file in directory:
        with open(Path + '/' + file, 'r', encoding="Latin-1") as myfile:
            data = myfile.read().replace('\n', ' ')
        files.append(data)
    return files


'''
returns different value if the word is there
'''
def getDoc(Path):
    folder = os.listdir(Path)
    X=[]
    for doc in folder:
        freq=[1] #frequency for W[0] is X[0] is 1
        with open(Path + '/' + doc, 'r', encoding="Latin-1") as myfile:
            data = myfile.read().replace('\n', ' ')
        data_Set = set(data.split(" "))
        for i in range(1,len(V)):
            if V[i] in data_Set:
                freq.append(1)
            else:
                freq.append(0)
        X.append(freq)
    return X

'''
tests accuracy on various set using W and L values along with data
'''
def testData(hamTrain,spamTrain,ham,spam,N):
    print("Value of iteration: "+str(N))
    W = calWeights(hamTrain, spamTrain, N)
    hamX = getDoc(ham)
    spamX = getDoc(spam)
    ham_i=0
    spam_i=0
    for i in range(len(hamX)):
        totalHam = 0
        for j in range(len(hamX[0])):
            totalHam= totalHam+ (W[j]*hamX[i][j])
        if totalHam<0:
            ham_i=ham_i+1
    for i1 in range(len(spamX)):
        totalSpam = 0
        for j1 in range(len(spamX[0])):
            totalSpam= totalSpam+ (W[j1]*spamX[i1][j1])
        if totalSpam>0:
            spam_i=spam_i+1
    accuracy = ((ham_i+spam_i)/(len(hamX)+len(spamX)))*100
    print("Accuracy : "+str(accuracy)+"%")
    return accuracy

if __name__== '__main__':
    V=[]
    ham70=r'C:\Users\manis\Desktop\MachineLearning-TextClassifier-master\DataSetLR\dataSet3\train\ham70'
    ham30=r'C:\Users\manis\Desktop\MachineLearning-TextClassifier-master\DataSetLR\dataSet3\train\ham30'
    ham100=r'C:\Users\manis\Desktop\MachineLearning-TextClassifier-master\DataSetLR\dataSet3\train\ham'
    spam70=r'C:\Users\manis\Desktop\MachineLearning-TextClassifier-master\DataSetLR\dataSet3\train\spam70'
    spam30=r'C:\Users\manis\Desktop\MachineLearning-TextClassifier-master\DataSetLR\dataSet3\train\spam30'
    spam100=r'C:\Users\manis\Desktop\MachineLearning-TextClassifier-master\DataSetLR\dataSet3\train\spam'
    hamTest=r'C:\Users\manis\Desktop\MachineLearning-TextClassifier-master\DataSetLR\dataSet3\test\ham'
    spamTest=r'C:\Users\manis\Desktop\MachineLearning-TextClassifier-master\DataSetLR\dataSet3\test\spam'


    n = [5,10,15,20]
    accur=[]
    for z in range(len(n)):
        print("Testing with 70% data " + " with a chosen value of iterations as " + str(n[z]))
        accur.append(testData(ham70, spam70, ham30, spam30, n[z]))

    N=(accur.index(max(accur)))

    #print(N)
    print("Testing with 100% data " + " with a chosen value of iterations as " + str(n[N]))
    testData(ham100,spam100,hamTest,spamTest,n[N])