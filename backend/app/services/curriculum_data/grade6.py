# Grade 6 Mathematics Curriculum Data — Federal NCP 2022-23
# Strands: Numbers and Operations, Algebra, Geometry & Statistics

GRADE_6_WORLDS = [
    {
        "title": "Integers & Algebra Domain",
        "description": "Traverse negative number labyrinths, ratio workshops, and solve your first algebraic chambers.",
        "grade": 6,
        "icon": "code",
        "theme_color": "amber",
        "display_order": 1,
        "topics": [
            {
                "title": "Sets, Integers & Rational Numbers",
                "description": "Set representations, integer arithmetic on the number line, and ordering rational numbers.",
                "learning_objectives": [
                    "Represent sets in descriptive and tabular forms",
                    "Add, subtract, multiply, and divide signed integers",
                    "Order positive and negative rational numbers on the number line"
                ],
                "grade": 6,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Integer Labyrinth",
                        "instructions": "Navigate signed operations and set intersections to unlock the labyrinth gates.",
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
                                "prompt": "What is the result of (-8) + 15?",
                                "question_type": "multiple_choice",
                                "options": ["A) -7", "B) 7", "C) -23", "D) 23"],
                                "correct_answer": "B) 7",
                                "explanation": "Start at -8 and add 15: 15 - 8 = 7.",
                                "step_by_step_solution": [
                                    "Step 1: Different signs: subtract the smaller absolute value from the larger.",
                                    "Step 2: 15 - 8 = 7.",
                                    "Step 3: The sign of the larger absolute value (15) is positive: +7."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Evaluate: (-6) × (-4) =",
                                "question_type": "multiple_choice",
                                "options": ["A) -24", "B) 24", "C) -10", "D) 10"],
                                "correct_answer": "B) 24",
                                "explanation": "Multiplying two negative numbers gives a positive product: (-6) × (-4) = +24.",
                                "step_by_step_solution": [
                                    "Step 1: Negative × Negative = Positive.",
                                    "Step 2: 6 × 4 = 24. Result = +24."
                                ],
                                "common_mistakes": {
                                    "-24": "Remember: negative times negative equals positive."
                                },
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] Calculate: (-12) - (-5) = (Enter the integer value):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "-7",
                                "explanation": "Subtracting a negative is the same as adding: (-12) + 5 = -7.",
                                "step_by_step_solution": [
                                    "Step 1: -(-5) becomes +5.",
                                    "Step 2: -12 + 5 = -7."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "If Set A = {1, 2, 3, 4} and Set B = {3, 4, 5, 6}, what is A ∩ B (the intersection)?",
                                "question_type": "multiple_choice",
                                "options": ["A) {1, 2}", "B) {3, 4}", "C) {1, 2, 3, 4, 5, 6}", "D) {5, 6}"],
                                "correct_answer": "B) {3, 4}",
                                "explanation": "The intersection contains elements that belong to BOTH sets: 3 and 4.",
                                "step_by_step_solution": [
                                    "Step 1: Identify elements common to both sets A and B.",
                                    "Step 2: 3 and 4 appear in both. Intersection = {3, 4}."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "Evaluate: (-36) ÷ 4 =",
                                "question_type": "multiple_choice",
                                "options": ["A) -9", "B) 9", "C) -8", "D) -12"],
                                "correct_answer": "A) -9",
                                "explanation": "A negative divided by a positive yields a negative quotient: -36 ÷ 4 = -9.",
                                "step_by_step_solution": [
                                    "Step 1: Negative ÷ Positive = Negative.",
                                    "Step 2: 36 ÷ 4 = 9. Result = -9."
                                ],
                                "difficulty": "easy",
                                "display_order": 5
                            },
                            {
                                "prompt": "Which integer is the SMALLEST: -15, -4, 0, -20?",
                                "question_type": "multiple_choice",
                                "options": ["A) 0", "B) -4", "C) -15", "D) -20"],
                                "correct_answer": "D) -20",
                                "explanation": "On the number line, numbers further to the left are smaller. -20 is furthest left, so it is the smallest.",
                                "step_by_step_solution": [
                                    "Step 1: Compare negative numbers: larger magnitude with a minus sign means smaller value.",
                                    "Step 2: -20 < -15 < -4 < 0."
                                ],
                                "common_mistakes": {
                                    "-4": "-4 is greater than -20. On a number line, -20 is further to the left."
                                },
                                "difficulty": "medium",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] The temperature in Quetta was -3°C at night and rose by 10°C during the day. What was the daytime temperature in °C?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "7",
                                "explanation": "-3 + 10 = 7°C.",
                                "step_by_step_solution": [
                                    "Step 1: Initial = -3°C.",
                                    "Step 2: Rise = +10°C.",
                                    "Step 3: -3 + 10 = 7°C."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "If Set U = {1, 2, 3, 4, 5} and Set A = {2, 4}, what is the complement A'?",
                                "question_type": "multiple_choice",
                                "options": ["A) {1, 3, 5}", "B) {2, 4}", "C) {1, 2, 3, 4, 5}", "D) {0}"],
                                "correct_answer": "A) {1, 3, 5}",
                                "explanation": "The complement A' contains elements of U that are NOT in A: {1, 3, 5}.",
                                "step_by_step_solution": [
                                    "Step 1: Remove {2, 4} from universal set {1, 2, 3, 4, 5}.",
                                    "Step 2: Remaining elements = {1, 3, 5}."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Ratio, Proportion & Linear Equations",
                "description": "Simplifying ratios, direct proportion, translating word problems into linear equations.",
                "learning_objectives": [
                    "Simplify ratios to lowest terms",
                    "Solve direct proportion problems using cross-multiplication",
                    "Solve single-variable linear equations (ax + b = c)"
                ],
                "grade": 6,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Ratio & Proportion Workshop",
                        "instructions": "Calibrate ratios and balance proportions across gears in the workshop.",
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
                                "prompt": "Simplify the ratio 18 : 24 to its lowest terms:",
                                "question_type": "multiple_choice",
                                "options": ["A) 2 : 3", "B) 3 : 4", "C) 3 : 5", "D) 6 : 8"],
                                "correct_answer": "B) 3 : 4",
                                "explanation": "Divide both numbers by their HCF (6): 18 ÷ 6 = 3, 24 ÷ 6 = 4. Ratio = 3 : 4.",
                                "step_by_step_solution": [
                                    "Step 1: HCF of 18 and 24 is 6.",
                                    "Step 2: 18 / 6 = 3.",
                                    "Step 3: 24 / 6 = 4. Simplified = 3 : 4."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Find the value of x in the proportion:  3 : 5 = 12 : x",
                                "question_type": "multiple_choice",
                                "options": ["A) 15", "B) 18", "C) 20", "D) 25"],
                                "correct_answer": "C) 20",
                                "explanation": "Product of extremes = Product of means: 3 × x = 5 × 12 = 60 => x = 60 / 3 = 20.",
                                "step_by_step_solution": [
                                    "Step 1: 3 / 5 = 12 / x.",
                                    "Step 2: 3x = 5 × 12 = 60.",
                                    "Step 3: x = 60 / 3 = 20."
                                ],
                                "difficulty": "medium",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] The ratio of boys to girls in a class of 35 students is 3 : 2. How many boys are there in the class?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "21",
                                "explanation": "Total parts = 3 + 2 = 5. Value of 1 part = 35 / 5 = 7. Boys = 3 × 7 = 21.",
                                "step_by_step_solution": [
                                    "Step 1: Total ratio parts = 3 + 2 = 5.",
                                    "Step 2: 1 part = 35 / 5 = 7.",
                                    "Step 3: Boys = 3 parts × 7 = 21."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "If 8 pens cost Rs. 160, how much do 15 pens cost?",
                                "question_type": "multiple_choice",
                                "options": ["A) Rs. 240", "B) Rs. 300", "C) Rs. 320", "D) Rs. 280"],
                                "correct_answer": "B) Rs. 300",
                                "explanation": "Cost of 1 pen = 160 / 8 = Rs. 20. Cost of 15 pens = 15 × 20 = Rs. 300.",
                                "step_by_step_solution": [
                                    "Step 1: Cost of 1 pen = 160 ÷ 8 = 20.",
                                    "Step 2: Cost of 15 pens = 15 × 20 = 300."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] Solve for y in the proportion: 4 : 7 = y : 28",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "16",
                                "explanation": "7y = 4 × 28 = 112 => y = 112 / 7 = 16.",
                                "step_by_step_solution": [
                                    "Step 1: 4 / 7 = y / 28.",
                                    "Step 2: 7y = 112.",
                                    "Step 3: y = 16."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "Express the ratio 250 grams to 1 kilogram in simplest form:",
                                "question_type": "multiple_choice",
                                "options": ["A) 1 : 2", "B) 1 : 4", "C) 1 : 5", "D) 250 : 1"],
                                "correct_answer": "B) 1 : 4",
                                "explanation": "1 kg = 1000 grams. Ratio = 250 : 1000 = 1 : 4.",
                                "step_by_step_solution": [
                                    "Step 1: Convert units to grams: 1 kg = 1000 g.",
                                    "Step 2: 250 : 1000 = 250/1000 = 1/4 = 1 : 4."
                                ],
                                "common_mistakes": {
                                    "250 : 1": "You must convert both quantities to the same unit before comparing."
                                },
                                "difficulty": "hard",
                                "display_order": 6
                            },
                            {
                                "prompt": "Two numbers are in the ratio 4 : 5. If their sum is 72, what is the smaller number?",
                                "question_type": "multiple_choice",
                                "options": ["A) 28", "B) 32", "C) 36", "D) 40"],
                                "correct_answer": "B) 32",
                                "explanation": "Total parts = 4 + 5 = 9. 1 part = 72 / 9 = 8. Smaller number = 4 × 8 = 32.",
                                "step_by_step_solution": [
                                    "Step 1: Sum of parts = 4 + 5 = 9.",
                                    "Step 2: 1 part = 72 / 9 = 8.",
                                    "Step 3: Smaller number = 4 × 8 = 32."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] Divide Rs. 900 between Asad and Babar in the ratio 2 : 3. How much does Babar receive in Rupees?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "540",
                                "explanation": "5 parts = 900 => 1 part = 180. Babar gets 3 parts = 3 × 180 = Rs. 540.",
                                "step_by_step_solution": [
                                    "Step 1: 2 + 3 = 5 parts.",
                                    "Step 2: 1 part = 900 / 5 = 180.",
                                    "Step 3: Babar (3 parts) = 3 × 180 = 540."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 8
                            }
                        ]
                    },
                    {
                        "title": "First Algebraic Chamber",
                        "instructions": "Decode algebraic expressions and solve one-variable equations.",
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
                                "prompt": "Solve for x:  2x + 7 = 19",
                                "question_type": "multiple_choice",
                                "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
                                "correct_answer": "B) 6",
                                "explanation": "2x = 19 - 7 = 12 => x = 12 / 2 = 6.",
                                "step_by_step_solution": [
                                    "Step 1: Subtract 7 from both sides: 2x = 12.",
                                    "Step 2: Divide by 2: x = 6."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "If y = 4, evaluate the expression: 3y - 5",
                                "question_type": "multiple_choice",
                                "options": ["A) 7", "B) 8", "C) 12", "D) 17"],
                                "correct_answer": "A) 7",
                                "explanation": "Substitute y = 4: 3(4) - 5 = 12 - 5 = 7.",
                                "step_by_step_solution": [
                                    "Step 1: Substitute: 3(4) - 5.",
                                    "Step 2: 12 - 5 = 7."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] Solve for m:  5m - 10 = 25. Enter the value of m:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "7",
                                "explanation": "5m = 25 + 10 = 35 => m = 35 / 5 = 7.",
                                "step_by_step_solution": [
                                    "Step 1: Add 10: 5m = 35.",
                                    "Step 2: Divide by 5: m = 7."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "Translate into an algebraic expression: 'Five more than twice a number n':",
                                "question_type": "multiple_choice",
                                "options": ["A) 2n - 5", "B) 2n + 5", "C) 5n + 2", "D) 2(n + 5)"],
                                "correct_answer": "B) 2n + 5",
                                "explanation": "'Twice a number n' is 2n. 'Five more than' means add 5: 2n + 5.",
                                "step_by_step_solution": [
                                    "Step 1: Twice n = 2n.",
                                    "Step 2: 5 more = 2n + 5."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "Solve for k:  k/3 + 4 = 9",
                                "question_type": "multiple_choice",
                                "options": ["A) 12", "B) 15", "C) 18", "D) 21"],
                                "correct_answer": "B) 15",
                                "explanation": "k/3 = 9 - 4 = 5 => k = 5 × 3 = 15.",
                                "step_by_step_solution": [
                                    "Step 1: k/3 = 9 - 4 = 5.",
                                    "Step 2: Multiply by 3: k = 15."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] If 4(p + 2) = 28, find the value of p:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "5",
                                "explanation": "Divide by 4: p + 2 = 7 => p = 7 - 2 = 5.",
                                "step_by_step_solution": [
                                    "Step 1: p + 2 = 28 / 4 = 7.",
                                    "Step 2: p = 7 - 2 = 5."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "The sum of a number x and 15 is equal to 32. What is the value of x?",
                                "question_type": "multiple_choice",
                                "options": ["A) 15", "B) 17", "C) 19", "D) 21"],
                                "correct_answer": "B) 17",
                                "explanation": "x + 15 = 32 => x = 32 - 15 = 17.",
                                "step_by_step_solution": [
                                    "Step 1: Equation: x + 15 = 32.",
                                    "Step 2: x = 32 - 15 = 17."
                                ],
                                "difficulty": "easy",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] Solve for z:  7z - 8 = 3z + 16. Enter the value of z:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "6",
                                "explanation": "7z - 3z = 16 + 8 => 4z = 24 => z = 6.",
                                "step_by_step_solution": [
                                    "Step 1: Subtract 3z: 4z - 8 = 16.",
                                    "Step 2: Add 8: 4z = 24.",
                                    "Step 3: Divide by 4: z = 6."
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
        "title": "Coordinate & Plane Coast",
        "description": "Chart angles across intersecting lines and measure the area of parallelograms and coastal statistical charts.",
        "grade": 6,
        "icon": "compass",
        "theme_color": "emerald",
        "display_order": 2,
        "topics": [
            {
                "title": "Angles, Parallel Lines & Triangles",
                "description": "Complementary, supplementary, vertically opposite angles, and transversal line angles.",
                "learning_objectives": [
                    "Identify complementary (90°) and supplementary (180°) angles",
                    "Determine vertically opposite angles at intersecting lines",
                    "Identify alternate and corresponding angles formed by parallel lines and transversals"
                ],
                "grade": 6,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Parallel Lines Archipelago",
                        "instructions": "Locate missing angles along intersecting coastlines and parallel shipping channels.",
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
                                "prompt": "Two angles are complementary. If one angle is 38°, what is the other angle?",
                                "question_type": "multiple_choice",
                                "options": ["A) 42°", "B) 52°", "C) 62°", "D) 142°"],
                                "correct_answer": "B) 52°",
                                "explanation": "Complementary angles add up to 90°. 90° - 38° = 52°.",
                                "step_by_step_solution": [
                                    "Step 1: Definition: Complementary angles sum to 90°.",
                                    "Step 2: 90° - 38° = 52°."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Two angles are supplementary. If one angle is 115°, what is the other angle?",
                                "question_type": "multiple_choice",
                                "options": ["A) 65°", "B) 75°", "C) 85°", "D) 95°"],
                                "correct_answer": "A) 65°",
                                "explanation": "Supplementary angles sum to 180°. 180° - 115° = 65°.",
                                "step_by_step_solution": [
                                    "Step 1: Supplementary sum = 180°.",
                                    "Step 2: 180° - 115° = 65°."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] Two lines intersect. If one angle is 72°, what is the size of its vertically opposite angle in degrees?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "72",
                                "explanation": "Vertically opposite angles are equal: 72°.",
                                "step_by_step_solution": [
                                    "Step 1: Vertically opposite angles are congruent.",
                                    "Step 2: Angle = 72°."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "When two parallel lines are cut by a transversal, corresponding angles are:",
                                "question_type": "multiple_choice",
                                "options": ["A) Supplementary", "B) Equal", "C) Complementary", "D) Unequal"],
                                "correct_answer": "B) Equal",
                                "explanation": "Corresponding angles occupying the same relative position at each intersection are equal.",
                                "step_by_step_solution": [
                                    "Step 1: Parallel lines theorem: Corresponding angles are equal."
                                ],
                                "difficulty": "easy",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] If alternate interior angles formed by parallel lines and a transversal are (3x)° and 75°, what is the value of x?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "25",
                                "explanation": "Alternate interior angles are equal: 3x = 75 => x = 25.",
                                "step_by_step_solution": [
                                    "Step 1: 3x = 75.",
                                    "Step 2: x = 75 / 3 = 25."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "An angle is twice its complement. What is the measure of the angle?",
                                "question_type": "multiple_choice",
                                "options": ["A) 30°", "B) 45°", "C) 60°", "D) 75°"],
                                "correct_answer": "C) 60°",
                                "explanation": "Let the angle be 2x and its complement be x. 2x + x = 90° => 3x = 90° => x = 30°. The angle is 2 × 30° = 60°.",
                                "step_by_step_solution": [
                                    "Step 1: x + 2x = 90°.",
                                    "Step 2: 3x = 90° => x = 30°.",
                                    "Step 3: Angle = 2x = 60°."
                                ],
                                "difficulty": "hard",
                                "display_order": 6
                            },
                            {
                                "prompt": "Two adjacent angles on a straight line are (2x + 10)° and (3x + 20)°. What is the value of x?",
                                "question_type": "multiple_choice",
                                "options": ["A) 25", "B) 30", "C) 35", "D) 40"],
                                "correct_answer": "B) 30",
                                "explanation": "Angles on a line sum to 180°: (2x + 10) + (3x + 20) = 180 => 5x + 30 = 180 => 5x = 150 => x = 30.",
                                "step_by_step_solution": [
                                    "Step 1: 5x + 30 = 180.",
                                    "Step 2: 5x = 150.",
                                    "Step 3: x = 30."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] In a triangle, one exterior angle is 125°. If one of the interior opposite angles is 55°, what is the other interior opposite angle in degrees?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "70",
                                "explanation": "Exterior angle = Sum of interior opposite angles: 125° - 55° = 70°.",
                                "step_by_step_solution": [
                                    "Step 1: Exterior angle theorem: ext = opp1 + opp2.",
                                    "Step 2: 125 = 55 + opp2.",
                                    "Step 3: opp2 = 125 - 55 = 70°."
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
                "title": "Area of Parallelograms, Trapezoids & Statistics",
                "description": "Area formulas for parallelograms and trapezoids, and calculating mean, median, mode, and range.",
                "learning_objectives": [
                    "Calculate the area of a parallelogram (base × height)",
                    "Calculate the area of a trapezoid (1/2 × (a + b) × h)",
                    "Determine mean, median, mode, and range of raw datasets"
                ],
                "grade": 6,
                "display_order": 2,
                "missions": [
                    {
                        "title": "The Statistical Shore",
                        "instructions": "Calculate land plot areas and central tendency statistics on the coastal survey.",
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
                                "prompt": "What is the area of a parallelogram with base 12 cm and perpendicular height 7 cm?",
                                "question_type": "multiple_choice",
                                "options": ["A) 42 cm²", "B) 84 cm²", "C) 96 cm²", "D) 38 cm²"],
                                "correct_answer": "B) 84 cm²",
                                "explanation": "Area of parallelogram = base × height = 12 × 7 = 84 cm².",
                                "step_by_step_solution": [
                                    "Step 1: Formula: A = b × h.",
                                    "Step 2: A = 12 × 7 = 84 cm²."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is the median of the numbers: 3, 7, 8, 12, 15?",
                                "question_type": "multiple_choice",
                                "options": ["A) 7", "B) 8", "C) 9", "D) 12"],
                                "correct_answer": "B) 8",
                                "explanation": "The numbers are arranged in order. The middle value is 8.",
                                "step_by_step_solution": [
                                    "Step 1: Ordered list: 3, 7, [8], 12, 15.",
                                    "Step 2: Middle number = 8."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] A trapezoid has parallel sides of length 10 cm and 14 cm, and a height of 6 cm. What is its area in cm²?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "72",
                                "explanation": "Area = 1/2 × (10 + 14) × 6 = 1/2 × 24 × 6 = 12 × 6 = 72 cm².",
                                "step_by_step_solution": [
                                    "Step 1: Formula: A = 1/2(a + b)h.",
                                    "Step 2: a + b = 10 + 14 = 24.",
                                    "Step 3: A = 0.5 × 24 × 6 = 72 cm²."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "What is the mode of this dataset: 4, 6, 7, 6, 9, 6, 4, 11?",
                                "question_type": "multiple_choice",
                                "options": ["A) 4", "B) 6", "C) 7", "D) 9"],
                                "correct_answer": "B) 6",
                                "explanation": "The number 6 appears 3 times, which is more frequent than any other number.",
                                "step_by_step_solution": [
                                    "Step 1: Count frequencies: 4 appears twice, 6 appears three times.",
                                    "Step 2: Mode = 6."
                                ],
                                "difficulty": "easy",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] Find the range of the numbers: 14, 28, 5, 42, 19, 31:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "37",
                                "explanation": "Range = Maximum - Minimum = 42 - 5 = 37.",
                                "step_by_step_solution": [
                                    "Step 1: Maximum = 42.",
                                    "Step 2: Minimum = 5.",
                                    "Step 3: Range = 42 - 5 = 37."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "The mean of five numbers is 18. What is the sum of the five numbers?",
                                "question_type": "multiple_choice",
                                "options": ["A) 72", "B) 80", "C) 90", "D) 100"],
                                "correct_answer": "C) 90",
                                "explanation": "Sum = Mean × Count = 18 × 5 = 90.",
                                "step_by_step_solution": [
                                    "Step 1: Mean = Sum / 5.",
                                    "Step 2: Sum = 18 × 5 = 90."
                                ],
                                "difficulty": "hard",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] What is the median of the six numbers: 5, 8, 10, 14, 18, 20?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "12",
                                "explanation": "With an even count, median is average of 3rd and 4th terms: (10 + 14) / 2 = 24 / 2 = 12.",
                                "step_by_step_solution": [
                                    "Step 1: Ordered list has 6 terms.",
                                    "Step 2: Two middle terms: 10 and 14.",
                                    "Step 3: Average = (10 + 14) / 2 = 12."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "A parallelogram has an area of 108 cm² and a base of 9 cm. What is its perpendicular height?",
                                "question_type": "multiple_choice",
                                "options": ["A) 11 cm", "B) 12 cm", "C) 13 cm", "D) 14 cm"],
                                "correct_answer": "B) 12 cm",
                                "explanation": "Height = Area / base = 108 / 9 = 12 cm.",
                                "step_by_step_solution": [
                                    "Step 1: A = b × h => 108 = 9 × h.",
                                    "Step 2: h = 108 / 9 = 12 cm."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
