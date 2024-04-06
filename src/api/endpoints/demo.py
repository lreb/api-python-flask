from flask import Blueprint, request
from models.model import db, Demo
from core.transaction_result import *
from core.security import token_required

demo_api = Blueprint('demo_api', __name__)

@demo_api.route('/increment/<int:number>/', methods=['GET'])
def incrementer(number):
    """
    Increment the given number by 1.

    Args:
        number (int): The number to be incremented.

    Returns:
        dict: A JSON response containing the incremented number.
    """
    return create_response_success("Incremented number is " + str(number+1))

@demo_api.route('/', methods=['GET'])
@token_required
def get_demo():
    """
    Get all demo records.

    Returns:
        dict: A JSON response containing the list of demo records.
    """
    try:
        demos = Demo.query.all() 
        demos_list = [{
            'id': demo.id, 
            'name': demo.name,
            'age': demo.age
            } for demo in demos]

        return create_response_success('success', demos_list)
    except Exception as error:
        result = {
            'result': 'error',
            'message': str(error),
            'data': None,
        }
        return create_response_error(str(error))


@demo_api.route('/<int:id>/', methods=['GET'])
@token_required
def get_demo_by_id(id):
    """
    Get a demo record by ID.

    Args:
        id (int): The ID of the demo record.

    Returns:
        dict: A JSON response with the demo record.
    """
    try:
        demo = Demo.query.get(id)
        if not demo:
            return create_response_error('Demo not found')

        demo_data = {
            #'id': demo.id,
            'name': demo.name,
            'age': demo.age
        }

        return create_response_success('success', demo_data)
    
    except Exception as error:
        return create_response_error(str(error))


@demo_api.route('/', methods=['POST'])
@token_required
def create_demo():
    """
    Create a new demo record.

    Returns:
        dict: A JSON response with the created demo record.
    """
    try:
        # Get the request data
        data = request.get_json()

        # Create a new demo record
        demo = Demo(name=data['name'], age=data['age'])
        db.session.add(demo)
        db.session.commit()

        # Return the created demo record
        return create_response_success('Demo created successfully', {
            'id': demo.id,
            'name': demo.name,
            'age': demo.age
        })
    
    except Exception as error:
        return create_response_error(str(error))
    

@demo_api.route('/update/<int:id>/', methods=['PUT'])
@token_required
def update_demo(id):
    """
    Update a demo record.

    Args:
        id (int): The ID of the demo record to update.

    Returns:
        dict: A JSON response with the updated demo record.
    """
    try:
        # Get the request data
        data = request.get_json()

        # Find the demo record to update
        demo = Demo.query.get(id)
        if not demo:
            return create_response_error('Demo not found')

        # Update the demo record
        demo.name = data['name']
        demo.age = data['age']
        db.session.commit()

        # Return the updated demo record
        return create_response_success('Demo updated successfully', {
            'id': demo.id,
            'name': demo.name,
            'age': demo.age
        })
    
    except Exception as error:
        return create_response_error(str(error))
    
@demo_api.route('/delete/<int:id>/', methods=['DELETE'])
@token_required
def delete_demo(id):
    """
    Delete a demo record.

    Args:
        id (int): The ID of the demo record to delete.

    Returns:
        dict: A JSON response indicating the success or failure of the deletion.
    """
    try:
        # Find the demo record to delete
        demo = Demo.query.get(id)
        if not demo:
            return create_response_error('Demo not found')

        # Delete the demo record
        db.session.delete(demo)
        db.session.commit()

        # Return a success response
        return create_response_success('Demo deleted successfully')
    
    except Exception as error:
        return create_response_error(str(error))
