
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

m="#!Z!s"

def check(cell):
    global m
    try:
        content = cell['source'][0]
    except:
        return False
    pattern= re.compile(m)
    q = pattern.search(content)
    if ( q is  None):
        return True
    return False


def create_question(file,new_file):
    marker="#!ANS!"
    global m
    m =marker

    with open(file,"r") as f:
        t=json.load(f)
    notebook=t['cells']
    keep= list(filter(check,notebook))
    t['cells']=keep
    with open (new_file,"w") as l:
        json.dump(t,l)


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
               
    
