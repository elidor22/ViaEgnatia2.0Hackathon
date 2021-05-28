import os
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import Flask, jsonify, request, render_template, make_response, redirect
import boto3
from predict import predict
from flask_cors import CORS, cross_origin
p = predict()

app = Flask(__name__, template_folder='template')
#app.config['CORS_HEADERS'] = '*'
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# Create a directory in a known location to save files to.
uploads_dir = '/home/elidor/uploads/'
results_dir = '/home/elidor/results/'
bucket_name = "ml-experiments"
folder_name = uploads_dir
base_url = 'https://ml-experiments.fra1.digitaloceanspaces.com/images/'


audio_urls = {'english':'https://ml-experiments.fra1.digitaloceanspaces.com/english.wav',
                'german':'https://ml-experiments.fra1.digitaloceanspaces.com/english.wav'}
description = 'The ancient city of Apollonia is situated in southwestern Albania, about 13 miles from the city of Fier. The fascinating landscape of the archeological park, which has been preserved in an exceptionally intact condition, comprises a successful combination between the beauty of monuments and nature, attractive through its long history, in an atmosphere of relaxation and meditation. Its foundation took place immediately after the foundation of Epidamnus – Dyrrachium and quickly became one of the most eminent cities of the Adriatic basin, which was mentioned more frequently from the other 30 (thirty) cities bearing the same name during Antiquity. The city lay in the territory of the political communion of the Taulantii and was broadly known as Apollonia of Illyria. According to the tradition it was founded during the first half of the 6th century BC by Greek colonist from Corfu and Corinth, led by Gylax, which named the city after his name (Gylakeia). After its quick establishment the city changed its name to Apollonia, according to the powerful divinity Apollo. It stands on a hilly plateau from where expands the fertile plain of Musacchia with the Adriatic Sea and the hills of Mallakastra. The ruins of Apollonia are discovered in the beginning of the 19th century.'


session = boto3.session.Session()
s3 = session.client('s3',
                        region_name='fra1',
                        endpoint_url='https://fra1.digitaloceanspaces.com',
                        aws_access_key_id='NS24MAUHRGZ56BDTJRSF',
                        aws_secret_access_key='Z6oz3oxKV47F91gEUoZNorpowqZ9gvLelsPKsfiTAXs')



@app.route('/upload', methods=['POST'])
@cross_origin(supports_credentials=True)
def upload():

    if request.method == 'POST':
        # save the single "profile" file
        profile = request.files['image']
        profile.save(os.path.join(uploads_dir, 'upload.jpg'))
        
       

        # save each "charts" file

        file_name = secure_filename(profile.filename)
        path = uploads_dir+'/upload.jpg'
        s3.upload_file(path, bucket_name, 'images/{}'.format(file_name), ExtraArgs={'ContentType': "image/jpg", 'ACL': "public-read"})
        pred = p.predict(path)
        original_url = base_url+file_name
        response = make_response(
        jsonify({
            'original_image':original_url,
            'predicted_image':base_url+ pred[0],
            'label': pred[1],
            'english':audio_urls['english'],
            'german':audio_urls['german'],
            'description':description

        })

    )

        return response

if __name__ == '__main__':
    app.run(debug=True)
