# coding=utf-8

############################阻塞是基于连接正常的情况下才会发生
import socket

ip_port=('192.168.43.151',9999)
#买手机
s=socket.socket()
#拨号
s.connect(ip_port)
while True:
    #发消息
    send_data=input(">>:").strip()
    s.send(bytes(send_data,encoding='utf8'))
    if len(send_data)==0: continue
    if send_data=='exit': break



    #解决黏包问题
    ready_tag=s.recv(1024)
    ready_tag=str(ready_tag,encoding='utf8')
    if ready_tag.startswith('Ready'):
        msg_size=int(ready_tag.split('|')[-1])
    start_tag='Start'
    s.send(bytes(start_tag,encoding='utf8'))


    recv_size = 0
    recv_msg = b''
    while recv_size < msg_size:
        recv_data=s.recv(1024)
        recv_msg+=recv_data
        recv_size+=len(recv_data)
        print('MSG_SIZE %s  RECE SIZE %s' %(msg_size,recv_size))

    print(str(recv_msg,encoding='utf8'))

    #挂电话
s.close()
