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

        return html(steps)
    except Exception as e:
        return {
            "statusCode": 400,
            "body": "Equation: " + q + "\n\n" + str(e),
            "isBase64Encoded": False,
            "headers": {
                "Content-Type": "text/html"
            }
        }


def html(steps):
    """
        Using chr(10) in place of '\n'. Otherwise this fails in Python 11. 
        I can't use Python 12 because its AWS Lambda base image does not 
        include YUM. YUM is used to install git so that we can clone the 
        equation solver app. 
    """
    items = [f"<tr><td>{step.strip(chr(10))}</td></tr>" for step in steps]

    response = {
        "statusCode": 200,
        "body": """
            <table>
                <thead>
                    <tr>
                        <th><h1>Solution</h1></th>
                    </tr>
                </thead>
                <tbody>"""
                    + "".join(items) + """
                </tbody>
            </table>""",
        "headers": {
            "Content-Type": "text/html"
        },
        "isBase64Encoded": False
    }

    return response

if __name__ == "__main__":
    handler({}, {})