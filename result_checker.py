import csv

def check_llm_responses(csv_file, search_text=None, prompt_filter=None, document_filter=None, filter_by_search_text=True):
    found_responses = []

    with open(csv_file, mode="r", newline="") as file:
        reader = csv.reader(file)
        current_prompt = None
        for row in reader:
            # Check if the row has at least two columns
            if len(row) < 2:
                continue

            if row[0] == "Prompt":
                current_prompt = row[1]
            elif row[0] == "Document Name" and row[1] == "LLM Response":
                continue  # Skip the header row
            elif current_prompt:
                document_name = row[0]
                llm_response = row[1]

                # Apply filters
                if (prompt_filter is None or prompt_filter == current_prompt) and \
                   (document_filter is None or document_filter == document_name) and \
                   (not filter_by_search_text or (search_text is not None and search_text in llm_response)):
                    found_responses.append((current_prompt, document_name, llm_response))

    return found_responses

csv_file = "Results.csv"
search_text = None#"25,984"
prompt_filter = "What is the value of cash assets in january of 2024"
document_filter = "No Needle"
filter_by_search_text = False  # Set to False to show all responses for the given prompt

found_responses = check_llm_responses(csv_file, search_text, prompt_filter, document_filter, filter_by_search_text)

if found_responses:
    if filter_by_search_text:
        print(f"Responses containing '{search_text}':")
    else:
        print(f"All responses for prompt '{prompt_filter}':")
    for response in found_responses:
        print(f"Document: {response[1]}, Response: {response[2]}")
else:
    if filter_by_search_text:
        print(f"No responses containing '{search_text}' were found.")
    else:
        print(f"No responses for prompt '{prompt_filter}' were found.")
