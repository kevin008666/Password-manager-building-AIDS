import base64
# decode the message that the user input
def decode(message):
    return base64.b64decode(message)
# encode the message that the user input
def encode(message):
    return base64.b64encode(message)
# main function
def main():
    print("Welcome to the Base64 Encoder/Decoder")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    choice = input("Please enter your choice: ")
    if choice == "1":
        message = input("Please enter the message you want to encode: ").encode("utf-8")
        a = encode(message)
        a = str(a,encoding="utf-8")
        print(a)
        main()
    elif choice == "2":
        message = input("Please enter the message you want to decode: ").encode("utf-8")
        a = decode(message)
        a = str(a,encoding="utf-8")
        print(a)
        main()
    elif choice == "3":
        print("Thank you for using this program")
        exit()
    else:
        print("Invalid choice")
        main()
main()