from etcd import *

def connectToServer(hosts):
    try:
        client = Client(host=hosts,allow_reconnect=True)
        return client
    except Exception as e:
        print(e)

def insertKeyValue(client,key,value):
    try:
        client.set(key,value)
        print(f"{key}-{value} Inserted successfully !!")
        return True
    except Exception as e:
        print(e)
    
def getKeyValue(client,key):
    try:
        response = client.get(key)
        if response is not None:
            return response.value
        else:
            return None
    except Exception as e:
        print(e)

def deleteKeyValue(client,key):
    try:
        client.delete(key)
        print(f"{key} Deleted successfully !!")
        return True
    except Exception as e:
        print(e)
        return False


def listAllKeys(client):
    try:
        response = client.get('/')
        keys = [node.key for node in response.leaves]
        return keys
    except Exception as e:
        print(e)
    



if __name__ == "__main__":
    hosts = (('localhost',2379),)
    client = connectToServer(hosts)
    print(client)
    # insertKeyValue(client,"hi","hello")

    # print(getKeyValue(client,"hi"))

    # deleteKeyValue(client,"hi")

    # print(listAllKeys(client))
    

