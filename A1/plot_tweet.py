# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

#%%
file1 = 'tweet_output'

letters = []
counts = []
with open(file1, 'rb') as f:
    for line in f.readlines():
        line_split = line.decode().split()
        letters.append(line_split[0])
        counts.append(int(line_split[1]))
                      
pron = [letter for letter in letters[:-1]]
freq = [count/counts[-1] for count in counts[:-1]]

#%%
plt.figure(figsize=(10, 6))
plt.bar(pron, freq)

plt.xlabel('Pronoun', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Frequency of Swedish Pronouns in Tweeter', fontsize=16)
#plt.legend()  # auto-legend with labels above.
plt.savefig('tweet.png')
plt.show()
