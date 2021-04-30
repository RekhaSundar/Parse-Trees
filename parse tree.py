#!/usr/bin/env python
# coding: utf-8

# In[1]:


#all required imports
from nltk.parse import RecursiveDescentParser
from nltk import CFG


# In[2]:


grammar1 = CFG.fromstring("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> 'saw'
V -> 'ate'
V -> 'walked'
NP -> 'john'
NP -> 'mary'
NP -> 'bob'
NP -> Det N | Det N PP
Det -> 'a'
Det -> 'an'
Det -> 'the'
Det -> 'my'
N -> 'cat'
N -> 'dog'
N -> 'man'
N -> 'telescope'
N -> 'park'
P -> 'in'
P -> 'on'
P -> 'by'
P -> 'with'
""")


# In[3]:


grammar2 = CFG.fromstring("""
S -> NP VP
NP -> Det Nom | PropN
Nom -> Adj Nom | N
VP -> V Adj | V NP | V S | V NP PP
PP -> P NP
PropN -> 'buster'
PropN -> 'chatterer'
PropN -> 'joe'
Det -> 'a'
Det -> 'the'
N -> 'bear'
N -> 'squirrel'
N -> 'tree'
N -> 'fish'
Adj -> 'angry'
Adj -> 'frightened'
Adj -> 'little'
Adj -> 'tall'
V -> 'chased'
V -> 'said'
V -> 'thought'
V -> 'was'
V -> 'put'
P -> 'on'
""")


# In[4]:


rd = RecursiveDescentParser(grammar1)
sentence1 = 'mary saw a telescope in the park'.split()
for t in rd.parse(sentence1):
    print(t)
t.draw()


# In[ ]:


#before executing this line restart the kernel and clear all outputs
rd = RecursiveDescentParser(grammar2)
sentence2 = 'the bear chased the frightened squirrel'.split()
for s in rd.parse(sentence2):
    print(s)
s.draw()


