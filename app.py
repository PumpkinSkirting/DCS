from flask import *
from uptime import *
from data import *
#import Doutput
#import Dinput


app = Flask(__name__)


@app.route('/')
def index():
    piuptime = uptime()/3600
    return render_template('index.html', piuptime=piuptime)

@app.route('/name/<username>')
def name(username):
    return username

@app.route('/update')
def update():
    return '<html><head></head><body><script></script></body>'

@app.route('/display', methods=['POST', 'GET'])
def manage():
    if request.method == 'POST':
        Data.user_act = request.form['action']
        if type(Data.user_act) == str:
            Dron_data.RWN_Data('w1', 'UI:{}'.format(Data.user_act))
    return render_template("display.html", start_state=Dron_data.RWN_Data('r1'), global_value=Dron_data.RWN_Data('r1'), dron_i=Dron_data.RWN_Data('r2'))

#Dron_data.RWN_Data('r2')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60426, debug=True)
