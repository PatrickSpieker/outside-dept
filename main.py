# importing:
# regex, requests, urllib, argv, and beautiful soup
import re
import requests
import urllib
import sys
from bs4 import BeautifulSoup
import json
from helpers import *
from pprint import pprint

# defining relevant functions
# picking up command line argument
try:
    dept = str(sys.argv[1])
except IndexError:
    print("You must pass the department code as an argument!")
    sys.exit(0);

# empty list for all Course JSON
nodes = []
# empty list for course links
links = []

# Prereq dictionary for link creation
link_dict = {}

# base url
url = "http://www.washington.edu/students/crscat/" + dept.lower() + ".html"
# fetching HTML
urllib.urlretrieve(url, "courseData.html")
# constructing regex pattern
deptPatt = dept.lower()+"\d\d\d"
coursePatt = "[A-Z].[A-Z]{1,3}\s\d\d\d"

soup = getSoup("courseData.html")

# courses required as prereqs, but located out of the department
outOfDept = []
def getNonDeptPrereqs(rawList, coursePatt, dept):
    ndPrereqs = []
    for section in rawList:
        options = re.compile(coursePatt).findall(section)
        for option in options:
            if dept not in option:
                ndPrereqs.append(option)
    return ndPrereqs

#print(getTags(patt, soup)+"\n")
for tag in getTags(deptPatt, soup):
    # only concerned with first child
    content = tag.findAll()[0]
    courseId = getCourseId(content, dept)
    rawList = getRawPrereqList(content)    
    ndPrereqs = getNonDeptPrereqs(rawList, coursePatt, dept);
    print(courseId, ndPrereqs)
    #courseClass = courseId.replace(" ", "").lower()
    # filtering out grad level courses
    #numCID = int(float(courseId[3:]))
    #if numCID < 500:

    #regPrereqs = getRegPrereqs(rawList, coursePatt)
    #regPrereqs = getNonDeptPrereqs(rawList, coursePatt, deptPatt);
    #print(regPrereqs)
    #choicePrereqs = getChoicePrereqs(rawList, coursePatt)
     

    """# creating JSON object to represent current node
    node = {u"course_id": courseId, u"regPrereqs": regPrereqs,
            u"choicePrereqs": choicePrereqs, u"numCID": numCID,
            u"highlighted": 0}
    nodes.append(node)
    
    # mapping a course's ID to its position in the list of links
    link_dict[courseId] = nodes.index(node)

        


for node in nodes:
    # iterating over the regular prereqs
    for prereq in node["regPrereqs"]:
        try:
            links.append({"source": link_dict[prereq], # source is the prereq
                          # target is the course itself
                          "target": link_dict[node["course_id"]] 
                          
                          });
        except KeyError as e:
            print(e, "didn't exist in the deptartment");




# setting up JSON output file
json_output = {"nodes": nodes,
               "links": links}


with open("course-data.json", "w") as outfile:
    json.dump(json_output, fp=outfile)
"""



