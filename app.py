from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/recruit")
def recruit():
    return render_template("recruit.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/inquiry")
def inquiry():
    return render_template("inquiry.html")


@app.route("/greeting")
def greeting():
    return render_template("greeting.html")

if __name__ == "__main__":
    app.run(debug=True)
