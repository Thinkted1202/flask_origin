from . import tools
from werkzeug.local import LocalStack, LocalProxy


@tools.cli.command('test_local')
def test_local():
    """測試線程"""
    def get_item():
        return test_stack.pop()

    test_stack = LocalStack()
    test_stack.push({'abc': '123'})
    test_stack.push({'abc': '1234'})

    item = get_item()
    print(item['abc'])
    print(item['abc'])

    test_stack = LocalStack()
    test_stack.push({'abc': '123'})
    test_stack.push({'abc': '1234'})
    item = LocalProxy(get_item)
    print(item['abc'])
    print(item['abc'])


