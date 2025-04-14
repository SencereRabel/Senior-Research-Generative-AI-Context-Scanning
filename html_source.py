
needle = "What percent was the NON-GAAP gross margin in Q4 FY25"

with open('Unedited_html.txt') as f:
    unedited_html = f.read()

with open('italic_needle_html.txt') as f:
	italic_needle_html = f.read()

with open('bold_needle_html.txt') as f:
	bold_needle_html = f.read()

with open('underlined_needle_html.txt') as f:
	underlined_needle_html = f.read()
