from sys import argv 
script, filename = argv

print ("We're going to erase %r." % filename )
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1: ") 
line2 = input("line 2: ") 
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

target.write(line1) 
target.write("\n") 
target.write(line2) 
target.write("\n") 
target.write(line3) 
target.write("\n")

print ("And finally, we close it.")
target.close()

jupyter@pytorch-and-fastai-test:~$ ls
JupyterExercises  train.csv  Untitled.ipynb
jupyter@pytorch-and-fastai-test:~$ cd JupyterExercises
jupyter@pytorch-and-fastai-test:~/JupyterExercises$ python ex16.py ex15_sample.txt
We're going to erase 'ex15_sample.txt'.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
?
Opening the file...
Truncating the file. Goodbye!
Now I'm going to ask you for three lines.
line 1: hey
line 2: what's up
line 3: hello!
I'm going to write these to the file.
And finally, we close it.
jupyter@pytorch-and-fastai-test:~/JupyterExercises$
