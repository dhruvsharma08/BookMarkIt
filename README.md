# BookMarkIt

**BookMarkIt** is a simple, efficient command-line tool to organize and manage your bookmarks. With **BookMarkIt**, you can store bookmarks across various collections such as **work**, **personal**, or any custom collections you create. Add, modify, delete, and view your bookmarks—all from an interactive CLI interface.

## Features:
- Add, modify, delete, and view bookmarks
- Organize bookmarks in multiple collections
- Automatically creates default collections: **work** and **personal** on first run
- Interactive CLI with simple commands to navigate and manage bookmarks
- View and open bookmarks directly from the command line

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/BookMarkIt.git
   cd BookMarkIt

 BookMarkIt

**BookMarkIt** is a simple, efficient command-line tool to organize and manage your bookmarks. With **BookMarkIt**, you can store bookmarks across various collections such as **work**, **personal**, or any custom collections you create. Add, modify, delete, and view your bookmarks—all from an interactive CLI interface.

## Features:
- Add, modify, delete, and view bookmarks
- Organize bookmarks in multiple collections
- Automatically creates default collections: **work** and **personal** on first run
- Interactive CLI with simple commands to navigate and manage bookmarks
- View and open bookmarks directly from the command line

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/BookMarkIt.git
   cd BookMarkIt
Usage
1. List All Collections
To view all your collections, simply run the script:

   ```bash
   python3 bookmark_manager.py
If it's your first time running the script, BookMarkIt will automatically add the default collections: work and personal.

2. Add a Collection
You can add a new collection using the --collection argument:

   ```bash
   python3 bookmark_manager.py add --collection "new_collection"

3. Add a Bookmark
To add a new bookmark to a specific collection:

   ```bash
   python3 bookmark_manager.py add --collection "work" --title "My Bookmark" --link "http://example.com" --description "A great site"

4. Modify a Bookmark
You can modify an existing bookmark by specifying the collection and index:

   ```bash
   python3 bookmark_manager.py modify --collection "work" --index 1 --title "Updated Title" --link "http://updated-link.com" --description "Updated description"

5. Delete a Bookmark
To delete a bookmark from a collection:

   ```bash
   python3 bookmark_manager.py delete --collection "work" --index 1

6. Open a Bookmark
To open a bookmark in your default browser:

   ```bash
   python3 bookmark_manager.py open --collection "work" --index 1

7. Help
To view all available commands and usage, run:

   ```bash
   python3 bookmark_manager.py --help
This will display a list of commands you can use, such as:

   ```bash
   add: Add a new collection or bookmark
   modify: Modify an existing bookmark
   delete: Delete a bookmark
   open: Open a bookmark in your default browser
   list: List all collections and bookmarks
   --help: Display this help message


Example of Help Command Output:
Running the command python3 bookmark_manager.py --help will show you the following options:

   ```bash
   usage: bookmark_manager.py [-h] [--collection COLLECTION] [--index INDEX]
                           [--title TITLE] [--link LINK]
                           [--description DESCRIPTION] {add, modify, delete, open, list, --help}
   bookmarks manager tool

   positional arguments:
   {add, modify, delete, open, list, --help}
    add                 Add a collection or bookmark
    modify              Modify an existing bookmark
    delete              Delete a bookmark
    open                Open a bookmark in your default browser
    list                List all collections and bookmarks
    --help              Show this help message

optional arguments:
  -h, --help            Show this help message
  --collection COLLECTION, -c COLLECTION
                        The collection name (e.g., work, personal)
  --index INDEX, -i INDEX
                        The index of the bookmark in the collection
  --title TITLE, -t TITLE
                        The title of the bookmark
  --link LINK, -l LINK  The URL of the bookmark
  --description DESCRIPTION, -d DESCRIPTION
                        A brief description of the bookmark

## Contribution
Feel free to fork the repository and submit issues or pull requests. Contributions to enhance or improve the project are always welcome!

