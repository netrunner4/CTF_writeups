# misc/Remote Computation

### Description
> The alien species use remote machines for all their computation needs. Pandora managed to hack into one, but broke its functionality in the process. Incoming computation requests need to be calculated and answered rapidly, in order to not alarm the aliens and ultimately pivot to other parts of their network. Not all requests are valid though, and appropriate error messages need to be sent depending on the type of error. Can you buy us some time by correctly responding to the next 500 requests?

We just need to write remote calculator, I used python

Code:
```python
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
        data_back = alien_calculator(data[start:end])
        s.send(f"{data_back}\n".encode())


def test ():
    ...

main()
```
After 500 equations we get:

Good job! *HTB{d1v1d3_bY_Z3r0_3rr0r}*
 
