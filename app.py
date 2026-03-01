from flask import Flask, render_template, request, send_file
from ImageGoNord import GoNord
import time

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    image_ready = False
    if request.method == "POST":
        print("POST recibido")
        file = request.files["image"]
        print("Archivo:", file.filename)
        file.save("static/input.jpg")
        print("Guardado")
        go_nord = GoNord()
        image = go_nord.open_image("static/input.jpg")
        print("Imagen abierta")
        go_nord.convert_image(image, save_path="static/output.jpg")
        print("Convertida")
        image_ready = True

    return render_template("index.html", image_ready=image_ready, timestamp=int(time.time()))


if __name__ == "__main__":
    app.run(debug=True)
