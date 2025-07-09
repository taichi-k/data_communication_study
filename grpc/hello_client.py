import time
import grpc
import hello_pb2, hello_pb2_grpc

def run():
    channel = grpc.insecure_channel('127.0.0.1:8081')
    stub = hello_pb2_grpc.HelloServiceStub(channel)
    while True:
        msg = "Hello"
        reply = stub.Say(hello_pb2.HelloRequest(message=msg))
        print("Sent:", msg, "Got reply:", reply.message)
        time.sleep(1)

if __name__ == '__main__':
    run()
