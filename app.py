from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtensions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'splabberbab39'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False