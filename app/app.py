from flask import Flask, redirect, url_for, render_template, send_file


app = Flask(__name__)



pro_jects = {
    '001': 'TP_Smart',
    '002': 'Shag_4_CheaP',
    '003': 'Wi_GarDen',
    '005': 'iN_iT'
}


# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Project Page route
@app.route('/projects')
def projects():
    return render_template('our-projects.html', project=pro_jects)

# About Us Page route
@app.route('/about-us')
def about():
    return render_template('about-us.html')

# Investor Page Route
@app.route('/investors')
def investor():
    return render_template('investor-page.html')

# Entrepreneur Page route
@app.route('/entrepreneur')
def entrepreneur():
    return render_template('ent-page.html')

# contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/legal')
def legal():
    return render_template('/legal.html')
