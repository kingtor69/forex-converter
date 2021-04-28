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

    # prepare message variables 
    # TODO: there's a more elegant way to do this
    msg_color = "secondary"
    btn_color = "primary"
    msgs = session.get('msgs', {})
    text_color = "light"
    form_display = ""
    # if we got a conversion, make that into a nice, human-readable message: 
    if session.get('converted'):
        session['msgs_are'] = True
        converted = session['converted']
        amt = session['amt']
        from_symbol = session.get('from_symbol')
        to_symbol = session.get('to_symbol')
        msg_color = "success"
        session['msgs'] = {msg_color: [f'{from_symbol} {amt} converted is ']}
        form_display = "none"
    elif session.get('msgs_are'):
        msg_color = "warning"
        text_color = "dark"
    else:
        msg_color = "danger"
        text_color = "dark"
        session['messages'] = {'danger': "The home page logic failed. If you're not Tor Kingdon, call him"}    



    return render_template('home.html', msg_color = msg_color, text_color = text_color, form_display = form_display, btn_color = btn_color)

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
        amt = ''
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
    codes = CurrencyCodes()
    rates = CurrencyRates()
    frm = session['from']
    to = session['to']
    amt = float(session['amt'])
    session['amt'] = f'{amt:.2f}'
    try: 
        session['from_symbol'] = codes.get_symbol(frm)
        session['to_symbol'] = codes.get_symbol(to)
        rate = rates.get_rate(frm, to)
        # TODO: if you really have a lot of spare time, look into making currency displayed as it would be locally (i.e. Europe would say 1.234.567,89€ instead of €1,234,567.89 or €1234567.89 as it will now)
        session['converted'] = f'{round(amt * rate, 2):.2f}'
    except:
        # in place of better error handling:
        flash("We got an error from Forex. If anyone who isn't named Tor Kingdon is reading this, please tell him he should fix it.", "bg-danger text-dark")
    
    return redirect('/')

@app.route('/reset')
def reset_session_data():
    session.clear()
    return redirect('/')