import grpc
from concurrent import futures
import time

# import generated class
import calculator_pb2
import calculator_pb2_grpc

# import the original calculator.py
import calculator

# create a class to define the server functions, 
# derived from calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    # expose calculator square root
    # the request and response are of the data type
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response
        
# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=18))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)
        
# listen on port 5001
print("Listening on port 5001")
server.add_insecure_port('[::]:5001')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)