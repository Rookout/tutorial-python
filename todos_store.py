class Store:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Store.__instance == None:
            Store()
        return Store.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if Store.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Store.__instance = self

        self.todos = []