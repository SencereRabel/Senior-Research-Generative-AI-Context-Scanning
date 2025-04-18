needle_top = "What percent was the NON-GAAP gross margin in Q4 FY25?"
needle_top_less_specific = "What percent was the NON-GAAP gross margin in quarter four of 2025?"

needle_bottom = "What is the value of the cash, cash equivalents and marketable securities in january of 2024"
needle_bottom_less_specific = "What is the value of cash assets in january of 2024"



with open('Unedited_html.txt') as f:
    unedited_html = f.read()

#Needle top
with open('no_needle_html(needle_top).txt') as f:
    no_needle_html_needle_top = f.read()

with open('italic_needle_html(needle_top).txt') as f:
	italic_needle_html_needle_top = f.read()

with open('bold_needle_html(needle_top).txt') as f:
	bold_needle_html_needle_top = f.read()

with open('underlined_needle_html(needle_top).txt') as f:
	underlined_needle_html_needle_bottom = f.read()

#Needle bottom
with open('no_needle_html(needle_bottom).txt') as f:
    no_needle_html_needle_bottom = f.read()

with open('italic_needle_html(needle_bottom).txt') as f:
	italic_needle_html_needle_bottom = f.read()

with open('bold_needle_html(needle_bottom).txt') as f:
	bold_needle_html_needle_bottom = f.read()

with open('underlined_needle_html(needle_bottom).txt') as f:
	underlined_needle_html_needle_bottom = f.read()
