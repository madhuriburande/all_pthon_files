# from flask import Blueprint, jsonify,request
# import json
#
# mod = Blueprint("user", __name__, url_prefix='/users')
#
# d1 = json.load(open(r"C:\Users\Admin\Desktop\flask\first_flask\user\data.json", 'r'))
#
#
# @mod.route('/', methods=['GET'])
# def show():
#     return jsonify(d1)
#
#
# @mod.route('/<user_id>/', methods=['GET'])
# def fetch_id(user_id):
#     response = [x for x in d1 if x['id'] == int(user_id)]
#     return jsonify(response)
#
#
# @mod.route('/details/',methods=['GET'])
# def fetch_user():
#     user_id = request.args.get('user_id')
#     print(user_id)
#     user_detail=[x for x in d1 if x['id'] == int(user_id)]
#     user_detail= user_detail[0] if user_detail else {}
#     return jsonify(user_detail)


# @mod.route('/create_user',methods=['GET'])
# def create_user():
#     user_data=request.get_json()
#     new_user_id=d1[-1]['id']+1
#     response=user_data
#     response['id']=new_user_id
#     d1.append(response)
#     json.dump(r"C:\Users\Admin\Desktop\flask\first_flask\user\data.json", 'w')
#     return jsonify(response)
#
