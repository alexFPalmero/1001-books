# 📚 1001 Books You Must Read Before You Die

A curated, interactive list of 1001 essential books from world literature, sorted by page count.

## Overview

This project presents the classic "1001 Books You Must Read Before You Die" list in an interactive web interface, allowing readers to track their progress and explore the collection.

## Files

- **index.html** - Interactive web interface with search, filter, and progress tracking
- **books.json** - Structured data file containing all 1001 books in JSON format
- **extract_books.py** - Python script to extract book data from HTML to JSON

## Features

### Web Interface (index.html)
- 📊 Visual statistics: total books, books read, pages read
- 🔍 Search by title or author
- 🎯 Filter by read/unread status
- 📖 Track reading progress (click on books to mark as read)
- 📱 Responsive design for mobile and desktop
- 🌑 Dark mode interface

### Data File (books.json)
Structured JSON format for easy data manipulation:
```json
{
  "rank": 1,
  "title": "Book Title",
  "author": "Author Name",
  "pages": 100,
  "read": false
}
```

## Statistics

- **Total Books:** 1,001
- **Total Pages:** 384,371
- **Shortest Book:** "El pozo y el péndulo" by Edgar Allan Poe (24 pages)
- **Longest Book:** "Episodios nacionales" by Benito Pérez Galdós (4,600 pages)

## Usage

### View the list
Open `index.html` in any modern web browser.

### Extract data
Run the Python script to regenerate the JSON file:
```bash
python3 extract_books.py
```

### Update progress
Click on any book in the web interface to mark it as read. Progress is saved in browser localStorage.

## Data Structure

Each book entry contains:
- **rank** - Position in the list (1-1001), sorted by page count
- **title** - Book title
- **author** - Author name
- **pages** - Number of pages
- **read** - Reading status (true/false)

## Languages

The book titles and author names are primarily in Spanish.

## License

This is a personal reading tracker based on the popular "1001 Books" list.
