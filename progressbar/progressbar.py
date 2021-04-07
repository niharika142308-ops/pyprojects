  
'''
Create Progress Bar with Python
Author: Niharika
            
'''

#import the necessary module!
from tqdm import tqdm, trange
from time import sleep 

'''desc: You can use this parameter to specify the description of your progress bar as follows:
Syntax:
tqdm (self, iterable, desc= “Text You want”) 
ascii: You can use ASCII characters to fill the progress bar as per your liking.
Syntax:

tqdm (self, iterable, ascii= “123456789$”, desc=”Text You Want”)
 '''
for i in tqdm(range(0, 100),ascii ="*$", desc ="my progress bar"):
    sleep(.1)
print("Iteration sucessful!")    