from flask import Flask, request

app = Flask(__name__)

# -------------------------
#  HOME PAGE HTML + CSS
# -------------------------
home_page = """
<!DOCTYPE html>
<html>
<head>
    <title>My Portfolio</title>
    <style>
        body { font-family: Arial; margin: 0; background: #f5f5f5; }
        header { background: #0078d7; padding: 20px; color: white; text-align: center; }
        nav a { color: white; margin: 0 10px; text-decoration: none; font-size: 18px; }
        section { padding: 20px; margin: 20px; background: white; border-radius: 8px; }
        .project-card { background: #e2e2e2; padding: 15px; border-radius: 8px; margin-top: 10px; }
        footer { text-align: center; padding: 10px; background: #0078d7; color: white; margin-top: 20px; }
    </style>
</head>

<body>

<header>
    <h1>Welcome to My Portfolio</h1>
    <nav>
        <a href="/">Home</a>
        <a href="/contact">Contact</a>
    </nav>
</header>

<section>
    <h2>Hello, I'm Divya</h2>
    <p>A passionate learner and developer!</p>
</section>

<section>
    <h2>Skills</h2>
    <ul>
        <li>Python</li>
        <li>Flask</li>
        <li>HTML & CSS</li>
    </ul>
</section>

<section>
    <h2>My Projects</h2>

    <div class="project-card">
        <h3>Campus Navigation Assistant</h3>
        <p>An interactive map for college navigation.</p>
    </div>

    <div class="project-card">
        <h3>To-Do List App</h3>
        <p>A simple web application to manage tasks.</p>
    </div>

</section>

<footer>
    © 2025 Divya | All Rights Reserved
</footer>

</body>
</html>
"""


# -------------------------
#  CONTACT PAGE HTML + CSS
# -------------------------
contact_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Contact Me</title>
    <style>
        body { font-family: Arial; margin: 0; background: #f5f5f5; }
        header { background: #0078d7; padding: 20px; color: white; text-align: center; }
        nav a { color: white; margin: 0 10px; text-decoration: none; font-size: 18px; }
        section { padding: 20px; margin: 20px; background: white; border-radius: 8px; }
        input, textarea { width: 98%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #ccc; }
        button { background: #0078d7; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer; }
        footer { text-align: center; padding: 10px; background: #0078d7; color: white; margin-top: 20px; }
    </style>
</head>

<body>

<header>
    <h1>Contact Me</h1>
    <nav>
        <a href="/">Home</a>
        <a href="/contact">Contact</a>
    </nav>
</header>

<section>
    <form method="POST">
        <label>Your Name:</label>
        <input type="text" name="name" required>

        <label>Your Email:</label>
        <input type="email" name="email" required>

        <label>Your Message:</label>
        <textarea name="message" required></textarea>

        <button type="submit">Send</button>
    </form>
</section>

<footer>
    © 2025 Divya | Portfolio
</footer>

</body>
</html>
"""


# -------------------------
#       FLASK ROUTES
# -------------------------

@app.route("/")
def home():
    return home_page

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print("\n--- New Message Received ---")
        print("Name:", request.form.get("name"))
        print("Email:", request.form.get("email"))
        print("Message:", request.form.get("message"))
        print("-----------------------------\n")
        return "<h2>Thank you! Your message has been sent.</h2>"

    return contact_page


# -------------------------
#      RUN APP
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
 