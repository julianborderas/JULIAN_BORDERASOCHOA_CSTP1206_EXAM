from flask import render_template, jsonify, json

# as the models file contains all the models, import what you need
from app.models import Alpaca, alpaca_user

class AlpacaController(object):

    # TODO: Implement Index
    # WHAT: Grabs data from model and uses it to display the relevant
    # alpacas from the database
    # CONDITIONS: If user specifies age, then must filter the list
    # RETURN: Return formatted Alpaca's to use for the view
    def index(self, age=None):
        results = alpaca_user.get_all(age)
        return render_template("index.html", results=results, age=age)
    
    # TODO: Implement Profile
    # WHAT: Grabs the relevant Alpaca from the model and uses it to
    # display the profile for that alpaca from the database
    # RETURN: Return formatted Alpaca to use for the view
    def profile(self, name):
        results = alpaca_user.get(name)
        return render_template("profile.html", results=results, contact=json.dumps(results['contact']), hobbies=results['hobbies'])
    
    # TODO: Implement Search
    # WHAT: Uses the data recieved to find the Alpaca from the data
    # CONDITIONS: If user specifies nothing you can return everything or nothing!
    # that part if determined by you however if something is specified, it must
    # be a filtered list of alpacas
    # RETURN: Return formatted alpacas as a list using the
    # search criteria
    def search(self, name=None):
        results = alpaca_user.get_all(name)
        
        return render_template("index.html", results=results, name=searched)
    
    # TODO: Implement Create
    # WHAT: Uses the data recieved to create an Alpaca model
    # REQUIREMENTS: Make a 'fake' save function in Alpaca that
    # Prints saving alpaca and then list the information recieved
    # and then give back a message stating what was saved
    # i.e Fred was created!
    # CONDITIONS:
    # RETURN: Return formatted message using the relevant information
    def create(self, id, name, displayName, bio, age, hobbies, contact, sex):
        alpaca = Alpaca(id, name, displayName, bio, age, hobbies, contact, sex)
        data = {'message': name + "was succesfully created"}
        print('Creating Alpaca', id, name, displayName, bio, age, hobbies, contact, sex)
        return jsonify(data)

    # TODO: Implement Delete
    # WHAT: Uses the data recieved to find the Alpaca from the data
    # and then deletes it
    # REQUIREMENTS: Make a 'fake' delete function in Alpaca that
    # Prints the alpaca that will be delted followed by deleting alpaca
    # and then list the information recieved and then give back a
    # message stating what was saved i.e Fred was deleted!
    # CONDITIONS:
    # RETURN: Return formatted message using the relevant information
    def delete(self, id, name, displayName, bio, age, hobbies, contact, sex):
        alpaca = Alpaca(id, name, displayName, bio, age, hobbies, contact, sex)
        alpaca.delete(id, name, displayName, bio, age, hobbies, contact, sex)
        data = { 'message': name + 'was succesfully deleted'}
        print('Deleting Alpaca', id, name, displayName, bio, age, hobbies, contact, sex)
        return jsonify(data)

alpaca_controller = AlpacaController()
