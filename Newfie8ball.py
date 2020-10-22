#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def magic():
    input("Whatta ya want?: ")
    return random.choice([ "buddy im sure of it" , "Looks good" , "I'd say" , "Sure what odds?" , "G'wan by!" , "I knows your'e not that stunned" , "Nar chance" , "You can forget 'bout dat, ol' man" ])


print("Hello,")
while True:
    if input("start or end: ").strip().lower() == "start":
        print(magic(), "\n")
        continue
    else:
        quit()

