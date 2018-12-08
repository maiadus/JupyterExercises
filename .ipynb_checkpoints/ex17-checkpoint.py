from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
in_file = open(from_file) 
indata = in_file.read()

print ("The input file is %d bytes long" % len(indata))

print ("Does the output file exist? %r" % exists(to_file)) 
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') 
out_file.write(indata)

print ("Alright, all done.")

out_file.close() 
in_file.close()

jupyter@pytorch-and-fastai-test:~$ cd JupyterExercises
jupyter@pytorch-and-fastai-test:~/JupyterExercises$ python ex17.py ex17.py
Traceback (most recent call last):
  File "ex17.py", line 4, in <module>
    script, from_file, to_file = argv
ValueError: not enough values to unpack (expected 3, got 2)
jupyter@pytorch-and-fastai-test:~/JupyterExercises$ python ex17.py ex17.py new file.py
Traceback (most recent call last):
  File "ex17.py", line 4, in <module>
    script, from_file, to_file = argv
ValueError: too many values to unpack (expected 3)
jupyter@pytorch-and-fastai-test:~/JupyterExercises$ python ex17.py ex17.py ex17.py
Copying from ex17.py to ex17.py
The input file is 540 bytes long
Does the output file exist? True
Ready, hit RETURN to continue, CTRL-C to abort.

Alright, all done.
jupyter@pytorch-and-fastai-test:~/JupyterExercises$