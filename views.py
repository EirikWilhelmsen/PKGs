from flask import Blueprint, render_template, request, jsonify

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/about')
def about():
    return render_template('about.html') 

@views.route("/profile/")
def profile():
    args = request.args
    platform_name = args.get('platform_name')
    return render_template("profile.html", platform_name=platform_name)