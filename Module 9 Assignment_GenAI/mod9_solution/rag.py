"""
Class which is the basic solution for a RAG AI solution
"""

from ollama import chat

class RAG:
    def __init__(self, model="llama3.2"):
        self.model = model

    def rag_response(self, prompt):
        response = chat(model=self.model, messages=[{'role': 'user', 'content': prompt}])
        result = response['message']['content']
        return result

    def generate_lookup_list(self, apod_data, file):
        lookup_prompt = f"""Analyze the following and based on the information provided, create a list of terms to look-up for more information. The list should be returned as a list of strings in python format. No other information should be returned. Information: {apod_data['explanation']}"""
        result = self.rag_response(lookup_prompt)

        terms = []
        for item in result.strip('[]').split(','):
            clean_item = item.strip().strip('"')
            terms.append(clean_item)

        file.write(f"\nAdditional Search Terms:\n")
        for term in terms:
            file.write(f"\u2022 {term}\n")
        return terms

    def generate_augmented_description(self, apod_data, wiki_context):
        rag_prompt = f"""
        NASA APOD Title: {apod_data['title']}
        Explanation: {apod_data['explanation']}

        Additional Context from Wikipedia:
        {wiki_context}

        Write a more detailed and accessible description of the image using all of the above.
        """
        return self.rag_response(rag_prompt)
