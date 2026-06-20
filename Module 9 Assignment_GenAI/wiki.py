import wikipedia
import warnings

## Handles warning message that can occur with wikipedia
warnings.filterwarnings('ignore')

def fetch_wikipedia_summary(query_term, file):
    try:                
        #Replaces spaces with underscores ('_')
        new_term = ""
        for i in query_term:
            if i == " ":
                new_term = new_term + "_"
            else:
                new_term = new_term + i
        query_term = new_term  

        results = wikipedia.search(query_term)  #Use wikipedia's search method to search for the term in query_term

#If there are no results of the search, print to file: "No article found for 'query_term'". and return None.
        if results == None:      
            file.write("No articles found for "+ query_term + ".\n")
            return None
        
# Otherwise, print to file: "Searching Wikipedia for 'query_term'..."
        else:
            file.write("\n" + "Searching Wikipedia for "+ query_term+ "..."+"\n")
        #Displays summary result
        
        first_result = results[0] # sliced the first result from the list in results.
        query_summary = wikipedia.summary(first_result) #Use wikipedia's summary method to retrieve a summary of the first returned searched result

        file.write("Summary of "+ first_result +": ")
        file.write(query_summary + "\n")

        return query_summary

    except:
        file.write(f"An issue occurred retrieving information for {query_term}.\n")






