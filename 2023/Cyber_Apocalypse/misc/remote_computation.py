import socket
host = "165.232.108.249"
port = 30317


def alien_calculator(dataline):
    try:    
        answer = round(eval(dataline),2)
    except ZeroDivisionError:
        return "DIV0_ERR"
    except SyntaxError:
        return "SYNTAX_ERR"
    if answer > 1337 or answer < -1337:
        return "MEM_ERR"
    return str(answer)

    
def main ():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(2048).decode()
    print(data)
    s.send("1\n".encode())
    while True:
        data = s.recv(2048).decode()
        print(data)
        start = data.find(":")+2 
        end = data.find("?")-3 
        data_back = alien_calculator(data[start:end])  #move data.find to func?
        s.send(f"{data_back}\n".encode())


def test ():
    ...

main()

