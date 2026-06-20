"""
Retrieve Wikipedia Summary based on formatted query term.
"""
import wikipedia
import warnings

## This handles a warning message that can sometimes occur with wikipedia 
warnings.filterwarnings('ignore') 


def fetch_wikipedia_summary(query_term, file):
    ## Search for article titles related to the query
    try:

        # Replace all spaces in the query_term with underscores ('_')
        formatted_query = query_term.replace(' ', '_')
        # Use wikipedia's search method to search for the query_term
        # Note: Multiple results will be returned in a list, we will only use the first entry. 
        results = wikipedia.search(formatted_query)


        # If there are no results of the search, print to file: "No article found for 'query_term'." and return None.
        if not results:
            file.write(f"No articles found for '{query_term}'\n.")
            return
        
        # Otherwise, print to file: "Searching Wikipedia for 'query_term'..."
        file.write(f"\n\nSearching Wikipedia for '{query_term}'...")

        # Display summary of the result
        # Use wikipedia's summary method to retrieve a summary of the first returned searched result (from above).
        query_summary = wikipedia.summary(results[0])

        # Print to file: "Summary of 'results':"
        # Print to file: 'query_summary'
        file.write(f"\nSummary of '{results[0]}':")
        file.write(query_summary)
        return query_summary  # Return 'query_summary'
    
    except:
        # Print to file: "An issue occured retrieving information for 'query_term'."
        file.write(f"An issue occured retrieving information for {query_term}.\n")