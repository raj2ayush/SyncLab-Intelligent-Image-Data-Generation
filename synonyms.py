# import requests
# from bs4 import BeautifulSoup

# def get_synonyms(word):
#     url = f"https://www.thesaurus.com/browse/{word}"
    
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Find synonyms from the webpage
#         synonyms = []
#         synonyms_section = soup.find('ul', class_='szYvJSVZyfoDF0zoOQi1')
#         if synonyms_section:
#             synonym_items = synonyms_section.find_all('a', class_='Bf5RRqL5MiAp4gB8wAZa')
#             synonyms = [item.text.strip() for item in synonym_items]
        
#         return synonyms
#     except requests.RequestException as e:
#         print("Error fetching data:", e)
#         return None

# #Example usage
# word = "happy"
# synonyms = get_synonyms(word)
# if synonyms:
#     print(f"Synonyms of '{word}': {', '.join(synonyms)}")
# else:
#     print("Failed to retrieve synonyms.")


import requests
from bs4 import BeautifulSoup

def get_synonyms(word):
    url = f"https://www.thesaurus.com/browse/{word}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find synonyms from the webpage
        synonyms = []
        synonyms_section = soup.find('ul', class_='szYvJSVZyfoDF0zoOQi1')
        if synonyms_section:
            synonym_items = synonyms_section.find_all('a', class_='Bf5RRqL5MiAp4gB8wAZa')
            synonyms = [item.text.strip() for item in synonym_items]
        
        return synonyms
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return None

def get_synonyms_for_phrase(phrase):
    words = phrase.split()
    synonyms_for_phrase = {}
    for word in words:
        synonyms = get_synonyms(word)
        synonyms_for_phrase[word] = synonyms
    return synonyms_for_phrase

# Example usage
# phrase = "happy faces"
# synonyms_for_phrase = get_synonyms_for_phrase(phrase)
# for word, synonyms in synonyms_for_phrase.items():
#     if synonyms:
#         print(f"Synonyms of '{word}': {', '.join(synonyms)}")
#     else:
#         print(f"Failed to retrieve synonyms for '{word}'.")
