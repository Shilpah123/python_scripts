# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:51:01 2020

@author: shilpa
"""

#This script performs the following tasks:
#Replaces <emphasis> with <i>; </emphasis> with </i>; <command> with <codeph>; nsnconcept with concept, nsntask with task, nsnmap with map
#Removes keys from concept,task,topic
#Removes rotate attribute from <entry> tag in tables
#Removes attributes that are not supported in ditamap.

#Note: You have to update the path to your directory in three places. Do not miss this out.

import glob
import os
from bs4 import BeautifulSoup as bs
globpath = "C:/Users/shilpa/Desktop/abc" #add your directory path here     

def replacer(filepath, to_replace, value):
    with open(filepath, "r", encoding="utf-8") as file:
        s=file.read()
    s=s.replace(to_replace, value)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(s)


for filepath in glob.iglob("C:/Users/shilpa/Desktop/abc/**/*.xml", recursive=True): #add your directory path here 
    replacer(filepath=filepath, to_replace="<emphasis>", value="<i>")
    replacer(filepath=filepath, to_replace="</emphasis>", value="</i>")
    replacer(filepath=filepath, to_replace="<command>", value="<codeph>")
    replacer(filepath=filepath, to_replace="</command>", value="</codeph>")
    replacer(filepath=filepath, to_replace="<result-entry>", value="")
    replacer(filepath=filepath, to_replace="</result-entry>", value="")
    replacer(filepath=filepath, to_replace='//NSN//DTD DITA Concept//EN" "nsnconcept.dtd"', value='//OASIS//DTD DITA Concept//EN" "concept.dtd"')
    replacer(filepath=filepath, to_replace='//NSN//DTD DITA Task//EN" "nsntask.dtd"', value='//OASIS//DTD DITA Task//EN" "task.dtd"')

for filepath in glob.iglob("C:/Users/sh001/Desktop/compare/mcas_backup_recovery_guide/**/*.ditamap", recursive=True): #add your directory path here 
    replacer(filepath=filepath, to_replace='//NSN//DTD DITA Map//EN" "nsnmap.dtd"', value='//OASIS//DTD DITA Map//EN" "map.dtd"')
    
    
def remove_key_attributes(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    s = bs(s, "xml")
    for tag in s.find_all(["concept", "task", "topic"]):
        attrs = dict(tag.attrs)
        for attr in attrs:
            if "keys" in attr:
                del tag.attrs[attr]
            #i.attrs["href"] = i.attrs["href"].lower()
    s = str(s)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)


for dirpath, directories, files in os.walk(globpath):
        for fname in files:
            if fname.endswith(".xml"):
                path = os.path.join(dirpath, fname)
                remove_key_attributes(path)
            
#Following code removes rotate attribute in the entry tag 
def remove_rotate_attributes(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    s = bs(s, "xml")
    for tag in s.find_all("entry"):
        attrs = dict(tag.attrs)
        for attr in attrs:
            if "rotate" in attr:
                del tag.attrs[attr]
            
    s = str(s)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)


for dirpath, directories, files in os.walk(globpath):  
        for fname in files:
            if fname.endswith(".xml"):
                path = os.path.join(dirpath, fname)
                remove_rotate_attributes(path)
                

#Following code removes maptype attribute in the map tag 
def clean_ditamap_attribute_maptype(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    s = bs(s, "xml")
    for tag in s.find_all("map"):
        attrs = dict(tag.attrs)
        for attr in attrs:
            if "maptype" in attr:
                del tag.attrs[attr]
            
    s = str(s)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)


for dirpath, directories, files in os.walk(globpath):  
        for fname in files:
            if fname.endswith(".ditamap"):
                path = os.path.join(dirpath, fname)
                clean_ditamap_attribute_maptype(path)
                

#Following code removes issue attribute in the map tag 
def clean_ditamap_attribute_issue(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    s = bs(s, "xml")
    for tag in s.find_all("map"):
        attrs = dict(tag.attrs)
        for attr in attrs:
            if "issue" in attr:
                del tag.attrs[attr]
            
    s = str(s)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)


for dirpath, directories, files in os.walk(globpath):  
        for fname in files:
            if fname.endswith(".ditamap"):
                path = os.path.join(dirpath, fname)
                clean_ditamap_attribute_issue(path)
                

#Following code removes release date attribute in the map tag 
def clean_ditamap_attribute_releasedate(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    s = bs(s, "xml")
    for tag in s.find_all("map"):
        attrs = dict(tag.attrs)
        for attr in attrs:
            if "ReleaseDate" in attr:
                del tag.attrs[attr]
            
    s = str(s)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)


for dirpath, directories, files in os.walk(globpath):  
        for fname in files:
            if fname.endswith(".ditamap"):
                path = os.path.join(dirpath, fname)
                clean_ditamap_attribute_releasedate(path)
                

#Following code removes filename attribute in the map tag 
def clean_ditamap_attribute_filename(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    s = bs(s, "xml")
    for tag in s.find_all("map"):
        attrs = dict(tag.attrs)
        for attr in attrs:
            if "Filename" in attr:
                del tag.attrs[attr]
            
    s = str(s)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)


for dirpath, directories, files in os.walk(globpath):  
        for fname in files:
            if fname.endswith(".ditamap"):
                path = os.path.join(dirpath, fname)
                clean_ditamap_attribute_filename(path)
                

#Following code removes AdditionalIdentifier attribute in the entry tag 
def clean_ditamap_attribute_addid(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    s = bs(s, "xml")
    for tag in s.find_all("map"):
        attrs = dict(tag.attrs)
        for attr in attrs:
            if "AdditionalIdentifier" in attr:
                del tag.attrs[attr]
            
    s = str(s)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)


for dirpath, directories, files in os.walk(globpath):  
        for fname in files:
            if fname.endswith(".ditamap"):
                path = os.path.join(dirpath, fname)
                clean_ditamap_attribute_addid(path)
                
                