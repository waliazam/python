from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def render(self):
        pass

class PDFDocument(Document):
    def render(self):
        return f"Rendering PDF: {self.content}"

class WordDocument(Document):
    def render(self):
        return f"Rendering Word: {self.content}"

class MarkdownDocument(Document):
    def render(self):
        return f"Rendering Markdown: {self.content}"

# Creating instances of document subclasses
pdf = PDFDocument("PDF Example")
word = WordDocument("Word Example")
markdown = MarkdownDocument("Markdown Example")

# Rendering documents
print(pdf.render())
print(word.render())
print(markdown.render())
