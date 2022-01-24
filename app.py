from flask import Flask,jsonify,request

app = Flask(__name__)

bus = []

train = []

flight=[]

@app.route('/')

@app.route('/bus' , methods=['POST'])
def create_bus():
  request_data = request.get_json()
  new_user = {
    'name':request_data['name'],
    'user':[]
  }
  bus.append(new_user)
  return jsonify(new_user,{'message': 'user created'})


@app.route('/bus' , methods=['DELETE'])
def delete_bus():
  request_data = request.get_json()
  new_user = {
    'name':request_data['name'],
    'user':[]
  }
  bus.append(new_user)
  return jsonify({'message': 'user deleted'})


@app.route('/bus/<string:name>')
def get_bus(name):
  for seater in bus:
    if seater['name'] == name:
          return jsonify(seater)
  return jsonify ({'message': 'user not found'})

@app.route('/bus')
def get_bus_users():
  return jsonify({'bus': bus})


@app.route('/bus/<string:name>/user' , methods=['POST'])
def create_user_in_bus(name):
  request_data = request.get_json()
  for seater in bus:
    if seater['name'] == name:
        new_user = {
            'name': request_data['name'],
            'age': request_data['age'],
            'gender': request_data['gender'],
            'startpoint':request_data['startpoint'],
            'destination':request_data['destination'],
            'coach':request_data['coach'],
            'no_of_tickets':request_data['no_of_tickets']
            
            
        }
        seater['user'].append(new_user)
        return jsonify({"message":"congrats!! successfully bus tickets booked"})
  return jsonify ({'message' :'fill all required information'})

@app.route('/bus/<string:name>/user' , methods=['PUT'])
def update_user_in_bus(name):
  request_data = request.get_json()
  for seater in bus:
    if seater['name'] == name:
        new_user = {
            
            'startpoint':request_data['startpoint'],
            'destination':request_data['destination'],
            'coach':request_data['coach'],
            'no_of_tickets':request_data['no_of_tickets']
            
            
        }
        seater['user'].append(new_user)
        return jsonify({"message":"congrats!! successfully bus tickets updated"})
  return jsonify ({'message' :'fill all required information'})


@app.route('/bus/<string:name>/user')
def get_user_in_bus(name):
  for seater in bus:
    if seater['name'] == name:
        return jsonify( {'user':seater['user'] } )
  return jsonify ({'message':'user not found'})

                #######   TRAIN PROCESS##############

@app.route('/train' , methods=['POST'])
def create_train():
  request_data = request.get_json()
  new_user = {
    'name':request_data['name'],
    'user':[]
  }
  bus.append(new_user)
  return jsonify(new_user)

@app.route('/train/<string:name>')
def get_train(name):
  for seater in train:
    if seater['name'] == name:
          return jsonify(seater)
  return jsonify ({'message': 'user not found'})

@app.route('/train')
def get_train_users():
  return jsonify({'train': train})


@app.route('/train/<string:name>/user' , methods=['POST'])
def create_user_in_train(name):
  request_data = request.get_json()
  for seater in train:
    if seater['name'] == name:
        new_user = {
            'name': request_data['name'],
            'age': request_data['age'],
            'gender': request_data['gender'],
            'startpoint':request_data['startpoint'],
            'destination':request_data['destination'],
            'coach':request_data['coach'],
            'no_of_tickets':request_data['no_of_tickets']
            
            
        }
        seater['user'].append(new_user)
        return jsonify({'message' :'congrats!! successfully train tickets updated'})
  return jsonify ({'message' :'fill all required information'})


@app.route('/train/<string:name>/user' , methods=['PUT'])
def update_user_in_train(name):
  request_data = request.get_json()
  for seater in train:
    if seater['name'] == name:
        new_user = {
            
            'startpoint':request_data['startpoint'],
            'destination':request_data['destination'],
            'coach':request_data['coach'],
            'no_of_tickets':request_data['no_of_tickets']
            
            
        }
        seater['user'].append(new_user)
        return jsonify({"message":"congrats!! successfully train tickets updated"})
  return jsonify ({'message' :'fill all required information'})


@app.route('/train/<string:name>/user')
def get_user_in_train(name):
  for seater in train:
    if seater['name'] == name:
        return jsonify( {'user':seater['user'] } )
  return jsonify ({'message':'user not found'})



  ###########################   FLIGHT PROCESS         ################

@app.route('/flight' , methods=['POST'])
def create_flight():
  request_data = request.get_json()
  new_user = {
    'name':request_data['name'],
    'user':[]
  }
  flight.append(new_user)
  return jsonify(new_user,{'message': 'user created'})


@app.route('/flight' , methods=['DELETE'])
def delete_flight():
  request_data = request.get_json()
  new_user = {
    'name':request_data['name'],
    'user':[]
  }
  flight.append(new_user)
  return jsonify({'message': 'user deleted'})


@app.route('/flight/<string:name>')
def get_flight(name):
  for seater in flight:
    if seater['name'] == name:
          return jsonify(seater)
  return jsonify ({'message': 'user not found'})

@app.route('/flight')
def get_flight_users():
  return jsonify({'flight': flight})


@app.route('/flight/<string:name>/user' , methods=['POST'])
def create_user_in_flight(name):
  request_data = request.get_json()
  for seater in flight:
    if seater['name'] == name:
        new_user = {
            'name': request_data['name'],
            'age': request_data['age'],
            'gender': request_data['gender'],
            'startpoint':request_data['startpoint'],
            'destination':request_data['destination'],
            'coach':request_data['coach'],
            'no_of_tickets':request_data['no_of_tickets']
            
            
        }
        seater['user'].append(new_user)
        return jsonify({"message":"congrats!! successfully flight tickets booked"})
  return jsonify ({'message' :'fill all required information'})

@app.route('/flight/<string:name>/user' , methods=['PUT'])
def update_user_in_flight(name):
  request_data = request.get_json()
  for seater in bus:
    if seater['name'] == name:
        new_user = {
            
            'startpoint':request_data['startpoint'],
            'destination':request_data['destination'],
            'coach':request_data['coach'],
            'no_of_tickets':request_data['no_of_tickets']
            
            
        }
        seater['user'].append(new_user)
        return jsonify({"message":"congrats!! successfully flight tickets updated"})
  return jsonify ({'message' :'fill all required information'})


@app.route('/flight/<string:name>/user')
def get_user_in_flight(name):
  for seater in flight:
    if seater['name'] == name:
        return jsonify( {'user':seater['user'] } )
  return jsonify ({'message':'user not found'})


app.run(port=5000)