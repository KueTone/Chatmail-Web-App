from app import myapp_obj
from app import myapp_obj, db
from app.models import User, Post
myapp_obj.app_context().push()

# initial database values
# exec(open('database.py').read())

# After session is over, delete all users to prevent user overlap
# User.query.delete()
# Post.query.delete()
# db.session.commit()


myapp_obj.run( debug=True)