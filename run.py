import Ai_caller as ac
#the prompt it is expected to answer
needle = ["What percent was the NON-GAAP gross margin in 2025","What percent was the NON-GAAP gross margin in Q4 FY25"]
for i in needle:
    ac.run_test(i)