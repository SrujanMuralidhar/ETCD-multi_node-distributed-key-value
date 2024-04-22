import streamlit as st 
import Client


hosts = (('localhost', 2359),('localhost', 2389),('localhost', 2369))
client = Client.connectToServer(hosts)
print(f"Members : {client.members}")
print(f"Leader : {client.leader}")
        

st.title("Distributed Key-Value store")



choice = st.selectbox("Select an action : ",
                      ("List all Keys","Insert a Key-Value","Delete a Key","Get the value for a specified key","Details"),
                      index=None,
                        placeholder="Choice...",
                      )

if choice == "List all Keys":
    keys = Client.listAllKeys(client)
    st.write(keys)

elif choice == "Delete a Key":
    keyToBeDeleted = st.text_input("Enter the key to be deleted : ")
    keyDeleteButton = st.button("Delete Key")
    if(keyDeleteButton):
        flag = Client.deleteKeyValue(client,keyToBeDeleted)
        if flag :
            st.success(f"Deleted successfully !!")
        else:
            st.warning(f"Key not found")
        
elif choice == "Get the value for a specified key":
    valueAtKey = st.text_input("Enter the key : ")
    getValueButton = st.button("Get Value")
    if(getValueButton):
        value = Client.getKeyValue(client,valueAtKey)
        if value:
            st.subheader(f"Value : {value}")
        else:
            st.warning(f"Key not found")

elif choice == "Insert a Key-Value":
    key = st.text_input("Enter the key : ")
    value = st.text_input("Enter the value : ")
    insertButton = st.button("Insert")
    
    if(insertButton):
        flag = Client.insertKeyValue(client,key,value)
        if flag:
            st.success(f"Inserted successfully !!")
        else:
            st.warning(f"Couldn't insert ")
        
elif choice == "Details":
    st.subheader("Cluster members : ")
    st.write(client.members)

    st.subheader("Cluster Leader : ")
    st.write(client.leader)
    


    