needle1_prompt1 = "What percent was the NON-GAAP gross margin in Q4 FY25?"
needle1_prompt2 = "What percent was the NON-GAAP gross margin in quarter four of 2025?"

needle3_prompt1 = "What percent was the NON-GAAP gross margin in Q3 FY25?"
needle3_prompt2 = "What percent was the NON-GAAP gross margin in quarter three of 2025?"

needle2_prompt1 = "What is the value of the cash, cash equivalents and marketable securities in january of 2024"
needle2_prompt2 = "What is the value of cash assets in january of 2024"

needle4_prompt1 = "What is the value of the cash, cash equivalents and marketable securities in january of 2025"
needle4_prompt2 = "What is the value of cash assets in january of 2025"




with open('Unedited_html.txt') as f:
    unedited_html = f.read()

#Needle1
with open('no_needle1.txt') as f:
    no_needle1 = f.read()

with open('italic_needle1.txt') as f:
	italic_needle1 = f.read()

with open('bold_needle1.txt') as f:
	bold_needle1 = f.read()

with open('underlined_needle1.txt') as f:
	underlined_needle1 = f.read()

#Needle2
with open('no_needle2.txt') as f:
    no_needle2 = f.read()

with open('italic_needle2.txt') as f:
	italic_needle2 = f.read()

with open('bold_needle2.txt') as f:
	bold_needle2 = f.read()

with open('underlined_needle2.txt') as f:
	underlined_needle2 = f.read()

#Needle3
with open('no_needle3.txt') as f:
    no_needle3 = f.read()

with open('italic_needle3.txt') as f:
	italic_needle3 = f.read()

with open('bold_needle3.txt') as f:
	bold_needle3 = f.read()

with open('underlined_needle3.txt') as f:
	underlined_needle3 = f.read()

#Needle4
with open('no_needle4.txt') as f:
    no_needle4 = f.read()

with open('italic_needle4.txt') as f:
	italic_needle4 = f.read()

with open('bold_needle4.txt') as f:
	bold_needle4 = f.read()

with open('underlined_needle4.txt') as f:
	underlined_needle4 = f.read()