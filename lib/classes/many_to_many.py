class Article:
    all = []  

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str) or not 5 <= len(title) <= 50 or hasattr(self, "_title"):
            raise ValueError('Title must be be string between 5 and 50 characters.')
        self._title = title

    @property
    def author(self):
        return self._author

        
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be of type Author.")
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = magazine

        
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not (2 <= len(name) <= 30) or hasattr(self, "_name"):
            raise ValueError("Name must be string between 2 and 30 characters.")
        self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        if self.articles():
            return list({article.magazine.category for article in self.articles()})
        else:
            return None


class Magazine:
    all =[]

    def __init__(self, name, category):
        
        self.name = name
        self.category = category
        type(self).all.append(self)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not (2 <= len(name) <= 16) or not isinstance(name, str):
            raise ValueError("Name must be string between 2 and 16 characters.")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str) or  len(category) < 1:
            raise TypeError("Category must be a string")
        self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        return list({article.author for article in self.articles()})

    def add_article(self, author, title):
        return Article(author, self, title)
    
    def article_titles(self):
        return ([article.title for article in self.articles()] if self.articles() else None)
    
    def contributing_authors(self):
        author_article_count = {}
        for article in self.articles():
            if article.author in author_article_count:
                author_article_count[article.author] += 1
            else:
                author_article_count[article.author] = 1

        contributing_authors = [author for author, count in author_article_count.items() if count >= 3]
        
        return contributing_authors if contributing_authors else None
    
    #bonus deliverable
    @classmethod
    def top_publisher(self):
        magazine_article_count = {}
        for article in Article.all:
            if article.magazine in magazine_article_count:
                magazine_article_count[article.magazine] += 1
            else:
                magazine_article_count[article.magazine] = 1
    
        return max(magazine_article_count, key=magazine_article_count.get) if magazine_article_count else None

