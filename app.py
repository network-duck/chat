from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder=".")

@app.route("/", methods=["GET", "POST"])
def home():
    # POST: save the submitted message
    if request.method == "POST":
        
        message = request.form.get("message", "").strip()

        if message:
            with open("messages.txt", "a") as file:
                file.write(message + "\n")

        return redirect("/")
    
    # GET: read all messages
    with open("messages.txt", "r") as file:
        messages = file.read().splitlines()
    
    return render_template("index.html", messages=messages)

app.run()