import flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask.views import MethodView
from flask_login import login_required
from flask_login import current_user
import models
import re
import json


class HomeScreenView(MethodView):
    decorators = [login_required]

    def get(self):
        print current_user.courses
        return render_template('home.html')

class DBButtonView(MethodView):
    def get(self):
        #user = models.User("test@test.com", "pass")
        #user = models.db.session.query(models.User).filter_by(id=1).first()
        #user.courses.append(models.db.session.query(models.Course).filter_by(id=1).first())
        #models.db.session.commit()

        #print models.db.session.query(models.Course).filter_by(id=1).first()
        return render_template('home.html')
