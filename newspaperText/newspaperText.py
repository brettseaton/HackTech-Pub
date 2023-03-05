import openai
import os
# Function to generate multiple choice questions with one correct answer
def generate_summary(article_text):
    # Set up OpenAI API parameters
    prompt = f"Generate a summary sentence of the following article, emphasizing the articles relationship to the environment: \n{article_text}\n\nSummary:"
    model = "text-davinci-003"
    temperature = 0.5
    max_tokens = 1500
    n = 1
    stop = "\n\n"

    # Use OpenAI API to generate questions
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=n,
        stop=stop
    )
    summary = response.choices[0].text.strip()
    return summary

def generate_label(summary_text):
    prompt = f"Label the following summary of an article as either 'High Environmental Sustainability' or 'Low Environmental Sustainability' or 'Not Related to Environmental Sustainability'\n {summary_text}\n\n"
    # Parse the response and return questions
    model = "text-davinci-003"
    temperature = 0.5
    max_tokens = 1500
    n = 1
    stop = "\n\n"
    
    
    # Use OpenAI API to generate labels
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=n,
        stop=stop
    )
    label= response.choices[0].text.strip()
    return label

def main():
    
    # parser = argparse.ArgumentParser(description="Input article text string.")
    # parser.add_argument("--text", metavar="input", type=str, help="input article text string")
    # args = parser.parse_args()
    # Set up OpenAI API key
    openai.api_key = "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"

    # Get article link from user
    folder_path = "/Users/BrettSeaton/Desktop/newspaperText/articles"

    for filename in os.listdir(folder_path):
        # Generate summary
            generatedSummary = generate_summary(filename)
            # Generate labels
            generatedLabels = generate_label(generatedSummary)

            print(generatedLabels)
    # Print the questions
    # for i in generatedLabels:
    #     QCA["Label"] = generatedLabels[i]
    # output.append(QCA)
    # QCA = {}
    
    # print(output)
    
    # return output

main()