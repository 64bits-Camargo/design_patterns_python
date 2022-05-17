from observer import Observer
from subject import Subject


if __name__ == '__main__':

    sendNotify = Subject()

    customer = Observer(sendNotify)

    customer.notify('teste', '1')