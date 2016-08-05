class weak():

    def __init__(self):
        self.hp = 5
        self.value = 20

class mild():

    def __init__(self):
        self.hp = 30
        self.value = 75

class potent():

    def __init__(self):
        self.hp = 80
        self.value = 150

class strong():

    def __init__(self):
        self.hp = 250
        self.value = 460
        
potencies = {'weak': weak(), 'mild': mild(), 'potent': potent(), 'strong': strong()}
