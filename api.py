from azure.storage.blob import ContentSettings
from flask import Flask, jsonify, request, render_template, make_response, redirect
import os, library, predict

app = Flask(__name__, template_folder='template')
# vendi ku ruhet fotoja qe mar nga arbri
app.config["imageUpload"] = "/home/ev/Downloads/Hackathon/ViaEgnatia2.0Hackathon-main/Arbri"

MY_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=viaegnatia20;AccountKey=5q2myTqtPWSaS9OUwta5Woc0opbWgaaOluLHAOa7tiqjiXsDq2sFCqAmoFaJc5tPk/Z+8SaYmgyulgKB6Vk3ng==;EndpointSuffix=core.windows.net"
MY_IMAGE_CONTAINER = "egnatia20"


# http://127.0.0.1:5000/upload ktu do uploadohet fotoja
@app.route("/upload", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image)
            image.save(os.path.join(
                app.config["imageUpload"], image.filename))
        return redirect(request.url)
    return render_template("upload.html")


def upload_language():
    if request.method == "POST":
        if request.files:
            language = request.argc.get("language")
            return language


# http://127.0.0.1:5000/getData ktu do meren te dhenat
# Name is the img name gotten from the predict class
def upload_newpicture(self, name):
    # Create blob with same name as local file name
    blob_client = self.blob_service_client.get_blob_client(container=MY_IMAGE_CONTAINER,
                                                           blob=name)
    # Get full path to the file
    upload_file_path = 'dataset/images/Church of Saint Mary in Apollonia/fr_arc_apollonia_07-1536x864.jpg'

    # Create blob on storage
    # Overwrite if it already exists!
    image_content_setting = ContentSettings(content_type='image/jpeg')
    print(f"uploading file - {name}")
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True, content_settings=image_content_setting)
    return name


# Method to get the description of the picture
def get_description():
    if request.method == "GET":

        for n in library.dbplaces:
            # predict.label should be the label returned form the predict class
            if predict.label == n["label"]:
                # if language != "en":
                #     totranslate.translate(n[description], upload_language)
                #     return

                return n["description"]

        response = make_response(

            jsonify(
                {
                    # Label is the label declared in the dummy db library
                    "Label": library.dbplaces["label"],
                    # Image is the image that gets returned to the user interface
                    "Image": predict.image,
                    "Voice": "bla bla bla bla",
                    # Description gotten from dummy db
                    "Description": library.dbplaces["description"]
                }
            ),
        )
    return response


if __name__ == '__main__':
    app.run(debug=True)
