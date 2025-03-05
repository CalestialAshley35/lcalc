from decimal import Decimal, getcontext
import math
from sympy import symbols, Eq, solve, expand, simplify, factor, diff, integrate, Matrix, sqrt, pi, tan, sin, cos, log
from sympy.geometry import Point, Line, Circle, Polygon, Triangle
from rich.console import Console
from rich.prompt import Prompt
from rich import print

getcontext().prec = 50

console = Console()

def evaluate_formula(formula):
    try:
        return eval(formula, {
            "Decimal": Decimal, "sqrt": sqrt, "log": log, "exp": math.exp, "pi": pi,
            "sin": sin, "cos": cos, "tan": tan, "asin": math.asin, "acos": math.acos, "atan": math.atan
        })
    except Exception as e:
        return f"Error: {e}"

def basic_operations(num1, num2, operation):
    try:
        num1 = Decimal(num1)
        num2 = Decimal(num2)
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            return num1 / num2 if num2 != 0 else "Error! Division by zero."
        elif operation == "^":
            return num1 ** num2
        elif operation == "%":
            return num1 % num2
        elif operation == "//":
            return num1 // num2
        else:
            return "Invalid operation!"
    except Exception as e:
        return f"Error: {e}"

def solve_equation(equation):
    try:
        x = symbols('x')
        equation = equation.replace("^", "**")
        eq = Eq(eval(equation.split('=')[0]), eval(equation.split('=')[1]))
        return solve(eq, x)
    except Exception as e:
        return f"Error: {e}"

def expand_expression(expr):
    try:
        x = symbols('x')
        return expand(expr)
    except Exception as e:
        return f"Error: {e}"

def simplify_expression(expr):
    try:
        x = symbols('x')
        return simplify(expr)
    except Exception as e:
        return f"Error: {e}"

def factor_expression(expr):
    try:
        x = symbols('x')
        return factor(expr)
    except Exception as e:
        return f"Error: {e}"

def differentiate_expression(expr):
    try:
        x = symbols('x')
        return diff(expr, x)
    except Exception as e:
        return f"Error: {e}"

def integrate_expression(expr):
    try:
        x = symbols('x')
        return integrate(expr, x)
    except Exception as e:
        return f"Error: {e}"

def matrix_operations(matrix1, matrix2, operation):
    try:
        mat1 = Matrix(matrix1)
        mat2 = Matrix(matrix2) if matrix2 else None
        if operation == "+":
            return mat1 + mat2
        elif operation == "-":
            return mat1 - mat2
        elif operation == "*":
            return mat1 * mat2
        elif operation == "det":
            return mat1.det()
        elif operation == "inv":
            return mat1.inv()
        elif operation == "transpose":
            return mat1.T
        else:
            return "Invalid operation!"
    except Exception as e:
        return f"Error: {e}"

def geometric_operations(user_input):
    try:
        if "distance" in user_input:
            point1 = Prompt.ask("Enter coordinates for point 1 (e.g., (x1, y1))")
            point2 = Prompt.ask("Enter coordinates for point 2 (e.g., (x2, y2))")
            point1 = Point(*eval(point1))
            point2 = Point(*eval(point2))
            return point1.distance(point2)
        elif "line" in user_input:
            point1 = Prompt.ask("Enter coordinates for point 1 (e.g., (x1, y1))")
            point2 = Prompt.ask("Enter coordinates for point 2 (e.g., (x2, y2))")
            point1 = Point(*eval(point1))
            point2 = Point(*eval(point2))
            line = Line(point1, point2)
            return line.equation()
        elif "circle" in user_input:
            center = Prompt.ask("Enter coordinates for the center (e.g., (x, y))")
            radius = Prompt.ask("Enter radius")
            center = Point(*eval(center))
            circle = Circle(center, Decimal(radius))
            return circle.equation()
        elif "polygon" in user_input:
            vertices = Prompt.ask("Enter the list of vertices for the polygon (e.g., [(x1, y1), (x2, y2), ...])")
            vertices = [Point(*v) for v in eval(vertices)]
            polygon = Polygon(*vertices)
            return polygon.area, polygon.perimeter
        elif "triangle" in user_input:
            point1 = Prompt.ask("Enter coordinates for point 1 (e.g., (x1, y1))")
            point2 = Prompt.ask("Enter coordinates for point 2 (e.g., (x2, y2))")
            point3 = Prompt.ask("Enter coordinates for point 3 (e.g., (x3, y3))")
            point1 = Point(*eval(point1))
            point2 = Point(*eval(point2))
            point3 = Point(*eval(point3))
            triangle = Triangle(point1, point2, point3)
            return triangle.area, triangle.perimeter
        else:
            return "Error: Invalid geometry operation."
    except Exception as e:
        return f"Error: {e}"

def show_welcome():
    console.print("[bold magenta]Welcome to lcalc (Linux Calculator)![/bold magenta]")
    console.print("[italic green]Supports: advanced algebra, calculus, trigonometry, matrices, geometry, and more.[/italic green]")

def calculator():
    show_welcome()

    while True:
        user_input = Prompt.ask("Enter a formula, equation, or operation (e.g., 2.5 + 3.4, sin(pi/2), x^2 - 5x + 6 = 0)", default="")

        if any(op in user_input for op in ['+', '-', '*', '/', '^', '%', '//']):
            parts = user_input.split()
            if len(parts) == 3:
                num1, operation, num2 = parts
                result = basic_operations(num1, num2, operation)
            else:
                result = "Error: Invalid format for basic operation. Use 'number operator number'."
        elif "=" in user_input:
            result = solve_equation(user_input)
        elif "expand" in user_input:
            expr = user_input.replace("expand", "").strip()
            result = expand_expression(expr)
        elif "simplify" in user_input:
            expr = user_input.replace("simplify", "").strip()
            result = simplify_expression(expr)
        elif "factor" in user_input:
            expr = user_input.replace("factor", "").strip()
            result = factor_expression(expr)
        elif "diff" in user_input:
            expr = user_input.replace("diff", "").strip()
            result = differentiate_expression(expr)
        elif "integrate" in user_input:
            expr = user_input.replace("integrate", "").strip()
            result = integrate_expression(expr)
        elif "matrix" in user_input:
            matrix1_str = Prompt.ask("Enter first matrix (e.g., [[1, 2], [3, 4]])")
            matrix2_str = Prompt.ask("Enter second matrix (or leave blank if not needed)")
            operation = Prompt.ask("Enter operation (+, -, *, det, inv, transpose)")
            matrix1 = eval(matrix1_str)
            matrix2 = eval(matrix2_str) if matrix2_str else None
            result = matrix_operations(matrix1, matrix2, operation)
        elif "geometry" in user_input:
            result = geometric_operations(user_input)
        else:
            result = evaluate_formula(user_input)

        console.print(f"[bold cyan]Result: {result}[/bold cyan]")

        cont = Prompt.ask("Do you want to perform another calculation? (yes/no)", choices=["yes", "no"]).strip().lower()
        if cont != "yes":
            console.print("[bold red]Thank you for using lcalc![/bold red]")
            break

calculator()