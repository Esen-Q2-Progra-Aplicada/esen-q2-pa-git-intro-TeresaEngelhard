from solution import ListUtil

def test_check_create_class():
    solution = ListUtil()
    assert solution is not None

def test_mehtod_getlist():
    solution = ListUtil()
    numberList = solution.getList()
    assert len(numberList) == 0

def test_getList_after_addnumbers():
    solution = ListUtil()
    solution.addNumbers(10)
    numberList = solution.getList()
    assert len(numberList) > 0

