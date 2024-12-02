import os
from flask import Flask
from extensions import db
from routes import enregistrer_routes
import os

def creer_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bdd_users_z3tl_user:JF1CTSHmk1xNX2HmAxjGyA7HdESu6i9R@dpg-ct6mtdlumphs739i6pn0-a.oregon-postgres.render.com/bdd_users_z3tl'


    # postgresql://bdd_users_z3tl_user:JF1CTSHmk1xNX2HmAxjGyA7HdESu6i9R@dpg-ct6mtdlumphs739i6pn0-a.oregon-postgres.render.com/bdd_users_z3tl

    #'sqlite:///' + os.path.join(basedir, 'users_groups.db')
    #postgresql://mon_app_bdd_user:PkkgarCb0GAKivPtQNPBrEfX2UBM3uVK@dpg-ct6d2e9opnds73devvhg-a.oregon-postgres.render.com/mon_app_bdd
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    enregistrer_routes(app)
    return app