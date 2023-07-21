import docx
from os import walk

def getFileNames(dir): #param: directory
    filenames = next(walk(dir), (None, None, []))[2]  # [] if no file
    return filenames

def getWordCount(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return len("\n".join(fullText).split(" "))

def getTotalWordCount(file_names):
    total_words = 0;
    for i in file_names:
        total_words += getWordCount(dir + "/" + i)
    return total_words

dir = "C:/Users/Codia/Desktop/royal_road_project/test_folder"

file_names = getFileNames(dir);
total_words = getTotalWordCount(file_names)

print("total words: " , total_words)
#print(getWordCount(dir + "/test2.docx"))

