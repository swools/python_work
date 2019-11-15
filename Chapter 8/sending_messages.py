messages = ["Hello", "How are you?", "What're you doing later?"]
sent_messages = list()

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"\nSending message, {current_message}")
        sent_messages.append(current_message)

send_messages(messages, sent_messages)

print(messages)
print(sent_messages)