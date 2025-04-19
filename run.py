import Ai_caller as ac
import html_source as hs
from datetime import datetime
import time

test = int(input("Enter which needle to test: "))
num_test = int(input("Enter number of times to run test: "))

for j in range (num_test):
    if test == 1:
        needle = [hs.needle1_prompt1,hs.needle1_prompt2]
        tag = "Test for needle 1"
    elif test ==2:
        needle = [hs.needle2_prompt1,hs.needle2_prompt2]
        tag = "test for needle 2"
    elif test ==3:
        needle = [hs.needle3_prompt1,hs.needle3_prompt2]
        tag = "test for needle 3"
    with open("Results.csv", "a") as f:
        now = datetime.now()
        f.write("-"*100+"\n")
        f.write(str(now)+"\n")
        f.write(tag+"\n")
        f.write("-"*100+"\n") 
    for i in needle:
        ac.run_test(i,test)
        time.sleep(60)