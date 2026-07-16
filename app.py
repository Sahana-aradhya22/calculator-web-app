from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    num1 = ""
    num2 = ""

    if request.method == "POST":
        try:
            num1 = request.form["num1"]
            num2 = request.form["num2"]

            n1 = float(num1)
            n2 = float(num2)

            operation = request.form["operation"]

            if operation == "add":
                result = n1 + n2

            elif operation == "subtract":
                result = n1 - n2

            elif operation == "multiply":
                result = n1 * n2

            elif operation == "divide":
                if n2 == 0:
                    result = "Cannot divide by zero"
                else:
                    result = n1 / n2

            # Display whole numbers without .0
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 2)

        except ValueError:
            result = "Please enter valid numbers"

    return render_template(
        "index.html",
        result=result,
        num1=num1,
        num2=num2
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
