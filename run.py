import Ai_caller as ac
import html_source as hs
from datetime import datetime
import time
# test = int(input("What are you testing\n\
#                  needle placement top & no needle type 1.\n\
#                  needle placement bottom type 2.\n \
#                  ENTER HERE:"))
for j in range (6):
    time.sleep(60)
    test =2
    if test == 1:
        needle = [hs.needle_top,hs.needle_top_less_specific]
        tag = "Test for top needle placement and no needle"
    elif test ==2:
        needle = [hs.needle_bottom,hs.needle_bottom_less_specific]
        tag = "test for bottom needle placement"
    with open("Results.txt", "a") as f:
        now = datetime.now()
        f.write("-"*100+"\n")
        f.write(str(now)+"\n")
        f.write(tag+"\n")
        f.write("-"*100+"\n")
        
    for i in needle:
        ac.run_test(i,test)