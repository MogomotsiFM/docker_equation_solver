import json
import equation_solver

def handler(event, context):
    print(event)

    try:
        q = event["queryStringParameters"]["eqn"]
    except Exception as e:
        return {
            "statusCode": 400,
            "body": "The linear equation should be a request parameter, i.e.: /?eqn='x^2+1=2'",
            "isBase64Encoded": False,
            "headers": {
                "Content-Type": "text/html"
            }
        }
    
    print(f"Question: {q}")

    try:
        _, steps = equation_solver.solve(q)

        return {
            "statusCode": 200,
            "body": json.dumps(steps),
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