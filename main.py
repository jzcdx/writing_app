import docx
from os import walk
from datetime import datetime

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

def getCurDay():
    #strftime and strptime are different af.
    cur_day = datetime.now()
    date_string = cur_day.strftime('%Y-%m-%d')
    parsed_date = datetime.strptime(date_string, '%Y-%m-%d')

    year = str(parsed_date.year)
    month = str(parsed_date.month)
    day = str(parsed_date.day)

    date = year + "-" + month + "-" + day

    print("date: " , date)
    #format: year-month-day, e.g: 2023-7-30 (string)
    return date

def dailyUpdate():
    #all the functions that we run once a day.
    #Read, get current day, update days, update stat totals

    dir = "C:/Users/Codia/Desktop/royal_road_project/test_folder"
    file_names = getFileNames(dir);


    total_words = getTotalWordCount(file_names)
    date = getCurDay()

    
    pass


dailyUpdate()
#print(getWordCount(dir + "/test2.docx"))

