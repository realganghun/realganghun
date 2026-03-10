from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = "1q2w3e4r"

@app.get("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)