# from first_flask import db
#
# class user_info(db.Model):
#     id = db.column(db.INT, primary_key=True)
#     username = db.column(db.String(45), index=True, unique=True)
#     email = db.column(db.String(45), unique=True)
#     password = db.column(db.String(120))
#
#     def __repr__(self):
#         return {
#             'user':self.username,
#             'emailid':self.email,
#             'pwd':self.password
#         }

# from first_flask import db
#
#
# class user_info(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(45))
#     email = db.Column(db.String(45))
#     password = db.Column(db.String(120))
#
#     def __repr__(self):
#         return {
#             'username': self.username,
#             'email': self.email,
#             'password': self.password
#         }