from flask import request, Flask, render_template, flash, redirect, url_for
import datetime
import webbrowser
import json
import dbms
import re
import bard
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/join")
def join():
    return render_template("login.html")

@app.route("/explore")
def explore():
    return render_template("tag.html")

logging.basicConfig(filename='api_logs.log', level=logging.INFO)

@app.route("/AI", methods=["GET", "POST"])
def ai():
    if request.method == "POST":
        global source, destination, start_date, end_date
        source = request.form.get("source")
        destination = request.form.get("destination")
        start_date = request.form.get("date")
        end_date = request.form.get("return")

        no_of_day = (datetime.datetime.strptime(end_date, "%Y-%m-%d") - datetime.datetime.strptime(start_date, "%Y-%m-%d")).days
        try:
            # Make API call to generate itinerary
            plan = bard.generate_itinerary(source, destination, start_date, end_date, no_of_day)
            
            # Log successful API call
            logging.info("API call to generate itinerary successful.")
        except Exception as e:
            # Log error if API call fails
            logging.error(f"Error in API call to generate itinerary: {e}")
            
            # Flash error message
            flash("Error in generating the plan. Please try again later.", "danger")
            
            # Redirect back to the AI page
            return redirect(url_for("ai"))

        if plan:
            # Render the result.html template with the plan data
            return render_template("result.html", plan=plan)

    # Render the AI.html template for GET requests
    return render_template('ai.html')





@app.route("/tag")
def tag():
    value = dbms.gettags()
    data = json.dumps(value)
    return render_template("tag.html", tag=data)

@app.route('/tag/<tag_id>')
def city_select(tag_id):
    value = dbms.getcitys(tag_id)
    data = json.dumps(value)
    return render_template("activity.html", tag=data, t_name=tag_id)

@app.route('/city/<city>')
def display_city(city):
    value = dbms.get_destination_info(city)
    data = json.dumps(value)
    c_name = re.sub(r'\(.*?\)', '', city).strip()
    value1 = [city.split()[0] + str(x) for x in range(1, 5)]
    data1 = json.dumps(value1)
    return render_template("city.html", city_slide=data1, city=c_name, city_detail=data)

@app.route("/<click>")
def other(click):
    return render_template(f"{click}.html")

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/")
    app.run()
