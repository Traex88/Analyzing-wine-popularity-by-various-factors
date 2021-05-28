# from wtforms import Form, StringField, TextAreaField, validators


# class SubmissionForm(Form):
#     title = StringField('Title', [validators.Length(min=0, max=12)])
#     category = StringField('Category', [validators.Length(min=0, max=30)])
#     text = TextAreaField('Text', [validators.Length(min=1, max=500)])

from wtforms import Form, StringField, TextAreaField, validators

class SubmissionForm(Form):
    subdeslen = StringField('deslen', [validators.Length(min=0, max=50)])
    subprice_range = StringField('price_range', [validators.Length(min=0, max=50)])
    subvariety = StringField('variety', [validators.Length(min=0, max=50)])
    subprovince = StringField('province', [validators.Length(min=0, max=50)])