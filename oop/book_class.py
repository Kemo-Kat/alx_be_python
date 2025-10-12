class Book:
    """
    A class to represent a Book with title, author, and publication year.
    Implements various magic methods for enhanced functionality.
    """
    
    def __init__(self, title, author, year):
        """
        Constructor - initializes a Book instance with title, author, and year.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created successfully!")
    
    def __del__(self):
        """
        Destructor - called when the object is about to be destroyed.
        Prints a deletion message with the book title.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String representation - returns a user-friendly string format.
        
        Returns:
            str: Book information in format "Title by Author, published in Year"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official representation - returns a string that can recreate the object.
        
        Returns:
            str: String that can be used with eval() to recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"










