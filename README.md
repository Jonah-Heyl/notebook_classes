# notebook_classes
Some useful scripts for classes with juypter notebooks.


# Usage of  Question and Answer script:

This script is for teaching juypter notebooks. It reads through juypter notebooks and creates new notebooks with only certain cells. This is useful for classes with juypter notebook assignments, what this allows the instructor to do is create one directory with notebooks containing answers and questions. They then run the script and it goes through and creates the question notebooks. We'll go through the steps.

1. Create a juypter notebook, and mark your answer cells with #!Ans!

2. Run the script, on the directory it will go through every file with .ipynb and run the script on it.

```
python crawl_script.py .
```

3. All done

---
Alternatively, you can use the script intended to run on one notebook at a time, you can import it into your notebook and then run it, with the code below.

```
import run as rn

rn.makefile("old_file","new_file")
```
