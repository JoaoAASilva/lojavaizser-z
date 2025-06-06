from main import app
from flask import render_template
from flask import Flask, render_template
p.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/catalogo")
def catalogo():
    return 
render_template('catalogo_completo.html')