from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
 
import time
 
app = Flask(__name__)
sched = None

# We maintain a joblist since apscheduler get_jobs() does not return any jobs when scheduled with date
joblist = {}

def para(s):
    return F"<p>{s}</p>"

def italicize(s):
    return F"<i>{s}</i>"

def header(htype, s):
    return F"<{htype}>{s}</{htype}>"

demo_string = header("h2", "Welcome to the flask_apscheduler demo!") + para("You can kick off a sleeper event by calling GET /event/sleeptime")
demo_string += italicize("Every event kicked off sleeps for seconds as specified in sleeptime")
demo_string += para("You can see a list of running events by calling GET /events")

def sleeper(sleeptime):
    jobname = F"sleeper_{sleeptime}"
    time.sleep(int(sleeptime))
    if jobname in joblist:
        del(joblist[jobname])

@app.route('/')
def welcome():
    return demo_string, 200

@app.route('/event/<sleeptime>')
def add_event(sleeptime):
    jobname = F"sleeper_{sleeptime}"
    try:
        if jobname not in joblist:
            joblist[jobname] = sched.add_job(func=sleeper, trigger='date', args=[sleeptime], id=jobname, max_instances=5)
            return F'created a sleeper job for {sleeptime} seconds', 200
        else:
            return F"Sleeper with sleeptime {sleeptime} is already running", 500
    except Exception as e:
        return F"{e}", 500

@app.route('/events')
def get_events():
    response = ''
    for job in joblist:
        response += header("h2", F"{job}")
    return response, 200

if __name__ == '__main__':
    sched = BackgroundScheduler(daemon=True)
    sched.start()
    app.run(debug=True)
