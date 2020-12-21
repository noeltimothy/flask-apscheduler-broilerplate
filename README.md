# flask-apscheduler-broilerplate
A simple flask app that demonstrates how to use apscheduler for running background tasks

# caveats
apscheduler works great to run jobs in the background using add_job()
add_job allows to scheduled jobs using the following approaches:
- Now using 'date'
- on an interval using 'interval'

The only problem is that get_jobs() fails to return the jobs that are running.
This code maintains a joblist so that those jobs can be fetched.

# how to run
This requires Python3.6 or later since it uses F-Strings
Run the flask server as follows:

```
# git clone https://github.com/noeltimothy/flask-apscheduler-broilerplate.git
# pip3 install apscheduler
# python3 app.py
```

On your browser vist the following pages to see the demo page with instructions:
```
http://localhost:5000/              ---> demo
http://localhost:5000/event/300     ---> add a job that takes 300 seconds to complete
http://localhost:5000/event/400     ---> add a job that takes 400 seconds to complete
http://localhost:5000/events        ---> list active jobs
```



