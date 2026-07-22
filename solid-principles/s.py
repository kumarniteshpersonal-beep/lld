# single responsibility principle - states that a class should have only one reason to change, meaning that it should have only one responsibility or job.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def authenticate(self, user, password):
        # authentication logic
        pass
    
    def update_profile(self, name, email):
        self.name = name
        self.email = email

# problems:
# 1. The User class has multiple responsibilities: it manages user data, handles authentication, and updates user profiles. 
# 2. we should avoid creating god classes that have too many responsibilities, as it can lead to code that is difficult to maintain and test.

class UserAuthentication:
    def authenticate(self, user, password):
        # authentication logic
        pass

class UserProfile:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update_profile(self, name, email):
        self.name = name
        self.email = email