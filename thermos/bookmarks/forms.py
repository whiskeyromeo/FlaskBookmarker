from flask_wtf import Form
from wtforms.fields import StringField
from flask.ext.wtf.html5 import URLField
from wtforms.validators import DataRequired, url, Regexp


class BookmarkForm(Form):
    url = URLField('The URL for your bookmark', validators=[DataRequired(),url()])
    description = StringField('Add a description', validators=[DataRequired()])
    tags = StringField('Tags', validators=[Regexp(r'^[a-zA-Z0-9, ]*$',
                                                 message="Tags can only contain letters and numbers")])
    
    def validate(self):
        if not self.url.data.startswith("http://") or self.url.data.startswith("https://"):
                self.url.data = "http://" + self.url.data
                
        if not Form.validate(self):
            return False
        
        if not self.description.data:
            self.description.data = self.url.data
            
        #Filter out any duplicated tags
        stripped = [t.strip() for t in self.tags.data.split(',')]
        not_empty = [tag for tag in stripped if tag]
        tagset = set(not_empty)
        self.tags.data = ",".join(tagset)

        return True
    
