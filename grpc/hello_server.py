import time
from concurrent import futures
import grpc
import hello_pb2, hello_pb2_grpc

class HelloService(hello_pb2_grpc.HelloServiceServicer):
    def Say(self, request, context):
        print("Received:", request.message)
        return hello_pb2.HelloReply(message="ACK")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    server.add_insecure_port('[::]:8081')
    server.start()
    print("gRPC server listening on 127.0.0.1:8081")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
