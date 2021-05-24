from os import path
from pydub import AudioSegment
from flask import Flask, Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import audioDB
from . import db


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
            flash(filename, category='error')

            q = audioDB.query(audioDB.id).filter(audioDB.name==filename)
            isexists = audioDB.query(q.exists()).scalar()

            # for fname in audioDB.name:
            #     if fname == filename:
            #         flash("File name already exists", category='error')
            #         isexists = True


            if isexists == False:
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
                flash("There is a file in the same name in the databse")

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
