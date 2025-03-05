# lcalc - Linux Calculator

lcalc is an advanced, feature-rich command-line calculator that supports a wide range of mathematical operations, from basic arithmetic to advanced algebra, calculus, trigonometry, matrix manipulations, and geometry operations. Designed with flexibility and precision in mind, lcalc leverages powerful libraries to provide accurate and efficient calculations.

---

## Features

- **Basic Arithmetic**: Perform addition, subtraction, multiplication, division, modulus, integer division, and exponentiation with high precision.
- **Algebra**: Solve equations, expand expressions, simplify formulas, and factorize polynomials.
- **Calculus**: Differentiate and integrate expressions with respect to variables.
- **Trigonometry**: Calculate sine, cosine, tangent, and their inverse functions with radian values.
- **Matrix Operations**:
  - Addition, subtraction, and multiplication of matrices.
  - Compute determinant, inverse, and transpose of matrices.
- **Geometry**:
  - Calculate distances, line equations, circle equations, polygon area, and perimeter.
  - Handle geometric shapes such as triangles, polygons, and circles.
- **User-Friendly Interface**: Interactive prompts powered by the `rich` library make it easy to input data and understand results.
- **Configurable Precision**: High-precision calculations enabled by the `decimal` module.

---

## Installation

Follow these simple steps to install and run `lcalc`:

1. Download the script:
   ```bash
   wget https://github.com/CalestialAshley35/lcalc/blob/main/lcalc.py
   ```
2. Run the script:
   ```bash
   python lcalc.py
   ```

**Note**: Ensure you have Python installed with the necessary libraries (`sympy`, `rich`, etc.). You can install them with pip:
```bash
pip install sympy rich
```

---

## Usage

Once you run the script, you will be greeted with the welcome message. You can then input a variety of mathematical operations. Below are some examples:

---

### Example Session

```plaintext
Welcome to lcalc (Linux Calculator)!
Supports: advanced algebra, calculus, trigonometry, matrices, geometry, and more.

Enter a formula, equation, or operation (e.g., 2.5 + 3.4, sin(pi/2), x^2 - 5x + 6 = 0): 3 + 5
Result: 8

Do you want to perform another calculation? (yes/no): yes

Enter a formula, equation, or operation (e.g., 2.5 + 3.4, sin(pi/2), x^2 - 5x + 6 = 0): x^2 - 5x + 6 = 0
Result: [2, 3]

Do you want to perform another calculation? (yes/no): yes

Enter a formula, equation, or operation (e.g., 2.5 + 3.4, sin(pi/2), x^2 - 5x + 6 = 0): diff(x**2 + 3*x + 2)
Result: 2*x + 3

Do you want to perform another calculation? (yes/no): no

Thank you for using lcalc!
```

---

## Supported Operations

### Basic Arithmetic
- Example: `3 + 5`, `10 / 2`, `2 ** 3`

### Algebra
- Solve Equations: `x^2 - 5x + 6 = 0`
- Expand Expressions: `expand((x + 1)**2)`
- Simplify Formulas: `simplify(x**2 + 2*x + 1)`
- Factorize Polynomials: `factor(x**2 - 4)`

### Calculus
- Differentiate: `diff(x**2 + 3*x + 2)`
- Integrate: `integrate(x**2)`

### Trigonometry
- Example: `sin(pi/2)`, `cos(pi)`, `tan(pi/4)`

### Matrices
- Input: `[[1, 2], [3, 4]]` for matrix operations.
- Operations: Add, subtract, multiply, determinant (`det`), inverse (`inv`), transpose (`transpose`).

### Geometry
- Calculate distances between points, line equations, circle equations, polygon area/perimeter, triangle properties, etc.

---

## License

This project is licensed under the **Apache License 2.0**. See the LICENSE file for more information.

---

## Contribution

Contributions are welcome! Feel free to fork the repository, create issues, or submit pull requests to enhance the functionality of `lcalc`.