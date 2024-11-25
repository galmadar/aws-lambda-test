import sys
def handler(event, context):
    print("a")
    print(event)
    print("a")
    print("b")
    print(context)
    print("b")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'