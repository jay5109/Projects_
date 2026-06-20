from ollama import chat                 # 4.a imports chat from ollama

class RAG:
    def __init__(self, model="llama3.2"):   # 4.b The constructor takes the arugument, LLM model "llama3.2" 
        self.model = model                  # and defined as an instance variable (self.model)

    def rag_response(self, prompt:str):         # 4.c
        response = chat(model= self.model, messages=[
            {
                'role': 'user',
                'content': prompt
                }
            ])
        
        return response['message']['content']
    
    # step 4d.i
    def generate_lookup_list(self, photo_explanation, file):
        lookup_prompt = "Analyze the following and based on the information provided, create a list of terms to look-up for more information. The list should be returned as a list of strings in python format. No other information should be returned. Information: " + str(photo_explanation)
        
    #step 4.d.ii
        result = self.rag_response(lookup_prompt)
        
    #step 4.d.iii: Converts the resulting single string to a list of strings where each string is a search term(s).
        split_results = result.split(",") 
        terms= []
        for i in split_results:  
            terms.append(i.strip(" ").strip('[]')) 
        
        #step 4.d.iiii : Prints to the file results.txt
        file.write("Additional Search Terms:\n")
        for term in terms:  # adds bullet points to before each term  using escape squence\u2022 
            file.write("\u2022" + term + "\n")

        return terms 
    
    #Step 4.e
    def generate_augmented_description(self, photo_title, photo_explanation, summary_wiki_content):
        rag_prompt = "NASA APOD Title: " + photo_title + "\n" + "Explanation: " + photo_explanation + "\n" + "Additional Context from Wikipedia: \n" + summary_wiki_content + "\n" + "Write a more detailed and accessible description of the image using all of the above."
        
        self.rag_response(rag_prompt)
        
        return self.rag_response(rag_prompt)
