from broker_pattern.client1.client1_proxy import Client1Proxy


def add_two_integers(num1, num2):
    client_proxy = Client1Proxy()
    if isinstance(num1, int) and isinstance(num2, int):
        print("Use addTwoNumbers feature in StatServer")
        return client_proxy.add_two_integers(num1, num2)
    else:
        return "Invalid"


def find_max_element(elements):
    client_proxy = Client1Proxy()
    print("Use findMaximumElement feature in StatServer")
    return client_proxy.find_maximum_element(elements)


if __name__ == '__main__':
    print("Starting Client 1.")

    res = add_two_integers(5, 6)
    print("The result received is", res)

    res = find_max_element([1, 7, 15.4, 20, 100, 124, -5, 14, 6])
    print("The result received is", res)
