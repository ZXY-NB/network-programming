# coding=utf-8
import socket
import subprocess
ip_port=('192.168.43.151',9999)
#买手机
s=socket.socket()
#买手机卡
s.bind(ip_port)
#开机
s.listen(5)
#等待电话
while True:
    conn,addr=s.accept()
    while True:
        #接受消息
        try:
            recv_data=conn.recv(1024)
            if len(recv_data)==0: break

            #发消息
            p=subprocess.Popen(str(recv_data,encoding='utf8'),shell=True,stdout=subprocess.PIPE)
            res=p.stdout.read()
            if len(res)==0:
                send_data='cmd ero'
            else:
                send_data=str(res,encoding='gbk')

            send_data=bytes(send_data,encoding='utf8')


            ready_tag='Ready|%s'%len(send_data)
            conn.send(ready_tag,encoding='utf8')
            feedback=conn.recv(1024)
            fendback=str(feedback,encoding='utf8')

            if feedback.startswith('Start'):
               conn.send(bytes(send_data,encoding='utf8'))
        except Exception:
            break

    #挂电话
    conn.close()
