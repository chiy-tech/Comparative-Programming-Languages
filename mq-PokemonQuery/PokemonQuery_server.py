# python3 PokemonQuery_server.py
# based on https://www.rabbitmq.com/tutorials/tutorial-six-python.html
import pika
import json
import pandas as pd

print("""\

              _                              
  _ __   ___ | | _____ _ __ ___   ___  _ __  
 | '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ 
 | |_) | (_) |   <  __/ | | | | | (_) | | | |
 | .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|
 |_|                                         

                    """)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

data = pd.read_csv('pokemon.csv')
def get_length(request):
    length = len(request['string'])
    return {'length': length}

# Use this function to implement the Pokemon Quary
def on_request(ch, method, props, body):
    try:
        request = json.loads(body.decode('utf-8'))

    except json.decoder.JSONDecodeError:
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print('Bad request:', body)
        return
    s = request['string'][:-1]
    print("----------------------------------------------------------")
    print("pokemon quary:", s)
    quary = data[data.Name==s]
    type1 = data[data["Type 1"]==s]
    type2 = data[data["Type 2"]==s]

    # Pokemon Query Name (Example: Pikachu)
    if(not quary.empty):
        quary = data[data.Name==s]
        summury = "Index:{} | Name:{} | Generation:{} | Type1:{} | Type2:{}".format(quary["#"].iloc[0], quary["Name"].iloc[0],quary["Generation"].iloc[0],quary["Type 1"].iloc[0],quary["Type 2"].iloc[0])   
        print(quary)
        print("Name Found!")
        print("Sending to clint the Json file:)")
        response = quary.to_json(orient='records', lines=True).split('\n')
        body = json.dumps(response).encode('utf-8')

    # Pokemon Query Type (Example: Grass)
    elif(not type1.empty):
        type1 = data[data["Type 1"]==s]
        json_file = type1.to_json(orient='records', lines=True).split('\n')
        #print(type1)
        print("Type1 Found!\n","Sending to clint the Json file:)")
        response = json_file
        body = json.dumps(response).encode('utf-8')

    if(not type2.empty):
        type2 = data[data["Type 1"]==s]
        json_file = type2.to_json(orient='records', lines=True).split('\n')
        #print(type2)
        print("Type2 Found!\n","Sending to clint the Json file:)")
        response = json_file
        body = json.dumps(response).encode('utf-8')

    # Pokemon Query Index number (Example: 25)
    elif(s > '0' and s < "800"):
        quary = data[data["#"]==int(s)]
        summury = "Index:{} | Name:{} | Generation:{} | Type1:{} | Type2:{}".format(quary["#"].iloc[0], quary["Name"].iloc[0],quary["Generation"].iloc[0],quary["Type 1"].iloc[0],quary["Type 2"].iloc[0])   
        print(quary)
        print("Index Found!")
        print("Sending to clint the Json file:)")
        response = quary.to_json(orient='records', lines=True).split('\n')
        body = json.dumps(response).encode('utf-8')

    # Pokemon Query Ability : (Example: =600, >300, <100, >=500, <=80, != 600)
    elif(s[0] == '='):
        temp = s[1:]
        res = data[data.Total==int(temp)]
        if(not res.empty):
            print("Ability Found!")
            print(res)
            print("Sending to clint the Json file:)")
            json_file = res.to_json(orient='records', lines=True).split('\n')
            response = json_file
            body = json.dumps(response).encode('utf-8')

        else:
            print("Nothing Found!")
            response = "Nothing found."
            body = json.dumps(response).encode('utf-8')

    elif(s[0] == '>'):
        temp = s[1:]
        if(temp[0] == '='):
            temp2 = temp[1:]
            res = data[data.Total>=int(temp2)]
            if(not res.empty):
                print("Ability Found!")
                print(res)
                print("Sending to clint the Json file:)")
                json_file = res.to_json(orient='records', lines=True).split('\n')
                response = json_file
                body = json.dumps(response).encode('utf-8')
            else:
                print("Nothing Found!")
                response = "Nothing found."
                body = json.dumps(response).encode('utf-8')

        else:
            res = data[data.Total>int(temp)]
            if(not res.empty):
                print("Ability Found!")
                print(res)
                print("Sending to clint the Json file:)")
                json_file = res.to_json(orient='records', lines=True).split('\n')
                response = json_file
                body = json.dumps(response).encode('utf-8')
            else:
                print("Nothing Found!")
                response = "Nothing found."
                body = json.dumps(response).encode('utf-8')

    elif(s[0] == '<'):
        temp = s[1:]
        if(temp[0] == '='):
            temp2 = temp[1:]
            res = data[data.Total<=int(temp2)]
            if(not res.empty):
                print("Ability Found!")
                print(res)
                print("Sending to clint the Json file:)")
                json_file = res.to_json(orient='records', lines=True).split('\n')
                response = json_file
                body = json.dumps(response).encode('utf-8')
            else:
                print("Nothing Found!")
                response = "Nothing found."
                body = json.dumps(response).encode('utf-8')
        else:

            res = data[data.Total<int(temp)]
            if(not res.empty):
                print("Ability Found!")
                print(res)
                print("Sending to clint the Json file:)")
                json_file = res.to_json(orient='records', lines=True).split('\n')
                response = json_file
                body = json.dumps(response).encode('utf-8')
            else:
                print("Nothing Found!")
                response = "Nothing found."
                body = json.dumps(response).encode('utf-8')

    elif(s[0:2] == "!="):
        temp = s[2:]
        res = data[data.Total != int(temp)]
        if(not res.empty):
            print("Ability Found!")
            print(res)
            print("Sending to clint the Json file:)")
            json_file = res.to_json(orient='records', lines=True).split('\n')
            response = json_file
            body = json.dumps(response).encode('utf-8')
        else:
            print("Nothing Found!")
            response = "Nothing found."
            body = json.dumps(response).encode('utf-8')

   #Pokemon Query Legendary  (Example: legendary, not legendary)
    elif(s == "legendary"):
        res = data[data.Legendary == True]
        if(not res.empty):
            print("Legendary Found!")
            print(res)
            print("Sending to clint the Json file:)")
            json_file = res.to_json(orient='records', lines=True).split('\n')
            response = json_file
            body = json.dumps(response).encode('utf-8')
        else:
            print("Nothing Found!")
            response = "Nothing found."
            body = json.dumps(response).encode('utf-8') 

    elif(s == "not legendary"):
        res = data[data.Legendary == False]
        if(not res.empty):
            print("Legendary Found!")
            print(res)
            print("Sending to clint the Json file:)")
            json_file = res.to_json(orient='records', lines=True).split('\n')
            response = json_file
            body = json.dumps(response).encode('utf-8')
        else:
            print("Nothing Found!")
            response = "Nothing found."
            body = json.dumps(response).encode('utf-8') 

    else:
        print("Nothing Found!")
        response = "Nothing found."
        body = json.dumps(response).encode('utf-8')

    #print("Query server closed :")
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print("Awaiting RPC requests")
channel.start_consuming()