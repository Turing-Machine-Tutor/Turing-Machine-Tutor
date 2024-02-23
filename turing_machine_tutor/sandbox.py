from configuration import Configuration


def test_me(number):
    if number==1:
        return "one"
    if number==2:
        return "two"
    if number==3:
        return "three"
    return


ok=Configuration(1,2,3)
print(ok.try_me(test_me))

