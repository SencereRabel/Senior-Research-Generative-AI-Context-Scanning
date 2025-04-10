import cohere
import html_source as hs
import REGEXTest as rt

#sets the api key
co = cohere.ClientV2(
    "VUdY53spW31gB3YZOTXRgNU60vkfXaUfqHEcCqKF"
)

#Text that the AI is expected to scan
document = hs.unedited_html
#the prompt it is expected to answer
needle = "What percent was the NON-GAAP gross margin in quarter 4"

doucment_name=["plain text", "unedited html","needle in bold", "needle italicized", "needle underlined"]
answers = []
counter = 0

for i in range(5):
    counter +=1
    if counter == 1:
        document = rt.cleaned_text
    elif counter == 2:
        document = hs.unedited_html
    elif counter == 3:
        document = hs.bold_needle_html
    elif counter == 4:
        document = hs.italic_needle_html
    elif counter == 5:
        document = hs.underlined_needle_html
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
    print(f"{doucment_name[i]:<{15}}: {answers[i]:<{10}}")
print("="*100)