"""
Routes and views for the flask application.
"""
import json
import urllib.request
import os

from datetime import datetime
from flask import render_template, request, redirect
from FlaskAppAML import app
from FlaskAppAML.forms import SubmissionForm

#WineQualityML (Brandie's) THIS SECTION IS TO BE UPDATED
BRAIN_ML_KEY=os.environ.get('API_KEY', "3ykY3j9WZDYvS0Dvf5VoJ1kA0yVT5HVzT+foY4SzKvD6LJhHoysBjlEQWaOniNQCGqsjKrytONq1kdxEWo3Scg==")
BRAIN_URL = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/91af20abfc58455182eaaa615d581c59/services/da7cdb9359a443f0abdef36d30ce8f1c/execute?api-version=2.0&details=true")
# Deployment environment variables defined on Azure (pull in with os.environ)
# Construct the HTTP request header
# HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ API_KEY)}
HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ BRAIN_ML_KEY)}


# Our main app page/route
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """Renders the home page which is the CNS of the web app currently, nothing pretty."""

    form = SubmissionForm(request.form)

    # Form has been submitted
    if request.method == 'POST' and form.validate():

        # Plug in the data into a dictionary object 
        #  - data from the input form
        #  - text data must be converted to lowercase
        data =  {
              "Inputs": {
                "input1": {
                  "ColumnNames": ["gender", "age", "size", "weight"],
                  "Values": [ [
                      0,
                      1,
                      form.title.data.lower(),
                      0

                    ]
                  ]
                }
              },
              "GlobalParameters": {}
            }
        body = str.encode(json.dumps(data))
        req = urllib.request.Request(BRAIN_URL, body, HEADERS)
        try:
            response = urllib.request.urlopen(req)
            #print(response)
            respdata = response.read()
            result = json.loads(str(respdata, 'utf-8'))
            # result = do_something_pretty(result)
            return render_template(
                'resultML.html',
                title="This is the result from AzureML running our example Student Brain Weight Prediction:",
                result=result)
        except urllib.error.HTTPError as err:
            result="The request failed with status code: " + str(err.code)
            return render_template(
                'resultML.html',
                title='There was an error',
                result=result)
    # Just serve up the input form
    return render_template(
        'formML.html',
        form=form,
        title='Run App',
        year=datetime.now().year,
        message='The Wine Quality Model generated via the Azure ML Api')


######################################################################
#Wine Rating ML Models
MLKEY_US=os.environ.get('API_KEY', "W4urY44dTQGrkQnlYZidPf9qhC7dV2y+syUV7akGKP5+bZ8Z+YMH46j4p4ATzijijzxNXsdrF3nNjcCmjnPIZw==")
MLURL_US=os.environ.get('URL',"https://ussouthcentral.services.azureml.net/workspaces/3734176412a549a2a4e3613e15756b2f/services/543adb9d102641afa368e61f5501b85f/execute?api-version=2.0&details=true")
MLHEADERS_US = {'Content-Type':'application/json', 'Authorization':('Bearer '+ MLKEY_US)}

MLKEY_CAN=os.environ.get('API_KEY', "aR0cLhZjFJ0U5IaAP2q2d5ix/7oXoIAJrkwYjbaWnWjDHq6mGP2SL/Zy6l8GrCQm7SuWtOY8KN4R/KwUuorsfw==")
MLURL_CAN=os.environ.get('URL',"https://ussouthcentral.services.azureml.net/workspaces/3734176412a549a2a4e3613e15756b2f/services/7bb143c75c15449c99c4e498b5a792bf/execute?api-version=2.0&details=true")
MLHEADERS_CAN = {'Content-Type':'application/json', 'Authorization':('Bearer '+ MLKEY_CAN)}

MLKEY_AUS=os.environ.get('API_KEY', "YNXWe8xgnrQGGVszq0PuOPXCoRhTwk2AKrmy+6Y9yHQIlLpXWwnBrtDeRRsyJEqalIkDJMxBYRvuk+tLcTclpQ==")
MLURL_AUS=os.environ.get('URL',"https://ussouthcentral.services.azureml.net/workspaces/3734176412a549a2a4e3613e15756b2f/services/0ca3bbedf4704511990b774f6e330041/execute?api-version=2.0&details=true")
MLHEADERS_AUS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ MLKEY_AUS)}

MLKEY_ARG=os.environ.get('API_KEY', "CB8iRFqPIX9hEnPnaUZsHorLrZpEu3R1vSd+s82a3Wv8rnKM2IlwuMnBcZ5VTXcWzU4Lioe3MhB5oSnSSzbOpw==")
MLURL_ARG=os.environ.get('URL',"https://ussouthcentral.services.azureml.net/workspaces/3734176412a549a2a4e3613e15756b2f/services/6bbdb51ce5a34fee90e1ee9ce3b10bee/execute?api-version=2.0&details=true")
MLHEADERS_ARG = {'Content-Type':'application/json', 'Authorization':('Bearer '+ MLKEY_ARG)}

MLKEY_FRA=os.environ.get('API_KEY', "epwlSyMUyPpSDofnkeP6p/Ey5QOj9MlUCRAsU+dMkBScc60yEzdw7lh8ktVVMzAmwxN+Vwf1mbbMGXtNa0mWhw==")
MLURL_FRA=os.environ.get('URL',"https://ussouthcentral.services.azureml.net/workspaces/3734176412a549a2a4e3613e15756b2f/services/924db838eeac4d14981304ac342035a6/execute?api-version=2.0&details=true")
MLHEADERS_FRA = {'Content-Type':'application/json', 'Authorization':('Bearer '+ MLKEY_FRA)}

MLKEY_ITA=os.environ.get('API_KEY', "Tw3JhjgrzueBuD51CAizNjrE0Knp13YodNcFQSVschUWbZXB1zKkzvxyer+sO6bIRa+a7XcTrMuU2iZezRqbzA==")
MLURL_ITA=os.environ.get('URL',"https://ussouthcentral.services.azureml.net/workspaces/3734176412a549a2a4e3613e15756b2f/services/096d97fe3f4c41649c4fbe92f327170e/execute?api-version=2.0&details=true")
MLHEADERS_ITA = {'Content-Type':'application/json', 'Authorization':('Bearer '+ MLKEY_ITA)}

MLKEY_SPA=os.environ.get('API_KEY', "U6FxZTEa50zK7UKpEV7Swb86a9Hg5tYkxmFxz792UQa5qzdFOOpH9JyZIvHm1LyvOis8o19QW88YrTZPDAvyNg==")
MLURL_SPA=os.environ.get('URL',"https://ussouthcentral.services.azureml.net/workspaces/3734176412a549a2a4e3613e15756b2f/services/bed77d07641b4206bac3e371710b42d7/execute?api-version=2.0&details=true")
MLHEADERS_SPA = {'Content-Type':'application/json', 'Authorization':('Bearer '+ MLKEY_SPA)}

@app.route('/ml', methods=['GET', 'POST'])
def ml():
    form = SubmissionForm(request.form)
    print(request.form)
    reqform = request.form.to_dict()

    if request.method == 'POST' and form.validate():
        selectedcountry = reqform["country"]
        print(selectedcountry)
        if selectedcountry == 'US':
            MLKEY = MLKEY_US
            MLURL = MLURL_US
            MLHEADERS = MLHEADERS_US
  
        elif selectedcountry == 'Canada':
            MLKEY = MLKEY_CAN
            MLURL = MLURL_CAN
            MLHEADERS = MLHEADERS_CAN

        elif selectedcountry == 'Australia':
            MLKEY = MLKEY_AUS
            MLURL = MLURL_AUS
            MLHEADERS = MLHEADERS_AUS

        elif selectedcountry == 'Argentina':
            MLKEY = MLKEY_ARG
            MLURL = MLURL_ARG
            MLHEADERS = MLHEADERS_ARG

        elif selectedcountry == 'France':
            MLKEY = MLKEY_FRA
            MLURL = MLURL_FRA
            MLHEADERS = MLHEADERS_FRA

        elif selectedcountry == 'Italy':
            MLKEY = MLKEY_ITA
            MLURL = MLURL_ITA
            MLHEADERS = MLHEADERS_ITA

        elif selectedcountry == 'Spain':
            MLKEY = MLKEY_SPA
            MLURL = MLURL_SPA
            MLHEADERS = MLHEADERS_SPA
            
        else:
            MLKEY = MLKEY_US
            MLURL = MLURL_US
            MLHEADERS = MLHEADERS_US             

        data =  {
              "Inputs": {
                "input1": {
                  "ColumnNames": ["Column 0", "points_range", "deslen", "price_range", "variety", "province"],
                  "Values": [ [
                      "2", 
                      "85-89", 
                      reqform["deslen"],
                      reqform["price_range"],
                      reqform["variety"],
                      reqform["province"]
                    ]
                  ]
                }
              },
              "GlobalParameters": {}
            }
        body = str.encode(json.dumps(data))
        req = urllib.request.Request(MLURL, body, MLHEADERS)
        try:
            response = urllib.request.urlopen(req)
            respdata = response.read()
            result = json.loads(str(respdata, 'utf-8'))
            result1 = format(result)
            return render_template(
                'resultML.html',
                title = " ",
                icountry = reqform["country"],
                ideslen = reqform["deslen"],
                ipricerg = reqform["price_range"],
                ivariety = reqform["variety"],
                iprovince = reqform["province"],
                result = result,
                result1 = result1)
        except urllib.error.HTTPError as err:
            result="The request failed with status code: " + str(err.code)
            return render_template(
                'resultML.html',
                title='There was an error',
                result=result)
    return render_template(
        'formML.html',
        form=form,
        title='Run App',
        year=datetime.now().year,
        message='The Wine Rating Model generated via the Azure ML Api')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

def format(jsondata):
    import itertools
    value = jsondata["Results"]["output1"]["value"]["Values"][0]
    print (value)
    sz1 = len(value)
    pwinerating = value[sz1-1]
    return pwinerating