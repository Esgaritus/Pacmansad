import zmq
import sys


def main():

	UsersConnected = {}

	context=zmq.Context()
	socket=context.socket(zmq.ROUTER)
	socket.bind("tcp://*:6666")

	poller= zmq.Poller()
	poller.register(socket, zmq.POLLIN)

	while True:
		socks= dict(poller.poll())

		if socket in socks:
			ident, *Mensaje = socket.recv_multipart()
			User = [ident, Mensaje]
			UsersConnected[ident] = eval(str(Mensaje))

			socket.send_multipart([ident, bytes(str(UsersConnected), 'ascii')])

				#socket.send_string('a')
			#print ("Movimiento: %s" % User)

		print(UsersConnected)

if __name__ == '__main__':
	main()
