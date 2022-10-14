from flask import Flask, render_template
import random
app = Flask(__name__)

# list of cat images
images = [
    "https://i.imgur.com/l8z9eSB.jpg",
    "https://i.imgur.com/Jl8Do1Y.jpg",
    "https://i.imgur.com/Ju9yXPd.jpg",
    "https://i.imgur.com/P1Ojt9b.jpg",
    "https://i.imgur.com/WFb3nlW.jpg",
    "https://i.imgur.com/xCUUanC.jpg",
    "https://i.imgur.com/eKRRRNj.jpg"
]
@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")