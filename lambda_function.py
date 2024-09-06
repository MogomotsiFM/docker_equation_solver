import json
import equation_solver

def handler(event, context):
    print(event)

    try:
        # Only the equation should be in the body
        q = event["body"]
        
        print(f"Question: {q}")

        _, steps = equation_solver.solve(q)

        return {
            "statusCode": 200,
            "body": json.dumps(steps),
            "headers": {
                "Content-Type": "application/json"
            },
            "isBase64Encoded": False
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": "Equation: " + q + "\n\n" + str(e),
            "isBase64Encoded": False,
            "headers": {
                "Content-Type": "application/json"
            }
        }


if __name__ == "__main__":
    handler({}, {})