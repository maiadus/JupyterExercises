from sys import argv
script, first, second, third = argv
print ("The script is called:", script) 
print ("Your first variable is:", first) 
print ("Your second variable is:", second) 
print ("Your third variable is:", third)

jupyter@pytorch-and-fastai-test:~$ ls
JupyterExercises
jupyter@pytorch-and-fastai-test:~$ python3 Exercise13.py uuhu bubhb jujju
python3: can't open file 'Exercise13.py': [Errno 2] No such file or directory
jupyter@pytorch-and-fastai-test:~$ ls
JupyterExercises
jupyter@pytorch-and-fastai-test:~$ pwd
/home/jupyter
jupyter@pytorch-and-fastai-test:~$ cd JupyterExercises/
jupyter@pytorch-and-fastai-test:~/JupyterExercises$ python3 Exercise13.py hi hey hello
  File "Exercise13.py", line 3
    print "The script is called:", script
                                ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("The script is called:", script)?
jupyter@pytorch-and-fastai-test:~/JupyterExercises$ python3 Exercise 13.py hi hey hello
python3: can't open file 'Exercise': [Errno 2] No such file or directory
jupyter@pytorch-and-fastai-test:~/JupyterExercises$ python3 Exercise13.py hi hey hello
The script is called: Exercise13.py
Your first variable is: hi
Your second variable is: hey
Your third variable is: hello
jupyter@pytorch-and-fastai-test:~/JupyterExercises$
