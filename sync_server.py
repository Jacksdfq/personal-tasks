#!/usr/bin/env python3
"""本地局域网同步服务器 - 个人任务管理系统
用法: python sync_server.py
手机和电脑连同一 WiFi，手机浏览器输入电脑显示的地址即可同步。
"""

import json
import os
import socket
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sync_data.json')
PORT = 8765


def get_local_ip():
    """获取本机局域网 IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.254.254.254', 1))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'


class SyncHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f'[{self.client_address[0]}] {args[0]}')

    def _cors(self, status=200, content_type='application/json'):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._cors()

    def do_GET(self):
        if self.path == '/api/data':
            self._cors()
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    content = f.read()
            else:
                content = '{"tasks":[],"projects":[],"habits":[],"templates":[],"userSettings":{},"lastModified":""}'
            self.wfile.write(content.encode('utf-8'))
        elif self.path == '/' or self.path == '/index.html':
            self._cors(200, 'text/html; charset=utf-8')
            idx = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
            if os.path.exists(idx):
                with open(idx, 'r', encoding='utf-8') as f:
                    self.wfile.write(f.read().encode('utf-8'))
            else:
                self.wfile.write(b'<h1>TaskSync OK</h1><p>index.html not found</p>')
        elif self.path == '/manifest.json':
            self._cors(200, 'application/json')
            mf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'manifest.json')
            if os.path.exists(mf):
                with open(mf, 'r', encoding='utf-8') as f:
                    self.wfile.write(f.read().encode('utf-8'))
            else:
                self.wfile.write(b'{}')
        elif self.path == '/sw.js':
            self._cors(200, 'application/javascript')
            sf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sw.js')
            if os.path.exists(sf):
                with open(sf, 'r', encoding='utf-8') as f:
                    self.wfile.write(f.read().encode('utf-8'))
            else:
                self.wfile.write(b'')
        else:
            self._cors(404, 'text/plain')
            self.wfile.write(b'Not Found')

    def do_POST(self):
        if self.path == '/api/data':
            try:
                n = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(n)
                data = json.loads(body)
                with open(DATA_FILE, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                self._cors()
                self.wfile.write(b'{"ok":true}')
            except Exception as e:
                self._cors(400)
                self.wfile.write(json.dumps({'ok': False, 'error': str(e)}).encode('utf-8'))
        else:
            self._cors(404)
            self.wfile.write(b'{"ok":false,"error":"not found"}')


if __name__ == '__main__':
    ip = get_local_ip()
    server = HTTPServer(('0.0.0.0', PORT), SyncHandler)
    print('=' * 50)
    print('  个人任务管理系统 - 本地同步服务')
    print('=' * 50)
    print(f'  电脑地址: http://{ip}:{PORT}')
    print(f'  手机浏览器输入上面地址即可打开应用')
    print(f'  数据文件: {DATA_FILE}')
    print(f'  按 Ctrl+C 停止服务')
    print('=' * 50)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n服务已停止')
        server.server_close()
