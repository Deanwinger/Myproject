from flask import render_template, request, Response
from app.forms import PKForm

from . import main

@main.route('/')
def index():
    pk_form = PKForm()
    return render_template('index.html', form=pk_form)

@main.route('/pk', methods=["GET", "POST"])
def pk():
    pk_form = PKForm(request.form)
    if pk_form.validate_on_submit():
        pk1_name = request.form.get('pk1')
        pk2_name = request.form.get('pk2')
        return render_template('pk.html', pk1=pk1_name, pk2=pk2_name)
    return Response("Invalid Input")

