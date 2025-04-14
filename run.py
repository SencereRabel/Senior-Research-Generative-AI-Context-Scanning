import Ai_caller as ac
import html_source as hs
from datetime import date, time, datetime


needle = [hs.needle_top,hs.needle_top_less_specific]
with open("Results.txt", "a") as f:
    now = datetime.now()
    f.write("-"*100+"\n")
    f.write("-"*100+"\n")
    f.write(str(now)+"\n")
for i in needle:
    ac.run_test(i)