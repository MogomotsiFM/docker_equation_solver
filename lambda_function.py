import sys
import equation_solver

def handler(event, context):
    print(event)

    # Problem statement is a query string parameter.
    eqn = event.setdefault("queryStringParameters", None)
    
    if eqn is None:
        # Problem statement is in the body.
        q = event.setdefault("eqn", None)
        if q is None:
            q = '(x-1)(4x+3)+105x-9=-12(-12x+10)+12'
    else:
        print("Equation", event["queryStringParameters"])
    
        q = event["queryStringParameters"]["eqn"]

    print(f"Question: {q}")

    try:
        _, steps = equation_solver.solve(q)

        return {
            "statusCode": 200,
            "body": steps,
            "headers": {
                "Content-Type": "text/html"
            },
            "isBase64Encoded": False
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": "Equation: " + q + "\n\n" + str(e),
            "isBase64Encoded": False,
            "headers": {
                "Content-Type": "text/html"
            }
        }


if __name__ == "__main__":
    handler({}, {})