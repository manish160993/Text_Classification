import os, os.path
import glob
import math
import os, os.path


# will be used to calculate the accuracy

def accuracy(square,newWeights,d):
    totalClassified = 0     #total emails
    classAccurately = 0     #email classified correctly
    for x in range(0, len(d)):
        totalClassified = totalClassified + 1
        classDiscovered = 0.0
        for i in range(0, len(newWeights)):
            if i == 0:
                classDiscovered = float(newWeights[i])
            else:
                classDiscovered = classDiscovered + (float(square[x][i - 1]) * float(newWeights[i]))
        if classDiscovered >= 0.5:
            classDiscovered = 1 #class discovered as sigma
        else:
            classDiscovered = 0
        if classDiscovered == square[x][-1]: #checking if the class is discovered correctly
            classAccurately = classAccurately + 1
    return ((classAccurately / totalClassified) * 100)


# calculating the log
def logFunction(square, weights):
    value = 0
    for x in range(len(square)-1):
        total = 0
        for i in range(len(square) - 1):
            total += square[x][i] * w[i]    #total vector
        expValue = math.exp(total)          #exponenetial eqn
        finalValue = square[x][-1] * total
        lastValue = math.log(1 + expValue)
        value += finalValue - lastValue
    #print(value)

# calculating the gradient ascent
def calGrad(square,weights,lambdaVal):
    newSquare = [[0 for x in range(len(square[0])+1)] for y in range(len(square))]
    for y in range(0,len(newSquare)):
        newSquare[y][0]=1
    for x in range(0,len(newSquare)):
        for y in range(1, len(newSquare[0])):
            newSquare[x][y]=square[x][y-1]
    for ascent in range(10):
        logFunction(newSquare, weights)
        w = weights
        eta = 0.02
        grad = [0 for x in range(len(newSquare))]
        for l in range(len(newSquare) - 1):
            total = 0
            for i in range(len(newSquare[l]) - 1):
                total += newSquare[l][i] * weights[i]
            expValue = math.exp(total)
            sigm = expValue / (expValue + 1)
            grad[l] = (square[l][-1] - sigm)
        for i in range(len(weights)):
            gradValue = 0
            for l in range(len(newSquare)):
                gradValue += newSquare[l][i] * grad[l]
            w[i] = w[i] + ((eta * gradValue) - (eta * lambdaVal * w[i]))
        weights = w
    return weights

# extract the vocabulary
def deriveVoc(path):
    occurrenceDict= []
    files = glob.glob(path+'\*')

    # iterate over the list getting each file
    for file in files:
        # open the file and then call .read() to get the text
        with open(file, encoding="utf8", errors='replace') as fileRead:
            text = fileRead.read()
            splitText = text.split(' ')
            for word in splitText:
                occurrenceDict.append(word)

    return set(occurrenceDict)

# extract the vocabulary
def extractDocVocab(path,classRes):
    occurrenceDict = []
    File = open(path, encoding="utf8", errors='replace' )
    text = File.read()
    splitText = text.split(' ')
    for word in splitText:
        occurrenceDict.append(word)

    newList = list(set(occurrenceDict))
    newList.append(classRes)
    return newList



if __name__ == "__main__":

    testHam = r'C:\Users\manis\Desktop\Github\Text_Classification\Naive\enron1\test\ham'
    testSpam = r'C:\Users\manis\Desktop\Github\Text_Classification\Naive\enron1\test\spam'
    trainHam = r'C:\Users\manis\Desktop\Github\Text_Classification\Naive\enron1\train\ham'
    trainSpam = r'C:\Users\manis\Desktop\Github\Text_Classification\Naive\enron1\train\spam'

    octave1 = deriveVoc(trainHam)
    octave2 = deriveVoc(trainSpam)
    octave3  =octave1.union(octave2)
    finalSet = list(octave3)

# find the original length of ham and spam
    splitHam = len([name for name in os.listdir(trainHam) if os.path.isfile(os.path.join(trainHam, name))])
    splitSpam = len([name for name in os.listdir(trainSpam) if os.path.isfile(os.path.join(trainSpam, name))])

    print("splitHam : ",splitHam)
    print("splitSpam : ",splitSpam)
    
    

    trainingHam = math.ceil(splitHam*0.7)
    trainingSpam = math.ceil(splitSpam*0.7)

    print("trainingHam : ",trainingHam)
    print("trainingSpam : ",trainingSpam)


    dict = []

    for x in range(0,2):
        if x==0:
            classRes = 0
            fileCount = 0
            files = glob.glob(trainHam + '\*')
        else:
            classRes = 1
            fileCount = 0
            files = glob.glob(trainSpam + '\*')
        for file in files:
            with open(file, encoding="utf8", errors='replace') as f:
                fileCount=fileCount+1
                if fileCount<=trainingHam and classRes==0:
                    dict.append(extractDocVocab(str(file),classRes))
                elif fileCount <= trainingSpam and classRes == 1:
                        dict.append(extractDocVocab(str(file), classRes))
                else:
                    break;

    square = [[0 for x in range(len(finalSet)+1)] for y in range(len(dict))]



    for x in range(0,len(dict)):
        wordList = list(dict[x])
        for y in range(0,len(wordList)-1):
            listWord = list(wordList)[y]
            xa = finalSet.index(listWord)
            square[x][xa] = 1
        square[x][len(finalSet)] = wordList[len(wordList)-1]


    dict1 = []
    for x in range(0, 2):
        if x == 0:
            classRes = 0
            files = glob.glob(trainHam + '\*')
            fileCount = 0
        else:
            classRes = 1
            files = glob.glob(trainSpam + '\*')
            fileCount = 0
        for file in files:
            with open(file, encoding="utf8", errors='replace') as f:
                fileCount = fileCount + 1

                if fileCount > trainingHam and fileCount <= splitHam and classRes == 0:
                    #print(fileCount)
                    dict1.append(extractDocVocab(str(file), classRes))
                elif fileCount > trainingSpam and fileCount <= splitSpam and classRes == 1:
                    #print(fileCount)
                    dict1.append(extractDocVocab(str(file), classRes))

    square1 = [[0 for x in range(len(finalSet) + 1)] for y in range(len(dict1))]
    for x in range(0, len(dict1)):
        wordList = list(dict1[x])
        for y in range(0, len(wordList) - 1):
            listWord = list(wordList)[y]
            if listWord in finalSet:
                z = finalSet.index(listWord)
                square1[x][z] = 1

        square1[x][len(finalSet)] = wordList[len(wordList) - 1]

    # Lamda Selection Calculation

    lamList = [ 0.05 , 3 , 7 , 13]
    accList = []
    for lam in lamList:
        print("For Lam :" + str(lam))
        w = [0 for x in range(len(finalSet) + 1)]
        newWeights = calGrad(square, w, lam)
        accList.append(accuracy(square1, newWeights,dict1))
        print(accList[-1])

    lamValue = lamList[accList.index(max(accList))]
    print("The winner of the lamda values is   ",max(accList)," ",str(lamValue))

    #retrain
    dict = []

    for x in range(0, 2):
        if x == 0:
            classRes = 0
            fileCount = 0
            files = glob.glob(trainHam + '\*')
        else:
            classRes = 1
            fileCount = 0
            files = glob.glob(trainSpam + '\*')
        for file in files:
            with open(file, encoding="utf8", errors='replace') as f:
                dict.append(extractDocVocab(str(file), classRes))

    square = [[0 for x in range(len(finalSet) + 1)] for y in range(len(dict))]

    for x in range(0, len(dict)):
        wordList = list(dict[x])
        for y in range(0, len(wordList) - 1):
            listWord = list(wordList)[y]
            z = finalSet.index(listWord)
            square[x][z] = 1
        square[x][len(finalSet)] = wordList[len(wordList) - 1]


    # Weight Calculation

    w = [0 for x in range(len(finalSet) + 1)]

    newWeights = calGrad(square, w, lamValue)

    dict = []
    for x in range(0, 2):
        if x == 0:
            classRes = 0
            files = glob.glob(testHam + '\*')
        else:
            classRes = 1
            files = glob.glob(testSpam + '\*')
        for file in files:
            with open(file, encoding="utf8", errors='replace') as f:
                dict.append(extractDocVocab(str(file), classRes))

    square = [[0 for x in range(len(finalSet) + 1)] for y in range(len(dict))]
    for x in range(0, len(dict)):
        wordList = list(dict[x])
        for pp in range(0, len(wordList) - 1):
            listWord = list(wordList)[pp]
            if listWord in finalSet:
                xa = finalSet.index(listWord)
                square[x][xa] = 1
        square[x][len(finalSet)] = wordList[len(wordList) - 1]

    print(accuracy(square, newWeights, dict))
