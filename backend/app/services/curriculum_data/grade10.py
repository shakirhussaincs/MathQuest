# Grade 10 Mathematics Curriculum Data — Federal NCP 2022-23
# Strands: Advanced Algebra, Trigonometry, Geometry & Statistics/Probability

GRADE_10_WORLDS = [
    {
        "title": "Quadratic & Variation Volcano",
        "description": "Calculate discriminants over volcanic chasms, balance variations, and resolve partial fractions.",
        "grade": 10,
        "icon": "flame",
        "theme_color": "rose",
        "display_order": 1,
        "topics": [
            {
                "title": "Quadratic Equations, Discriminant & Roots",
                "description": "Standard quadratic formula, discriminant nature of roots, and symmetric relations of roots.",
                "learning_objectives": [
                    "Solve quadratic equations using the quadratic formula x = (-b ± √(b² - 4ac)) / (2a)",
                    "Classify the nature of roots using the discriminant Δ = b² - 4ac",
                    "Determine the sum (α + β = -b/a) and product (αβ = c/a) of roots"
                ],
                "grade": 10,
                "display_order": 1,
                "missions": [
                    {
                        "title": "The Quadratic Crucible",
                        "instructions": "Test discriminant values and formulate equations from given roots in the volcanic crucible.",
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
                                "prompt": "What is the discriminant formula for the quadratic equation ax² + bx + c = 0?",
                                "question_type": "multiple_choice",
                                "options": ["A) b² - 4ac", "B) b² + 4ac", "C) -b ± √(b² - 4ac)", "D) 4ac - b²"],
                                "correct_answer": "A) b² - 4ac",
                                "explanation": "The discriminant Δ is given by Δ = b² - 4ac.",
                                "step_by_step_solution": [
                                    "Step 1: In the quadratic formula, the expression under the square root is the discriminant.",
                                    "Step 2: Δ = b² - 4ac."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "If the discriminant Δ = b² - 4ac = 0, the roots of the quadratic equation are:",
                                "question_type": "multiple_choice",
                                "options": ["A) Real and distinct", "B) Real and equal", "C) Imaginary / Complex", "D) Irrational"],
                                "correct_answer": "B) Real and equal",
                                "explanation": "When Δ = 0, √(Δ) = 0, so both roots are -b / (2a), meaning real and equal (repeated).",
                                "step_by_step_solution": [
                                    "Step 1: Δ = 0 implies roots = -b/(2a) ± 0.",
                                    "Step 2: Both roots are identical: Real and equal."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] Find the discriminant of the quadratic equation: x² - 6x + 9 = 0:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "0",
                                "explanation": "a = 1, b = -6, c = 9. Δ = (-6)² - 4(1)(9) = 36 - 36 = 0.",
                                "step_by_step_solution": [
                                    "Step 1: a = 1, b = -6, c = 9.",
                                    "Step 2: Δ = (-6)² - 4(1)(9) = 36 - 36 = 0."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "For the equation 2x² - 8x + 5 = 0, what is the SUM of the roots (α + β)?",
                                "question_type": "multiple_choice",
                                "options": ["A) -4", "B) 4", "C) 5/2", "D) -5/2"],
                                "correct_answer": "B) 4",
                                "explanation": "Sum of roots α + β = -b/a = -(-8)/2 = 8/2 = 4.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: Sum = -b/a.",
                                    "Step 2: a = 2, b = -8.",
                                    "Step 3: -(-8) / 2 = 8 / 2 = 4."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] What is the PRODUCT of the roots of 3x² + 7x - 12 = 0?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "-4",
                                "explanation": "Product of roots αβ = c/a = (-12) / 3 = -4.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: Product = c/a.",
                                    "Step 2: c = -12, a = 3.",
                                    "Step 3: -12 / 3 = -4."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "If roots of a quadratic equation are 3 and -5, what is the quadratic equation?",
                                "question_type": "multiple_choice",
                                "options": ["A) x² + 2x - 15 = 0", "B) x² - 2x - 15 = 0", "C) x² + 8x - 15 = 0", "D) x² - 8x + 15 = 0"],
                                "correct_answer": "A) x² + 2x - 15 = 0",
                                "explanation": "Sum S = 3 + (-5) = -2. Product P = 3 × (-5) = -15. Equation: x² - Sx + P = x² - (-2)x + (-15) = x² + 2x - 15 = 0.",
                                "step_by_step_solution": [
                                    "Step 1: S = 3 + (-5) = -2.",
                                    "Step 2: P = 3 × (-5) = -15.",
                                    "Step 3: x² - Sx + P = 0 => x² + 2x - 15 = 0."
                                ],
                                "difficulty": "hard",
                                "display_order": 6
                            },
                            {
                                "prompt": "What is the nature of the roots of x² - 4x + 7 = 0?",
                                "question_type": "multiple_choice",
                                "options": ["A) Real and equal", "B) Real and distinct", "C) Imaginary / Complex conjugates", "D) Rational"],
                                "correct_answer": "C) Imaginary / Complex conjugates",
                                "explanation": "Δ = (-4)² - 4(1)(7) = 16 - 28 = -12. Since Δ < 0, roots are complex/imaginary.",
                                "step_by_step_solution": [
                                    "Step 1: Δ = b² - 4ac = 16 - 28 = -12.",
                                    "Step 2: Δ < 0 implies non-real, complex conjugate roots."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] Solve for the positive root of: x² - 5x - 6 = 0:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "6",
                                "explanation": "(x - 6)(x + 1) = 0 => x = 6 or x = -1. The positive root is 6.",
                                "step_by_step_solution": [
                                    "Step 1: Factorize: (x - 6)(x + 1) = 0.",
                                    "Step 2: x = 6 or x = -1.",
                                    "Step 3: Positive root = 6."
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
                "title": "Theory of Variations & Partial Fractions",
                "description": "Direct, inverse, and joint variations, constant of variation k, and partial fraction decomposition.",
                "learning_objectives": [
                    "Solve direct and inverse variation problems using proportionality constant k",
                    "Solve joint variation problems",
                    "Resolve proper rational algebraic fractions into partial fractions"
                ],
                "grade": 10,
                "display_order": 2,
                "missions": [
                    {
                        "title": "The Variation & Fractions Vault",
                        "instructions": "Determine variation constants and resolve complex rational fractions into simpler components.",
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
                                "prompt": "If y varies directly as x (y ∝ x) and y = 12 when x = 3, what is the constant of variation k?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2", "B) 3", "C) 4", "D) 36"],
                                "correct_answer": "C) 4",
                                "explanation": "y = kx => 12 = k(3) => k = 12 / 3 = 4.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: y = kx.",
                                    "Step 2: 12 = 3k => k = 4."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "[Numeric Entry] If y varies directly as x with k = 5, what is y when x = 8?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "40",
                                "explanation": "y = kx = 5 × 8 = 40.",
                                "step_by_step_solution": [
                                    "Step 1: y = 5 × 8 = 40."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 2
                            },
                            {
                                "prompt": "If y varies inversely as x (y ∝ 1/x) and y = 6 when x = 4, what is the value of y when x = 8?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2", "B) 3", "C) 4", "D) 12"],
                                "correct_answer": "B) 3",
                                "explanation": "y = k/x => k = xy = 4 × 6 = 24. When x = 8, y = 24 / 8 = 3.",
                                "step_by_step_solution": [
                                    "Step 1: k = x × y = 4 × 6 = 24.",
                                    "Step 2: When x = 8: y = 24 / 8 = 3."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "Which form represents the partial fractions of: 1 / ((x - 2)(x + 3))?",
                                "question_type": "multiple_choice",
                                "options": [
                                    "A) A / (x - 2) + B / (x + 3)",
                                    "B) (Ax + B) / ((x - 2)(x + 3))",
                                    "C) A / (x - 2)² + B / (x + 3)",
                                    "D) A / (x - 2) + B / (x - 2)²"
                                ],
                                "correct_answer": "A) A / (x - 2) + B / (x + 3)",
                                "explanation": "Distinct linear non-repeated factors in denominator decompose as A/(x - 2) + B/(x + 3).",
                                "step_by_step_solution": [
                                    "Step 1: The denominator has distinct linear factors.",
                                    "Step 2: Partial fractions form is A/(x - 2) + B/(x + 3)."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] In the identity: 1 / ((x - 1)(x + 1)) = A / (x - 1) + B / (x + 1), what is the value of A?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "0.5",
                                "explanation": "1 = A(x + 1) + B(x - 1). Put x = 1: 1 = A(2) => A = 1/2 = 0.5.",
                                "step_by_step_solution": [
                                    "Step 1: 1 = A(x + 1) + B(x - 1).",
                                    "Step 2: Substitute x = 1: 1 = A(1 + 1) + 0 => 2A = 1 => A = 0.5."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "If z varies jointly as x and y (z = kxy), and z = 36 when x = 3 and y = 4, what is the constant k?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2", "B) 3", "C) 4", "D) 6"],
                                "correct_answer": "B) 3",
                                "explanation": "36 = k(3)(4) => 12k = 36 => k = 3.",
                                "step_by_step_solution": [
                                    "Step 1: z = kxy => 36 = k(3)(4) = 12k.",
                                    "Step 2: k = 36 / 12 = 3."
                                ],
                                "difficulty": "medium",
                                "display_order": 6
                            },
                            {
                                "prompt": "A proper rational fraction is one in which the degree of numerator P(x) is:",
                                "question_type": "multiple_choice",
                                "options": [
                                    "A) Less than degree of denominator Q(x)",
                                    "B) Greater than degree of denominator Q(x)",
                                    "C) Equal to degree of denominator Q(x)",
                                    "D) Zero"
                                ],
                                "correct_answer": "A) Less than degree of denominator Q(x)",
                                "explanation": "A fraction P(x)/Q(x) is proper if deg(P) < deg(Q).",
                                "step_by_step_solution": [
                                    "Step 1: Definition: Proper rational fraction requires deg(Numerator) < deg(Denominator)."
                                ],
                                "difficulty": "easy",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] In the partial fraction decomposition of (5x + 1) / ((x + 1)(x - 1)) = A/(x + 1) + B/(x - 1), find the value of B:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "3",
                                "explanation": "5x + 1 = A(x - 1) + B(x + 1). Put x = 1: 5(1) + 1 = B(2) => 6 = 2B => B = 3.",
                                "step_by_step_solution": [
                                    "Step 1: 5x + 1 = A(x - 1) + B(x + 1).",
                                    "Step 2: Substitute x = 1: 6 = 2B => B = 3."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 8
                            }
                        ]
                    },
                    {
                        "title": "Partial Fractions & Variations Mastery",
                        "instructions": "Decompose quadratic factors and analyze inverse square proportions in the volcano archive.",
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
                                "prompt": "When resolving 1 / ((x - 1)(x + 2)²), which partial fraction terms must be included for the repeated factor (x + 2)²?",
                                "question_type": "multiple_choice",
                                "options": [
                                    "A) B / (x + 2) + C / (x + 2)²",
                                    "B) B / (x + 2)² only",
                                    "C) (Bx + C) / (x + 2)",
                                    "D) B / (x - 2) + C / (x + 2)"
                                ],
                                "correct_answer": "A) B / (x + 2) + C / (x + 2)²",
                                "explanation": "For a repeated linear factor (x - a)², partial fractions require both terms: A/(x - a) + B/(x - a)².",
                                "step_by_step_solution": [
                                    "Step 1: Repeated linear factor rule.",
                                    "Step 2: Include power 1 and power 2: B/(x + 2) + C/(x + 2)²."
                                ],
                                "difficulty": "medium",
                                "display_order": 1
                            },
                            {
                                "prompt": "If y varies inversely as the square of x (y ∝ 1/x²) and y = 16 when x = 2, what is the constant k?",
                                "question_type": "multiple_choice",
                                "options": ["A) 32", "B) 48", "C) 64", "D) 8"],
                                "correct_answer": "C) 64",
                                "explanation": "y = k / x² => k = yx² = 16 × 2² = 16 × 4 = 64.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: y = k / x².",
                                    "Step 2: k = y × x² = 16 × 4 = 64."
                                ],
                                "difficulty": "medium",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] Using the same variation (y = 64 / x²), what is y when x = 4?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "4",
                                "explanation": "y = 64 / 4² = 64 / 16 = 4.",
                                "step_by_step_solution": [
                                    "Step 1: y = 64 / 16 = 4."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "For an irreducible quadratic factor (x² + 1) in the denominator, the corresponding partial fraction numerator must be of the form:",
                                "question_type": "multiple_choice",
                                "options": ["A) A (constant)", "B) Ax + B (linear)", "C) Ax² + B", "D) A / x"],
                                "correct_answer": "B) Ax + B (linear)",
                                "explanation": "An irreducible quadratic factor of degree 2 requires a linear numerator of degree 1 (Ax + B).",
                                "step_by_step_solution": [
                                    "Step 1: Quadratic factor rule: Numerator has degree 1 less than denominator.",
                                    "Step 2: Form = (Ax + B) / (x² + 1)."
                                ],
                                "difficulty": "hard",
                                "display_order": 4
                            },
                            {
                                "prompt": "If α and β are the roots of x² - 6x + 8 = 0, what is the value of α + β?",
                                "question_type": "multiple_choice",
                                "options": ["A) -6", "B) 6", "C) 8", "D) -8"],
                                "correct_answer": "B) 6",
                                "explanation": "Sum of roots = -b/a = -(-6)/1 = 6.",
                                "step_by_step_solution": [
                                    "Step 1: α + β = -b/a = -(-6)/1 = 6."
                                ],
                                "difficulty": "easy",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] If α + β = 6 and αβ = 8, what is the value of α² + β²?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "20",
                                "explanation": "α² + β² = (α + β)² - 2αβ = 6² - 2(8) = 36 - 16 = 20.",
                                "step_by_step_solution": [
                                    "Step 1: Identity: α² + β² = (α + β)² - 2αβ.",
                                    "Step 2: 6² - 2(8) = 36 - 16 = 20."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "If force F varies inversely as the square of distance d (F ∝ 1/d²), what happens to F if the distance d is DOUBLED?",
                                "question_type": "multiple_choice",
                                "options": [
                                    "A) F doubles",
                                    "B) F is halved",
                                    "C) F decreases by a factor of 4 (one-fourth)",
                                    "D) F stays the same"
                                ],
                                "correct_answer": "C) F decreases by a factor of 4 (one-fourth)",
                                "explanation": "When d is replaced by 2d: (2d)² = 4d², so F becomes 1/4 of its original value.",
                                "step_by_step_solution": [
                                    "Step 1: F₁ = k / d².",
                                    "Step 2: F₂ = k / (2d)² = k / (4d²) = (1/4)F₁."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] What is the constant term c in the quadratic equation x² - 7x + c = 0 if one root is 3 and the other root is 4?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "12",
                                "explanation": "Product of roots c = α × β = 3 × 4 = 12.",
                                "step_by_step_solution": [
                                    "Step 1: Product of roots = c/a = c/1.",
                                    "Step 2: 3 × 4 = 12 => c = 12."
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
        "title": "Trigonometric & Circle Summit",
        "description": "Prove Pythagorean trigonometric identities, solve angle of elevation heights, and master circle theorems.",
        "grade": 10,
        "icon": "globe",
        "theme_color": "emerald",
        "display_order": 2,
        "topics": [
            {
                "title": "Trigonometric Identities & Heights/Distances",
                "description": "Pythagorean identities (sin²θ + cos²θ = 1), right triangle trigonometry, and angles of elevation/depression.",
                "learning_objectives": [
                    "Prove and apply identities: sin²θ + cos²θ = 1, 1 + tan²θ = sec²θ, 1 + cot²θ = csc²θ",
                    "Evaluate trigonometric ratios for standard angles (0°, 30°, 45°, 60°, 90°)",
                    "Solve real-world problems involving angles of elevation and depression"
                ],
                "grade": 10,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Trigonometric Peak",
                        "instructions": "Ascend the summit by verifying circular identities and calculating heights from observation angles.",
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
                                "prompt": "Which of the following is a fundamental Pythagorean trigonometric identity?",
                                "question_type": "multiple_choice",
                                "options": [
                                    "A) sin²θ - cos²θ = 1",
                                    "B) sin²θ + cos²θ = 1",
                                    "C) tan²θ - 1 = sec²θ",
                                    "D) sinθ + cosθ = 1"
                                ],
                                "correct_answer": "B) sin²θ + cos²θ = 1",
                                "explanation": "From the Pythagorean theorem on the unit circle: sin²θ + cos²θ = 1.",
                                "step_by_step_solution": [
                                    "Step 1: Fundamental identity: sin²θ + cos²θ = 1."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is the exact value of tan(45°)?",
                                "question_type": "multiple_choice",
                                "options": ["A) 0", "B) 1/2", "C) 1", "D) √3"],
                                "correct_answer": "C) 1",
                                "explanation": "In an isosceles right triangle with 45°: opposite = adjacent, so tan(45°) = 1.",
                                "step_by_step_solution": [
                                    "Step 1: tan(45°) = sin(45°) / cos(45°) = (1/√2) / (1/√2) = 1."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "Simplify: 1 + tan²θ =",
                                "question_type": "multiple_choice",
                                "options": ["A) cot²θ", "B) sec²θ", "C) csc²θ", "D) cos²θ"],
                                "correct_answer": "B) sec²θ",
                                "explanation": "Divide sin²θ + cos²θ = 1 by cos²θ gives tan²θ + 1 = sec²θ.",
                                "step_by_step_solution": [
                                    "Step 1: 1 + tan²θ = 1 + sin²θ/cos²θ = (cos²θ + sin²θ)/cos²θ = 1/cos²θ = sec²θ."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "From a point on the ground 30 meters from the base of a tower, the angle of elevation to the top of the tower is 45°. What is the height of the tower?",
                                "question_type": "multiple_choice",
                                "options": ["A) 15 m", "B) 30 m", "C) 30√3 m", "D) 60 m"],
                                "correct_answer": "B) 30 m",
                                "explanation": "tan(45°) = Height / Distance => 1 = Height / 30 => Height = 30 meters.",
                                "step_by_step_solution": [
                                    "Step 1: tan(θ) = Opposite / Adjacent.",
                                    "Step 2: tan(45°) = Height / 30.",
                                    "Step 3: 1 = Height / 30 => Height = 30 m."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] If cos(θ) = 3/5, what is the value of 5 × sin(θ) for an acute angle θ?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "4",
                                "explanation": "sin²θ = 1 - cos²θ = 1 - 9/25 = 16/25 => sinθ = 4/5. 5 × (4/5) = 4.",
                                "step_by_step_solution": [
                                    "Step 1: sinθ = √(1 - (3/5)²) = √(16/25) = 4/5.",
                                    "Step 2: 5 × (4/5) = 4."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "What is 1 + cot²θ equal to?",
                                "question_type": "multiple_choice",
                                "options": ["A) tan²θ", "B) sec²θ", "C) csc²θ", "D) sin²θ"],
                                "correct_answer": "C) csc²θ",
                                "explanation": "1 + cot²θ = csc²θ (cosecant squared).",
                                "step_by_step_solution": [
                                    "Step 1: Identity: 1 + cot²θ = csc²θ."
                                ],
                                "difficulty": "medium",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] Evaluate: sin²(60°) + cos²(60°) = (Enter the numerical value):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "1",
                                "explanation": "By the Pythagorean identity, sin²θ + cos²θ = 1 for any angle θ.",
                                "step_by_step_solution": [
                                    "Step 1: (√3/2)² + (1/2)² = 3/4 + 1/4 = 1."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "An observer on top of a 50-meter cliff looks down at a boat on the sea. The angle of depression is 30°. How far is the boat from the base of the cliff? (Use tan(30°) = 1/√3 ≈ 0.577)",
                                "question_type": "multiple_choice",
                                "options": ["A) 50 m", "B) 50√3 m (≈ 86.6 m)", "C) 100 m", "D) 25√3 m"],
                                "correct_answer": "B) 50√3 m (≈ 86.6 m)",
                                "explanation": "tan(30°) = Height / Distance => 1/√3 = 50 / d => d = 50√3 m ≈ 86.6 m.",
                                "step_by_step_solution": [
                                    "Step 1: Angle of depression = angle of elevation from boat = 30°.",
                                    "Step 2: tan(30°) = 50 / d => 1/√3 = 50 / d.",
                                    "Step 3: d = 50√3 m."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Circle Theorems & Grouped Statistics",
                "description": "Chords, tangents, perpendicular bisectors of circles, and calculating grouped mean and variance.",
                "learning_objectives": [
                    "Apply circle theorems regarding chords, perpendicular bisectors, and tangents",
                    "Understand that a tangent to a circle is perpendicular to the radius at the point of contact",
                    "Calculate the mean and standard deviation for grouped frequency distributions"
                ],
                "grade": 10,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Circle & Variance Observatory",
                        "instructions": "Verify chord-tangent theorems and evaluate grouped distribution variance in the observatory.",
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
                                "prompt": "A straight line drawn from the center of a circle to bisect a chord (which is not a diameter) is:",
                                "question_type": "multiple_choice",
                                "options": ["A) Parallel to the chord", "B) Perpendicular to the chord", "C) Tangent to the chord", "D) Equal to the chord"],
                                "correct_answer": "B) Perpendicular to the chord",
                                "explanation": "A fundamental theorem states: The line segment joining the center of a circle to the midpoint of a chord is perpendicular to the chord.",
                                "step_by_step_solution": [
                                    "Step 1: Circle Theorem: Line from center bisecting chord is at right angles (perpendicular) to it."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is the angle between a tangent to a circle and the radius drawn to the point of contact?",
                                "question_type": "multiple_choice",
                                "options": ["A) 45°", "B) 60°", "C) 90°", "D) 180°"],
                                "correct_answer": "C) 90°",
                                "explanation": "A tangent at any point on a circle is perpendicular (90°) to the radius through the point of contact.",
                                "step_by_step_solution": [
                                    "Step 1: Tangent-radius theorem: Angle = 90 degrees."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] A chord of length 16 cm is at a distance of 6 cm from the center of a circle. What is the radius of the circle in cm?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "10",
                                "explanation": "Half chord = 8 cm. Distance = 6 cm. r² = 8² + 6² = 64 + 36 = 100 => r = 10 cm.",
                                "step_by_step_solution": [
                                    "Step 1: Perpendicular from center bisects chord: 16 / 2 = 8 cm.",
                                    "Step 2: Right triangle: r² = 8² + 6² = 64 + 36 = 100.",
                                    "Step 3: r = 10 cm."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "In grouped frequency data, what is the formula for the arithmetic mean (X̄)?",
                                "question_type": "multiple_choice",
                                "options": ["A) Σf / Σx", "B) Σ(fx) / Σf", "C) Σ(fx) / N²", "D) Σf × Σx"],
                                "correct_answer": "B) Σ(fx) / Σf",
                                "explanation": "Grouped mean = Sum of (frequency × class mark) divided by the sum of frequencies: Σ(fx) / Σf.",
                                "step_by_step_solution": [
                                    "Step 1: Formula for grouped mean: X̄ = Σ(fx) / Σf."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "From an external point P, two tangents PA and PB are drawn to a circle. The lengths of PA and PB are:",
                                "question_type": "multiple_choice",
                                "options": ["A) Equal", "B) Unequal", "C) Reciprocal", "D) Perpendicular"],
                                "correct_answer": "A) Equal",
                                "explanation": "Tangents drawn to a circle from an external point are equal in length (PA = PB).",
                                "step_by_step_solution": [
                                    "Step 1: Theorem: Tangents from an external point to a circle are congruent."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] A grouped dataset has Σ(fx) = 1,440 and Σf = 40. What is the mean of the data?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "36",
                                "explanation": "Mean = 1,440 / 40 = 36.",
                                "step_by_step_solution": [
                                    "Step 1: Mean = 1,440 / 40 = 36."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "The angle subtended by an arc at the center of a circle is _____ the angle subtended by it at any point on the remaining circumference.",
                                "question_type": "multiple_choice",
                                "options": ["A) Equal to", "B) Half of", "C) Double (twice)", "D) Four times"],
                                "correct_answer": "C) Double (twice)",
                                "explanation": "The central angle theorem states that the angle at the center is double the angle subtended at the circumference.",
                                "step_by_step_solution": [
                                    "Step 1: Inscribed angle theorem: Central angle = 2 × Inscribed angle."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] If the angle subtended by an arc at the center of a circle is 110°, what is the angle subtended by the same arc at the circumference in degrees?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "55",
                                "explanation": "Angle at circumference = Central angle / 2 = 110° / 2 = 55°.",
                                "step_by_step_solution": [
                                    "Step 1: 110 / 2 = 55°."
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
