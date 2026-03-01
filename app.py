from flask import Flask, render_template, request, send_file
from ImageGoNord import GoNord
import time
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    filename = ""
    image_ready = False
    if request.method == "POST":
        for f in ["static/input.jpg", "static/output.jpg"]:
            if os.path.exists(f):
                os.remove(f)        
        print("POST recibido")
        file = request.files["image"]
        print("Archivo:", file.filename)
        filename = file.filename
        file.save(f"static/{filename}")
        print("Guardado")
        go_nord = GoNord()
        image = go_nord.open_image(f"static/{filename}")
        go_nord.convert_image(image, save_path=f"static/output_{filename}") 
        image_ready = True

    return render_template("index.html", filename=filename, image_ready=image_ready, timestamp=int(time.time()))


if __name__ == "__main__":
    app.run(debug=True)
