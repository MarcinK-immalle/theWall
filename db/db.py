class Message:
    def __init__(self):
        self.time = ""
        self.content = ""

# in-memory opslag van messages
messages = []

#test static/base messages
m1 = Message()
m1.time = "2019-02-18 11:00"
m1.content = "Hallo!"
    
m2 = Message()
m2.time = "2019-02-18 11:05"
m2.content = "De muur?"

messages.append(m1)
messages.append(m2)

def getMessages():
    #returned de messages list
    global messages

    return messages

def postMessages(message, timestamp):
    #maakt message obj en append de db
    global messages

    m = Message()
    m.content = message
    m.time = timestamp
    messages.append(m)