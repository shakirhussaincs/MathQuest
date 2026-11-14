# Grade 8 Mathematics Curriculum Data — Federal NCP 2022-23
# Strands: Real Numbers, Algebra, Geometry, Mensuration & Information Handling

GRADE_8_WORLDS = [
    {
        "title": "Real Numbers & Algebra Keep",
        "description": "Master square roots by division, unlock algebraic identity armories, and solve simultaneous systems.",
        "grade": 8,
        "icon": "cpu",
        "theme_color": "blue",
        "display_order": 1,
        "topics": [
            {
                "title": "Real Numbers, Squares, Roots & Cubes",
                "description": "Rational and irrational numbers, square roots by division method, and cube roots.",
                "learning_objectives": [
                    "Distinguish between rational and irrational numbers",
                    "Compute square roots of numbers and decimals using the division method",
                    "Calculate cubes and cube roots of perfect cubes"
                ],
                "grade": 8,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Square Root Spire",
                        "instructions": "Ascend the spire by evaluating square roots, cube roots, and identifying irrational numbers.",
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
                                "prompt": "Which of these numbers is an IRRATIONAL number?",
                                "question_type": "multiple_choice",
                                "options": ["A) √4", "B) √9", "C) √7", "D) 3/5"],
                                "correct_answer": "C) √7",
                                "explanation": "7 is not a perfect square, so √7 cannot be expressed as a fraction of integers. It is irrational.",
                                "step_by_step_solution": [
                                    "Step 1: √4 = 2 (Rational).",
                                    "Step 2: √9 = 3 (Rational).",
                                    "Step 3: √7 is a non-terminating, non-repeating decimal (Irrational)."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "[Numeric Entry] What is the square root of 576?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "24",
                                "explanation": "24 × 24 = 576. So √576 = 24.",
                                "step_by_step_solution": [
                                    "Step 1: 20² = 400, 30² = 900.",
                                    "Step 2: Ends in 6, so last digit is 4 or 6.",
                                    "Step 3: 24 × 24 = 576."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 2
                            },
                            {
                                "prompt": "What is the cube root of 216 (∛216)?",
                                "question_type": "multiple_choice",
                                "options": ["A) 4", "B) 6", "C) 8", "D) 16"],
                                "correct_answer": "B) 6",
                                "explanation": "6 × 6 × 6 = 216. Therefore, ∛216 = 6.",
                                "step_by_step_solution": [
                                    "Step 1: 6 × 6 = 36.",
                                    "Step 2: 36 × 6 = 216.",
                                    "Step 3: ∛216 = 6."
                                ],
                                "difficulty": "easy",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] Find the square root of 1.44:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "1.2",
                                "explanation": "√(1.44) = √(144/100) = 12/10 = 1.2.",
                                "step_by_step_solution": [
                                    "Step 1: 1.44 = 144 / 100.",
                                    "Step 2: √144 = 12, √100 = 10.",
                                    "Step 3: 12 / 10 = 1.2."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "Between which two consecutive whole numbers does √50 lie?",
                                "question_type": "multiple_choice",
                                "options": ["A) 5 and 6", "B) 6 and 7", "C) 7 and 8", "D) 8 and 9"],
                                "correct_answer": "C) 7 and 8",
                                "explanation": "7² = 49 and 8² = 64. Since 49 < 50 < 64, √50 lies between 7 and 8.",
                                "step_by_step_solution": [
                                    "Step 1: 7² = 49.",
                                    "Step 2: 8² = 64.",
                                    "Step 3: 49 < 50 < 64 => 7 < √50 < 8."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] Evaluate: ∛(-64) = (Enter the integer value):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "-4",
                                "explanation": "(-4) × (-4) × (-4) = -64. So ∛(-64) = -4.",
                                "step_by_step_solution": [
                                    "Step 1: Cube root of a negative number is negative.",
                                    "Step 2: (-4)³ = -64 => ∛(-64) = -4."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "What is the smallest positive integer by which 72 must be multiplied to make it a perfect square?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2", "B) 3", "C) 4", "D) 6"],
                                "correct_answer": "A) 2",
                                "explanation": "72 = 2³ × 3² = 2² × 3² × 2. The factor 2 is unpaired. Multiplying by 2 makes 144 = 12², a perfect square.",
                                "step_by_step_solution": [
                                    "Step 1: Prime factorization of 72: 2 × 2 × 2 × 3 × 3.",
                                    "Step 2: Pairs: (2 × 2) and (3 × 3). One 2 is left over.",
                                    "Step 3: Must multiply by 2."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] A square lawn has an area of 1,225 m². What is the length of one side in meters?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "35",
                                "explanation": "Side = √1225. 35 × 35 = 1,225 m.",
                                "step_by_step_solution": [
                                    "Step 1: Side = √Area = √1225.",
                                    "Step 2: 35 × 35 = 1225."
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
                "title": "Algebraic Identities & Simultaneous Equations",
                "description": "Standard identities, factoring quadratics by splitting the middle term, and simultaneous equations.",
                "learning_objectives": [
                    "Apply (a ± b)², a² - b², and (a ± b)³ algebraic identities",
                    "Factorize quadratic trinomials by splitting the middle term",
                    "Solve simultaneous linear equations in two variables"
                ],
                "grade": 8,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Identities Armory",
                        "instructions": "Forge quadratic trinomials and deploy expansion identities in the armory.",
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
                                "prompt": "Expand using an identity: (x + 5)² =",
                                "question_type": "multiple_choice",
                                "options": ["A) x² + 25", "B) x² + 10x + 25", "C) x² + 5x + 25", "D) 2x + 10"],
                                "correct_answer": "B) x² + 10x + 25",
                                "explanation": "(a + b)² = a² + 2ab + b² = x² + 2(x)(5) + 5² = x² + 10x + 25.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: (a + b)² = a² + 2ab + b².",
                                    "Step 2: a = x, b = 5.",
                                    "Step 3: x² + 2(x)(5) + 25 = x² + 10x + 25."
                                ],
                                "common_mistakes": {
                                    "x² + 25": "Do not forget the middle term 2ab!"
                                },
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Factorize: x² - 49",
                                "question_type": "multiple_choice",
                                "options": ["A) (x - 7)²", "B) (x + 7)(x - 7)", "C) (x - 49)(x + 1)", "D) x(x - 49)"],
                                "correct_answer": "B) (x + 7)(x - 7)",
                                "explanation": "Difference of squares: a² - b² = (a + b)(a - b) = (x + 7)(x - 7).",
                                "step_by_step_solution": [
                                    "Step 1: x² - 7² = (x + 7)(x - 7)."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "Factorize the quadratic trinomial: x² + 7x + 12",
                                "question_type": "multiple_choice",
                                "options": ["A) (x + 2)(x + 6)", "B) (x + 3)(x + 4)", "C) (x + 1)(x + 12)", "D) (x - 3)(x - 4)"],
                                "correct_answer": "B) (x + 3)(x + 4)",
                                "explanation": "Find two numbers whose product is 12 and sum is 7: 3 and 4. (x + 3)(x + 4).",
                                "step_by_step_solution": [
                                    "Step 1: Factors of 12 that add to 7 are 3 and 4.",
                                    "Step 2: Split middle term: x² + 3x + 4x + 12.",
                                    "Step 3: Group: x(x + 3) + 4(x + 3) = (x + 3)(x + 4)."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "[Numeric Entry] prompt": "[Numeric Entry] If a + b = 9 and ab = 20, what is the value of a² + b²?",
                                "prompt": "[Numeric Entry] If a + b = 9 and ab = 20, what is the value of a² + b²?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "41",
                                "explanation": "a² + b² = (a + b)² - 2ab = 9² - 2(20) = 81 - 40 = 41.",
                                "step_by_step_solution": [
                                    "Step 1: (a + b)² = a² + b² + 2ab.",
                                    "Step 2: a² + b² = (a + b)² - 2ab.",
                                    "Step 3: 81 - 2(20) = 81 - 40 = 41."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "Factorize: x² - 5x + 6",
                                "question_type": "multiple_choice",
                                "options": ["A) (x - 2)(x - 3)", "B) (x + 2)(x + 3)", "C) (x - 1)(x - 6)", "D) (x + 1)(x - 6)"],
                                "correct_answer": "A) (x - 2)(x - 3)",
                                "explanation": "Product is +6 and sum is -5: (-2) × (-3) = 6, and (-2) + (-3) = -5. (x - 2)(x - 3).",
                                "step_by_step_solution": [
                                    "Step 1: Find factors of 6 adding to -5: -2 and -3.",
                                    "Step 2: (x - 2)(x - 3)."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] Evaluate 102² using the algebraic identity (100 + 2)²:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "10404",
                                "explanation": "(100 + 2)² = 100² + 2(100)(2) + 2² = 10,000 + 400 + 4 = 10,404.",
                                "step_by_step_solution": [
                                    "Step 1: a = 100, b = 2.",
                                    "Step 2: 10,000 + 400 + 4 = 10,404."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "Factorize: 2x² + 5x + 3",
                                "question_type": "multiple_choice",
                                "options": ["A) (2x + 1)(x + 3)", "B) (2x + 3)(x + 1)", "C) (x + 1)(x + 3)", "D) (2x - 3)(x - 1)"],
                                "correct_answer": "B) (2x + 3)(x + 1)",
                                "explanation": "2 × 3 = 6. Factors of 6 that add to 5 are 2 and 3: 2x² + 2x + 3x + 3 = 2x(x + 1) + 3(x + 1) = (2x + 3)(x + 1).",
                                "step_by_step_solution": [
                                    "Step 1: a × c = 2 × 3 = 6.",
                                    "Step 2: Split 5x as 2x + 3x.",
                                    "Step 3: 2x(x + 1) + 3(x + 1) = (2x + 3)(x + 1)."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] Evaluate 99 × 101 using the identity (100 - 1)(100 + 1):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "9999",
                                "explanation": "(100 - 1)(100 + 1) = 100² - 1² = 10,000 - 1 = 9,999.",
                                "step_by_step_solution": [
                                    "Step 1: (a - b)(a + b) = a² - b².",
                                    "Step 2: 100² - 1 = 10,000 - 1 = 9,999."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 8
                            }
                        ]
                    },
                    {
                        "title": "Simultaneous Systems Trial",
                        "instructions": "Solve systems of two linear equations using substitution and elimination.",
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
                                "prompt": "Solve the system: x + y = 10 and x - y = 4. What is the value of x?",
                                "question_type": "multiple_choice",
                                "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
                                "correct_answer": "C) 7",
                                "explanation": "Add the equations: (x + y) + (x - y) = 10 + 4 => 2x = 14 => x = 7.",
                                "step_by_step_solution": [
                                    "Step 1: Add both equations: 2x = 14.",
                                    "Step 2: x = 7."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "[Numeric Entry] In the system x + y = 10 and x - y = 4, what is the value of y?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "3",
                                "explanation": "x = 7. 7 + y = 10 => y = 3.",
                                "step_by_step_solution": [
                                    "Step 1: Substitute x = 7 into x + y = 10.",
                                    "Step 2: 7 + y = 10 => y = 3."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 2
                            },
                            {
                                "prompt": "Solve for y:  2x + y = 11  and  x + y = 7",
                                "question_type": "multiple_choice",
                                "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
                                "correct_answer": "A) 3",
                                "explanation": "Subtract second equation from first: (2x - x) = 11 - 7 => x = 4. Then 4 + y = 7 => y = 3.",
                                "step_by_step_solution": [
                                    "Step 1: Subtract equations: x = 4.",
                                    "Step 2: Substitute x = 4: 4 + y = 7 => y = 3."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] Solve the system: 3x + 2y = 16 and y = x - 2. What is the value of x?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "4",
                                "explanation": "Substitute y = x - 2: 3x + 2(x - 2) = 16 => 5x - 4 = 16 => 5x = 20 => x = 4.",
                                "step_by_step_solution": [
                                    "Step 1: 3x + 2(x - 2) = 16.",
                                    "Step 2: 3x + 2x - 4 = 16 => 5x = 20.",
                                    "Step 3: x = 4."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "The cost of 2 notebooks and 3 pens is Rs. 130. The cost of 2 notebooks and 1 pen is Rs. 90. What is the cost of 1 pen?",
                                "question_type": "multiple_choice",
                                "options": ["A) Rs. 15", "B) Rs. 20", "C) Rs. 25", "D) Rs. 30"],
                                "correct_answer": "B) Rs. 20",
                                "explanation": "2n + 3p = 130, 2n + p = 90. Subtract: 2p = 40 => p = Rs. 20.",
                                "step_by_step_solution": [
                                    "Step 1: (2n + 3p) - (2n + p) = 130 - 90.",
                                    "Step 2: 2p = 40 => p = 20."
                                ],
                                "difficulty": "hard",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] In the system 4x + 3y = 25 and 4x - 3y = 7, find the value of x:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "4",
                                "explanation": "Add equations: 8x = 32 => x = 4.",
                                "step_by_step_solution": [
                                    "Step 1: Add equations: 8x = 32.",
                                    "Step 2: x = 4."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "The sum of two numbers is 45 and their difference is 15. What is the larger number?",
                                "question_type": "multiple_choice",
                                "options": ["A) 25", "B) 30", "C) 35", "D) 40"],
                                "correct_answer": "B) 30",
                                "explanation": "x + y = 45, x - y = 15. 2x = 60 => x = 30.",
                                "step_by_step_solution": [
                                    "Step 1: 2x = 45 + 15 = 60.",
                                    "Step 2: x = 30."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] Solve the system: 5x + 2y = 29 and 3x - y = 13. What is the value of y?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "2",
                                "explanation": "From eq2: y = 3x - 13. Substitute: 5x + 2(3x - 13) = 29 => 11x - 26 = 29 => 11x = 55 => x = 5. Then y = 3(5) - 13 = 2.",
                                "step_by_step_solution": [
                                    "Step 1: y = 3x - 13.",
                                    "Step 2: 5x + 6x - 26 = 29 => 11x = 55 => x = 5.",
                                    "Step 3: y = 15 - 13 = 2."
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
        "title": "Geometric Fortress",
        "description": "Construct right-angled proofs with Pythagoras and measure the capacity of cylindrical keeps.",
        "grade": 8,
        "icon": "box",
        "theme_color": "indigo",
        "display_order": 2,
        "topics": [
            {
                "title": "Pythagoras Theorem & Solid Mensuration",
                "description": "Pythagoras theorem in right triangles, and surface area/volume of cylinders, cones, and spheres.",
                "learning_objectives": [
                    "State and apply Pythagoras theorem (a² + b² = c²)",
                    "Calculate the surface area and volume of cylinders (V = πr²h)",
                    "Calculate the surface area and volume of spheres"
                ],
                "grade": 8,
                "display_order": 1,
                "missions": [
                    {
                        "title": "The Pythagorean Bastion",
                        "instructions": "Calculate hypotenuse lengths and compute the volume of cylindrical towers.",
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
                                "prompt": "In a right-angled triangle with legs a = 3 cm and b = 4 cm, what is the length of the hypotenuse c?",
                                "question_type": "multiple_choice",
                                "options": ["A) 5 cm", "B) 6 cm", "C) 7 cm", "D) 8 cm"],
                                "correct_answer": "A) 5 cm",
                                "explanation": "c² = a² + b² = 3² + 4² = 9 + 16 = 25 => c = √25 = 5 cm.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: c² = a² + b².",
                                    "Step 2: c² = 9 + 16 = 25.",
                                    "Step 3: c = 5 cm."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is the volume of a cylinder with radius 7 cm and height 10 cm? (Use π = 22/7)",
                                "question_type": "multiple_choice",
                                "options": ["A) 1,440 cm³", "B) 1,540 cm³", "C) 1,640 cm³", "D) 1,740 cm³"],
                                "correct_answer": "B) 1,540 cm³",
                                "explanation": "Volume = πr²h = (22/7) × 7² × 10 = 22 × 7 × 10 = 1,540 cm³.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: V = πr²h.",
                                    "Step 2: V = (22/7) × 49 × 10 = 154 × 10 = 1,540 cm³."
                                ],
                                "difficulty": "medium",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] In a right triangle, hypotenuse c = 13 cm and one leg a = 5 cm. What is the length of the other leg b in cm?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "12",
                                "explanation": "b² = c² - a² = 13² - 5² = 169 - 25 = 144 => b = √144 = 12 cm.",
                                "step_by_step_solution": [
                                    "Step 1: b² = 169 - 25 = 144.",
                                    "Step 2: b = 12 cm."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "Which set of side lengths forms a right-angled triangle?",
                                "question_type": "multiple_choice",
                                "options": ["A) 4, 5, 6", "B) 6, 8, 10", "C) 5, 6, 7", "D) 7, 8, 9"],
                                "correct_answer": "B) 6, 8, 10",
                                "explanation": "6² + 8² = 36 + 64 = 100 = 10². It satisfies Pythagoras theorem.",
                                "step_by_step_solution": [
                                    "Step 1: Check 6² + 8² = 36 + 64 = 100.",
                                    "Step 2: 10² = 100. Both match => Right triangle."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "What is the formula for the total surface area of a sphere of radius r?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2πr²", "B) 3πr²", "C) 4πr²", "D) (4/3)πr³"],
                                "correct_answer": "C) 4πr²",
                                "explanation": "Surface area of a sphere is 4πr².",
                                "step_by_step_solution": [
                                    "Step 1: Surface area = 4πr².",
                                    "Step 2: (4/3)πr³ is the formula for volume."
                                ],
                                "difficulty": "easy",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] Calculate the curved surface area of a cylinder with radius 7 cm and height 5 cm in cm²: (Use π = 22/7)",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "220",
                                "explanation": "Curved Surface Area = 2πrh = 2 × (22/7) × 7 × 5 = 220 cm².",
                                "step_by_step_solution": [
                                    "Step 1: CSA = 2πrh.",
                                    "Step 2: 2 × (22/7) × 7 × 5 = 220 cm²."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "A ladder 10 meters long leans against a vertical wall. If the base of the ladder is 6 meters from the wall, how high up the wall does the ladder reach?",
                                "question_type": "multiple_choice",
                                "options": ["A) 6 m", "B) 7 m", "C) 8 m", "D) 9 m"],
                                "correct_answer": "C) 8 m",
                                "explanation": "h² = 10² - 6² = 100 - 36 = 64 => h = √64 = 8 meters.",
                                "step_by_step_solution": [
                                    "Step 1: Hypotenuse = 10, base = 6.",
                                    "Step 2: h² = 100 - 36 = 64.",
                                    "Step 3: h = 8 m."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] What is the volume of a sphere of radius 3 cm in terms of π? (Enter the coefficient of π):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "36",
                                "explanation": "V = (4/3)πr³ = (4/3) × π × 27 = 36π. The coefficient is 36.",
                                "step_by_step_solution": [
                                    "Step 1: V = (4/3)π(3³) = (4/3)π(27).",
                                    "Step 2: 4 × 9 = 36π. Coefficient = 36."
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
                "title": "Frequency Distributions & Histograms",
                "description": "Grouped frequency distributions, class boundaries, midpoints, and histograms.",
                "learning_objectives": [
                    "Construct grouped frequency tables with equal class intervals",
                    "Calculate class marks (midpoints) and determine class width",
                    "Interpret histograms and frequency polygons"
                ],
                "grade": 8,
                "display_order": 2,
                "missions": [
                    {
                        "title": "The Histogram Tower",
                        "instructions": "Analyze grouped frequency intervals and plot data distributions across the fortress.",
                        "category": "practice",
                        "difficulty": "medium",
                        "question_count": 8,
                        "xp_reward": 20,
                        "pass_percentage": 60,
                        "unlock_condition": "always",
                        "display_order": 1,
                        "is_boss": False,
                        "questions": [
                            {
                                "prompt": "What is the midpoint (class mark) of the class interval 20 - 30?",
                                "question_type": "multiple_choice",
                                "options": ["A) 24", "B) 25", "C) 26", "D) 27"],
                                "correct_answer": "B) 25",
                                "explanation": "Midpoint = (Lower limit + Upper limit) / 2 = (20 + 30) / 2 = 25.",
                                "step_by_step_solution": [
                                    "Step 1: (20 + 30) / 2 = 50 / 2 = 25."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is the class width (size) of the class interval 10 - 20?",
                                "question_type": "multiple_choice",
                                "options": ["A) 5", "B) 10", "C) 15", "D) 20"],
                                "correct_answer": "B) 10",
                                "explanation": "Class width = Upper limit - Lower limit = 20 - 10 = 10.",
                                "step_by_step_solution": [
                                    "Step 1: 20 - 10 = 10."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] What is the midpoint of the class interval 40 - 60?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "50",
                                "explanation": "(40 + 60) / 2 = 100 / 2 = 50.",
                                "step_by_step_solution": [
                                    "Step 1: (40 + 60) / 2 = 50."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "In a histogram, the area of each bar is proportional to the:",
                                "question_type": "multiple_choice",
                                "options": ["A) Class limit", "B) Class frequency", "C) Class mark", "D) Cumulative frequency"],
                                "correct_answer": "B) Class frequency",
                                "explanation": "In a histogram with equal class intervals, bar height and area are proportional to class frequency.",
                                "step_by_step_solution": [
                                    "Step 1: By definition of a histogram, bar heights represent frequency."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "For the class intervals 10-19, 20-29, 30-39, what is the lower class boundary of 20-29?",
                                "question_type": "multiple_choice",
                                "options": ["A) 19.0", "B) 19.5", "C) 20.0", "D) 20.5"],
                                "correct_answer": "B) 19.5",
                                "explanation": "Lower class boundary = (19 + 20) / 2 = 19.5.",
                                "step_by_step_solution": [
                                    "Step 1: Average upper limit of previous class (19) and lower limit of current class (20).",
                                    "Step 2: (19 + 20) / 2 = 19.5."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] A frequency distribution has frequencies: 5, 8, 12, 10, 5. What is the total sample size N?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "40",
                                "explanation": "N = 5 + 8 + 12 + 10 + 5 = 40.",
                                "step_by_step_solution": [
                                    "Step 1: 5 + 8 + 12 + 10 + 5 = 40."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "Which class interval is the modal class if frequencies are: 0-10: 4, 10-20: 9, 20-30: 16, 30-40: 7?",
                                "question_type": "multiple_choice",
                                "options": ["A) 0-10", "B) 10-20", "C) 20-30", "D) 30-40"],
                                "correct_answer": "C) 20-30",
                                "explanation": "The interval 20-30 has the highest frequency (16), making it the modal class.",
                                "step_by_step_solution": [
                                    "Step 1: Highest frequency is 16.",
                                    "Step 2: Corresponding class is 20-30."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] In a grouped frequency table, the class boundaries are 9.5 - 19.5. What is the class width?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "10",
                                "explanation": "Class width = 19.5 - 9.5 = 10.",
                                "step_by_step_solution": [
                                    "Step 1: 19.5 - 9.5 = 10."
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
