import argparse
import json
import os
import webbrowser
import re

# Path where bookmarks will be stored
BOOKMARKS_FILE = 'bookmarks.json'

# Function to load bookmarks from the file
def load_bookmarks():
    if os.path.exists(BOOKMARKS_FILE):
        with open(BOOKMARKS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save bookmarks to the file
def save_bookmarks(bookmarks):
    with open(BOOKMARKS_FILE, 'w') as file:
        json.dump(bookmarks, file, indent=4)

# Function to validate collection name (only alphabets and underscores allowed)
def is_valid_collection_name(name):
    return bool(re.match(r'^[A-Za-z_]+$', name))

# Function to display all collections
def list_collections():
    bookmarks = load_bookmarks()

    if not bookmarks:
        print("\033[93mNo collections found. Adding default collections...\033[0m")
        add_default_collections()
        return

    print("\033[1mCollections available:\033[0m")
    for idx, collection_name in enumerate(bookmarks.keys(), 1):
        print(f"\033[94m{idx}. {collection_name}\033[0m")  # Blue for collection names

    print("\033[92ma. Add new collection\033[0m")
    print("\033[92mm. Modify a collection\033[0m")
    print("\033[92md. Delete a collection\033[0m")
    print("\033[93mb. Back\033[0m")
    print("\033[91mq. Quit\033[0m")

    choice = input("\033[1mSelect a collection (number), add (a), modify (m), delete (d), back (b), or quit (q): \033[0m")

    if choice == 'q':
        exit()
    elif choice == 'b':
        return
    elif choice == 'a':
        add_collection()
    elif choice == 'm':
        modify_collection()
    elif choice == 'd':
        delete_collection()
    elif choice.isdigit() and 1 <= int(choice) <= len(bookmarks):
        selected_collection = list(bookmarks.keys())[int(choice) - 1]
        list_bookmarks(selected_collection)
    else:
        print("\033[91mInvalid choice, please try again.\033[0m")
        list_collections()

# Function to display bookmarks in a collection
def list_bookmarks(collection_name):
    bookmarks = load_bookmarks()

    if collection_name not in bookmarks:
        print(f"\033[91mNo collection named '{collection_name}' found.\033[0m")
        return

    collection_bookmarks = bookmarks[collection_name]
    print(f"\n\033[1mBookmarks in collection '{collection_name}':\033[0m")

    print(f"\033[94m{'Index':<5} {'Title':<30} {'Link':<40} {'Description':<50}\033[0m")
    print("-" * 130)
    for idx, bookmark in enumerate(collection_bookmarks, start=1):
        print(f"{idx:<5} {bookmark['title']:<30} {bookmark['link']:<40} {bookmark['description']:<50}")

    print("\n\033[92ma. Add new bookmark\033[0m")
    print("\033[92mm. Modify a bookmark\033[0m")
    print("\033[92md. Delete a bookmark\033[0m")
    print("\033[93mb. Back\033[0m")
    print("\033[91mq. Quit\033[0m")

    choice = input("\033[1mSelect a bookmark to open (number), add (a), modify (m), delete (d), back (b), or quit (q): \033[0m")

    if choice == 'q':
        exit()
    elif choice == 'b':
        list_collections()
    elif choice == 'a':
        add_bookmark(collection_name)
    elif choice == 'm':
        modify_bookmark(collection_name)
    elif choice == 'd':
        delete_bookmark(collection_name)
    elif choice.isdigit() and 1 <= int(choice) <= len(collection_bookmarks):
        open_bookmark(collection_name, int(choice) - 1)
    else:
        print("\033[91mInvalid choice, please try again.\033[0m")
        list_bookmarks(collection_name)

# Function to open a bookmark in the default web browser
def open_bookmark(collection_name, index):
    bookmarks = load_bookmarks()

    if collection_name not in bookmarks or index < 0 or index >= len(bookmarks[collection_name]):
        print(f"\033[91mInvalid collection or index.\033[0m")
        return

    link = bookmarks[collection_name][index]['link']
    webbrowser.open(link)
    print(f"\033[92mOpening bookmark '{bookmarks[collection_name][index]['title']}'...\033[0m")

# Function to add default collections (work and personal)
def add_default_collections():
    bookmarks = load_bookmarks()

    # Add default collections if not already present
    if "work" not in bookmarks:
        bookmarks["work"] = []
    if "personal" not in bookmarks:
        bookmarks["personal"] = []

    save_bookmarks(bookmarks)
    print("\033[92mDefault collections 'work' and 'personal' added.\033[0m")

    list_collections()

# Function to add a new collection
def add_collection():
    collection_name = input("\033[92mEnter new collection name (alphabets and underscores only): \033[0m")

    if not is_valid_collection_name(collection_name):
        print("\033[91mInvalid collection name. Only alphabets and underscores are allowed.\033[0m")
        return

    bookmarks = load_bookmarks()
    if collection_name in bookmarks:
        print(f"\033[91mCollection '{collection_name}' already exists!\033[0m")
        return

    bookmarks[collection_name] = []
    save_bookmarks(bookmarks)
    print(f"\033[92mCollection '{collection_name}' added.\033[0m")

    list_collections()

# Function to modify an existing collection
def modify_collection():
    bookmarks = load_bookmarks()

    collection_name = input("\033[92mEnter the name of the collection to modify: \033[0m")
    
    if collection_name not in bookmarks:
        print(f"\033[91mCollection '{collection_name}' does not exist.\033[0m")
        return

    new_name = input(f"\033[92mEnter new name for collection '{collection_name}': \033[0m")

    if not is_valid_collection_name(new_name):
        print("\033[91mInvalid collection name. Only alphabets and underscores are allowed.\033[0m")
        return

    if new_name in bookmarks:
        print(f"\033[91mCollection '{new_name}' already exists.\033[0m")
        return

    bookmarks[new_name] = bookmarks.pop(collection_name)
    save_bookmarks(bookmarks)
    print(f"\033[92mCollection '{collection_name}' has been renamed to '{new_name}'.\033[0m")

    list_collections()

# Function to delete a collection
def delete_collection():
    bookmarks = load_bookmarks()

    collection_name = input("\033[92mEnter the name of the collection to delete: \033[0m")

    if collection_name not in bookmarks:
        print(f"\033[91mCollection '{collection_name}' does not exist.\033[0m")
        return

    del bookmarks[collection_name]
    save_bookmarks(bookmarks)
    print(f"\033[92mCollection '{collection_name}' has been deleted.\033[0m")

    list_collections()

# Function to add a bookmark to a collection
def add_bookmark(collection_name):
    bookmarks = load_bookmarks()

    title = input("\033[92mEnter bookmark title: \033[0m")
    link = input("\033[92mEnter bookmark link: \033[0m")
    description = input("\033[92mEnter bookmark description: \033[0m")

    if collection_name not in bookmarks:
        bookmarks[collection_name] = []

    bookmark = {
        'title': title,
        'link': link,
        'description': description
    }

    bookmarks[collection_name].append(bookmark)

    # Sort bookmarks by title
    bookmarks[collection_name] = sorted(bookmarks[collection_name], key=lambda x: x['title'])

    save_bookmarks(bookmarks)
    print(f"\033[92mBookmark '{title}' added to collection '{collection_name}'.\033[0m")

    list_bookmarks(collection_name)

# Function to modify a bookmark in a collection
def modify_bookmark(collection_name):
    bookmarks = load_bookmarks()

    if collection_name not in bookmarks:
        print(f"\033[91mCollection '{collection_name}' does not exist.\033[0m")
        return

    collection_bookmarks = bookmarks[collection_name]

    index = int(input(f"\033[92mEnter the index of the bookmark to modify (1-{len(collection_bookmarks)}): \033[0m")) - 1
    if 0 <= index < len(collection_bookmarks):
        new_title = input(f"\033[92mEnter new title (current: {collection_bookmarks[index]['title']}): \033[0m")
        new_link = input(f"\033[92mEnter new link (current: {collection_bookmarks[index]['link']}): \033[0m")
        new_description = input(f"\033[92mEnter new description (current: {collection_bookmarks[index]['description']}): \033[0m")

        collection_bookmarks[index] = {
            'title': new_title or collection_bookmarks[index]['title'],
            'link': new_link or collection_bookmarks[index]['link'],
            'description': new_description or collection_bookmarks[index]['description']
        }

        save_bookmarks(bookmarks)
        print(f"\033[92mBookmark '{collection_bookmarks[index]['title']}' has been modified.\033[0m")

        list_bookmarks(collection_name)
    else:
        print("\033[91mInvalid bookmark index.\033[0m")

# Function to delete a bookmark in a collection
def delete_bookmark(collection_name):
    bookmarks = load_bookmarks()

    if collection_name not in bookmarks:
        print(f"\033[91mCollection '{collection_name}' does not exist.\033[0m")
        return

    collection_bookmarks = bookmarks[collection_name]

    index = int(input(f"\033[92mEnter the index of the bookmark to delete (1-{len(collection_bookmarks)}): \033[0m")) - 1
    if 0 <= index < len(collection_bookmarks):
        deleted_bookmark = collection_bookmarks.pop(index)
        save_bookmarks(bookmarks)

        # Reindex bookmarks after deletion
        for idx, bookmark in enumerate(collection_bookmarks, start=1):
            bookmark['index'] = idx

        print(f"\033[92mBookmark '{deleted_bookmark['title']}' has been deleted.\033[0m")

        if len(collection_bookmarks) > 0:
            list_bookmarks(collection_name)
        else:
            list_collections()
    else:
        print("\033[91mInvalid bookmark index.\033[0m")

# Function to handle the case when no arguments are passed
def no_arguments():
    print("\nUse \033[92m--help\033[0m to see available commands and their usage.\n")
    list_collections()

# Main function to handle arguments
def main():
    parser = argparse.ArgumentParser(description="Bookmark Manager")

    parser.add_argument(
        'command', choices=['add', 'modify', 'delete', 'open', 'list', '--help'],
        help="Command to perform on bookmarks",
        nargs='?'  # Make the command optional
    )
    parser.add_argument('--collection', type=str, help="Collection name for the operation")
    parser.add_argument('--index', type=int, help="Index of the bookmark")
    parser.add_argument('--title', type=str, help="Title of the bookmark")
    parser.add_argument('--link', type=str, help="Link of the bookmark")
    parser.add_argument('--description', type=str, help="Description of the bookmark")

    args = parser.parse_args()

    if args.command is None:
        no_arguments()
        return

    if args.command == '--help':
        print(parser.format_help())
        return

    if args.command == 'add':
        if args.collection:
            add_bookmark(args.collection)
        else:
            print("\033[91mPlease provide a collection name with --collection.\033[0m")
    elif args.command == 'modify':
        modify_bookmark(args.collection)
    elif args.command == 'delete':
        delete_bookmark(args.collection)
    elif args.command == 'open':
        open_bookmark(args.collection, args.index)
    elif args.command == 'list':
        list_bookmarks(args.collection)

if __name__ == "__main__":
    main()
