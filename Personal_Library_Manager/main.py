import streamlit as st
import json 

st.set_page_config(page_title="Personal Library", page_icon="📚")
# Streamlit app for managing a personal library
# library ko load krna 
def load_libaray():
    try:
        with open ("library.json","r")as file: # r mtlb read format 
            return json.load(file)
    except FileNotFoundError:
            return []
    
# library ko save karna
def save_library():
    with open("library.json","w")as file:
         json.dump(library,file, indent=4)

# initialized library
library = load_libaray()

st.title("Personal Library 📚")
# Display the library
menu = st.sidebar.selectbox("Select option", ["View Library", "Add Book", "Delete Book", "Search Book"])


if menu == "view Library":
  
    st.sidebar("Your Library")
if library:
     st.table(library)
else:
    st.write("No Books in your library. Add some books to get started! 📖")


# Add book
if menu == "Add Book":
    st.header("Add a new book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=2020, max_value=2025, step=1)
    genre = st.text_input("Genre")
    read_status = st.radio("Read Status", ["Not Read", "Reading", "Read"])


    # Add book
 
    if st.button("Add Book"):
        if title and author and year and genre and read_status:
            # Create a new book entry
            library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
            # Save the updated library
            save_library()
            st.success(f"Book '{title}' added successfully!")
        else:
            st.error("Please fill in all fields.")
            st.rerun()
# Delete book
elif menu == "Delete Book":
    st.subheader("Delete a book")
    book_to_delete = st.selectbox("Select a book to delete", [book["title"] for book in library])
    
    if st.button("Delete Book"):
        if book_to_delete:
            # Find the book in the library and remove it
            library[:] = [book for book in library if book["title"] != book_to_delete]
            # Save the updated library
            save_library()
            st.success(f"Book '{book_to_delete}' deleted successfully!")
        else:
            st.error("Please select a book to delete.")
            st.rerun()





elif menu == "Search Book":
    st.subheader("Search a book 🔍")
    
    # Input from user
    search_term = st.text_input("Enter book title or author name")

    # Initialize result as empty
    result = []

    # Search button
    if st.button("Search"):
        # Perform case-insensitive search
        result = [
            book for book in library
            if search_term.lower() in book['title'].lower()
            or search_term.lower() in book['author'].lower()
        ]

        # Show result
        if result:
            st.success(f"🔎 Found {len(result)} result(s)")
            st.table(result)
        else:
            st.warning("😔 No book found with that title or author.")


# save and exit
elif menu == "save and exit":
    save_library()
    st.success("Library save successfully!")

 
# elif menu == "Search Book":
#     st.subheader("Search a book 🔍")
#     search_term = st.text_input("Search a book title or author name")

#     if st.button('Search'):
#         result = [
#     book for book in library
#     if search_term.lower() in book['title'].lower() 
#     or search_term.lower() in book['author'].lower()
# ]

#     if result:
#      st.table(result)
#     else:
#      st.warning("no book found 😔")



        


