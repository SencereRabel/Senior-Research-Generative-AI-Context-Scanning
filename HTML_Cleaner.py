
import html_source as hs
from bs4 import BeautifulSoup

def clean_page():
    html_content = hs.unedited_html

    soup = BeautifulSoup(html_content, 'html.parser')

    # Get all text from the entire document
    all_text = soup.get_text()
    # Split the text into lines and remove leading/trailing white space from each line
    lines = [line.strip() for line in all_text.splitlines()]
    # Join the lines back together with a single space separating them
    cleaned_text = ' '.join(lines)

    # Optionally, you can remove multiple spaces between words
    cleaned_text = ' '.join(cleaned_text.split())
    return(cleaned_text)

def print_plaintext():
    cleaned_text = clean_page()
    
    print("="*100)
    print("All Text:")
    print("-"*75)
    print(cleaned_text)
    print("="*100)
    