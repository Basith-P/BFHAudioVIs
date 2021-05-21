from os import name
from flask import Flask, Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import audioDB, User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
# def home():
    # if request.method == 'POST':
    #     note = request.form.get('note')

    #     if len(note) < 1:
    #         flash('Note is too short!', category='error')
    #     else:
    #         new_note = Note(data=note, user_id=current_user.id)
    #         db.session.add(new_note)
    #         db.session.commit()
    #         flash('Note added!', category='success')

    # return render_template("home.html", user=current_user)


# @views.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        audio = request.files['aud-in']

        if not audio:
          flash("Couldn't upload the audio!", category='error')
        else:
            filename = secure_filename(audio.filename)
            mimetype = audio.mimetype
            audiofile = audioDB(audio=audio.read(), mimetype=mimetype, name=filename, user_id=current_user.id)
            db.session.add(audiofile)
            db.session.commit()
            flash('Audio uploaded!', category='success')

    return render_template("home.html", user=current_user)





@views.route('/delete-audio', methods=['POST'])
def delete_audio():
    audio = json.loads(request.data)
    audioId = audio['audioId']
    audio = audio.query.get(audioId)
    if audio:
        if audio.user_id == current_user.id:
            db.session.delete(audio)
            db.session.commit()

    return jsonify({})
