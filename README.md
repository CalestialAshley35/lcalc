# lcalc: Advanced Linux Calculator

**lcalc** is a comprehensive command-line tool for performing advanced mathematical and geometric calculations. It is designed to handle a wide range of operations, including basic arithmetic, algebra, calculus, trigonometry, matrix manipulations, and geometry. Built with Python, **lcalc** leverages libraries like `sympy`, `decimal`, and `rich` for precision and an elegant user interface.

---

## Features

- **Arithmetic Operations**: Perform addition, subtraction, multiplication, division, exponentiation, modulus, and floor division with high precision using Python's `Decimal` module.
- **Algebra**: Solve equations, expand, simplify, and factor expressions.
- **Calculus**: Differentiate and integrate mathematical expressions symbolically.
- **Trigonometry**: Handle trigonometric functions like sine, cosine, tangent, and their inverses.
- **Matrix Operations**: Add, subtract, multiply matrices, compute determinants, find matrix inverses, and transpose matrices.
- **Geometry**: Work with points, lines, circles, polygons, and triangles to calculate distances, equations, areas, and perimeters.
- **Custom Precision**: Configure precision for calculations (up to 50 decimal places).
- **Interactive User Interface**: Intuitive command-line prompts powered by the `rich` library.

---

## Installation

To install **lcalc**, follow these steps:

1. Download the script:
   ```bash
   wget https://github.com/CalestialAshley35/lcalc/raw/main/lcalc.py
   ```

2. Run the script:
   ```bash
   python lcalc.py
   ```

---

## Usage

Once installed, launch the calculator by executing the script. You will be greeted with an interactive interface to perform various types of calculations.

### Examples of Supported Operations:

#### Basic Arithmetic:
```plaintext
Input: 2.5 + 3.4
Result: 5.9
```

#### Algebra:
- **Solving an equation**:
  ```plaintext
  Input: x^2 - 5x + 6 = 0
  Result: [2, 3]
  ```

- **Expanding an expression**:
  ```plaintext
  Input: expand (x + 2)^2
  Result: x**2 + 4*x + 4
  ```

- **Simplifying an expression**:
  ```plaintext
  Input: simplify x^2 - 2x + x
  Result: x**2 - x
  ```

- **Factoring an expression**:
  ```plaintext
  Input: factor x^2 - 4
  Result: (x - 2)*(x + 2)
  ```

#### Calculus:
- **Differentiating an expression**:
  ```plaintext
  Input: diff x^3 + 3x^2
  Result: 3*x**2 + 6*x
  ```

- **Integrating an expression**:
  ```plaintext
  Input: integrate x^2
  Result: x**3/3
  ```

#### Matrices:
- **Matrix addition**:
  ```plaintext
  Input: matrix [[1, 2], [3, 4]] + [[5, 6], [7, 8]]
  Result: Matrix([[6, 8], [10, 12]])
  ```

- **Determinant of a matrix**:
  ```plaintext
  Input: matrix [[1, 2], [3, 4]] det
  Result: -2
  ```

#### Geometry:
- **Distance between points**:
  ```plaintext
  Input: geometry distance
  Coordinates for point 1: (0, 0)
  Coordinates for point 2: (3, 4)
  Result: 5.0
  ```

- **Equation of a line through two points**:
  ```plaintext
  Input: geometry line
  Coordinates for point 1: (0, 0)
  Coordinates for point 2: (3, 4)
  Result: -4*x + 3*y
  ```

---

## Example Session

Below is an example interaction with **lcalc**:

```plaintext
Welcome to lcalc (Linux Calculator)!
Supports: advanced algebra, calculus, trigonometry, matrices, geometry, and more.

Enter a formula, equation, or operation (e.g., 2.5 + 3.4, sin(pi/2), x^2 - 5x + 6 = 0): x^2 - 5x + 6 = 0
Result: [2, 3]

Do you want to perform another calculation? (yes/no): yes
Enter a formula, equation, or operation (e.g., 2.5 + 3.4, sin(pi/2), x^2 - 5x + 6 = 0): geometry distance
Enter coordinates for point 1 (e.g., (x1, y1)): (0, 0)
Enter coordinates for point 2 (e.g., (x2, y2)): (3, 4)
Result: 5.0

Do you want to perform another calculation? (yes/no): no
Thank you for using lcalc!
```

---

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) file for details.