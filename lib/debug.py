#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")
magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture")
Article(author_1, magazine_1, "How to wear a tutu with style")
Article(author_1, magazine_1, "How to be single and happy")
Article(author_1, magazine_1, "Dating life in NYC")
Article(author_1, magazine_2, "Carrara Marble is so 2020")
Article(author_2, magazine_2, "2023 Eccentric Design Trends")

# contributing_authors_vogue = magazine_1.contributing_authors()
# if contributing_authors_vogue:
#     print(f"Contributing authors for {magazine_1.name}:")
#     for author in contributing_authors_vogue:
#         print(f"- {author.name}")

top_magazine = Magazine.top_publisher()
print(f"Top Publisher: {top_magazine.name}")
# don't remove this line, it's for debugging!
ipdb.set_trace()