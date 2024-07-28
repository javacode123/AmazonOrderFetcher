from service.client import Client
from service.order import Order
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('email', type=str, help='Email address for login')
    parser.add_argument('password', type=str, help='Password for login')
    args = parser.parse_args()
    # TODO get user info from conf
    client = Client(args.email, args.password)
    client.sign_in()
    order = Order(client)
    order.save_orders()
