markdown
# Conway's Prime Producing Machine (FRACTRAN GUI)

An interactive desktop GUI application implementing **John Horton Conway's Prime Producing Machine** using the **FRACTRAN** esoteric programming language.



## Overview

**FRACTRAN** is a Turing-complete esoteric programming language created by mathematician **John Horton Conway**.

The program operates on an ordered list of rational fractions and an integer register $N$. In Conway's 10-fraction configuration:

$$\left[ \frac{7}{3}, \frac{99}{98}, \frac{13}{49}, \frac{39}{35}, \frac{36}{91}, \frac{10}{143}, \frac{49}{13}, \frac{7}{11}, \frac{1}{2}, \frac{91}{1} \right]$$

Starting from initial accumulator $N = 10$, the algorithm iteratively multiplies $N$ by the first fraction in the list that yields an integer. Whenever the value of $N$ becomes an exact power of 10 ($10^p = 2^p \cdot 5^p$), the exponent $p$ corresponds to a **prime number**.



## Features

- **Tkinter GUI:** Centered desktop interface with customizable iteration steps.
- **Exact Fraction Arithmetic:** Uses Python's native `fractions.Fraction` to avoid floating-point errors.
- **Visual State Highlighting:** Identifies and highlights pure powers of 10 in red text.
- **Zero External Dependencies:** Built entirely with Python's standard library.



## Requirements & Setup

### Prerequisites

- Python 3.8+
- Tkinter (standard on Windows/macOS; on Debian/Ubuntu install via `sudo apt-get install python3-tk`)

### Installation & Run

bash
git clone https://github.com/YOUR_USERNAME/conway-prime-machine.git
cd conway-prime-machine
python main.py




## How It Works

1. Set the initial factor: $N = 10$.
2. In each iteration step, traverse the fraction sequence:
   $$L_F = \left[ \frac{7}{3}, \frac{99}{98}, \frac{13}{49}, \frac{39}{35}, \frac{36}{91}, \frac{10}{143}, \frac{49}{13}, \frac{7}{11}, \frac{1}{2}, \frac{91}{1} \right]$$
3. Find the first fraction $f$ where the product $N \times f$ has a denominator of $1$.
4. Update $N \leftarrow N \times f$.
5. If $N = 10^k$ ($k \ge 1$), format the printed output in red.
6. Continue until reaching the requested repetition limit.



## Project Structure

text
conway-prime-machine/
├── main.py
├── README.md
└── .gitignore




## References

- Conway, J. H. (1987). *FRACTRAN: A Simple Esoteric Programming Language for Number Theory*.
- [FRACTRAN - Wikipedia](https://en.wikipedia.org/wiki/FRACTRAN)
