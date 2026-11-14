# Grade 5 Mathematics Curriculum Data — Federal NCP 2022-23
# Strands: Numbers and Operations, Geometry, Measurement & Data Handling

GRADE_5_WORLDS = [
    {
        "title": "Isle of Operations",
        "description": "Master operations up to 1,000,000, BODMAS precedence arenas, and percentage forges.",
        "grade": 5,
        "icon": "zap",
        "theme_color": "rose",
        "display_order": 1,
        "topics": [
            {
                "title": "Operations up to 1,000,000 & Order of Operations (BODMAS)",
                "description": "Multi-digit multiplication, long division, and evaluating expressions using BODMAS rules.",
                "learning_objectives": [
                    "Perform operations with numbers up to 1,000,000",
                    "Apply the correct order of operations (BODMAS/PEMDAS)",
                    "Solve multi-step word problems involving whole numbers"
                ],
                "grade": 5,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Order of Operations Arena",
                        "instructions": "Evaluate mathematical expressions in the arena following strict BODMAS precedence.",
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
                                "prompt": "Evaluate: 12 + 6 ÷ 3 =",
                                "question_type": "multiple_choice",
                                "options": ["A) 6", "B) 14", "C) 18", "D) 4"],
                                "correct_answer": "B) 14",
                                "explanation": "Division takes precedence over addition: 6 ÷ 3 = 2. Then 12 + 2 = 14.",
                                "step_by_step_solution": [
                                    "Step 1: Perform Division first: 6 ÷ 3 = 2.",
                                    "Step 2: Perform Addition: 12 + 2 = 14."
                                ],
                                "common_mistakes": {
                                    "6": "(12 + 6) ÷ 3 = 18 ÷ 3 = 6. This is wrong because division must be done before addition!"
                                },
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Calculate: (15 - 5) × 4 =",
                                "question_type": "multiple_choice",
                                "options": ["A) 20", "B) 35", "C) 40", "D) 45"],
                                "correct_answer": "C) 40",
                                "explanation": "Brackets first: 15 - 5 = 10. Then 10 × 4 = 40.",
                                "step_by_step_solution": [
                                    "Step 1: Solve inside brackets: 15 - 5 = 10.",
                                    "Step 2: Multiply: 10 × 4 = 40."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] Evaluate: 20 - 3 × 4 + 2 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "10",
                                "explanation": "Multiply first: 3 × 4 = 12. Then left to right: 20 - 12 = 8, 8 + 2 = 10.",
                                "step_by_step_solution": [
                                    "Step 1: Multiplication: 3 × 4 = 12.",
                                    "Step 2: Subtraction: 20 - 12 = 8.",
                                    "Step 3: Addition: 8 + 2 = 10."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "Evaluate: 8 + (12 - 4) ÷ 2 =",
                                "question_type": "multiple_choice",
                                "options": ["A) 8", "B) 10", "C) 12", "D) 16"],
                                "correct_answer": "C) 12",
                                "explanation": "Brackets first: 12 - 4 = 8. Then division: 8 ÷ 2 = 4. Finally addition: 8 + 4 = 12.",
                                "step_by_step_solution": [
                                    "Step 1: Brackets: 12 - 4 = 8.",
                                    "Step 2: Division: 8 ÷ 2 = 4.",
                                    "Step 3: Addition: 8 + 4 = 12."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] Solve: 50 ÷ (2 + 3) × 4 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "40",
                                "explanation": "Brackets: 2 + 3 = 5. Then left to right: 50 ÷ 5 = 10. Then 10 × 4 = 40.",
                                "step_by_step_solution": [
                                    "Step 1: Brackets: 2 + 3 = 5.",
                                    "Step 2: Division: 50 ÷ 5 = 10.",
                                    "Step 3: Multiplication: 10 × 4 = 40."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "Evaluate: 100 - [4 × (15 - 5)] =",
                                "question_type": "multiple_choice",
                                "options": ["A) 40", "B) 60", "C) 80", "D) 20"],
                                "correct_answer": "B) 60",
                                "explanation": "Innermost parentheses: 15 - 5 = 10. Square brackets: 4 × 10 = 40. Outer subtraction: 100 - 40 = 60.",
                                "step_by_step_solution": [
                                    "Step 1: Inner brackets: 15 - 5 = 10.",
                                    "Step 2: Box brackets: 4 × 10 = 40.",
                                    "Step 3: 100 - 40 = 60."
                                ],
                                "difficulty": "hard",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] Evaluate: 7 × 8 - 36 ÷ 6 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "50",
                                "explanation": "Multiply and divide first: 7 × 8 = 56, and 36 ÷ 6 = 6. Then 56 - 6 = 50.",
                                "step_by_step_solution": [
                                    "Step 1: 7 × 8 = 56.",
                                    "Step 2: 36 ÷ 6 = 6.",
                                    "Step 3: 56 - 6 = 50."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "Which expression gives a value of 24?",
                                "question_type": "multiple_choice",
                                "options": [
                                    "A) 6 + 6 × 2",
                                    "B) (6 + 6) × 2",
                                    "C) 6 × 6 - 2",
                                    "D) 6 × 2 + 6 × 3"
                                ],
                                "correct_answer": "B) (6 + 6) × 2",
                                "explanation": "(6 + 6) × 2 = 12 × 2 = 24.",
                                "step_by_step_solution": [
                                    "Step 1: In option B: 6 + 6 = 12.",
                                    "Step 2: 12 × 2 = 24."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    },
                    {
                        "title": "Grand Million Trial",
                        "instructions": "Execute multi-digit multiplications and divisions on large whole numbers.",
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
                                "prompt": "Calculate: 1,250 × 40 =",
                                "question_type": "multiple_choice",
                                "options": ["A) 40,000", "B) 45,000", "C) 50,000", "D) 60,000"],
                                "correct_answer": "C) 50,000",
                                "explanation": "125 × 4 = 500. Append the two zeros: 50,000.",
                                "step_by_step_solution": [
                                    "Step 1: 1,250 × 4 = 5,000.",
                                    "Step 2: 5,000 × 10 = 50,000."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Divide: 14,400 ÷ 12 =",
                                "question_type": "multiple_choice",
                                "options": ["A) 1,100", "B) 1,200", "C) 1,400", "D) 120"],
                                "correct_answer": "B) 1,200",
                                "explanation": "144 ÷ 12 = 12. Append two zeros: 1,200.",
                                "step_by_step_solution": [
                                    "Step 1: 144 ÷ 12 = 12.",
                                    "Step 2: 14,400 ÷ 12 = 1,200."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] What is 3,500 × 20?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "70000",
                                "explanation": "35 × 2 = 70. Append three zeros: 70,000.",
                                "step_by_step_solution": [
                                    "Step 1: 3,500 × 2 = 7,000.",
                                    "Step 2: 7,000 × 10 = 70,000."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "A factory produces 425 bicycles every day. How many bicycles does it produce in 30 days?",
                                "question_type": "multiple_choice",
                                "options": ["A) 11,750", "B) 12,500", "C) 12,750", "D) 13,000"],
                                "correct_answer": "C) 12,750",
                                "explanation": "425 × 30 = 12,750 bicycles.",
                                "step_by_step_solution": [
                                    "Step 1: 425 × 3 = 1,275.",
                                    "Step 2: 1,275 × 10 = 12,750."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] Divide 18,750 ÷ 25 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "750",
                                "explanation": "18,750 ÷ 25 = 750.",
                                "step_by_step_solution": [
                                    "Step 1: 187 ÷ 25 = 7 remainder 12.",
                                    "Step 2: Bring down 5 -> 125 ÷ 25 = 5.",
                                    "Step 3: Bring down 0 -> 0. Quotient = 750."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "What is the remainder when 4,528 is divided by 15?",
                                "question_type": "multiple_choice",
                                "options": ["A) 8", "B) 13", "C) 11", "D) 7"],
                                "correct_answer": "B) 13",
                                "explanation": "4,528 = 15 × 301 + 13. Remainder is 13.",
                                "step_by_step_solution": [
                                    "Step 1: 45 ÷ 15 = 3 (4500).",
                                    "Step 2: 28 ÷ 15 = 1 remainder 13.",
                                    "Step 3: Remainder = 13."
                                ],
                                "difficulty": "hard",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] 250 students paid Rs. 1,200 each for a school excursion. What is the total amount collected in Rupees?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "300000",
                                "explanation": "250 × 1,200 = 300,000 Rupees.",
                                "step_by_step_solution": [
                                    "Step 1: 25 × 12 = 300.",
                                    "Step 2: Append three zeros: 300,000."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "If 1,000,000 - 345,678 = ?",
                                "question_type": "multiple_choice",
                                "options": ["A) 654,322", "B) 654,312", "C) 655,322", "D) 754,322"],
                                "correct_answer": "A) 654,322",
                                "explanation": "1,000,000 - 345,678 = 654,322.",
                                "step_by_step_solution": [
                                    "Step 1: Regroup across zeros: 999,999 - 345,678 = 654,321.",
                                    "Step 2: Add 1: 654,322."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Fractions, Decimals & Percentages",
                "description": "Multiplication and division of fractions, decimals, and conversions to percentages.",
                "learning_objectives": [
                    "Multiply and divide proper fractions and mixed numbers",
                    "Multiply and divide decimals by powers of 10 and whole numbers",
                    "Convert between fractions, decimals, and percentages"
                ],
                "grade": 5,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Percent & Fraction Forge",
                        "instructions": "Transmute fractions into percentages and divide fractions using reciprocals.",
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
                                "prompt": "Calculate: 2/3 × 3/4 =",
                                "question_type": "multiple_choice",
                                "options": ["A) 5/7", "B) 1/2", "C) 6/7", "D) 2/7"],
                                "correct_answer": "B) 1/2",
                                "explanation": "(2 × 3) / (3 × 4) = 6/12 = 1/2.",
                                "step_by_step_solution": [
                                    "Step 1: Multiply numerators: 2 × 3 = 6.",
                                    "Step 2: Multiply denominators: 3 × 4 = 12.",
                                    "Step 3: Simplify: 6/12 = 1/2."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is 3/4 ÷ 1/2?",
                                "question_type": "multiple_choice",
                                "options": ["A) 3/8", "B) 1 1/2", "C) 2/3", "D) 3/2"],
                                "correct_answer": "B) 1 1/2",
                                "explanation": "Invert divisor and multiply: 3/4 × 2/1 = 6/4 = 3/2 = 1 1/2.",
                                "step_by_step_solution": [
                                    "Step 1: Multiply by reciprocal of 1/2: 3/4 × 2/1.",
                                    "Step 2: (3 × 2) / (4 × 1) = 6/4 = 3/2 = 1 1/2."
                                ],
                                "difficulty": "medium",
                                "display_order": 2
                            },
                            {
                                "prompt": "What is 45% written as a fraction in simplest form?",
                                "question_type": "multiple_choice",
                                "options": ["A) 45/10", "B) 9/20", "C) 4/5", "D) 9/10"],
                                "correct_answer": "B) 9/20",
                                "explanation": "45% = 45/100. Divide numerator and denominator by 5: 9/20.",
                                "step_by_step_solution": [
                                    "Step 1: 45% = 45/100.",
                                    "Step 2: Simplify by dividing by 5: 45 ÷ 5 = 9, 100 ÷ 5 = 20.",
                                    "Step 3: Result = 9/20."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] What is 25% of 200?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "50",
                                "explanation": "25% = 1/4. 1/4 of 200 = 50.",
                                "step_by_step_solution": [
                                    "Step 1: 25% = 25/100 = 1/4.",
                                    "Step 2: 200 ÷ 4 = 50."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "What is 0.65 expressed as a percentage?",
                                "question_type": "multiple_choice",
                                "options": ["A) 6.5%", "B) 65%", "C) 650%", "D) 0.65%"],
                                "correct_answer": "B) 65%",
                                "explanation": "0.65 × 100% = 65%.",
                                "step_by_step_solution": [
                                    "Step 1: Multiply by 100 to convert to percentage: 0.65 × 100 = 65%."
                                ],
                                "difficulty": "easy",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] Solve: 3.45 × 100 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "345",
                                "explanation": "Multiplying by 100 shifts the decimal point 2 places to the right: 345.",
                                "step_by_step_solution": [
                                    "Step 1: Move decimal 2 places right: 3.45 -> 345."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "A test has 50 questions. Tariq answered 80% correctly. How many questions did Tariq answer correctly?",
                                "question_type": "multiple_choice",
                                "options": ["A) 35", "B) 40", "C) 42", "D) 45"],
                                "correct_answer": "B) 40",
                                "explanation": "80% of 50 = (80 / 100) × 50 = 40 questions.",
                                "step_by_step_solution": [
                                    "Step 1: (80/100) × 50 = 4000 / 100 = 40."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] Solve: 4.8 ÷ 6 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "0.8",
                                "explanation": "48 ÷ 6 = 8, so 4.8 ÷ 6 = 0.8.",
                                "step_by_step_solution": [
                                    "Step 1: 4.8 = 48 tenths.",
                                    "Step 2: 48 tenths ÷ 6 = 8 tenths = 0.8."
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
        "title": "Polygon Peak",
        "description": "Calculate angles in geometric solids, apply unitary proportions, and measure 3D volumes.",
        "grade": 5,
        "icon": "mountain",
        "theme_color": "orange",
        "display_order": 2,
        "topics": [
            {
                "title": "Angles in Polygons & 3D Solid Nets",
                "description": "Angle sum in triangles (180°) and quadrilaterals (360°), and flat nets of 3D solids.",
                "learning_objectives": [
                    "Calculate missing angles in triangles (sum = 180°)",
                    "Calculate missing angles in quadrilaterals (sum = 360°)",
                    "Identify folding nets of cubes, cuboids, and pyramids"
                ],
                "grade": 5,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Triangle Angle Summit",
                        "instructions": "Calculate missing angles across triangular crags and quadrilateral plateaus.",
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
                                "prompt": "What do the interior angles of any quadrilateral add up to?",
                                "question_type": "multiple_choice",
                                "options": ["A) 180°", "B) 270°", "C) 360°", "D) 540°"],
                                "correct_answer": "C) 360°",
                                "explanation": "A quadrilateral can be split into 2 triangles: 2 × 180° = 360°.",
                                "step_by_step_solution": [
                                    "Step 1: Quadrilateral has 4 sides.",
                                    "Step 2: Sum of angles = (4 - 2) × 180° = 360°."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "[Numeric Entry] A right-angled triangle has one acute angle of 35°. What is the measurement (in degrees) of the other acute angle?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "55",
                                "explanation": "In a right triangle, the two acute angles sum to 90°. 90° - 35° = 55°.",
                                "step_by_step_solution": [
                                    "Step 1: Right angle = 90°.",
                                    "Step 2: Remaining two angles sum to 90°.",
                                    "Step 3: 90° - 35° = 55°."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 2
                            },
                            {
                                "prompt": "Three angles of a quadrilateral are 100°, 85°, and 75°. What is the fourth angle?",
                                "question_type": "multiple_choice",
                                "options": ["A) 90°", "B) 100°", "C) 110°", "D) 120°"],
                                "correct_answer": "B) 100°",
                                "explanation": "100° + 85° + 75° = 260°. Fourth angle = 360° - 260° = 100°.",
                                "step_by_step_solution": [
                                    "Step 1: Sum of known angles: 100 + 85 + 75 = 260°.",
                                    "Step 2: Total = 360°.",
                                    "Step 3: 360° - 260° = 100°."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "In an isosceles triangle, the angle between the two equal sides is 40°. What is the size of each of the other two base angles?",
                                "question_type": "multiple_choice",
                                "options": ["A) 60°", "B) 70°", "C) 80°", "D) 140°"],
                                "correct_answer": "B) 70°",
                                "explanation": "Remaining angle sum = 180° - 40° = 140°. Since base angles are equal: 140° ÷ 2 = 70° each.",
                                "step_by_step_solution": [
                                    "Step 1: 180° - 40° = 140°.",
                                    "Step 2: 140° ÷ 2 = 70°."
                                ],
                                "difficulty": "hard",
                                "display_order": 4
                            },
                            {
                                "prompt": "How many square faces are connected in the net of a cube?",
                                "question_type": "multiple_choice",
                                "options": ["A) 4", "B) 5", "C) 6", "D) 8"],
                                "correct_answer": "C) 6",
                                "explanation": "A cube has 6 identical square faces, so its flat unfolding net has 6 squares.",
                                "step_by_step_solution": [
                                    "Step 1: A cube has 6 faces.",
                                    "Step 2: Its net has 6 squares."
                                ],
                                "difficulty": "easy",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] Each angle in an equilateral triangle is equal. What is the degree measurement of each angle?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "60",
                                "explanation": "180° ÷ 3 = 60°.",
                                "step_by_step_solution": [
                                    "Step 1: 180° / 3 = 60°."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "A quadrilateral has all four angles equal. What is the size of each angle?",
                                "question_type": "multiple_choice",
                                "options": ["A) 45°", "B) 60°", "C) 90°", "D) 120°"],
                                "correct_answer": "C) 90°",
                                "explanation": "360° ÷ 4 = 90° (this quadrilateral is a rectangle or square).",
                                "step_by_step_solution": [
                                    "Step 1: 360° / 4 = 90°."
                                ],
                                "difficulty": "medium",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] In a quadrilateral, two opposite angles are 110° and 110°. If the third angle is 70°, what is the fourth angle in degrees?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "70",
                                "explanation": "110° + 110° + 70° = 290°. 360° - 290° = 70°.",
                                "step_by_step_solution": [
                                    "Step 1: 110 + 110 + 70 = 290°.",
                                    "Step 2: 360 - 290 = 70°."
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
                "title": "Unitary Method, Volume & Averages",
                "description": "Direct proportion problems using unitary method, volume of cuboids, and data averages.",
                "learning_objectives": [
                    "Solve direct proportion problems using the unitary method",
                    "Calculate volume of cubes and cuboids (V = l × w × h)",
                    "Find the average (mean) of a set of numbers"
                ],
                "grade": 5,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Unitary & Volume Vault",
                        "instructions": "Determine single-unit scaling and compute spatial volumes in the mountain vaults.",
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
                                "prompt": "If 6 notebooks cost Rs. 180, what is the cost of 1 notebook?",
                                "question_type": "multiple_choice",
                                "options": ["A) Rs. 25", "B) Rs. 30", "C) Rs. 35", "D) Rs. 40"],
                                "correct_answer": "B) Rs. 30",
                                "explanation": "Cost of 1 notebook = 180 ÷ 6 = Rs. 30.",
                                "step_by_step_solution": [
                                    "Step 1: Unit cost = Total cost ÷ Quantity.",
                                    "Step 2: 180 ÷ 6 = Rs. 30."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "If 4 kg of rice costs Rs. 480, how much will 7 kg of rice cost?",
                                "question_type": "multiple_choice",
                                "options": ["A) Rs. 720", "B) Rs. 840", "C) Rs. 960", "D) Rs. 800"],
                                "correct_answer": "B) Rs. 840",
                                "explanation": "Cost of 1 kg = 480 ÷ 4 = Rs. 120. Cost of 7 kg = 7 × 120 = Rs. 840.",
                                "step_by_step_solution": [
                                    "Step 1: Find 1 unit cost: 480 / 4 = 120.",
                                    "Step 2: Multiply by 7: 7 × 120 = 840."
                                ],
                                "difficulty": "medium",
                                "display_order": 2
                            },
                            {
                                "prompt": "What is the volume of a cuboid box with length 8 cm, width 5 cm, and height 4 cm?",
                                "question_type": "multiple_choice",
                                "options": ["A) 120 cm³", "B) 140 cm³", "C) 160 cm³", "D) 180 cm³"],
                                "correct_answer": "C) 160 cm³",
                                "explanation": "Volume = length × width × height = 8 × 5 × 4 = 160 cm³.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: V = l × w × h.",
                                    "Step 2: V = 8 × 5 × 4 = 40 × 4 = 160 cm³."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] What is the volume of a cube with edge length 5 cm in cubic centimeters?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "125",
                                "explanation": "Volume of cube = s³ = 5 × 5 × 5 = 125 cm³.",
                                "step_by_step_solution": [
                                    "Step 1: V = 5 × 5 × 5 = 125 cm³."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "What is the average (mean) of the numbers: 10, 15, 20, 25, 30?",
                                "question_type": "multiple_choice",
                                "options": ["A) 18", "B) 20", "C) 22", "D) 25"],
                                "correct_answer": "B) 20",
                                "explanation": "Sum = 10 + 15 + 20 + 25 + 30 = 100. Average = 100 ÷ 5 = 20.",
                                "step_by_step_solution": [
                                    "Step 1: Add all values: 10 + 15 + 20 + 25 + 30 = 100.",
                                    "Step 2: Divide by total count (5): 100 / 5 = 20."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "[Numeric Entry] prompt": "[Numeric Entry] A car travels 180 km in 3 hours at constant speed. How many kilometers does it travel in 5 hours?",
                                "prompt": "[Numeric Entry] A car travels 180 km in 3 hours at constant speed. How many kilometers does it travel in 5 hours?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "300",
                                "explanation": "Speed = 180 / 3 = 60 km/h. Distance in 5 hours = 5 × 60 = 300 km.",
                                "step_by_step_solution": [
                                    "Step 1: Distance in 1 hour = 180 / 3 = 60 km.",
                                    "Step 2: Distance in 5 hours = 5 × 60 = 300 km."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "A tank in the shape of a cuboid has length 2 m, width 1.5 m, and height 1 m. How many cubic meters of water does it hold when full?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2.5 m³", "B) 3.0 m³", "C) 3.5 m³", "D) 4.0 m³"],
                                "correct_answer": "B) 3.0 m³",
                                "explanation": "Volume = 2 × 1.5 × 1 = 3.0 m³.",
                                "step_by_step_solution": [
                                    "Step 1: V = 2 × 1.5 × 1 = 3.0 m³."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] The scores of 4 cricket innings are 45, 60, 55, and 80. What is the batsman's batting average for these innings?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "60",
                                "explanation": "Sum = 45 + 60 + 55 + 80 = 240. Average = 240 / 4 = 60.",
                                "step_by_step_solution": [
                                    "Step 1: Sum = 45 + 60 + 55 + 80 = 240.",
                                    "Step 2: Average = 240 / 4 = 60."
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
