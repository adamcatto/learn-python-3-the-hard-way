from sys import argv
from time import sleep
from tqdm import tqdm

script, user_name = argv
prompt = '> '

def prog_bar(sleep_interval=0.01, rng=50, ncols=75, descr='Loading...'):
    for i in tqdm (range (rng),  
                   desc=descr,  
                   ascii=False, ncols=ncols): 
        sleep(sleep_interval) 

def sleep_dots(num_dots=3):
    for i in range(num_dots):
        print('.')
        sleep(0.5)

print(f'Hi, {user_name}, this is {script} talking!')
sleep_dots()
print('I have some questions for you...')
sleep_dots()
print(f'Do you like me, {user_name}? [y]/[n]')
likes = input(prompt)
prog_bar(descr="Processing...")
if likes in ['y', 'Y']:
    likes = True
else:
    likes = False
print(f"So, you said {likes} to liking me. Alright!")


