def _if(bool, func1, func2):
    func1() if bool else func2()


def truthy():
    print('True')


def falsey():
    print('False')