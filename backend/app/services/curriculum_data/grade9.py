# Grade 9 Mathematics Curriculum Data — Federal NCP 2022-23
# Strands: Number Systems, Matrices, Logarithms, Algebra & Geometry

GRADE_9_WORLDS = [
    {
        "title": "Matrix & Logarithm Nexus",
        "description": "Unlock complex arithmetic, evaluate logarithmic laws, and compute determinant matrices.",
        "grade": 9,
        "icon": "grid",
        "theme_color": "violet",
        "display_order": 1,
        "topics": [
            {
                "title": "Real & Complex Numbers, Radicals & Logarithms",
                "description": "Imaginary unit i, complex arithmetic, laws of logarithms, and scientific exponential notation.",
                "learning_objectives": [
                    "Perform operations with complex numbers (z = a + bi) and find conjugates",
                    "Apply laws of logarithms: log(xy), log(x/y), log(xⁿ), and change of base",
                    "Simplify radical expressions and solve logarithmic equations"
                ],
                "grade": 9,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Logarithmic & Complex Nexus",
                        "instructions": "Manipulate complex planes and evaluate logarithms using foundational laws.",
                        "category": "concept_exploration",
                        "difficulty": "medium",
                        "question_count": 8,
                        "xp_reward": 20,
                        "pass_percentage": 60,
                        "unlock_condition": "always",
                        "display_order": 1,
                        "is_boss": False,
                        "questions": [
                            {
                                "prompt": "What is the value of i² where i is the imaginary unit?",
                                "question_type": "multiple_choice",
                                "options": ["A) 1", "B) -1", "C) 0", "D) -i"],
                                "correct_answer": "B) -1",
                                "explanation": "By definition, the imaginary unit satisfies i = √(-1), which means i² = -1.",
                                "step_by_step_solution": [
                                    "Step 1: Definition of imaginary unit: i = √(-1).",
                                    "Step 2: i² = -1."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is the complex conjugate of z = 4 - 3i?",
                                "question_type": "multiple_choice",
                                "options": ["A) -4 - 3i", "B) -4 + 3i", "C) 4 + 3i", "D) 3 - 4i"],
                                "correct_answer": "C) 4 + 3i",
                                "explanation": "The conjugate of a - bi is a + bi. Thus, the conjugate of 4 - 3i is 4 + 3i.",
                                "step_by_step_solution": [
                                    "Step 1: To find the conjugate, reverse the sign of the imaginary part.",
                                    "Step 2: 4 - 3i -> 4 + 3i."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "According to the laws of logarithms, log_a(x · y) is equal to:",
                                "question_type": "multiple_choice",
                                "options": ["A) log_a(x) · log_a(y)", "B) log_a(x) + log_a(y)", "C) log_a(x) - log_a(y)", "D) y · log_a(x)"],
                                "correct_answer": "B) log_a(x) + log_a(y)",
                                "explanation": "Product law of logarithms: log_a(xy) = log_a(x) + log_a(y).",
                                "step_by_step_solution": [
                                    "Step 1: First law of logarithms states log(xy) = log(x) + log(y)."
                                ],
                                "difficulty": "easy",
                                "display_order": 3
                            },
                            {
                                "[Numeric Entry] prompt": "[Numeric Entry] Evaluate log_2(32). Enter the exact value:",
                                "prompt": "[Numeric Entry] Evaluate log_2(32). Enter the exact value:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "5",
                                "explanation": "Since 2⁵ = 32, log_2(32) = 5.",
                                "step_by_step_solution": [
                                    "Step 1: Write in exponential form: 2ʸ = 32.",
                                    "Step 2: 2⁵ = 32 => y = 5."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "Simplify: (2 + 3i) + (4 - 5i) =",
                                "question_type": "multiple_choice",
                                "options": ["A) 6 - 2i", "B) 6 + 2i", "C) 8 - 2i", "D) 6 - 8i"],
                                "correct_answer": "A) 6 - 2i",
                                "explanation": "Add real parts: 2 + 4 = 6. Add imaginary parts: 3i - 5i = -2i. Sum = 6 - 2i.",
                                "step_by_step_solution": [
                                    "Step 1: Real parts: 2 + 4 = 6.",
                                    "Step 2: Imaginary parts: 3i - 5i = -2i.",
                                    "Step 3: Combine: 6 - 2i."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] Solve for x:  log_3(x) = 4. Enter the value of x:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "81",
                                "explanation": "x = 3⁴ = 81.",
                                "step_by_step_solution": [
                                    "Step 1: Convert to exponential form: x = 3⁴.",
                                    "Step 2: 3 × 3 × 3 × 3 = 81."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "What is the product of (1 + i) and (1 - i)?",
                                "question_type": "multiple_choice",
                                "options": ["A) 0", "B) 1", "C) 2", "D) 2i"],
                                "correct_answer": "C) 2",
                                "explanation": "(1 + i)(1 - i) = 1² - i² = 1 - (-1) = 1 + 1 = 2.",
                                "step_by_step_solution": [
                                    "Step 1: Difference of squares: 1² - i².",
                                    "Step 2: Since i² = -1, 1 - (-1) = 2."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] If log_10(2) ≈ 0.3010, what is log_10(20)?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "1.301",
                                "explanation": "log_10(20) = log_10(2 × 10) = log_10(2) + log_10(10) = 0.3010 + 1 = 1.3010.",
                                "step_by_step_solution": [
                                    "Step 1: log(20) = log(2 × 10) = log(2) + log(10).",
                                    "Step 2: 0.3010 + 1 = 1.3010."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Matrices, Determinants & Cramer's Rule",
                "description": "Matrix operations, determinants of 2x2 matrices, multiplicative inverse, and Cramer's Rule.",
                "learning_objectives": [
                    "Perform matrix addition, subtraction, and multiplication",
                    "Evaluate determinants and identify singular matrices (det A = 0)",
                    "Solve systems of 2 linear equations using Cramer's rule"
                ],
                "grade": 9,
                "display_order": 2,
                "missions": [
                    {
                        "title": "The Determinant Matrix",
                        "instructions": "Compute matrix determinants and invert 2x2 matrices to stabilize the grid.",
                        "category": "practice",
                        "difficulty": "hard",
                        "question_count": 8,
                        "xp_reward": 20,
                        "pass_percentage": 60,
                        "unlock_condition": "always",
                        "display_order": 1,
                        "is_boss": False,
                        "questions": [
                            {
                                "prompt": "Evaluate the determinant of matrix A = [[3, 2], [1, 4]]:",
                                "question_type": "multiple_choice",
                                "options": ["A) 10", "B) 14", "C) 12", "D) -10"],
                                "correct_answer": "A) 10",
                                "explanation": "det(A) = ad - bc = (3 × 4) - (2 × 1) = 12 - 2 = 10.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: det = ad - bc.",
                                    "Step 2: (3 × 4) - (2 × 1) = 12 - 2 = 10."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "A square matrix A is called SINGULAR if its determinant is:",
                                "question_type": "multiple_choice",
                                "options": ["A) 1", "B) 0", "C) -1", "D) Positive"],
                                "correct_answer": "B) 0",
                                "explanation": "By definition, a singular matrix has a determinant equal to zero (and thus no multiplicative inverse).",
                                "step_by_step_solution": [
                                    "Step 1: Singular matrix definition: |A| = 0."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] Find the value of k such that matrix [[k, 8], [2, 4]] is singular:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "4",
                                "explanation": "det = 0 => (4k) - (8 × 2) = 0 => 4k = 16 => k = 4.",
                                "step_by_step_solution": [
                                    "Step 1: 4k - 16 = 0.",
                                    "Step 2: 4k = 16 => k = 4."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "What is the order (dimensions) of a matrix with 3 rows and 2 columns?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2 × 3", "B) 3 × 2", "C) 6 × 1", "D) 3 × 3"],
                                "correct_answer": "B) 3 × 2",
                                "explanation": "Order of a matrix is given as rows × columns: 3 × 2.",
                                "step_by_step_solution": [
                                    "Step 1: Rows come first, columns second: 3 × 2."
                                ],
                                "difficulty": "easy",
                                "display_order": 4
                            },
                            {
                                "prompt": "What is the multiplicative identity matrix of order 2 × 2?",
                                "question_type": "multiple_choice",
                                "options": ["A) [[0, 0], [0, 0]]", "B) [[1, 1], [1, 1]]", "C) [[1, 0], [0, 1]]", "D) [[0, 1], [1, 0]]"],
                                "correct_answer": "C) [[1, 0], [0, 1]]",
                                "explanation": "The 2×2 identity matrix I has 1s on the main diagonal and 0s elsewhere: [[1, 0], [0, 1]].",
                                "step_by_step_solution": [
                                    "Step 1: Identity matrix I = [[1, 0], [0, 1]]."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] Compute the determinant of matrix [[5, 3], [-2, 4]]:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "26",
                                "explanation": "det = (5 × 4) - (3 × (-2)) = 20 - (-6) = 20 + 6 = 26.",
                                "step_by_step_solution": [
                                    "Step 1: ad - bc = (5 × 4) - (3 × -2).",
                                    "Step 2: 20 - (-6) = 26."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "In Cramer's rule for the system 2x + y = 7 and x - y = 2, what is the determinant of the coefficient matrix D?",
                                "question_type": "multiple_choice",
                                "options": ["A) -3", "B) -1", "C) 3", "D) 1"],
                                "correct_answer": "A) -3",
                                "explanation": "D = [[2, 1], [1, -1]]. det(D) = (2 × -1) - (1 × 1) = -2 - 1 = -3.",
                                "step_by_step_solution": [
                                    "Step 1: Matrix D = [[2, 1], [1, -1]].",
                                    "Step 2: det(D) = 2(-1) - 1(1) = -2 - 1 = -3."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] Using Cramer's rule, if D = -3 and Dx = -9, what is the value of x?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "3",
                                "explanation": "x = Dx / D = (-9) / (-3) = 3.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: x = Dx / D.",
                                    "Step 2: x = -9 / -3 = 3."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 8
                            }
                        ]
                    },
                    {
                        "title": "Matrix Inversion & Cramer's Trial",
                        "instructions": "Invert matrices using adjugates and solve linear systems with Cramer's determinants.",
                        "category": "practice",
                        "difficulty": "hard",
                        "question_count": 8,
                        "xp_reward": 20,
                        "pass_percentage": 60,
                        "unlock_condition": "always",
                        "display_order": 2,
                        "is_boss": False,
                        "questions": [
                            {
                                "prompt": "For which value of k does the matrix [[2, k], [3, 6]] NOT have a multiplicative inverse?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2", "B) 3", "C) 4", "D) 6"],
                                "correct_answer": "C) 4",
                                "explanation": "Inverse does not exist when det = 0: (2 × 6) - (3k) = 0 => 12 - 3k = 0 => k = 4.",
                                "step_by_step_solution": [
                                    "Step 1: A matrix has no inverse if singular: det = 0.",
                                    "Step 2: 12 - 3k = 0 => 3k = 12 => k = 4."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "The transpose of a matrix A = [[1, 2], [3, 4]] is obtained by:",
                                "question_type": "multiple_choice",
                                "options": [
                                    "A) Interchanging rows and columns to get [[1, 3], [2, 4]]",
                                    "B) Changing signs of all elements",
                                    "C) Multiplying by -1",
                                    "D) Swapping diagonal elements only"
                                ],
                                "correct_answer": "A) Interchanging rows and columns to get [[1, 3], [2, 4]]",
                                "explanation": "Transposition interchanges rows into columns.",
                                "step_by_step_solution": [
                                    "Step 1: Row 1 [1, 2] becomes Column 1 [1, 2]ᵀ.",
                                    "Step 2: Row 2 [3, 4] becomes Column 2 [3, 4]ᵀ.",
                                    "Step 3: Transpose = [[1, 3], [2, 4]]."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] If det(A) = 5, what is the determinant of its inverse det(A⁻¹) as a decimal?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "0.2",
                                "explanation": "det(A⁻¹) = 1 / det(A) = 1 / 5 = 0.2.",
                                "step_by_step_solution": [
                                    "Step 1: Theorem: det(A⁻¹) = 1 / det(A).",
                                    "Step 2: 1 / 5 = 0.2."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "A square matrix is called SYMMETRIC if:",
                                "question_type": "multiple_choice",
                                "options": ["A) Aᵀ = -A", "B) Aᵀ = A", "C) det(A) = 0", "D) A² = I"],
                                "correct_answer": "B) Aᵀ = A",
                                "explanation": "A matrix is symmetric if it is equal to its transpose (Aᵀ = A).",
                                "step_by_step_solution": [
                                    "Step 1: Definition: Symmetric matrix satisfies Aᵀ = A."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "In Cramer's rule for 3x - 2y = 1 and 2x + y = 10, if D = 7 and Dy = 28, what is the value of y?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2", "B) 3", "C) 4", "D) 7"],
                                "correct_answer": "C) 4",
                                "explanation": "y = Dy / D = 28 / 7 = 4.",
                                "step_by_step_solution": [
                                    "Step 1: y = Dy / D.",
                                    "Step 2: 28 / 7 = 4."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] In the same system (D = 7, Dy = 28), if Dx = 21, what is the value of x?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "3",
                                "explanation": "x = Dx / D = 21 / 7 = 3.",
                                "step_by_step_solution": [
                                    "Step 1: x = Dx / D = 21 / 7 = 3."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "What is the product of matrix [[1, 0], [0, 1]] and any matrix M of the same order?",
                                "question_type": "multiple_choice",
                                "options": ["A) Zero matrix", "B) M", "C) M²", "D) -M"],
                                "correct_answer": "B) M",
                                "explanation": "The identity matrix I satisfies IM = MI = M.",
                                "step_by_step_solution": [
                                    "Step 1: I is the multiplicative identity: I × M = M."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] Compute the determinant of matrix A = [[-3, 5], [-2, 4]]:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "-2",
                                "explanation": "det = (-3 × 4) - (5 × (-2)) = -12 - (-10) = -12 + 10 = -2.",
                                "step_by_step_solution": [
                                    "Step 1: ad - bc = (-3 × 4) - (5 × -2).",
                                    "Step 2: -12 - (-10) = -2."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 8
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "title": "Cartesian & Deductive Ridge",
        "description": "Traverse coordinate geometry ridges, calculate distances, and apply polynomial theorems.",
        "grade": 9,
        "icon": "crosshair",
        "theme_color": "purple",
        "display_order": 2,
        "topics": [
            {
                "title": "Polynomial Theorems & Algebraic Formulas",
                "description": "Remainder theorem, factor theorem, factoring cubic expressions, and algebraic fractions.",
                "learning_objectives": [
                    "Use the Remainder Theorem to find remainders of polynomial divisions",
                    "Apply the Factor Theorem to determine roots and factors of polynomials",
                    "Simplify complex rational algebraic fractions"
                ],
                "grade": 9,
                "display_order": 1,
                "missions": [
                    {
                        "title": "The Remainder & Factor Redoubt",
                        "instructions": "Test polynomial factors and find remainders without performing long division.",
                        "category": "practice",
                        "difficulty": "hard",
                        "question_count": 8,
                        "xp_reward": 20,
                        "pass_percentage": 60,
                        "unlock_condition": "always",
                        "display_order": 1,
                        "is_boss": False,
                        "questions": [
                            {
                                "prompt": "By the Remainder Theorem, what is the remainder when P(x) = x² - 3x + 5 is divided by (x - 2)?",
                                "question_type": "multiple_choice",
                                "options": ["A) 1", "B) 3", "C) 5", "D) 7"],
                                "correct_answer": "B) 3",
                                "explanation": "Evaluate P(2): P(2) = 2² - 3(2) + 5 = 4 - 6 + 5 = 3.",
                                "step_by_step_solution": [
                                    "Step 1: Set divisor x - 2 = 0 => x = 2.",
                                    "Step 2: P(2) = 2² - 3(2) + 5 = 4 - 6 + 5 = 3."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "According to the Factor Theorem, (x - a) is a factor of polynomial P(x) if and only if:",
                                "question_type": "multiple_choice",
                                "options": ["A) P(a) = 1", "B) P(a) = 0", "C) P(0) = a", "D) P(a) > 0"],
                                "correct_answer": "B) P(a) = 0",
                                "explanation": "A linear term (x - a) is a factor if the remainder upon division is zero, meaning P(a) = 0.",
                                "step_by_step_solution": [
                                    "Step 1: Factor Theorem: (x - a) is a factor <=> P(a) = 0."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "Is (x - 1) a factor of P(x) = x³ - 4x² + 5x - 2?",
                                "question_type": "multiple_choice",
                                "options": ["A) Yes, because P(1) = 0", "B) No, because P(1) = 2", "C) No, because P(1) = -2", "D) Cannot be determined"],
                                "correct_answer": "A) Yes, because P(1) = 0",
                                "explanation": "P(1) = 1³ - 4(1)² + 5(1) - 2 = 1 - 4 + 5 - 2 = 0. Since P(1) = 0, (x - 1) is a factor.",
                                "step_by_step_solution": [
                                    "Step 1: Evaluate P(1) = 1 - 4 + 5 - 2 = 0.",
                                    "Step 2: P(1) = 0 confirms it is a factor."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] Find the remainder when P(x) = 2x³ - 5x + 7 is divided by (x - 1):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "4",
                                "explanation": "P(1) = 2(1)³ - 5(1) + 7 = 2 - 5 + 7 = 4.",
                                "step_by_step_solution": [
                                    "Step 1: P(1) = 2(1) - 5(1) + 7 = 4."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "Simplify the rational algebraic expression: (x² - 9) / (x + 3)",
                                "question_type": "multiple_choice",
                                "options": ["A) x - 3", "B) x + 3", "C) x - 9", "D) 1 / (x + 3)"],
                                "correct_answer": "A) x - 3",
                                "explanation": "x² - 9 = (x - 3)(x + 3). Dividing by (x + 3) leaves x - 3.",
                                "step_by_step_solution": [
                                    "Step 1: Factor numerator: (x - 3)(x + 3).",
                                    "Step 2: Cancel (x + 3) with denominator: x - 3."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] For what value of k will (x - 2) be a factor of P(x) = x² - kx + 6?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "5",
                                "explanation": "P(2) = 0 => 2² - 2k + 6 = 0 => 10 - 2k = 0 => 2k = 10 => k = 5.",
                                "step_by_step_solution": [
                                    "Step 1: P(2) = 4 - 2k + 6 = 0.",
                                    "Step 2: 10 - 2k = 0 => 2k = 10 => k = 5."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "What is the HCF of the algebraic expressions (x² - 4) and (x² - 4x + 4)?",
                                "question_type": "multiple_choice",
                                "options": ["A) x + 2", "B) x - 2", "C) (x - 2)²", "D) x² - 4"],
                                "correct_answer": "B) x - 2",
                                "explanation": "x² - 4 = (x - 2)(x + 2). x² - 4x + 4 = (x - 2)². The common factor is (x - 2).",
                                "step_by_step_solution": [
                                    "Step 1: Factorize first: (x - 2)(x + 2).",
                                    "Step 2: Factorize second: (x - 2)².",
                                    "Step 3: Common factor = (x - 2)."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] Evaluate the remainder when x⁴ - 16 is divided by (x + 2):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "0",
                                "explanation": "P(-2) = (-2)⁴ - 16 = 16 - 16 = 0.",
                                "step_by_step_solution": [
                                    "Step 1: Divisor x + 2 = 0 => x = -2.",
                                    "Step 2: (-2)⁴ - 16 = 16 - 16 = 0."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Coordinate Geometry & Parallelogram Theorems",
                "description": "Distance and midpoint formulas on the Cartesian plane, and deductive properties of parallelograms.",
                "learning_objectives": [
                    "Calculate the distance between two points using d = √((x₂-x₁)² + (y₂-y₁)²)",
                    "Find the midpoint of a line segment connecting two points",
                    "Apply theorems on congruent triangles and parallelograms"
                ],
                "grade": 9,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Coordinate & Theorem Outpost",
                        "instructions": "Map coordinates, measure Euclidean distances, and verify geometric theorems.",
                        "category": "concept_exploration",
                        "difficulty": "hard",
                        "question_count": 8,
                        "xp_reward": 20,
                        "pass_percentage": 60,
                        "unlock_condition": "always",
                        "display_order": 1,
                        "is_boss": False,
                        "questions": [
                            {
                                "prompt": "What is the distance between points (0, 0) and (3, 4)?",
                                "question_type": "multiple_choice",
                                "options": ["A) 5", "B) 7", "C) 12", "D) 25"],
                                "correct_answer": "A) 5",
                                "explanation": "Distance d = √((3 - 0)² + (4 - 0)²) = √(9 + 16) = √25 = 5.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: d = √((x₂-x₁)² + (y₂-y₁)²).",
                                    "Step 2: d = √(3² + 4²) = √(9 + 16) = √25 = 5."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What are the coordinates of the midpoint between (2, 4) and (6, 8)?",
                                "question_type": "multiple_choice",
                                "options": ["A) (4, 6)", "B) (3, 5)", "C) (8, 12)", "D) (4, 4)"],
                                "correct_answer": "A) (4, 6)",
                                "explanation": "Midpoint M = ((2 + 6)/2, (4 + 8)/2) = (8/2, 12/2) = (4, 6).",
                                "step_by_step_solution": [
                                    "Step 1: x_mid = (2 + 6) / 2 = 4.",
                                    "Step 2: y_mid = (4 + 8) / 2 = 6.",
                                    "Step 3: Midpoint = (4, 6)."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] Find the distance between points (1, 2) and (4, 6):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "5",
                                "explanation": "d = √((4 - 1)² + (6 - 2)²) = √(3² + 4²) = √(9 + 16) = 5.",
                                "step_by_step_solution": [
                                    "Step 1: Δx = 4 - 1 = 3.",
                                    "Step 2: Δy = 6 - 2 = 4.",
                                    "Step 3: d = √(3² + 4²) = √25 = 5."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "In any parallelogram, the diagonals:",
                                "question_type": "multiple_choice",
                                "options": ["A) Are equal in length", "B) Bisect each other", "C) Are perpendicular", "D) Are parallel"],
                                "correct_answer": "B) Bisect each other",
                                "explanation": "A fundamental theorem of parallelograms states that the diagonals bisect each other at their point of intersection.",
                                "step_by_step_solution": [
                                    "Step 1: Core theorem of Euclidean geometry: Parallelogram diagonals bisect each other."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "Which point lies on the line given by 2x - y = 5?",
                                "question_type": "multiple_choice",
                                "options": ["A) (2, 1)", "B) (3, 1)", "C) (1, 3)", "D) (4, 2)"],
                                "correct_answer": "B) (3, 1)",
                                "explanation": "Substitute (3, 1): 2(3) - 1 = 6 - 1 = 5. Verified.",
                                "step_by_step_solution": [
                                    "Step 1: Test (3, 1): 2(3) - 1 = 5. Matches equation."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] What is the x-coordinate of the midpoint between (-4, 5) and (8, 11)?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "2",
                                "explanation": "x = (-4 + 8) / 2 = 4 / 2 = 2.",
                                "step_by_step_solution": [
                                    "Step 1: (-4 + 8) / 2 = 4 / 2 = 2."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "In a parallelogram ABCD, if angle A is 70°, what is the measure of adjacent angle B?",
                                "question_type": "multiple_choice",
                                "options": ["A) 70°", "B) 90°", "C) 110°", "D) 120°"],
                                "correct_answer": "C) 110°",
                                "explanation": "Adjacent angles of a parallelogram are supplementary: 180° - 70° = 110°.",
                                "step_by_step_solution": [
                                    "Step 1: Adjacent angles sum to 180°.",
                                    "Step 2: 180° - 70° = 110°."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] What is the distance between points (-2, -3) and (6, 3)?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "10",
                                "explanation": "d = √((6 - (-2))² + (3 - (-3))²) = √(8² + 6²) = √(64 + 36) = √100 = 10.",
                                "step_by_step_solution": [
                                    "Step 1: Δx = 6 - (-2) = 8.",
                                    "Step 2: Δy = 3 - (-3) = 6.",
                                    "Step 3: d = √(8² + 6²) = √100 = 10."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 8
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
