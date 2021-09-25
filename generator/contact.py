from model.contact import Contact
import random
import getopt
import sys
import string
import os.path
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "/data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digital_for_phone(maxlen):
    symbols = string.digits + "-" + "+"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_for_email(maxlen):
    nickname = "".join([random.choice(string.ascii_letters + string.digits) for i in
                        range(random.randrange(maxlen))])
    domain = "".join([random.choice(string.ascii_letters + string.digits + "-") for i in
                      range(random.randrange(maxlen))])
    cctld = "".join([random.choice(string.ascii_letters + "."*10) for i in range(random.randrange(5))])
    return nickname + "@" + domain + cctld


testdata = [Contact(firstname="", lastname="", address="", email="", email2="",
                    email3="", homephone="", mobilephone="", workphone="", secondaryphone="")] + [
               Contact(firstname=random_string("name", 10), lastname=random_string("lastname", 10),
                       address=random_string("address", 10),
                       email=random_string_for_email(10), email2=random_string_for_email(10),
                       email3=random_string_for_email(10), homephone=random_digital_for_phone(10),
                       mobilephone=random_digital_for_phone(10), workphone=random_digital_for_phone(10),
                       secondaryphone=random_digital_for_phone(10))
               for i in range(5)
           ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".." + f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
