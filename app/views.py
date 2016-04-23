from flask import render_template
from flask import Flask
from flask import request
import matplotlib.pyplot as plt
import numpy as np
from cStringIO import StringIO
app = Flask(__name__)


html = '''
<html>
    <body>
        <img src="data:image/png;base64,{}" />
    </body>
</html>
'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display_plot',methods=['POST'])
def display_plot():
    if True:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        xs = np.linspace(-10, 10, 1000)
        ax.plot(xs, np.sin(xs), label='sin(x)')
        ax.plot(xs, np.cos(xs), label='cos(x)')
        ax.legend()

        io = StringIO()
        fig.savefig(io, format='png')
        data = io.getvalue().encode('base64')
        return html.format(data)

if __name__ == '__main__':
    app.run(debug=True)
