#Azure uses app.py and looks for it to do whatever it tells it to do
# All our code will be in here

from flask import Flask
from flask import render_template, request
from flask import request 

app = Flask(__name__)
@app.route("/") #/ means root, .route is function, when the git request shows up to the server and it's blank, it wants whatever is in root
# function returns the index.html
# if url asking for specific resource, then ask it to do specific things
def index():
    return render_template('index.html') #returning page, execute html

#flask is a python file executing python functions
# @ is the decorator
# when the 
@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method== 'POST':
        form = request.form
        userRadius = float(form['radius'])
        userHeight = float(form['height'])
        pi = 3.14
        areaTop = pi*userRadius**2
        areaSides = 2*(pi*(userRadius*userHeight))
        totalArea = areaTop + areaSides
        totalPrice = 24*totalArea + 15*totalArea
        str = "${:,.2f}"
        totalPrice = str.format(totalPrice)
        return render_template('estimate.html', estimate=totalPrice)
    return render_template('estimate.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

