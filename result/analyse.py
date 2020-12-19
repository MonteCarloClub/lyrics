import os

root = './useful/sorted-last200'
output = './analysis'

for rapperfilename in os.listdir(root):
    
    with open(f'{root}/{rapperfilename}', 'r', encoding='UTF-8') as rapperfile:
        
        for line in rapperfile.readlines():

            