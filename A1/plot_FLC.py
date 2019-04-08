# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

#%%
file1 = 'FLC_output'

letters = []
counts = []
with open(file1, 'rb') as f:
    for line in f.readlines():
        line_split = line.decode().split()
        if line_split[0] >= 'a' and line_split[0] <= 'z':
            letters.append(line_split[0])
            counts.append(int(line_split[1]))
                      
    

#%%
plt.figure(figsize=(10, 6))
#plt.plot(letters, counts, '.-')
plt.bar(letters, counts)

plt.xlabel('First Letter', fontsize=12)
plt.ylabel('Counts', fontsize=12)
plt.title('First Letter Count', fontsize=16)
#plt.legend()  # auto-legend with labels above.
plt.savefig('FLC.png')
plt.show()

#%%
'''
with open(file1, 'r') as f:
    reals = [line.split()[1] for 
             line in f.readlines() if 
             line.split() and line.split()[0] == 'real']
with open(file1, 'r') as f:
    users = [line.split()[1] for 
             line in f.readlines() if 
             line.split() and line.split()[0] == 'user']

reals = [float(time.split('m')[0]) * 60 + 
         float(time.split('m')[1][:-1]) for 
         time in reals]
users = [float(time.split('m')[0]) * 60 + 
         float(time.split('m')[1][:-1]) for 
         time in users]
'''
