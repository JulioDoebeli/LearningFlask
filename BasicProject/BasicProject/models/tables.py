from BasicProject import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    __tablename__ = "users"

    id = db.Collum(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    
    def __init__(self, username, password, name, email):
        self.username = username;
        self.password = password;
        self.name = name;
        self.email = email;


    def __repr__(self):
        return "<User %r>" % self.username

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Collum(db.Integer, primary_key = True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.Foreignkey('users.id'), nullable=False)
    
    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content;
        self.user_id = user_id;
    
        def __repr__(self):
            return "<Post %r>" % self.content

class Follower(db.Model):
    __tablename__ = "followers"

    id          = db.Collum(db.Integer, primary_key = True)
    user_id     = db.Column(db.Integer, db.Foreignkey('users.id'), nullable=False)
    follower_id = db.Column(db.Integer, db.Foreignkey('users.id'), nullable=False)
    
    user        = db.relationship('User', foreign_keys=user_id)
    follower_id = db.relationship('User', foreign_keys=follower_id)
