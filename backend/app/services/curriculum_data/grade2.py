# Grade 2 Mathematics Curriculum Data — Federal NCP 2022-23
# Strands: Numbers and Operations, Geometry, Measurement & Data Handling

GRADE_2_WORLDS = [
    {
        "title": "Meadow of Numbers",
        "description": "Roam across fields of 3-digit numbers, regrouping rivers, and multiplication orchards.",
        "grade": 2,
        "icon": "sparkles",
        "theme_color": "teal",
        "display_order": 1,
        "topics": [
            {
                "title": "3-Digit Numbers & Place Value (Up to 1000)",
                "description": "Hundreds, tens, and ones, expanded notation, and number comparisons up to 1000.",
                "learning_objectives": [
                    "Read, write, and compare numbers up to 1000",
                    "Identify place value of hundreds, tens, and ones",
                    "Write numbers in expanded form (e.g., 345 = 300 + 40 + 5)"
                ],
                "grade": 2,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Triple-Digit Meadow",
                        "instructions": "Identify the values of hundreds, tens, and ones in 3-digit numbers.",
                        "category": "concept_exploration",
                        "difficulty": "easy",
                        "question_count": 8,
                        "xp_reward": 20,
                        "pass_percentage": 60,
                        "unlock_condition": "always",
                        "display_order": 1,
                        "is_boss": False,
                        "questions": [
                            {
                                "prompt": "In the number 358, what is the value of the digit 3?",
                                "question_type": "multiple_choice",
                                "options": ["A) 3", "B) 30", "C) 300", "D) 358"],
                                "correct_answer": "C) 300",
                                "explanation": "3 is in the hundreds place, so its place value is 300.",
                                "step_by_step_solution": [
                                    "Step 1: In 358: 3 is Hundreds, 5 is Tens, 8 is Ones.",
                                    "Step 2: 3 hundreds = 300."
                                ],
                                "common_mistakes": {
                                    "30": "5 is in the tens place (50), 3 is in the hundreds place (300)."
                                },
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is the expanded form of 472?",
                                "question_type": "multiple_choice",
                                "options": ["A) 400 + 70 + 2", "B) 40 + 7 + 2", "C) 400 + 7 + 20", "D) 4 + 7 + 2"],
                                "correct_answer": "A) 400 + 70 + 2",
                                "explanation": "4 hundreds (400) + 7 tens (70) + 2 ones (2) = 472.",
                                "step_by_step_solution": [
                                    "Step 1: Break down into place values: 400 + 70 + 2."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "Which comparison symbol correctly fills the blank: 645 ___ 654?",
                                "question_type": "multiple_choice",
                                "options": ["A) >", "B) <", "C) =", "D) +"],
                                "correct_answer": "B) <",
                                "explanation": "Both have 6 hundreds. Comparing the tens: 4 tens is less than 5 tens. So 645 < 654.",
                                "step_by_step_solution": [
                                    "Step 1: Hundreds digits are equal (6 = 6).",
                                    "Step 2: Tens digit of 645 is 4; tens digit of 654 is 5.",
                                    "Step 3: Since 4 < 5, 645 < 654."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] What number has 5 hundreds, 0 tens, and 9 ones?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "509",
                                "explanation": "500 + 0 + 9 = 509.",
                                "step_by_step_solution": [
                                    "Step 1: Hundreds = 5, Tens = 0, Ones = 9.",
                                    "Step 2: Combine: 509."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "What number is 100 more than 280?",
                                "question_type": "multiple_choice",
                                "options": ["A) 290", "B) 380", "C) 281", "D) 180"],
                                "correct_answer": "B) 380",
                                "explanation": "Adding 100 increases the hundreds digit by 1: 200 + 100 = 300, so 380.",
                                "step_by_step_solution": [
                                    "Step 1: 280 + 100 = 380."
                                ],
                                "difficulty": "easy",
                                "display_order": 5
                            },
                            {
                                "prompt": "Which number is an EVEN number?",
                                "question_type": "multiple_choice",
                                "options": ["A) 143", "B) 257", "C) 368", "D) 491"],
                                "correct_answer": "C) 368",
                                "explanation": "Even numbers end in 0, 2, 4, 6, or 8. 368 ends in 8.",
                                "step_by_step_solution": [
                                    "Step 1: Look at the last digit (ones place).",
                                    "Step 2: 8 is even, so 368 is even."
                                ],
                                "difficulty": "medium",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] How many tens are in the number 600?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "60",
                                "explanation": "600 / 10 = 60 tens (or 6 hundreds = 60 tens).",
                                "step_by_step_solution": [
                                    "Step 1: 1 hundred = 10 tens.",
                                    "Step 2: 6 hundreds = 60 tens."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "Arrange these numbers in ascending order (smallest to greatest): 712, 172, 271.",
                                "question_type": "multiple_choice",
                                "options": [
                                    "A) 172, 271, 712",
                                    "B) 712, 271, 172",
                                    "C) 271, 172, 712",
                                    "D) 172, 712, 271"
                                ],
                                "correct_answer": "A) 172, 271, 712",
                                "explanation": "172 (1 hundred) < 271 (2 hundreds) < 712 (7 hundreds).",
                                "step_by_step_solution": [
                                    "Step 1: Compare hundreds: 172 is smallest.",
                                    "Step 2: Next is 271.",
                                    "Step 3: Largest is 712."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Addition, Subtraction & Repeated Addition",
                "description": "Multi-digit addition and subtraction with regrouping, and introduction to multiplication.",
                "learning_objectives": [
                    "Add up to 3-digit numbers with carrying",
                    "Subtract up to 3-digit numbers with borrowing",
                    "Represent multiplication as repeated addition and arrays"
                ],
                "grade": 2,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Regrouping Rapids",
                        "instructions": "Navigate addition and subtraction with carrying and borrowing across rapids.",
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
                                "prompt": "Calculate: 48 + 27 =",
                                "question_type": "multiple_choice",
                                "options": ["A) 65", "B) 75", "C) 71", "D) 85"],
                                "correct_answer": "B) 75",
                                "explanation": "8 + 7 = 15 (write 5, carry 1). 1 + 4 + 2 = 7. Total = 75.",
                                "step_by_step_solution": [
                                    "Step 1: Add ones: 8 + 7 = 15 ones = 1 ten and 5 ones.",
                                    "Step 2: Add tens: 1 (carried) + 4 + 2 = 7 tens.",
                                    "Step 3: Combine: 75."
                                ],
                                "common_mistakes": {
                                    "65": "Did you forget to add the 1 carried ten?"
                                },
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Calculate: 63 - 28 =",
                                "question_type": "multiple_choice",
                                "options": ["A) 35", "B) 45", "C) 37", "D) 41"],
                                "correct_answer": "A) 35",
                                "explanation": "Borrow 1 ten from 6 (becomes 5). 13 - 8 = 5. 5 - 2 = 3. Result = 35.",
                                "step_by_step_solution": [
                                    "Step 1: Cannot take 8 from 3. Regroup 1 ten: 13 ones.",
                                    "Step 2: 13 - 8 = 5 ones.",
                                    "Step 3: 5 tens - 2 tens = 3 tens. Result = 35."
                                ],
                                "common_mistakes": {
                                    "45": "Remember to reduce the tens digit from 6 to 5 after regrouping."
                                },
                                "difficulty": "medium",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] Solve: 135 + 242 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "377",
                                "explanation": "135 + 242 = 377.",
                                "step_by_step_solution": [
                                    "Step 1: Ones: 5 + 2 = 7.",
                                    "Step 2: Tens: 3 + 4 = 7.",
                                    "Step 3: Hundreds: 1 + 2 = 3. Total = 377."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "A shopkeeper had 85 mangoes and sold 39. How many mangoes are left?",
                                "question_type": "multiple_choice",
                                "options": ["A) 46", "B) 54", "C) 44", "D) 56"],
                                "correct_answer": "A) 46",
                                "explanation": "85 - 39 = 46 mangoes.",
                                "step_by_step_solution": [
                                    "Step 1: Regroup 1 ten: 15 - 9 = 6.",
                                    "Step 2: 7 - 3 = 4 tens. Total = 46."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] What is 300 - 150?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "150",
                                "explanation": "300 - 150 = 150.",
                                "step_by_step_solution": [
                                    "Step 1: 30 tens - 15 tens = 15 tens = 150."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "Solve: 256 + 184 =",
                                "question_type": "multiple_choice",
                                "options": ["A) 430", "B) 440", "C) 445", "D) 450"],
                                "correct_answer": "B) 440",
                                "explanation": "6 + 4 = 10 (0, carry 1). 1 + 5 + 8 = 14 (4, carry 1). 1 + 2 + 1 = 4. Total = 440.",
                                "step_by_step_solution": [
                                    "Step 1: 6 + 4 = 10 (carry 1).",
                                    "Step 2: 1 + 5 + 8 = 14 (carry 1).",
                                    "Step 3: 1 + 2 + 1 = 4. Sum = 440."
                                ],
                                "difficulty": "hard",
                                "display_order": 6
                            },
                            {
                                "prompt": "Hamza scored 124 points in game 1 and 188 points in game 2. How many points did he score in total?",
                                "question_type": "multiple_choice",
                                "options": ["A) 302", "B) 312", "C) 322", "D) 310"],
                                "correct_answer": "B) 312",
                                "explanation": "124 + 188 = 312 points.",
                                "step_by_step_solution": [
                                    "Step 1: 4 + 8 = 12 (carry 1).",
                                    "Step 2: 1 + 2 + 8 = 11 (carry 1).",
                                    "Step 3: 1 + 1 + 1 = 3. Total = 312."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] Calculate: 500 - 235 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "265",
                                "explanation": "500 - 235 = 265.",
                                "step_by_step_solution": [
                                    "Step 1: Regroup across zeros: 10 - 5 = 5.",
                                    "Step 2: 9 - 3 = 6.",
                                    "Step 3: 4 - 2 = 2. Difference = 265."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 8
                            }
                        ]
                    },
                    {
                        "title": "Repeated Addition Orchard",
                        "instructions": "Harvest fruit by grouping items and converting repeated addition into multiplication.",
                        "category": "practice",
                        "difficulty": "medium",
                        "question_count": 8,
                        "xp_reward": 20,
                        "pass_percentage": 60,
                        "unlock_condition": "always",
                        "display_order": 2,
                        "is_boss": False,
                        "questions": [
                            {
                                "prompt": "Which multiplication expression represents: 3 + 3 + 3 + 3?",
                                "question_type": "multiple_choice",
                                "options": ["A) 3 × 3", "B) 4 × 3", "C) 3 + 4", "D) 4 × 4"],
                                "correct_answer": "B) 4 × 3",
                                "explanation": "There are 4 groups of 3, which is 4 × 3 = 12.",
                                "step_by_step_solution": [
                                    "Step 1: Count how many 3s: there are 4.",
                                    "Step 2: Written as multiplication: 4 × 3."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "There are 5 baskets. Each basket contains 2 apples. How many apples are there in total?",
                                "question_type": "multiple_choice",
                                "options": ["A) 7", "B) 8", "C) 10", "D) 12"],
                                "correct_answer": "C) 10",
                                "explanation": "5 groups of 2 = 5 × 2 = 10 apples.",
                                "step_by_step_solution": [
                                    "Step 1: 2 + 2 + 2 + 2 + 2 = 10.",
                                    "Step 2: 5 × 2 = 10."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] What is 4 × 5?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "20",
                                "explanation": "4 groups of 5 is 20.",
                                "step_by_step_solution": [
                                    "Step 1: 5 + 5 + 5 + 5 = 20."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "Which addition sentence matches 3 × 4?",
                                "question_type": "multiple_choice",
                                "options": ["A) 3 + 3 + 3", "B) 4 + 4 + 4", "C) 3 + 4", "D) 4 + 4 + 4 + 4"],
                                "correct_answer": "B) 4 + 4 + 4",
                                "explanation": "3 × 4 means 3 groups of 4: 4 + 4 + 4 = 12.",
                                "step_by_step_solution": [
                                    "Step 1: 3 times 4 = 4 + 4 + 4."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "An array has 3 rows with 5 stars in each row. How many stars are there altogether?",
                                "question_type": "multiple_choice",
                                "options": ["A) 8", "B) 12", "C) 15", "D) 18"],
                                "correct_answer": "C) 15",
                                "explanation": "3 rows × 5 stars = 15 stars.",
                                "step_by_step_solution": [
                                    "Step 1: 3 × 5 = 15."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] What is 10 × 3?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "30",
                                "explanation": "10 groups of 3 = 30.",
                                "step_by_step_solution": [
                                    "Step 1: Count by tens 3 times: 10, 20, 30."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "If 1 car has 4 wheels, how many wheels do 6 cars have?",
                                "question_type": "multiple_choice",
                                "options": ["A) 20", "B) 24", "C) 28", "D) 30"],
                                "correct_answer": "B) 24",
                                "explanation": "6 cars × 4 wheels = 24 wheels.",
                                "step_by_step_solution": [
                                    "Step 1: 6 × 4 = 24."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "Divide 12 candies equally among 3 children. How many candies does each child get?",
                                "question_type": "multiple_choice",
                                "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
                                "correct_answer": "B) 4",
                                "explanation": "12 shared equally into 3 groups gives 4 in each group (12 ÷ 3 = 4).",
                                "step_by_step_solution": [
                                    "Step 1: Think what multiplied by 3 gives 12: 3 × 4 = 12.",
                                    "Step 2: 12 ÷ 3 = 4 candies each."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "title": "Dimension Grove",
        "description": "Explore 3D geometric solids, patterns, standard measurement units, and clock reading.",
        "grade": 2,
        "icon": "globe",
        "theme_color": "blue",
        "display_order": 2,
        "topics": [
            {
                "title": "3D Shapes & Patterns",
                "description": "Attributes of 3D solids (cube, cuboid, cylinder, cone, sphere) and visual patterns.",
                "learning_objectives": [
                    "Identify cube, cuboid, sphere, cylinder, and cone",
                    "Count faces, edges, and vertices of 3D solids",
                    "Identify and extend growing and repeating geometric patterns"
                ],
                "grade": 2,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Solid Geometry Sanctuary",
                        "instructions": "Examine 3D solids and uncover pattern rules in the ancient geometric grove.",
                        "category": "concept_exploration",
                        "difficulty": "easy",
                        "question_count": 8,
                        "xp_reward": 20,
                        "pass_percentage": 60,
                        "unlock_condition": "always",
                        "display_order": 1,
                        "is_boss": False,
                        "questions": [
                            {
                                "prompt": "Which 3D shape looks like a football or a globe?",
                                "question_type": "multiple_choice",
                                "options": ["A) Cylinder", "B) Cone", "C) Sphere", "D) Cube"],
                                "correct_answer": "C) Sphere",
                                "explanation": "A sphere is completely round with no edges and no vertices, like a ball.",
                                "step_by_step_solution": [
                                    "Step 1: A round 3D solid is called a sphere."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "How many flat faces does a standard cube have?",
                                "question_type": "multiple_choice",
                                "options": ["A) 4", "B) 6", "C) 8", "D) 12"],
                                "correct_answer": "B) 6",
                                "explanation": "A cube has 6 square faces (top, bottom, front, back, left, right).",
                                "step_by_step_solution": [
                                    "Step 1: Think of a playing die (dice): numbers 1 to 6 on 6 faces."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] How many corners (vertices) does a cube have?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "8",
                                "explanation": "A cube has 8 vertices (4 on top, 4 on the bottom).",
                                "step_by_step_solution": [
                                    "Step 1: Count corners: 4 top corners + 4 bottom corners = 8."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "Which 3D solid has 2 flat circular faces and 1 curved surface, like a tin of soup?",
                                "question_type": "multiple_choice",
                                "options": ["A) Cone", "B) Cylinder", "C) Cuboid", "D) Sphere"],
                                "correct_answer": "B) Cylinder",
                                "explanation": "A cylinder has 2 circular ends and a curved surface connecting them.",
                                "step_by_step_solution": [
                                    "Step 1: Tin can shape = Cylinder."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "Which 3D shape has 1 circular base and 1 pointed top vertex, like an ice-cream cone?",
                                "question_type": "multiple_choice",
                                "options": ["A) Cylinder", "B) Cone", "C) Cube", "D) Pyramid"],
                                "correct_answer": "B) Cone",
                                "explanation": "A cone has a circular base tapering to a single apex.",
                                "step_by_step_solution": [
                                    "Step 1: Pointed solid with round base = Cone."
                                ],
                                "difficulty": "easy",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] How many straight edges does a cube have?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "12",
                                "explanation": "A cube has 12 edges (4 top, 4 bottom, 4 vertical).",
                                "step_by_step_solution": [
                                    "Step 1: 4 top edges + 4 bottom edges + 4 vertical edges = 12."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "What is the missing term in this growing pattern: 2, 4, 6, 8, __, 12?",
                                "question_type": "multiple_choice",
                                "options": ["A) 9", "B) 10", "C) 11", "D) 14"],
                                "correct_answer": "B) 10",
                                "explanation": "The rule is to add 2 each time. 8 + 2 = 10.",
                                "step_by_step_solution": [
                                    "Step 1: Pattern increases by +2.",
                                    "Step 2: 8 + 2 = 10."
                                ],
                                "difficulty": "medium",
                                "display_order": 7
                            },
                            {
                                "prompt": "Which shape can both roll and slide?",
                                "question_type": "multiple_choice",
                                "options": ["A) Cube", "B) Cylinder", "C) Sphere", "D) Triangular prism"],
                                "correct_answer": "B) Cylinder",
                                "explanation": "A cylinder rolls on its curved surface and slides on its flat circular face.",
                                "step_by_step_solution": [
                                    "Step 1: Curved face allows rolling.",
                                    "Step 2: Flat face allows sliding. A cylinder has both."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Standard Units, Time & Pictographs",
                "description": "Standard metric measurement (m, cm, kg, g, L), clock reading to half/quarter hour, and charts.",
                "learning_objectives": [
                    "Use meters and centimeters to measure length",
                    "Use kilograms and grams to measure mass",
                    "Read analog clocks to the half-hour and quarter-hour, and read pictographs"
                ],
                "grade": 2,
                "display_order": 2,
                "missions": [
                    {
                        "title": "The Metric Clocktower",
                        "instructions": "Measure distances, tell precise times, and read data on the clocktower charts.",
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
                                "prompt": "How many centimeters are there in 1 meter?",
                                "question_type": "multiple_choice",
                                "options": ["A) 10 cm", "B) 50 cm", "C) 100 cm", "D) 1000 cm"],
                                "correct_answer": "C) 100 cm",
                                "explanation": "There are exactly 100 centimeters in 1 meter.",
                                "step_by_step_solution": [
                                    "Step 1: Standard metric length conversion: 1 m = 100 cm."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "When the minute hand points to 6 and the hour hand is between 4 and 5, what time is it?",
                                "question_type": "multiple_choice",
                                "options": ["A) 4 o'clock", "B) Half past 4 (4:30)", "C) 5 o'clock", "D) Half past 5 (5:30)"],
                                "correct_answer": "B) Half past 4 (4:30)",
                                "explanation": "Minute hand at 6 indicates 30 minutes past the hour. Since the hour hand is past 4, it is 4:30.",
                                "step_by_step_solution": [
                                    "Step 1: 6 on clock = 30 minutes (half past).",
                                    "Step 2: Hour hand has passed 4. Time is 4:30."
                                ],
                                "difficulty": "medium",
                                "display_order": 2
                            },
                            {
                                "prompt": "Which unit is best to measure the mass of a bag of flour?",
                                "question_type": "multiple_choice",
                                "options": ["A) Millimeters", "B) Centimeters", "C) Kilograms", "D) Liters"],
                                "correct_answer": "C) Kilograms",
                                "explanation": "Kilograms (kg) are used to measure heavier masses like bags of flour.",
                                "step_by_step_solution": [
                                    "Step 1: Mass/weight is measured in grams or kilograms.",
                                    "Step 2: For heavy grocery items, kilograms (kg) is the standard unit."
                                ],
                                "difficulty": "easy",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] How many grams are equal to 1 kilogram?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "1000",
                                "explanation": "1 kilogram = 1000 grams.",
                                "step_by_step_solution": [
                                    "Step 1: 'Kilo' means one thousand.",
                                    "Step 2: 1 kg = 1000 g."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "What time is shown when the minute hand points to 3 and the hour hand is just past 7?",
                                "question_type": "multiple_choice",
                                "options": ["A) Quarter past 7 (7:15)", "B) Quarter to 7 (6:45)", "C) Half past 7 (7:30)", "D) 7 o'clock"],
                                "correct_answer": "A) Quarter past 7 (7:15)",
                                "explanation": "The minute hand at 3 represents 15 minutes past the hour (quarter past). It is 7:15.",
                                "step_by_step_solution": [
                                    "Step 1: 3 on the clock = 3 × 5 = 15 minutes.",
                                    "Step 2: 15 minutes past 7 is Quarter past 7."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "In a pictograph, 1 picture of an apple represents 2 real apples. If there are 4 apple pictures next to Bilal's name, how many real apples does Bilal have?",
                                "question_type": "multiple_choice",
                                "options": ["A) 4", "B) 6", "C) 8", "D) 10"],
                                "correct_answer": "C) 8",
                                "explanation": "4 pictures × 2 apples per picture = 8 apples.",
                                "step_by_step_solution": [
                                    "Step 1: Key: 1 picture = 2 apples.",
                                    "Step 2: 4 × 2 = 8 apples."
                                ],
                                "difficulty": "medium",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] A water bottle has a capacity of 2 liters. How many liters can 4 identical bottles hold?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "8",
                                "explanation": "4 × 2 = 8 liters.",
                                "step_by_step_solution": [
                                    "Step 1: 4 bottles × 2 liters each = 8 liters."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "A ribbon was 95 cm long. Ayesha cut off 38 cm to wrap a gift. How much ribbon is left?",
                                "question_type": "multiple_choice",
                                "options": ["A) 53 cm", "B) 57 cm", "C) 67 cm", "D) 63 cm"],
                                "correct_answer": "B) 57 cm",
                                "explanation": "95 - 38 = 57 cm.",
                                "step_by_step_solution": [
                                    "Step 1: 15 - 8 = 7.",
                                    "Step 2: 8 - 3 = 5 tens.",
                                    "Step 3: Remaining length = 57 cm."
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
