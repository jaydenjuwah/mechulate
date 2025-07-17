from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/stress', methods=['GET', 'POST'])
def stress():
    result = None
    error = None
    if request.method == 'POST':
        try:
            force = float(request.form['force'])
            area = float(request.form['area'])
            if area == 0 or force==0:
                raise ValueError("Area and Force cannot be zero.")
            stress = force / area
            result = round(stress, 2)
        except Exception as e:
            error = str(e)
    return render_template('stress.html', result=result, error=error)

@app.route('/beam', methods=['GET', 'POST'])
def beam():
    result = None
    error = None
    if request.method == 'POST':
        try:
            force = float(request.form['force'])
            length = float(request.form['length'])
            youngs = float(request.form['youngs'])
            inertia = float(request.form['inertia'])
            if youngs == 0 or inertia == 0:
                raise ValueError("Young's Modulus and Inertia must be non-zero.")
            deflection = (force * length**3) / (3 * youngs * inertia)
            result =  round(deflection, 2)
        except Exception as e:
            error = str(e)
    return render_template('beam.html', result=result, error=error)


@app.route('/gear', methods=['GET', 'POST'])
def gear():
    result = None
    error = None
    if request.method == 'POST':
        try:
            driver_teeth = int(request.form['driver'])
            driven_teeth = int(request.form['driven'])
            if driver_teeth == 0:
                raise ValueError("Driver teeth cannot be zero.")
            ratio = driven_teeth / driver_teeth
            result = round(ratio, 2)
        except Exception as e:
            error = str(e)
    return render_template('gear.html', result=result, error=error)


@app.route('/strain', methods=['GET', 'POST'])
def strain():
    result = None
    error = None
    if request.method == 'POST':
        try:
            change = float(request.form['change'])
            original = float(request.form['original'])
            if original == 0 or change == 0:
                raise ValueError("Original length and change in length cannot be zero.")
            strain = change / original
            result = round(strain, 5)
        except Exception as e:
            error = str(e)
    return render_template('strain.html', result=result, error=error)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


if __name__ == '__main__':
    app.run(debug=True)
