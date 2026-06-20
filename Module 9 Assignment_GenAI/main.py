import datetime
from rag import RAG
from apod import APOD
from wiki import fetch_wikipedia_summary

def run_rag(date = "2024-12-14"):
    # 3.a Uses current date by default if no date is provided.
    if date == None:    
        date = datetime.date.today() 
        
    with open("results.txt", "w") as file:
        
        # Step 3.b
        apod = APOD('ELAgLGPJaS2081IZDz6oNGPo3VdAyeCg11pSGbrG') # instantiates the class APOD, using the NASA API Key
        img_data = apod.fetch_apod(date) # retrieves apod info for the given date
        img_explanation = img_data.get("explanation")

        print("Original APOD Image Information:\n")
        print(img_explanation)

        file.write("Original APOD Image Information:\n")
        file.write("\n" + img_explanation + "\n")

        # Step 3.c: RAG class  generates lookup terms
        rag = RAG()
        terms = rag.generate_lookup_list(img_explanation, file)

        # Step 3.d : Gathers Wikipedia summaries
        wiki_text = ""
        for term in terms:
            summary = fetch_wikipedia_summary(term, file)
            if summary:
                wiki_text= wiki_text + term + " " + summary + " "
                

        # Step 3.e Creates RAG Generated decriptions
        title = img_data.get("title", "Unknown Title") # Get the title from NASA data
        augmented_desc = rag.generate_augmented_description(title, img_explanation, wiki_text)

        print("\nRAG Generated Description:\n")
        print(augmented_desc)

        file.write("\nRAG Generated Description:\n")
        file.write(augmented_desc + "\n")

        # Step5: Image handling
        file.write("\nLink to this photo:\n")

        img_link = img_data.get("hdurl") or img_data.get("url")
        file.write(img_link + "\n")

        apod.download_image(img_link, "nasa_apod_image.jpg")
        
def main ():
    run_rag()

if __name__ == "__main__":
    main()
    
    