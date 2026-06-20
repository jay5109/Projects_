
Name: Jeremy Perez (jperez64)
Module 9: Assignment: Generative Artificial Intelligence
	Due: 03/29/2026 at 11:59 PM

Approach:

- main.py
Imported the datetime library, the class RAG() from rag.py, the class APOD() from apod.py and fetch_wikipedia_summary from wiki.py. 
Defined the run_rag method with the argument date and the given date in string format. Used conditional if statements to use current date if no date is provided. The if statement compares the value for date with None. If true, it will then use datetime library and invoke the today() function to capture the current date and store into the variable date. Opened a text file called "results.txt" to write.

Instantiated the APOD class from api.py to pass my generated api key as a string and stored into apod. Next called the method fetch_apod with argument date and stores result into the variable, img_data. Then prints explanation results to the terminal and the results.txt. Then initialized the class rag in the variable rag. Referenced the variable rag with the method generate_lookup_list() and the arguments img_explanation and file. Created an empty variable, wiki_text, to hold the generate info from Wikipedia. 

A for loop is used to iterated through each term. Then invokes the fetch_wikipedia_summary method from wiki.py with arguments term and file and stored in the variable summary. Using an if statement, checks if there is a summary and if there is, it appends the term, an empty space, the summary and another empty space to empty variable wiki_text. To get the title, used get("title", "Unknown Title") method and referenced the img_data and stored into the variable title. Then used the generate_augmented_description() method with the arguments (title, img_explanation, wiki_text). Referenced the rag class from the varaible rag and stored the augmented descriptions in the variable "augmented_desc". 

Then prints the string "RAG Generated Description"  along with the results in augmented_desc in the terminal and the results.txt file using two file.write() for the string, the variable and newline to match outputs. To retrieved the APOD photo, first printed the string "Link to this photo: " to the text file. Then use logical OR  and the get() function to retrieve the hdurl or the url of the image and stored in the variable img_link. 

Then printed the linked to results.txt. lastly using the download_image() method from class APOD, I saved the image as "nasa_apod_image.jpg". Lastly, defined the main() method and called the run_rag() method. Used the dunder method __name__ == "__main__" to only run the main() function in the module main.py.


- rag.py
Imported the class APOD from apod.py, chat from Ollama

Created the class RAG with the constructor that takes argument model = "llama3.2" and defines model as the instance variable, self.model.

Contains the method rag_response with argument prompt to accept strings. to send information to the LLM, I followed the Usage format from ollama-python README.md: 

response = chat(model= self.model, messages=
            {
                'role': 'user',
                'content': prompt
                }
            ])
returned response['message']['content']

* Tells the LLM which model to use, using a user to submit a prompt and returns its response.

Contains the method generate_lookup_list, with arguments photo_explaination and file. Contains lookup_prompt with the given prompt and concatenated photo_explaination variable converted as a string. then called  the method rag_response with lookup_prompt and stored into "result".
Then converted the string in result as a list of strings where each string is a search term.
	- First used the split() function to split each by commas from "result" and stored into "split_results".
	- Created an empty list, terms and 
	- Used a for loop to use the strip() function and remove whitespaces and [] and then appends to the empty list.

Then wrote to the file result.txt, creating a header for the search terms then a newline('\n'). Then used a for-loop to iterate through each term in the list terms, adding a bullet point using the escape code \u2022 then concatenated the term and a newline. Returns the list terms, to the txt file. Contains the method generate_augmented_description with arguments, photo_title, photo_explanation and summary_wiki_content. The variable rag_prompt contains the given prompt for rag_prompt, with concatenated arguments and a newline. Then invoked the rag_response method with rag_prompt and returned the results of self.rag_response(rag_prompt).


- wiki.py
Used the provided file wiki.py. In the method fetch_wikipedia_summary(query_term,file) included the empty variable, new_term . Then a for-loop to iterate through each item , i, in query_term. Then a nested if and else statement; to check if "i" is a space, if so it will add an underscore to new_term. Otherwise adds i to new_term. Returned the result of the loop to the variable query_term.  In the variable results, called the search method from the wikipedia library and search for the term with argument query_term.

An if statement compares the results to None. If there are no results, writes the string "No articles found for ", concatenated the term in query_term and a newline in results.txt. Otherwise performs the else statement; writes a newline, the given string "Searching Wikipedia for " and  concatenated query term in results.txt. Then sliced results at index 0 for the first searched result and store into the variable first_result. Using wikipedia's summary method, passed the argument first_result to retrieve a summary of the searched result and stored into the variable query_summary. Then wrote the given string "Summary of" and concatenated the first_result and the result of query_summary to results.txt. 


- api.py
Imported the request library. Created the class API, a constructor with instance variables API_KEY and NASA_URL.
Defined the method get_response with argument params. This method sends a get request to nasa url using the api key in params and returned response in json format.


- apod.py
Imported the class API from the module api.py and the requests library.
Created the child class APOD to the parent class API and a constructor with instance variable API_KEY. Stored the NASA link in the variable "url". Used the super() method to inherit the API_KEY and NASA_URL from class API's constructor. Defined the method fetch_apod to take the date as string through params and call the get_response method from class API and returns the response in json format.

Defined the method download_image with arguments url, and filename.
Used get response to download the img from the link in url and stored result in the variable response. Used an if statement to check if the status code is 200. If so, prints the given string along with the filename else, prints the status code of response and the given string.


Known Bugs: If main.py is executed multiple times, the result.txt file may print bits of my code where the "Additional Search Terms:" are listed. 




 

