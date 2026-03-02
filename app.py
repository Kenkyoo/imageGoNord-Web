from flask import Flask, render_template, request, send_file
from ImageGoNord import GoNord
import time
import os
import glob

app = Flask(__name__)
os.makedirs("static/images", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    filename = ""
    image_ready = False
    if request.method == "POST":
        for f in glob.glob("static/images/*"):
            os.remove(f)        
        print("POST recibido")
        file = request.files["image"]
        print("Archivo:", file.filename)
        filename = file.filename
        file.save(f"static/images/{filename}")
        print("Guardado")
        go_nord = GoNord()
        image = go_nord.open_image(f"static/images/{filename}")
        go_nord.convert_image(image, save_path=f"static/images/output_{filename}") 
        image_ready = True

    return render_template("index.html", filename=filename, image_ready=image_ready, timestamp=int(time.time()))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
