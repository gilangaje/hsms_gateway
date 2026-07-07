client = HsmsClient(ip, port)

client.connect()

client.select()

client.send(frame)

frame = client.receive()

client.linktest()

client.disconnect()