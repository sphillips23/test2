from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)

app.config.update(
    SECRET_KEY = '5647826548275846254896548927548932'
)

books_dict = [
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "pages": "295", "classification": "fiction", "details":"read, recommend","acquisition":"library" }
]

# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="My Library", books=books_dict
    )


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        title = form["title"]
        author = form["author"]
        pages = form["pages"]
        classification = form["classification"]
        details = form.getlist("details")
        acquisition = form["acquisition"]

        print(title)
        print(author)
        print(pages)
        print(classification)
        print(details)
        print(acquisition)
        

        details_string = ", ".join(details)

        add_book_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "classification": classification,
            "details": details_string,
            "acquisition": acquisition,
        }
        print(add_book_dict)
        books_dict.append(
            add_book_dict
        )
        print(books_dict)

        flash('Success', category='success')

        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    
@app.route("/about", methods=["GET"])
def about():
    return render_template(
        "about.html", pageTitle="About My Library"
    )
    
if __name__ == "__main__":
    app.run(debug=True)



