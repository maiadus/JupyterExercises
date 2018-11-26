from sys import argv 
script, user_name = argv
prompt = '.'

print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = input(prompt)

print ("Where do you live %s?" % user_name)
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print ("""
Alright, so you said %r about liking me. You live in %r. Not sure where that is. And you have a %r computer. Nice.
""" % (likes, lives, computer))

jupyter@pytorch-and-fastai-test:~$ cd JupyterExercises
jupyter@pytorch-and-fastai-test:~/JupyterExercises$ python Exercise14.py maia
Hi maia, I'm the Exercise14.py script.
I'd like to ask you a few questions.
Do you like me maia?
.perhaps
Where do you live maia?
.miami
What kind of computer do you have?
.mac

Alright, so you said 'perhaps' about liking me. You live in 'miami'. Not sure where that is. And you have a 'mac' computer. Nice.

jupyter@pytorch-and-fastai-test:~/JupyterExercises$
