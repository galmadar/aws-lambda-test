import sys


def handler(event, context):
    print({"event": event, "context": context})
    return 'Hello from AWS Lambda using Python (2)' + sys.version + '!'

    
if __name__ == '__main__':
    handler({"hello":2}, {"content":"hello"})