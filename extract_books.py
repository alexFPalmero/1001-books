#!/usr/bin/env python3
"""
Extract book data from index.html and create a structured JSON file
"""
from bs4 import BeautifulSoup
import json
import re

def parse_books(html_file):
    """Parse HTML file and extract book information"""
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all book items
    book_items = soup.find_all('li', class_='book-item')
    
    books = []
    
    for item in book_items:
        # Extract rank
        rank_elem = item.find('span', class_='book-rank')
        rank_text = rank_elem.text.strip() if rank_elem else ""
        rank = int(re.sub(r'[^0-9]', '', rank_text)) if rank_text else 0
        
        # Extract title
        title_elem = item.find('div', class_='book-title')
        title = title_elem.text.strip() if title_elem else ""
        
        # Extract author
        author_elem = item.find('div', class_='book-author')
        author = author_elem.text.strip() if author_elem else ""
        
        # Extract pages from data-pages attribute
        pages = int(item.get('data-pages', 0))
        
        # Check if book has been read
        read = 'read' in item.get('class', [])
        
        book = {
            "rank": rank,
            "title": title,
            "author": author,
            "pages": pages,
            "read": read
        }
        
        books.append(book)
    
    # Sort by rank to ensure correct order
    books.sort(key=lambda x: x['rank'])
    
    return books

def main():
    html_file = '/home/user/1001-books/index.html'
    output_file = '/home/user/1001-books/books.json'
    
    print(f"Parsing {html_file}...")
    books = parse_books(html_file)
    
    print(f"Found {len(books)} books")
    
    # Write to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully created {output_file}")
    
    # Display some stats
    read_count = sum(1 for book in books if book['read'])
    total_pages = sum(book['pages'] for book in books)
    
    print(f"\nStats:")
    print(f"  Total books: {len(books)}")
    print(f"  Books read: {read_count}")
    print(f"  Total pages: {total_pages:,}")
    
    # Show first few entries as sample
    print(f"\nFirst 3 books:")
    for book in books[:3]:
        print(f"  {book['rank']}. {book['title']} by {book['author']} ({book['pages']} pages, read: {book['read']})")

if __name__ == '__main__':
    main()
