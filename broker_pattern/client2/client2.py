from broker_pattern.client2.client2_proxy import Client2Proxy


def get_char_count(string):
    client_proxy = Client2Proxy()
    print("Using get character count from StrServer")
    return client_proxy.get_char_count(string)


def convert_to_upper_case(string):
    client_proxy = Client2Proxy()
    print("Using convert to uppercase from StrServer")
    return client_proxy.convert_to_upper_case(string)


def create_password(length):
    client_proxy = Client2Proxy()
    print("Using create password from PasswordServer")
    return client_proxy.create_password(length)


if __name__ == '__main__':

    print("Starting Client 2.")

    res = get_char_count("Hello World")
    print("The result received is", res)

    res = convert_to_upper_case("Hello World")
    print("The result received is", res)

    res = create_password(10)
    print("The result received is", res)
