import ch_message

ch_message.send_message.send("hello")

txt = ch_message.receive_message.receive()
print(txt)