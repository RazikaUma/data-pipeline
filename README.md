# data-pipeline
The Repo contains the code for Simple Data pipeline which converts AWS ELB logs to structured output(JSON) and anonymize user data (username, firstname,email etc..)

util.py -- 
     anonymize the URL(name,email,username,password) 
     parse the log lines into json format
     
     
app.py -- 
    picks up input log file and write the output file

# ELB log format :
   https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html#access-log-entry-syntax

# Sample input : 
   https://github.com/RazikaUma/data-pipeline/blob/master/elb_log_file.txt

# Sample output : 
   https://github.com/RazikaUma/data-pipeline/blob/master/anonymized_data.txt

# Design : 
     https://github.com/RazikaUma/data-pipeline/blob/master/design.png

Installation
To get this repo running:

  Install Python 3. You can find instructions here.
  Create a virtual environment.
  Clone this repo 
  Install the package- pip install data-anonymizer-mapper

Usage
Execute the app.py script
You should see output from app.py.



