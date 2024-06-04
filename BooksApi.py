# Open Library API
from olclient.openlibrary import OpenLibrary
from pprint import pprint
import olclient.common as common
ol = OpenLibrary()

search_results = ol.Work.get("OL25132735M")
pprint(search_results)
# No possibility to search by Tittle

