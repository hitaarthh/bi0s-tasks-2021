def encrypt(shift, message):
    new = ""
    for i in message:
        if 65 <= ord(i) <= 90:
            if ord(i) + shift <= 90:
                new += chr(ord(i) + shift)
            else:
                new += chr(ord(i) + shift - 26)

        elif 97 <= ord(i) <= 122:
            if ord(i) + shift <= 122:
                new += chr(ord(i) + shift)
            else:
                new += chr(ord(i) + shift - 26)
        else:
            new += i
    print(new)


def decrypt(shift, message):
    new = ""
    for i in message:
        if 65 <= ord(i) <= 90:
            if ord(i) - shift >= 65:
                new += chr(ord(i) - shift)
            else:
                new += chr(26 + (ord(i) - shift))
        elif 97 <= ord(i) <= 122:
            if ord(i) - shift >= 97:
                new += chr(ord(i) - shift)
            else:
                new += chr(26 + (ord(i) - shift))
        else:
            new += i
    print(new)


choice = int(input("Enter choice : "))
shift = int(input("Enter shift value : "))
message = input("Input message : ")

if choice == 0:
    encrypt(shift, message)
elif choice == 1:
    decrypt(shift, message)
else:
    print("Invalid shift value!")

