from models import User, db


class userService:
    # get all the users
    def getAll():

        try:        
            users = User.query.all()
            userList = [user.toJson() for user in users]
        except Exception as e:
            db.session.rollback()  # Roll back changes if an exception occurs
            print(f"Error during commit: {str(e)}")
            return None
        
        return userList
    
    # create or update a user
    def post(newUser):
        try:
            db.session.add(newUser)
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # Roll back changes if an exception occurs
            print(f"Error during commit: {str(e)}")
            return None
        
        return newUser.toJson()
    
    def getById(id):
        try:
            user = User.query.get(id).toJson()
        
        except Exception as e:
            db.session.rollback()  # Roll back changes if an exception occurs
            print(f"Error during commit: {str(e)}")
            return None
        
        return user
    
    def delete(user_id):
        try:
            # Retrieve the user to be deleted
            user_to_delete = User.query.get(user_id)

            if user_to_delete:
                # Delete the user from the session
                db.session.delete(user_to_delete)
                db.session.commit()
                return True
            else:
                return False
        except Exception as e:
            db.session.rollback()  # Roll back changes if an exception occurs
            print(f"Error during commit: {str(e)}")
            return False
