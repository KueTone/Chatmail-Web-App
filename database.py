from app import myapp_obj, db
from app.models import User, Post
myapp_obj.app_context().push()

johnathon = User(username = 'kuetone',
                email='sammyshark@example.com',
                first='Johnathon',
                last='Lu',
                age = 20,
                bio='Marine biology student')
johnathon.set_password('password')
db.session.add(johnathon)

alicia = User(username = 'al',
                email='alicia@hotmail.com',
                first='alicia',
                last='arnold',
                age = 19,
                bio='aviation')
alicia.set_password('word')
db.session.add(alicia)

u = User(username = 'ExampleUser',
         email = 'user@example.com', 
         first = 'Who-ser', 
         last = 'User', 
         age = 10, 
         bio = "This is an example of a user's profile and information")
u.set_password('pass')
db.session.add(u)

u2 = User(username = 'DeleteUserEx',
         email = 'user@example.com', 
         first = 'us', 
         last = 'er', 
         age = 10, 
         bio = "Delete this user")
u2.set_password('delete')
db.session.add(u2)

email1 = Post(body = 'asdfjk l;qwe ruiopzx cvnm,.',
              author_id = 1, receive_id = 2)
db.session.add(email1)

email2 = Post(body = 'What are you here to?',
              author_id = 1, receive_id = 2)
db.session.add(email2)
email3 = Post(body = 'Big word register babes.', author_id = 2, receive_id = 1)
db.session.add(email3)

email4 = Post(body = 'What have you done??!??',
              author_id = 2 , receive_id = 1)
db.session.add(email4)

email5 = Post(body = 'Why am I here??!??', author_id=2, receive_id=1)
db.session.add(email5)

db.session.commit()