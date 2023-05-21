class Book:
    def __init__(self, title, page_count, publication_year=None):
        self.title = title
        self.page_count = page_count
        self.publication_year = publication_year

    def get_title(self):
        return self.title

    def get_page_count(self):
        return self.page_count

    def get_publication_year(self):
        return self.publication_year





