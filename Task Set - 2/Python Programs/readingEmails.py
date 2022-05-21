mail = input("Input e-mail id : ")
parts = mail.split("@")
local = parts[0]
parts = parts[1].split(".")
domain = parts[0]
ext = parts[1]
if domain.isnumeric() == 0 and len(local) <= 64 and len(ext) <= 3:
    status = 0
    for i in local:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57 or i in "!#$%^&*{}|~_+-=/'":
            status += 1

    for i in domain:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
            status += 1
    if domain.endswith("-") or domain.startswith("-"):
        status += 1

    if status == (len(local) + len(domain)):
        print("True")
    else:
        print("False")

else:
    print("False")
