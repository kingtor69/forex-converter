from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyCodes, CurrencyRates

app = Flask(__name__)
app.config['SECRET_KEY'] = 'splabberbab39'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = "DebugToolbarExtension(app)"

@app.route('/')
def build_home_page():
    """build home page HTML from templates"""
    msg_color = "secondary"
    btn_color = "primary"
    if session.get('msgs_are'):
        btn_off = "deactivate"
        btn_color = "muted"
    msgs = session.get('msgs', {})
    ## there's a better way to do this, such that there can be messages of different colors
    for key in msgs.keys(): 
        if key == 'info': 
            msg_color = "info" 
        if key == 'errors': 
            msg_color = "warning"
        
    return render_template('home.html', msg_color = msg_color, btn_off = "deactivate", btn_color = btn_color)

@app.route('/submit', methods = ['POST'])
def handle_form_submission():
    """retrieve data from form and check for errors"""
    # get list of valid currency codes from Forex
    codes = CurrencyCodes()
    
    # gather to and from codes user entered and convert to upper case
    from_code = request.form['from'].upper()
    to_code = request.form['to'].upper()
    
    # gather raw amount from form (this will be a string)
    raw_amt = request.form['amt']
    

    # check for proper formatting and prepare error messages and append to error message list
    error_msgs = []
    if not codes.get_currency_name(from_code):
        error_msgs.append(f"From currency code ({from_code}) is not valid.")
        from_code = ''
    if not codes.get_currency_name(to_code):
        error_msgs.append(f"To currency code ({to_code}) is not valid.")
        to_code = ''
    # amount is a little trickier to test:
    try:
        amt = (round(float(raw_amt), 2))
        if amt < 0:
            session['amt'] = ''
            error_msgs.append(f"Amount ({raw_amt}) must be a positive number.")
        elif amt == 0:
            session['amt'] = ''
            error_msgs.append(f"Amount ({raw_amt}) can not be zero.")
    # if that didn't work, it is not a number
    except:
        session['amt'] = ''
        error_msgs.append(f"Amount ({raw_amt}) must be a number.")
        
    # save entries to session data
    session['from'] = from_code
    session['to'] = to_code
    session['amt'] = amt

    # if we got any errors, format them in session['msgs'] and redirect to top
    if len(error_msgs) > 0:
        # save error messages to session
        session['msgs'] = {'errors': error_msgs}
        session['msgs_are'] = True

        # show error messages and auto-completed correct entries on home page
        return redirect('/')
    
    # if we didn't get any errors, move on to converting
    return redirect('/convert')

@app.route('/convert')
def convert_currency():
    # try:
    codes = CurrencyCodes()
    rates = CurrencyRates()
    frm = session['from']
    to = session['to']
    session['converted'] = round(rates.get_rates(frm, to), 2)
    # except:
    #     # should work, but for troubleshooting purposes:
    #     flash("We got an error from Forex. If anyone who isn't named Tor Kingdon is reading this, please tell him he should fix it.", "bg-danger text-dark")

    return redirect('/')

@app.route('/reset')
def reset_session_data():
    session.clear()
    # return redirect('/')