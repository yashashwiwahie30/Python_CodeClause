import time
string = " My name is Yashashwi Wahie"
wordcount = len(string.split())
print(string)
while True:
    st = time.time()
    inputtext = str(input("Enter the sentence: "))
    et = time.time()
    accuracy = len(set(inputtext.split()) & set(string.split()))
    accuracy = accuracy/wordcount
    timetaken = et - st
    wpm = wordcount/timetaken
    print("WPM: ", wpm, "Accuracy: ", accuracy, "Timetaken", timetaken)