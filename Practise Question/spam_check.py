# code to find spam messages

message = input("Enter any message: ")

if "Make lot of Money" in message or "Buy now" in message or "Subscribe this" in message or "click this" in message:
    print("This is spam message")

else:
    print(message)