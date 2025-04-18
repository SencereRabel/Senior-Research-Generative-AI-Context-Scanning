import cohere
import html_source as hs
import HTML_Cleaner as hc
# Fetch key
with open('/Users/senrabel/Desktop/Key.txt') as f:
    key = f.read()

# Sets the API key
co = cohere.ClientV2(key)

# Text that the AI is expected to scan
document = ""

def call_ai(document, needle):
    response = co.chat(
        model="command-a-03-2025",
        messages=[
            {
                "role": "system",
                "content": f"Your goal is to help users find information within a string of text. When prompted with a question your answer must be a numerical value, \
                it should not have any characters that aren't numbers. If the information is not in the string of text just say the phrase 'Needle not found.' \
                The string of text you will be searching is {document} \
                To summarize you will check a string text and give a response to a question asked but the response must be a number.",
            },
            {
                "role": "user",
                "content": f"How many days are in october",
            },
            {
                "role": "assistant",
                "content": "31",
            },
            {
                "role": "user",
                "content": f"Find the answer to the the following question:{needle}",
            },
        ],
    )
    return response.message.content[0].text

def run_test(needle, test):
    document_name = []
    answers = []
    counter = 5

    # Run test for test 1
    if test == 1:
        for i in range(6):
            counter += 1
            if counter == 1:
                document = hc.clean_page()
                document_name.append('Plaintext')
            elif counter == 2:
                document = hs.unedited_html
                document_name.append('Unedited HTML')
            elif counter == 3:
                document = hs.bold_needle_html_needle_top
                document_name.append('Needle Bold')
            elif counter == 4:
                document = hs.italic_needle_html_needle_top
                document_name.append('Needle Italic')
            elif counter == 5:
                document = hs.underlined_needle_html_needle_top
                document_name.append('Needle Underlined')
            elif counter == 6:
                document = hs.no_needle_html_needle_top
                document_name.append('No Needle')

            # Make the AI call for each iteration
            llmResponse = call_ai(document, needle)
            answers.append(llmResponse)

    # Run test for test 2
    elif test == 2:
        for i in range(1):
            counter += 1
            if counter == 1:
                document = hc.clean_page()
                document_name.append('Plaintext')
            elif counter == 2:
                document = hs.unedited_html
                document_name.append('Unedited HTML')
            elif counter == 3:
                document = hs.bold_needle_html_needle_bottom
                document_name.append('Needle Bold')
            elif counter == 4:
                document = hs.italic_needle_html_needle_bottom
                document_name.append('Needle Italic')
            elif counter == 5:
                document = hs.underlined_needle_html_needle_bottom
                document_name.append('Needle Underlined')
            elif counter == 6:
                document = hs.no_needle_html_needle_bottom
                document_name.append('No Needle')

            # Make the AI call for each iteration
            llmResponse = call_ai(document, needle)
            answers.append(llmResponse)


    with open("Results.txt", "a") as f:
        print("=" * 100)
        f.write("=" * 100 + "\n")
        print(f"Prompt: {needle}")
        f.write(f"Prompt: {needle}\n")
        for i in range(len(answers)):
            print(f"{document_name[i]:<{15}}: {answers[i]:<{10}}")
            f.write(f"{document_name[i]:<{15}}: {answers[i]:<{10}}\n")
            print("-" * 100)