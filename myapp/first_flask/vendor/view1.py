# # from flask import Blueprint, jsonify
# #
# # from first_flask.vendor.models import user_info
# #
# # #import json
# # mod=Blueprint('vendor',__name__,url_prefix='/user')
# #
# # @mod.route('/',methods=['GET'])
# # def fetch_user():
# #     users=user_info.query.all() #select from * user_info
# #     response=[x.__repe--() for x in users]
# #     return jsonify(response)
# #
# from flask import Blueprint, jsonify, request
#
# from first_flask import db
# from first_flask.vendor.models import user_info
#
# import json
#
# mod = Blueprint('vendor', __name__, url_prefix='/user')
#
#
# @mod.route('/', methods=['GET'])
# def fetch_user():
#     users = user_info.query.all()  # select * from user
#     #print(users[0].username, users[1].username)  ## on consule print username in table.
#     response = [x.__repr__() for x in users]
#     return jsonify(response)
#
#
# @mod.route('/<user_id>', methods=['GET'])  ## reference by id or get by id
# def show_id(user_id):
#     users = user_info.query.get(int(user_id))
#     # print(users.username)  ##  print username on consule,if we get user id from postman
#     response = users.__repr__()  # here show the details of perticular user_id on postman when we pass the user id like 1,2
#     response.pop('password')
#     return jsonify(response)


# @mod.route('/get-user', methods=['GET'])
# def fetch_user_by_name():
#     username = request.args.get('username')
#     user = user_info.query.filter(user_info.username == username).first()   ## here show user deatils when we pass username on postman like http://127.0.0.1:7000/user/get-user?username=komal and first use for only first match if username twoor more.
#     print(user)  #### here show user id when we pass username on postman like http://127.0.0.1:7000/user/get-user?username=komal
#     response = user.__repr__()
#     #response=[x.__repr__() for x in user]  ## here we use for if twoor more user name are same when we use this line
#     return jsonify(response)
#
# @mod.route('/create_user',methods=['POST'])    ## here  we add or create new user from postman and it willbe show on table.
# def create_user1():
#     user_data=request.get_json()
#     user=user_info(
#         username=user_data['username'],
#         email=user_data['email'],
#         password=user_data['password']
#     )
#     db.session.add(user)     ## session.add is user for add user in table
#     db.session.commit()      ## seesion.commit is used to save user data in table.
#     return 'user add successfully!!!'
#
# ## same above but using form process
# @mod.route('create_user_form',methods=['POST'])
# def create_form():
#     username=request.form.get('username')
#     password=request.form.get('password')
#     email=request.form.get('email')
#     user=user_info(
#         username=username,
#         email=email,
#         password=password
#     )
#     db.session.add(user)
#     db.session.commit()
#     return "User added successfully by form!!!"
#
# @mod.route('update_user/<user_id>/',methods=['PUT'])
# def update_user(user_id):
#     user_data=request.get_json()
#     user=user_info.query.get(int(user_id))
#     user.email=user_data['email']     ##update email by user_id
#     db.session.commit()
#     return "user details update successfully!!!"
#
# @mod.route('/delete_user/<user_id>',methods=['DELETE'])
# def delete_user(user_id):
#     user=user_info.query.get(int(user_id))
#     db.session.delete(user)
#     db.session.commit()
#     return "user has been deleted successfully!!!"
#
#
