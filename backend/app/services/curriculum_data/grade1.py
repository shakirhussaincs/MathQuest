# Grade 1 Mathematics Curriculum Data — Federal NCP 2022-23
# Strands: Numbers and Operations, Geometry, Measurement & Currency

GRADE_1_WORLDS = [
    {
        "title": "Numberland Safari",
        "description": "Explore numbers up to 100, tens and ones, and wild animal addition trails in the savannah.",
        "grade": 1,
        "icon": "compass",
        "theme_color": "emerald",
        "display_order": 1,
        "topics": [
            {
                "title": "Counting & Place Value (1–100)",
                "description": "Count forward and backward, compare quantities, and understand tens and ones.",
                "learning_objectives": [
                    "Count, read, and write numbers up to 100",
                    "Identify place value of tens and ones in 2-digit numbers",
                    "Compare and order numbers from smallest to largest"
                ],
                "grade": 1,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Safari Number Quest",
                        "instructions": "Count the animals on the safari path, compare numbers, and complete counting sequences.",
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
                                "prompt": "How many zebras are in a group of 5 zebras if 2 more join them?",
                                "question_type": "multiple_choice",
                                "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
                                "correct_answer": "B) 7",
                                "explanation": "Start with 5 and count on 2 more: 6, 7. So there are 7 zebras.",
                                "step_by_step_solution": [
                                    "Step 1: Identify the initial count: 5 zebras.",
                                    "Step 2: Add 2 more: 5 + 2 = 7.",
                                    "Step 3: Verification: 5, 6, 7. Correct total is 7."
                                ],
                                "common_mistakes": {
                                    "6": "You only counted 1 zebra instead of 2.",
                                    "8": "Check your counting; 5 + 2 is 7, not 8."
                                },
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Which number comes directly after 19?",
                                "question_type": "multiple_choice",
                                "options": ["A) 18", "B) 20", "C) 21", "D) 29"],
                                "correct_answer": "B) 20",
                                "explanation": "Counting forward: 18, 19, 20. The number after 19 is 20.",
                                "step_by_step_solution": [
                                    "Step 1: Recall the counting sequence in the teens.",
                                    "Step 2: After nineteen (19) comes twenty (20)."
                                ],
                                "common_mistakes": {
                                    "18": "18 comes before 19, not after.",
                                    "21": "21 comes after 20."
                                },
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "Which number is greater: 14 or 17?",
                                "question_type": "multiple_choice",
                                "options": ["A) 14", "B) 17", "C) They are equal", "D) Neither"],
                                "correct_answer": "B) 17",
                                "explanation": "Both have 1 ten, but 17 has 7 ones while 14 has 4 ones. 7 is greater than 4, so 17 is greater.",
                                "step_by_step_solution": [
                                    "Step 1: Compare the tens digit: both have 1 ten.",
                                    "Step 2: Compare the ones digit: 7 is greater than 4.",
                                    "Step 3: Therefore, 17 > 14."
                                ],
                                "common_mistakes": {
                                    "14": "Look at the ones digit: 4 is smaller than 7."
                                },
                                "difficulty": "easy",
                                "display_order": 3
                            },
                            {
                                "prompt": "What is the missing number in the sequence: 10, 20, 30, __, 50?",
                                "question_type": "multiple_choice",
                                "options": ["A) 35", "B) 40", "C) 45", "D) 60"],
                                "correct_answer": "B) 40",
                                "explanation": "We are skip-counting by tens: 10, 20, 30, 40, 50.",
                                "step_by_step_solution": [
                                    "Step 1: Notice the pattern increases by 10 each time.",
                                    "Step 2: 30 + 10 = 40.",
                                    "Step 3: Verify the next number: 40 + 10 = 50."
                                ],
                                "common_mistakes": {
                                    "35": "We are counting by tens, not fives."
                                },
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] Count the total: You have 8 apples and find 3 more. How many apples do you have in total?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "11",
                                "explanation": "8 + 3 = 11.",
                                "step_by_step_solution": [
                                    "Step 1: Start at 8.",
                                    "Step 2: Count up 3: 9, 10, 11."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "Which of these numbers is the smallest: 25, 12, 31, 19?",
                                "question_type": "multiple_choice",
                                "options": ["A) 25", "B) 12", "C) 31", "D) 19"],
                                "correct_answer": "B) 12",
                                "explanation": "12 has only 1 ten and 2 ones, which is less than 19, 25, and 31.",
                                "step_by_step_solution": [
                                    "Step 1: Look at the tens digits: 12 and 19 have 1 ten, 25 has 2 tens, 31 has 3 tens.",
                                    "Step 2: Between 12 and 19, 12 has fewer ones (2 < 9).",
                                    "Step 3: Smallest number is 12."
                                ],
                                "common_mistakes": {
                                    "19": "12 is smaller than 19 because 2 ones is less than 9 ones."
                                },
                                "difficulty": "medium",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] If you count backwards from 15, what number comes right before 15?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "14",
                                "explanation": "15 - 1 = 14.",
                                "step_by_step_solution": [
                                    "Step 1: Count backwards from 15: 15, 14, 13...",
                                    "Step 2: The number immediately before 15 is 14."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "Which number represents eight tens and three ones?",
                                "question_type": "multiple_choice",
                                "options": ["A) 38", "B) 83", "C) 803", "D) 11"],
                                "correct_answer": "B) 83",
                                "explanation": "8 tens = 80, 3 ones = 3. 80 + 3 = 83.",
                                "step_by_step_solution": [
                                    "Step 1: Value of 8 tens is 80.",
                                    "Step 2: Value of 3 ones is 3.",
                                    "Step 3: Combine them: 83."
                                ],
                                "common_mistakes": {
                                    "38": "Remember the tens digit comes first: 8 tens is 80, not 30."
                                },
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    },
                    {
                        "title": "The Tens & Ones Outpost",
                        "instructions": "Break numbers into bundles of ten and single units to master place value.",
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
                                "prompt": "In the number 47, what digit is in the tens place?",
                                "question_type": "multiple_choice",
                                "options": ["A) 4", "B) 7", "C) 40", "D) 11"],
                                "correct_answer": "A) 4",
                                "explanation": "In 47, 4 is in the tens place (meaning 40) and 7 is in the ones place.",
                                "step_by_step_solution": [
                                    "Step 1: In a 2-digit number, the left digit is Tens, right is Ones.",
                                    "Step 2: Tens digit is 4."
                                ],
                                "common_mistakes": {
                                    "7": "7 is in the ones place.",
                                    "40": "The digit itself is 4, which has a value of 40."
                                },
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is the value of 5 in the number 52?",
                                "question_type": "multiple_choice",
                                "options": ["A) 5", "B) 50", "C) 500", "D) 2"],
                                "correct_answer": "B) 50",
                                "explanation": "5 is in the tens place, so its value is 5 tens = 50.",
                                "step_by_step_solution": [
                                    "Step 1: Identify place: tens place.",
                                    "Step 2: 5 tens = 50."
                                ],
                                "common_mistakes": {
                                    "5": "The digit is 5, but its place value is 50."
                                },
                                "difficulty": "medium",
                                "display_order": 2
                            },
                            {
                                "prompt": "Which sum equals 64?",
                                "question_type": "multiple_choice",
                                "options": ["A) 60 + 4", "B) 6 + 4", "C) 60 + 40", "D) 40 + 6"],
                                "correct_answer": "A) 60 + 4",
                                "explanation": "64 is made of 6 tens (60) and 4 ones (4). 60 + 4 = 64.",
                                "step_by_step_solution": [
                                    "Step 1: Decompose 64 into tens and ones.",
                                    "Step 2: 6 tens = 60, 4 ones = 4.",
                                    "Step 3: 60 + 4 = 64."
                                ],
                                "common_mistakes": {
                                    "40 + 6": "40 + 6 is 46, not 64."
                                },
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] How many tens are there in 70?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "7",
                                "explanation": "70 = 7 tens and 0 ones.",
                                "step_by_step_solution": [
                                    "Step 1: Divide 70 by 10.",
                                    "Step 2: 70 / 10 = 7 tens."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "What number is 10 more than 35?",
                                "question_type": "multiple_choice",
                                "options": ["A) 36", "B) 45", "C) 25", "D) 55"],
                                "correct_answer": "B) 45",
                                "explanation": "Adding 10 increases the tens digit by 1: 3 tens + 1 ten = 4 tens. So 35 + 10 = 45.",
                                "step_by_step_solution": [
                                    "Step 1: Start with 35.",
                                    "Step 2: Add 10: 35 + 10 = 45."
                                ],
                                "common_mistakes": {
                                    "36": "You added 1 one instead of 1 ten."
                                },
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "Which number has 9 tens and 0 ones?",
                                "question_type": "multiple_choice",
                                "options": ["A) 9", "B) 90", "C) 99", "D) 19"],
                                "correct_answer": "B) 90",
                                "explanation": "9 tens and 0 ones is ninety (90).",
                                "step_by_step_solution": [
                                    "Step 1: 9 tens = 90.",
                                    "Step 2: 0 ones = 0.",
                                    "Step 3: Total = 90."
                                ],
                                "difficulty": "easy",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] What is 10 less than 80?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "70",
                                "explanation": "80 - 10 = 70.",
                                "step_by_step_solution": [
                                    "Step 1: 8 tens minus 1 ten = 7 tens.",
                                    "Step 2: 7 tens = 70."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "Ali has 3 bundles of 10 pencils and 6 single pencils. How many pencils does Ali have altogether?",
                                "question_type": "multiple_choice",
                                "options": ["A) 9", "B) 30", "C) 36", "D) 63"],
                                "correct_answer": "C) 36",
                                "explanation": "3 bundles of 10 = 30 pencils. 30 + 6 = 36 pencils.",
                                "step_by_step_solution": [
                                    "Step 1: 3 bundles of 10 = 30.",
                                    "Step 2: Add 6 singles: 30 + 6 = 36."
                                ],
                                "common_mistakes": {
                                    "9": "You added 3 + 6 without realizing each bundle has 10 pencils.",
                                    "63": "Don't reverse the tens and ones."
                                },
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Basic Addition and Subtraction",
                "description": "Combine groups and find differences within 20 and up to 100 without carrying.",
                "learning_objectives": [
                    "Add 1-digit numbers with sums up to 20",
                    "Subtract 1-digit numbers from numbers up to 20",
                    "Solve single-step addition and subtraction word problems"
                ],
                "grade": 1,
                "display_order": 2,
                "missions": [
                    {
                        "title": "River Crossing Addition",
                        "instructions": "Solve addition challenges to build stepping stones across the river.",
                        "category": "practice",
                        "difficulty": "easy",
                        "question_count": 8,
                        "xp_reward": 20,
                        "pass_percentage": 60,
                        "unlock_condition": "always",
                        "display_order": 1,
                        "is_boss": False,
                        "questions": [
                            {
                                "prompt": "What is 4 + 5?",
                                "question_type": "multiple_choice",
                                "options": ["A) 8", "B) 9", "C) 10", "D) 11"],
                                "correct_answer": "B) 9",
                                "explanation": "4 + 5 = 9.",
                                "step_by_step_solution": [
                                    "Step 1: Start at 4.",
                                    "Step 2: Count up 5: 5, 6, 7, 8, 9."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is 7 + 3?",
                                "question_type": "multiple_choice",
                                "options": ["A) 9", "B) 10", "C) 11", "D) 12"],
                                "correct_answer": "B) 10",
                                "explanation": "7 and 3 make a number bond of 10.",
                                "step_by_step_solution": [
                                    "Step 1: 7 + 3 = 10 (Pairs that make 10)."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] Calculate: 6 + 6 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "12",
                                "explanation": "Double 6 is 12.",
                                "step_by_step_solution": [
                                    "Step 1: 6 + 6 = 12."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "Sara has 9 marbles. Her brother gives her 6 more. How many marbles does Sara have now?",
                                "question_type": "multiple_choice",
                                "options": ["A) 14", "B) 15", "C) 16", "D) 17"],
                                "correct_answer": "B) 15",
                                "explanation": "9 + 6 = 15.",
                                "step_by_step_solution": [
                                    "Step 1: 9 + 1 = 10.",
                                    "Step 2: 10 + 5 = 15."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "What is 12 + 5?",
                                "question_type": "multiple_choice",
                                "options": ["A) 16", "B) 17", "C) 18", "D) 19"],
                                "correct_answer": "B) 17",
                                "explanation": "2 ones + 5 ones = 7 ones. So 12 + 5 = 17.",
                                "step_by_step_solution": [
                                    "Step 1: 2 + 5 = 7.",
                                    "Step 2: 10 + 7 = 17."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] Solve: 20 + 30 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "50",
                                "explanation": "2 tens + 3 tens = 5 tens = 50.",
                                "step_by_step_solution": [
                                    "Step 1: 2 + 3 = 5.",
                                    "Step 2: 20 + 30 = 50."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "Which two numbers add up to 8?",
                                "question_type": "multiple_choice",
                                "options": ["A) 3 and 4", "B) 5 and 3", "C) 6 and 3", "D) 4 and 5"],
                                "correct_answer": "B) 5 and 3",
                                "explanation": "5 + 3 = 8.",
                                "step_by_step_solution": [
                                    "Step 1: Check 5 + 3: 5, 6, 7, 8. Correct."
                                ],
                                "difficulty": "easy",
                                "display_order": 7
                            },
                            {
                                "prompt": "A baker baked 14 cupcakes in the morning and 5 in the afternoon. How many cupcakes were baked in total?",
                                "question_type": "multiple_choice",
                                "options": ["A) 18", "B) 19", "C) 20", "D) 21"],
                                "correct_answer": "B) 19",
                                "explanation": "14 + 5 = 19 cupcakes.",
                                "step_by_step_solution": [
                                    "Step 1: 4 + 5 = 9 ones.",
                                    "Step 2: 1 ten + 9 ones = 19."
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
        "title": "Shapes & Time Valley",
        "description": "Discover shapes, patterns, clock hands, and currency in the geometric oasis.",
        "grade": 1,
        "icon": "map",
        "theme_color": "cyan",
        "display_order": 2,
        "topics": [
            {
                "title": "2D Shapes & Spatial Sense",
                "description": "Name circles, squares, rectangles, triangles and understand positions.",
                "learning_objectives": [
                    "Identify circle, square, rectangle, and triangle",
                    "Count sides and corners of 2D shapes",
                    "Use spatial position words (above, below, inside, outside)"
                ],
                "grade": 1,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Shape Detective Expedition",
                        "instructions": "Inspect shapes and their properties to solve the mystery of the geometric temple.",
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
                                "prompt": "How many sides does a triangle have?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
                                "correct_answer": "B) 3",
                                "explanation": "A triangle always has exactly 3 straight sides and 3 corners.",
                                "step_by_step_solution": [
                                    "Step 1: 'Tri' means three.",
                                    "Step 2: A triangle has 3 sides."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Which shape has 4 equal straight sides and 4 square corners?",
                                "question_type": "multiple_choice",
                                "options": ["A) Circle", "B) Triangle", "C) Square", "D) Oval"],
                                "correct_answer": "C) Square",
                                "explanation": "A square has 4 straight sides that are all equal in length.",
                                "step_by_step_solution": [
                                    "Step 1: Identify key feature: 4 equal sides.",
                                    "Step 2: That defines a square."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "Which shape has no straight sides and no corners?",
                                "question_type": "multiple_choice",
                                "options": ["A) Square", "B) Circle", "C) Rectangle", "D) Triangle"],
                                "correct_answer": "B) Circle",
                                "explanation": "A circle is round with a continuous curved boundary.",
                                "step_by_step_solution": [
                                    "Step 1: Round shape with zero straight sides = Circle."
                                ],
                                "difficulty": "easy",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] How many corners (vertices) does a rectangle have?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "4",
                                "explanation": "A rectangle has 4 corners.",
                                "step_by_step_solution": [
                                    "Step 1: Count the corners where sides meet: 1, 2, 3, 4."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "If a bird is sitting on a branch and a worm is on the ground under the tree, where is the bird compared to the worm?",
                                "question_type": "multiple_choice",
                                "options": ["A) Below", "B) Above", "C) Inside", "D) Left"],
                                "correct_answer": "B) Above",
                                "explanation": "The bird is high up in the tree, which is above the ground.",
                                "step_by_step_solution": [
                                    "Step 1: Branch is higher than ground.",
                                    "Step 2: Higher means 'above'."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "Which of these everyday objects has a circular face?",
                                "question_type": "multiple_choice",
                                "options": ["A) A book", "B) A wall clock face", "C) A door", "D) A brick"],
                                "correct_answer": "B) A wall clock face",
                                "explanation": "A standard round clock face is shaped like a circle.",
                                "step_by_step_solution": [
                                    "Step 1: Books and doors are rectangular.",
                                    "Step 2: A round clock face is a circle."
                                ],
                                "difficulty": "medium",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] How many sides does a rectangle have?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "4",
                                "explanation": "A rectangle has 4 sides (opposite sides are equal).",
                                "step_by_step_solution": [
                                    "Step 1: A rectangle is a four-sided quadrilateral: 4 sides."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "Look at the pattern: Circle, Square, Circle, Square, Circle, ___. What shape comes next?",
                                "question_type": "multiple_choice",
                                "options": ["A) Triangle", "B) Square", "C) Circle", "D) Rectangle"],
                                "correct_answer": "B) Square",
                                "explanation": "The repeating pattern alternates: Circle, Square. After Circle comes Square.",
                                "step_by_step_solution": [
                                    "Step 1: The repeating core is (Circle, Square).",
                                    "Step 2: Following Circle is Square."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Measurement, Time & Currency",
                "description": "Compare length, tell time on the hour, and count Pakistani rupee coins and notes.",
                "learning_objectives": [
                    "Compare length, height, and mass (heavy/light, long/short)",
                    "Read time to the hour on an analog clock",
                    "Recognize Pakistani currency (Rs. 1, 2, 5, 10 coins and notes)"
                ],
                "grade": 1,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Time & Coin Bazaar",
                        "instructions": "Help the shopkeeper tell time and count coins in the village marketplace.",
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
                                "prompt": "On an analog clock, the minute hand points to 12 and the hour hand points to 3. What time is it?",
                                "question_type": "multiple_choice",
                                "options": ["A) 12 o'clock", "B) 3 o'clock", "C) 6 o'clock", "D) 9 o'clock"],
                                "correct_answer": "B) 3 o'clock",
                                "explanation": "When the long minute hand points to 12, the short hour hand shows the hour. Here it points to 3, so it is 3 o'clock.",
                                "step_by_step_solution": [
                                    "Step 1: Minute hand at 12 means ':00' (o'clock).",
                                    "Step 2: Hour hand at 3 means 3 o'clock."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Which object is heavier: an elephant or a feather?",
                                "question_type": "multiple_choice",
                                "options": ["A) A feather", "B) An elephant", "C) Both are equal", "D) Cannot tell"],
                                "correct_answer": "B) An elephant",
                                "explanation": "An elephant has much greater mass and is much heavier than a light feather.",
                                "step_by_step_solution": [
                                    "Step 1: Compare the weight of both objects.",
                                    "Step 2: An elephant is heavy; a feather is light."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "You have a 5-rupee coin and a 2-rupee coin. How much money do you have in total?",
                                "question_type": "multiple_choice",
                                "options": ["A) Rs. 3", "B) Rs. 7", "C) Rs. 8", "D) Rs. 10"],
                                "correct_answer": "B) Rs. 7",
                                "explanation": "5 + 2 = 7 rupees.",
                                "step_by_step_solution": [
                                    "Step 1: Add the coin values: 5 + 2 = 7 rupees."
                                ],
                                "difficulty": "easy",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] How many hours are shown when the hour hand points to 8 and the minute hand is at 12? Enter the hour number:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "8",
                                "explanation": "It is 8 o'clock, so the hour is 8.",
                                "step_by_step_solution": [
                                    "Step 1: The hour hand points directly to 8."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "Which pencil is the longest: Pencil A (10 paperclips long), Pencil B (6 paperclips long), or Pencil C (12 paperclips long)?",
                                "question_type": "multiple_choice",
                                "options": ["A) Pencil A", "B) Pencil B", "C) Pencil C", "D) All are equal"],
                                "correct_answer": "C) Pencil C",
                                "explanation": "12 is greater than 10 and 6, so Pencil C is the longest.",
                                "step_by_step_solution": [
                                    "Step 1: Compare lengths in paperclips: 6 < 10 < 12.",
                                    "Step 2: 12 is greatest, so Pencil C is longest."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "How many 5-rupee coins make 10 rupees?",
                                "question_type": "multiple_choice",
                                "options": ["A) 1", "B) 2", "C) 3", "D) 4"],
                                "correct_answer": "B) 2",
                                "explanation": "5 + 5 = 10, so two 5-rupee coins make 10 rupees.",
                                "step_by_step_solution": [
                                    "Step 1: 5 + 5 = 10.",
                                    "Step 2: Exactly 2 coins are needed."
                                ],
                                "difficulty": "medium",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] A notebook costs Rs. 15. You pay with a Rs. 20 note. How many rupees do you get back in change?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "5",
                                "explanation": "20 - 15 = 5 rupees.",
                                "step_by_step_solution": [
                                    "Step 1: Subtract cost from payment: 20 - 15 = 5 rupees."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "If school starts at 8 o'clock and you study for 1 hour, what time is it when you finish your first lesson?",
                                "question_type": "multiple_choice",
                                "options": ["A) 7 o'clock", "B) 9 o'clock", "C) 10 o'clock", "D) 12 o'clock"],
                                "correct_answer": "B) 9 o'clock",
                                "explanation": "8 o'clock plus 1 hour is 9 o'clock.",
                                "step_by_step_solution": [
                                    "Step 1: 8 + 1 = 9.",
                                    "Step 2: The time is 9 o'clock."
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
