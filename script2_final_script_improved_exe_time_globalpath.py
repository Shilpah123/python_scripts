# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:09:03 2020

@author: shilpa
"""

globpath = "C:/Users/shilpa/Desktop/abc" #add your directory path here     
#Following code changes the figure, concept, table id to lowercase in .xml files.
import os
from bs4 import BeautifulSoup as bs

def lower_figcontab_id(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    s = bs(s, "xml")
    imgs = s.find_all(["fig", "concept", "table"])
    for i in imgs:
        if "id" in i.attrs:
            i.attrs["id"] = i.attrs["id"].lower()
    s = str(s)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)


for dirpath, directories, files in os.walk(globpath):
         for fname in files:
            if fname.endswith(".xml"):
                path = os.path.join(dirpath, fname)
                lower_figcontab_id(path)



#Following code changes topic references in .ditamap files to lowercase and changes file reference extension from .xml to .dita.
def lower_topic_references(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    s = bs(s, "xml")
    imgs = s.find_all("topicref")
    for i in imgs:
        if "href" in i.attrs:
            i.attrs["href"] = i.attrs["href"].replace(".xml", ".dita").lower()
    s = str(s)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)



for dirpath, directories, files in os.walk(globpath):   
           for fname in files:
                if fname.endswith(".ditamap"): 
                    path = os.path.join(dirpath, fname)
                    lower_topic_references(path)


#Following code will update references of images, topics to lowercase in all .xml files. 

def lower_file_references(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    s = bs(s, "xml")
    imgs = s.find_all(["image", "xref", "topicref"])
    for i in imgs:
        if "href" in i.attrs:
            i.attrs["href"] = i.attrs["href"].lower()
    s = str(s)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)


for dirpath, directories, files in os.walk(globpath):
          for fname in files:
                if fname.endswith(".xml"):
                    path = os.path.join(dirpath, fname)
                    lower_file_references(path)

# Following code changes the extension of file reference in topics from xml to dita. 

def change_file_extension_in_references(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    s = bs(s, "xml")
    imgs = s.find_all(["xref"])
    for i in imgs:
        if "href" in i.attrs:
            i.attrs["href"] = i.attrs["href"].replace(".xml",".dita")
    s = str(s)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)


for dirpath, directories, files in os.walk(globpath):   
        for fname in files:
            if fname.endswith(".xml"):
                path = os.path.join(dirpath, fname)
                change_file_extension_in_references(path)


# Following code changes the file extension from .xml to .dita and changes filename to lowercase. 

for dir,subdir,listfilename in os.walk(globpath):
    for filename in listfilename:
        new_filename = filename.replace(".xml",".dita").lower() 
        src = os.path.join(dir, filename) 
        dst = os.path.join(dir, new_filename) 
        os.rename(src,dst)