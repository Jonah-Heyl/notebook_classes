#here we are just importing some modules we need
from sys import argv
import os

try:
    import json
except:
    os.system('pip install json')
    import json
try:
    import re
except:
    os.system('pip install re')
    import re 
    
#this is the default global marker
m="#!Z!s"

#this is checks the first line in each cell to see if it has the marker
def check(cell):
    global m # we pass m like this so the function only has one arg, means we can use the filter function
    try: 
        content = cell['source'][0] 
    except:
        return False
    pattern= re.compile(m) #this uses regex to check if the marker is in the first line
    q = pattern.search(content)
    if ( q is  None): #if the marker is not in the first row we keep the cell
        return True
    return False


def create_question(file,new_file): #this function creates the question files
    marker="#!ANS!"
    global m
    m =marker

    with open(file,"r") as f: #here we open the notebook as a json
        t=json.load(f)
    notebook=t['cells']
    keep= list(filter(check,notebook)) #this returns all the cells we want to keep
    t['cells']=keep
    with open (new_file,"w") as l: #this makes the new json file
        json.dump(t,l)

#this code is used to walk through all the files in a dirrectory and apply the code if nessary
for root, subFolders, files in os.walk(argv[1]):
    for fname in files:
        if fname.endswith(".ipynb") and not fname.endswith("_QU.ipynb"):
            f1=os.path.join(root, fname)
            f2=os.path.join(root, fname.replace(".ipynb","_QU.ipynb"))
            if os.path.exists(f2):
                if (os.path.getctime(f2) < os.path.getctime(f1)):
                    create_question(f1,f2)
            else:
                create_question(f1,f2)
               
    
