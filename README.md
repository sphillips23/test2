# Library of books

Basic Python Flash web application where users can track the books they own and have read. 

---

# Sarah Phillips and Beth Tiggelaar

Our application keeps track of the books added to our library. It inlcudes the title, author, pages, classification, details, and acquisition information for each book added. There is also an About page that can be accessed through a link at the top of the page with the names and a picture of the application creators. This project is a part of our Digital Product Management class. 

---

## Instructions for running the application

1. Clone this repository to local computer

2. Create a new virtual environment

   - Windows: `python -m venv ./venv`
   - Mac: `python3 -m venv ./venv`

3. Activate the new virtual environment

   - Windows: `.\venv\Scripts\activate`
   - Mac: `source ./venv/bin/activate`

4. Install the dependencies `pip install -r requirements.txt`

5. Run the program using either:

   - `flask run`
   - `python app.py`

6. Use the application by visiting the URL in your web browser


### TO-DO

- [x] Catch all selected activities in /add and put them into the list
- [x] About page
- [ ] Styling using Bootstrap 5 framework
- [ ] Custom error messages
- [ ] Flash messages
- [ ] API



