from abc import abstractmethod,ABC

class BaseHandler(ABC):
    def __init__(self):
        self.next_handler = None
    
    @abstractmethod
    def handle(self):
        raise NotImplementedError("please implement handle function")
    
    def set_nexthandler(self,next_handler):
        self.next_handler = next_handler
        return self.next_handler
    
    def next(self,req):
        if self.next_handler is None:
            return True
        return self.next_handler.handle(req)

class CheckUserNameHandler(BaseHandler):
    def handle(self, req):
        if "username" in req:
            print("username correct...")
            return self.next(req)
        return False

class CheckPasswordHandler(BaseHandler):
    def handle(self, req):
        if "password" in req:
            print("password correct...")
            return self.next(req)
        return False

class CheckAuthZHandler(BaseHandler):
    def handle(self, req):
        if "internal" in req:
            print("authz done...")
            return self.next(req)
        return False

# main middleware / client code
# create handler
username_handler = CheckUserNameHandler()
password_handler = CheckPasswordHandler()
authz_handler = CheckAuthZHandler()

# connect handler
password_handler.set_nexthandler(authz_handler)
username_handler.set_nexthandler(password_handler)

# final run
req = "username:nitesh,password:lolol,role:internal"
handler = username_handler
handler.handle(req)