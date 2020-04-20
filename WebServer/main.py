import socket

address='127.0.0.1'
port=50000

URLS = {
    '/': "hello there",
    'wtf': "kek"
}

def geturl(request):
    r = request.split(" ")
    method = r[0]
    url = r[1]
    return (method, url)


def getheaders(request):
    method, url = geturl(request)
    if not method == "GET":
        return ("HTTP/1.1 405 Method is not allowed\n\n", 405)

    if not url in URLS:
        return ("HTTP/1.1 404 Not found\n\n", 404)

    return ("HTTP/1.1 200 OK\n\n", 200)


def getresponse(request):
    headers, code = getheaders(request)
    response = (headers + "hello world").encode()
    return (response, code)


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((address, port))
    server_socket.listen()
    print("Listen on {}:{}".format(address, port))

    while True:
        client_socket, addr = server_socket.accept()
        msg = client_socket.recv(1024)

        print(msg.decode("utf-8"))
        print(addr)

        response, code = getresponse(msg.decode())
        client_socket.sendall(response)
        client_socket.close()



def main():
    try:
        run()
    except KeyboardInterrupt:
        print("Okey okey got you")
        return

if __name__ == "__main__":
    main()