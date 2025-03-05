# lcalc: Advanced Calculator for Linux

**lcalc** is a feature-rich, command-line-based calculator designed for Linux users. It supports a wide range of mathematical operations, including algebra, calculus, trigonometry, geometry, matrix computations, unit conversions, and more. The tool is designed for advanced users and developers seeking a powerful and flexible computation tool directly from the terminal.

## Features

- **Basic Arithmetic Operations:** Addition, subtraction, multiplication, division, modulus, integer division, and exponentiation.
- **Algebraic Computations:** Solve equations, expand, simplify, factorize expressions, and more.
- **Calculus Functions:** Differentiate and integrate mathematical expressions.
- **Trigonometry:** Evaluate sine, cosine, tangent, and other trigonometric functions.
- **Matrix Operations:** Perform matrix addition, subtraction, multiplication, determinant calculation, inversion, and transposition.
- **Geometric Calculations:**
  - Distance between points
  - Equations of lines and circles
  - Properties of polygons and triangles (e.g., area, perimeter)
- **Unit Conversions:**
  - Weight: Convert between kilograms, grams, pounds, and ounces.
  - Length: Convert between meters, centimeters, millimeters, kilometers, miles, yards, and feet.
- **Currency Conversion:** Get real-time currency conversions using forex data.

## Installation

To install lcalc, run the following command:

```bash
wget https://github.com/CalestialAshley35/lcalc/raw/main/lcalc.py
python lcalc.py
```

Ensure that Python 3 and the required libraries (`sympy`, `rich`, and `forex-python`) are installed on your system. You can install them via pip:

```bash
pip install sympy rich forex-python
```

## Usage

Launch `lcalc` by running:

```bash
python lcalc.py
```

Upon launch, you will be greeted with an interactive prompt. You can input a formula, equation, or operation to compute. Below are some examples of the supported commands:

### Arithmetic Operations

Input:
```
5 + 3
```
Output:
```
8
```

### Solving Equations

Input:
```
x^2 - 5x + 6 = 0
```
Output:
```
[2, 3]
```

### Expanding an Expression

Input:
```
expand (x + 2)^3
```
Output:
```
x**3 + 6*x**2 + 12*x + 8
```

### Simplifying Expressions

Input:
```
simplify (x^2 - 4) / (x - 2)
```
Output:
```
x + 2
```

### Differentiating a Function

Input:
```
diff x^2 + 3x
```
Output:
```
2*x + 3
```

### Integrating a Function

Input:
```
integrate x^2
```
Output:
```
x**3/3
```

### Matrix Operations

When prompted:
1. Enter the first matrix: `[[1, 2], [3, 4]]`
2. Enter the second matrix: `[[5, 6], [7, 8]]`
3. Choose an operation: `+`

Output:
```
Matrix([[6, 8], [10, 12]])
```

### Geometry

**Finding Distance Between Points:**
Input:
```
geometry distance
```
Follow prompts to input two points, e.g., `(1, 2)` and `(4, 6)`.
Output:
```
5.0
```

### Unit Conversions

**Convert Weight:**
Input:
```
weight conversion
```
Follow prompts to input value and units, e.g., `1 kg to lb`.
Output:
```
2.20462
```

**Convert Length:**
Input:
```
length conversion
```
Follow prompts to input value and units, e.g., `1 mile to km`.
Output:
```
1.60934
```

### Currency Conversion

Input:
```
currency conversion
```
Follow prompts to input the amount and currencies, e.g., `100 USD to EUR`.

## Example Session

```bash
Welcome to lcalc (Linux Calculator)!
Supports: advanced algebra, calculus, trigonometry, matrices, geometry, conversions, and more.

Enter a formula, equation, or operation: x^2 - 4x + 4 = 0
Result: [2]

Do you want to perform another calculation? (yes/no): yes

Enter a formula, equation, or operation: diff sin(x)
Result: cos(x)

Do you want to perform another calculation? (yes/no): no

Thank you for using lcalc!
```

## License

lcalc is licensed under the Apache License 2.0. You are free to use, modify, and distribute the software in compliance with the license.

For more details, refer to the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

---

**Note:** Ensure a stable internet connection for real-time currency conversion functionality.