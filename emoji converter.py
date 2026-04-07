msg = input("Enter a message: ")

msg = msg.replace(":)", "😊")
msg = msg.replace(":(", "😞")
msg = msg.replace(":D", "😃")
msg = msg.replace(":/", "😕")
print(f"Converted emoji : {msg}")
