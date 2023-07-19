import docx
from os import walk

"""
DB: 
day {
    "words": integer,
    "timestamp": datetime
}
"""

def getFileNames(dir): #param: directory
    filenames = next(walk(dir), (None, None, []))[2]  # [] if no file
    return filenames

def getWordCount(filepath):
    doc = docx.Document(filepath)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return len("\n".join(fullText).split(" "))


dir = "C:/Users/Codia/Desktop/royal_road_project/test_folder"
print(getFileNames(dir))

print(getWordCount("test.docx"))
