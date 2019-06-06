from mypkg.greetings import say_hello_to


def test_say_hello_appends_name():
    assert say_hello_to("world") == "hello world"


# this is an example of testing from a fixture
#def test_say_hello_appends_name_from_fixture(my_string_fixture):
#    assert say_hello_to(my_string_fixture) == "hello {}".format(my_string_fixture)
