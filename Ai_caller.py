import cohere
import html_source as hs
import HTML_Cleaner as hc

#fetch key
with open('/Users/senrabel/Desktop/Key.txt') as f:
    key = f.read()
#sets the api key
co = cohere.ClientV2(
    key
)

#Text that the AI is expected to scan
document = ""



def run_test(needle):
    document_name=[]
    answers = []
    counter = 1
    for i in range(2):
        counter +=1
        if counter == 1:
            document = hc.clean_page()
            document_name.append('Plaintext')
        elif counter == 2:
            document = hs.unedited_html
            document_name.append('Unedited HTML')
        elif counter == 3:
            document = hs.bold_needle_html
            document_name.append('Needle Bold')
        elif counter == 4:
            document = hs.italic_needle_html
            document_name.append('Needle Italic')
        elif counter == 5:
            document = hs.underlined_needle_html
            document_name.append('Needle Underlined')
        response = co.chat(
            model="command-a-03-2025",
            messages=[
                {
                    "role": "system",
                    "content": f"Your goal is to help users find information within a string of text. When prompted with a question your answer must be a numerical value, \
                    it should not have any characters that aren't numbers. The string of text you will be searching is {document} \
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
        llmRespone = response.message.content[0].text
        answers.append(llmRespone)

    print("="*100)
    print(f"Prompt: {needle}")
    for i in range(len(answers)):
        print(f"{document_name[i]:<{15}}: {answers[i]:<{10}}")
        print("-"*100)
