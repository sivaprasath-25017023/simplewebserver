from http.server import HTTPServer, BaseHTTPRequestHandler

htmlcontent = '''
<!doctype html>
<html>
    <head>
        <title>shocksiva</title>
    </head>
    <body>
        <font color="Lightpink" face="Impact" size="65">
            <h1 align="center"><b>List of protocol in TCP/IP Model</b></h1>
        </font>
        <font color="Darkgreen" face="Candara">
        <h2 align="center">
            Application Layer - HTTP, FTP, DNS, Telnet & SSH <br>
            Transport Layer - TCP & UDP <br>
            Network Layer - IPV4/IPV6 <br>
        </h2>
    </font>
    </body>
</html>
'''

class serverResponse(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(htmlcontent.encode())

print("This is my webserver") 
server_address =('',5000)
httpd = HTTPServer(server_address,serverResponse)
httpd.serve_forever()