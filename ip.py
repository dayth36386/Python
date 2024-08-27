while True:
    ip = input("====================== Menu ===================\n"
               "1. Exit Please Enter 'x'\n"
               "2. Search Class Ip Please Enter IPv4 address: ")
    if ip == 'X' or ip == 'x':
        break
    ip_split = ip.split('.')
    if len(ip_split) == 4:
            for i in range(len(ip_split)):
                if ip_split[i].isnumeric() and int(ip_split[i]) <= 255:
                    if i == 3:
                        if int(ip_split[0]) <= 127:
                            print(f"{ip} is Class A")
                        elif int(ip_split[0]) <= 191:
                            print(f"{ip} is Class B")
                        elif int(ip_split[0]) <= 223:
                            print(f"{ip} is Class C")
                        elif int(ip_split[0]) <= 239:
                            print(f"{ip} is Class D")
                        elif int(ip_split[0]) <= 255:
                            print(f"{ip} is Class E")
                else:
                    print("Please Enter is Numeric Or <255 Error Octet{0} [{1}]".format(i+1,ip_split[i]))
                    break
    else:
        print("You must have 4 Octet")
