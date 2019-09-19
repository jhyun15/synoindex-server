#-*- coding: utf-8 -*-
import os
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


config = {
    'bindAddr': 'localhost',
    'bindPort': 9998
}


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if "/synoindex" in self.path:
            query = urlparse(self.path).query
            query_components = parse_qs(query)

            if "args" in query_components:
                args = query_components["args"]
                if len(args) == 1:
                    msg = 'Synoindex NOT Support [%s] argument, but response OK to clients!' % args[0]
                elif len(args) >= 2:
                    msg = indexing(args)
            else:
                msg = 'Synoindex response OK to clients!'

            self.send_response(200)
            self.end_headers()
            self.wfile.write(msg.encode())
        else:
            self.send_response(404)
            self.end_headers()

        return


def indexing(arg):
    msg = 'Synoindex %s %s' % (str(arg[0]), str(arg[1]))
    pname = '/usr/syno/bin/synoindex'
    if os.path.isfile(pname):
        try:
            cmd = [pname, arg[0], arg[1].encode('utf-8')]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()
        except Exception as e:
            msg = 'Exception:%s' % e
    else:
        msg = 'Synoindex is not exist'
    return msg


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = (config['bindAddr'], config['bindPort'])
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print('Stopping httpd...')
