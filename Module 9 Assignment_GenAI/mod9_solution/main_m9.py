"""
Alternate version of main.py which utilizes the API and APOD Classes

"""

import datetime
from apod import APOD
from wiki import fetch_wikipedia_summary
from rag import RAG

def run_rag(date=None):
    if not date:
        date = str(datetime.date.today())

    NASA_API_KEY = "7pfdFUF92KvPV6mxt7OWUX8RVs5pMRiuWDI1E8fg" 

    nasa = APOD(NASA_API_KEY)

    with open("results.txt", "w") as file:
        response = nasa.fetch_apod(date)

        file.write("Original APOD Image Information:\n\n")
        file.write(response['explanation'] + "\n")
        print("Original APOD Image Information:\n")
        print(response['explanation'] + "\n")

        rag = RAG()
        terms = rag.generate_lookup_list(response, file)

        wiki_context = ""
        for term in terms:
            wiki_info = fetch_wikipedia_summary(term, file)
            if wiki_info:
                wiki_context += f"\n\n{term}: {wiki_info}"

        file.write("\n\nRAG Generated Description:\n\n")
        augmented = rag.generate_augmented_description(response, wiki_context)
        file.write(augmented + "\n")

        print("\n\nRAG Generated Description:\n")
        print(augmented + "\n")

        file.write(f"\nLink to this photo:\n")
        if response["hdurl"]:
            file.write(response["hdurl"] + "\n")
            nasa.download_image(response["hdurl"], "nasa_apod_image.jpg")
        else:
            file.write(response["url"] + "\n")
            nasa.download_image(response["url"], "nasa_apod_image.jpg")

if __name__ == "__main__":
    run_rag("2024-12-14")  # change the date to explore different APODs
