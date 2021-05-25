from flask import Flask, Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import audioDB
from . import db
import json


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
# def home():

def home():
    if request.method == 'POST':
        audio = request.files['aud-in']

        if not audio:
          flash("Couldn't upload the audio!", category='error')
        else:
            mimetype = audio.mimetype
            # filename = audio.filename
            filename = secure_filename(audio.filename)

            q = audioDB.query.filter_by(name = filename)

            if not q:
                # if mimetype != 'audio/wav':
                #     # files                                                                         
                #     src = filename
                #     dst = filename+".wav"

                #     # convert wav to mp3                                                            
                #     sound = AudioSegment.from_mp3(src)
                #     sound.export(dst, format="wav")

                #     filename = secure_filename(dst)
                #     mimetype = dst.mimetype
                # else:
                #     filename = secure_filename(audio.filename)
                #     mimetype = audio.mimetype
                
                audiofile = audioDB(audio=audio.read(), mimetype=mimetype, name=filename, user_id=current_user.id)
                db.session.add(audiofile)
                db.session.commit()
                flash(filename + " - type of file = " + mimetype, category='success')
            else:
                flash("filename already exists")

            ##################################################
            ##################################################

    return render_template("home.html", user = current_user)




@views.route('/delete-audio', methods=['POST'])
def delete_audio():
    audio = json.loads(request.data)
    audioId = audio['audioId']
    audio = audioDB.query.get(audioId)
    if audio:
        if audio.user_id == current_user.id:
            db.session.delete(audio)
            db.session.commit()

    return jsonify({})

# @view.route('/play')
