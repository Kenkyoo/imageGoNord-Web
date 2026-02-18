from flask import Flask, render_template, request, send_file
from ImageGoNord import GoNord

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    image_ready = False

    if request.method == "POST":
        file = request.files["image"]
        file.save("input.jpg")

        go_nord = GoNord()
        image = go_nord.open_image("static/input.jpg")
        go_nord.enable_avg_algorithm()
        go_nord.convert_image(image, save_path="static/output.jpg")

        image_ready = True

    return render_template("index.html", image_ready=image_ready)


if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
