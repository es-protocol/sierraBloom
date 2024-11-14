from flask import Blueprint, render_template
from .models import Project

bleuprint = Blueprint('sierra_b', __name__)


pro_jects = {
    '001': 'TP_Smart',
    '002': 'Shag_4_CheaP',
    '003': 'Wi_GarDen',
    '005': 'iN_iT'
}

# Home Route
@bleuprint.route('/')
def index():
    return render_template('index.html')

# Project Page route
@bleuprint.route('/projects')
def projects():
    return render_template('our-projects.html', project=pro_jects)


# About Us Page route
@bleuprint.route('/about-us')
def about():
    return render_template('about-us.html')

# Investor Page Route
@bleuprint.route('/investors')
def investor():
    return render_template('investor-page.html')

# Entrepreneur Page route
@bleuprint.route('/entrepreneur')
def entrepreneur():
    return render_template('ent-page.html')

# contact page route
@bleuprint.route('/contact')
def contact():
    return render_template('contact.html')

@bleuprint.route('/legal')
def legal():
    return render_template('/legal.html')