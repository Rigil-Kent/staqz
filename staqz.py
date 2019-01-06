from datetime import datetime
import stock as stock
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


userportfolio = ["NKE","UA","AMZN","NOK", "BPMX", "DIS", "AMD", "S"]
app = Flask(__name__)
app.config['SECRET_KEY'] = "one ring to rule"
bootstrap = Bootstrap(app)
moment = Moment(app)

class SetupForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    passwd = PasswordField('Password: ', validators=[DataRequired()])
    passrepeat = PasswordField('Repeat Password: ', validators=[DataRequired()])
    apikey = StringField('API Key: ', validators=[DataRequired()])
    portfolio = StringField("Watchlist: ", validators=[DataRequired()])
    submit = SubmitField('Sign Up')


@app.route('/')
def index():
    return render_template("index.html", userportfolio=userportfolio)


@app.route('/portfolio/<asset>')
def asset(asset):
    finances = stock.get_financials(asset)
    name = stock.get_name(asset)

    return render_template('stock.html', current_time=datetime.utcnow() , userportfolio=userportfolio, asset=asset, name=name, price=finances[0], change=finances[1], volume=finances[2], opening=finances[3],high=finances[4], low=finances[5], close=finances[6], change_percentage=finances[7], penny=finances[8])

@app.route('/signup')
def signup():
    username=None
    apikey=None
    portfolio=None
    form = SetupForm()

    if form.validate_on_submit():
        username = form.username.data 
        apikey = form.apikey.data
        portfolio = form.portfolio.data
        form.username.data = ''
        form.apikey.data = ''
        form.portfolio.data = ''.split(',')

    return render_template('signup.html', userportfolio=userportfolio, form=form, username=username, apikey=apikey, portfolio=portfolio)


@app.errorhandler(404)
def file_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def server_error(e):
    if e == 'Global Quote':
        return render_template('api_error.html')
    else:
        return render_template("500.html")

        
@app.route('/secret/tetris')
def tetris():
    
    return render_template('tetris.html')


if __name__ == "__main__":
    app.run()

'''for item in userportfolio:
    finances = stock.get_financials(item)
    print("Market information for {}".format(stock.get_name(item)))
    print("Current share price: {}".format(finances[0]))
    print("Previous close price: {}".format(finances[6]))
    print("Change in price {}".format(finances[1]))
    print("Change percentage: {}".format(finances[7]))
    print("high: {}".format(finances[4]))
    print("low: {}".format(finances[5]))
    print("open: {}".format(finances[3]))
    print("volume: {}".format(finances[2]))'''