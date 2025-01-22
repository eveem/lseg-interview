from flask import Flask, render_template

app = Flask(__name__)

dogs = [
    { "name": "Lunar", "image": "lunar.jpg" },
    { "name": "Solar", "image": "solar.jpg" },
    { "name": "Stellar", "image": "stellar.jpg" },
]

current_dog_index = 0

@app.route("/")
def home():
    global current_dog_index
    dog = dogs[current_dog_index]
    current_dog_index = (current_dog_index + 1) % len(dogs)
    return render_template("index.html", dog_name=dog["name"], dog_image=dog["image"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)