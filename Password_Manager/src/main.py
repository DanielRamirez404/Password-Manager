from behavior import *

def __main__() -> int:

    LoginInfo.load()

    showLoginWindow(onLogIn=onLogIn, onSignUp=onSignUp, onExit=onExit)

    return 0

__main__()
