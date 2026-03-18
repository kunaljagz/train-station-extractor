import openai

class LLMExtractor:
    def __init__(self, api_key):
        openai.api_key = api_key

    def extract_data(self, diagram_text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Extract structured data from the following train station diagram text: {diagram_text}"}
            ]
        )
        return response['choices'][0]['message']['content']

if __name__ == '__main__':
    api_key = 'your_openai_api_key_here'
    llm_extractor = LLMExtractor(api_key)
    diagram_text = "Sample text from train station diagram."
    structured_data = llm_extractor.extract_data(diagram_text)
    print(structured_data)