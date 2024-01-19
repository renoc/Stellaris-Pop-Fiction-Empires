import os
import json
import re

def read_existing_file(filename='user_empire_designs_v3.4.txt'):
    #print("Reading File")
    with open("../" + filename, 'r') as open_file:
        filecontents = open_file.read()
    #print(filecontents[:32] + "...")
    #print("File read finished")
    return filecontents

def seperate_empires(filecontents):
    re.subn("^}$","^\},$",)
    x = json.loads(filecontents)
    # print (x)
