from flask import Blueprint, jsonify, request

mod = Blueprint("user", __name__, url_prefix='/user_info')

import json

d1 = json.load(open(r"C:\Users\Admin\Desktop\flask\first_flask\product\data1.json", 'r'))


#print(d1)
@mod.route('/', methods=['GET'])
def display():
    return jsonify(d1)


@mod.route('/<user_id>/', methods=['GET'])
def show(user_id):
    responce = [x for x in d1 if x['id'] == int(user_id)]
    return jsonify(responce)


@mod.route('/details/',methods=['GET'])
def fetch_user():
    user_id = request.args.get('user_id')
    print(user_id)
    user_detail=[x for x in d1 if x['id'] == int(user_id)]
    user_detail= user_detail[0] if user_detail else {}
    return jsonify(user_detail)

@mod.route('/create_user',methods=['post'])
def create_user1():
    user_data=request.get_json()
    new_user_id=d1[-1]['id']+1
    responce=user_data
    responce['id']=new_user_id
    d1.append(responce)
    json.dump(d1,open(r"C:\Users\Admin\Desktop\flask\first_flask\product\data1.json",'w'))
    return jsonify(responce)

# def create_user1():
#     user_data=request.get_json()
#     new_user_id=d1[-1]['id']+1
#     responce=user_data
#     responce= {
#         "id": 5,
#         "name": "Abc",
#         "pass": "23xy"
#     }
#     d1.append(responce)
#     json.dump(d1,open(r"C:\Users\Admin\Desktop\flask\first_flask\product\data1.json",'w'))
#     return "user create sucessfully."

@mod.route('/update/<user_id>/',methods=['PUT'])
def update_user(user_id):
    user_data=request.get_json()
    for d in d1:
        if d['id'] == int(user_id):
            if 'name' in user_data:
                d['name']= user_data['name']
            if 'password' in user_data:
                d['password']= user_data['password']
    json.dump(d1,open(r"C:\Users\Admin\Desktop\flask\first_flask\product\data1.json",'w'))
    return "user update sucessfully."

@mod.route('/delete/<user_id>/',methods=['DELETE'])
def delete_user(user_id):
    for index,val in enumerate(d1):
        if val['id'] == int(user_id):
            del d1[index]
    json.dump(d1,open(r"C:\Users\Admin\Desktop\flask\first_flask\product\data1.json",'w'))
    return "Delete user sucessfully."





