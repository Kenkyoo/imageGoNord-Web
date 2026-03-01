from flask import Flask, render_template, request, send_file
from ImageGoNord import GoNord
import time
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    image_up = False
    image_ready = False
    if request.method == "POST":
        for f in ["static/input.jpg", "static/output.jpg"]:
            if os.path.exists(f):
                os.remove(f)        
        print("POST recibido")
        file = request.files["image"]
        print("Archivo:", file.filename)
        file.save("static/input.jpg")
        print("Guardado")
        image_up = True
        go_nord = GoNord()
        image = go_nord.open_image("static/input.jpg")
        print("Imagen abierta")
        go_nord.convert_image(image, save_path="static/output.jpg")
        print("Convertida")
        image_ready = True

    return render_template("index.html", image_ready=image_ready, image_up=image_up, timestamp=int(time.time()))


if __name__ == "__main__":
    app.run(debug=True)
