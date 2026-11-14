# Grade 3 Mathematics Curriculum Data — Federal NCP 2022-23
# Strands: Numbers and Operations, Fractions, Geometry & Data Handling

GRADE_3_WORLDS = [
    {
        "title": "Realm of Numerals",
        "description": "Enter the kingdom of four-digit numbers, Roman numerals, multiplication forges, and fraction fields.",
        "grade": 3,
        "icon": "book-open",
        "theme_color": "indigo",
        "display_order": 1,
        "topics": [
            {
                "title": "4-Digit Numbers, Roman Numerals & Arithmetic",
                "description": "Place value up to 9,999, Roman numerals I–XII, and multiplying 2-digit numbers.",
                "learning_objectives": [
                    "Read, write, compare, and order numbers up to 9,999",
                    "Recognize Roman numerals from I to XII",
                    "Multiply 2-digit numbers by 1-digit numbers and solve division facts"
                ],
                "grade": 3,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Millennium Gate",
                        "instructions": "Master 4-digit thousands place values and Roman numerals to open the ancient gateway.",
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
                                "prompt": "In the number 6,429, what is the place value of the digit 6?",
                                "question_type": "multiple_choice",
                                "options": ["A) 60", "B) 600", "C) 6,000", "D) 60,000"],
                                "correct_answer": "C) 6,000",
                                "explanation": "6 is in the thousands place, so its value is 6,000.",
                                "step_by_step_solution": [
                                    "Step 1: In 6,429: 6 is Thousands, 4 is Hundreds, 2 is Tens, 9 is Ones.",
                                    "Step 2: 6 thousands = 6,000."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Which Hindu-Arabic numeral is represented by the Roman numeral IX?",
                                "question_type": "multiple_choice",
                                "options": ["A) 8", "B) 9", "C) 11", "D) 15"],
                                "correct_answer": "B) 9",
                                "explanation": "In Roman numerals, X is 10 and I before X means 10 - 1 = 9.",
                                "step_by_step_solution": [
                                    "Step 1: X = 10, I = 1.",
                                    "Step 2: IX = 10 - 1 = 9."
                                ],
                                "common_mistakes": {
                                    "11": "XI is 11 (10 + 1), while IX is 9 (10 - 1)."
                                },
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "What is the Roman numeral for 12?",
                                "question_type": "multiple_choice",
                                "options": ["A) VII", "B) X", "C) XII", "D) IIX"],
                                "correct_answer": "C) XII",
                                "explanation": "X (10) + II (2) = XII (12).",
                                "step_by_step_solution": [
                                    "Step 1: 10 is X.",
                                    "Step 2: 2 is II.",
                                    "Step 3: 10 + 2 = XII."
                                ],
                                "difficulty": "easy",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] Write the standard number for: 4 thousands + 7 hundreds + 3 tens + 5 ones:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "4735",
                                "explanation": "4,000 + 700 + 30 + 5 = 4,735.",
                                "step_by_step_solution": [
                                    "Step 1: Thousands = 4, Hundreds = 7, Tens = 3, Ones = 5.",
                                    "Step 2: Number = 4735."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "Round 3,468 to the nearest hundred:",
                                "question_type": "multiple_choice",
                                "options": ["A) 3,400", "B) 3,500", "C) 3,470", "D) 4,000"],
                                "correct_answer": "B) 3,500",
                                "explanation": "Look at the tens digit (6). Since 6 ≥ 5, round the hundreds up from 4 to 5: 3,500.",
                                "step_by_step_solution": [
                                    "Step 1: Identify hundreds place (4) and look at the digit to its right (6).",
                                    "Step 2: Since 6 is 5 or greater, round up to 3,500."
                                ],
                                "common_mistakes": {
                                    "3,400": "Since the tens digit is 6 (≥ 5), you must round up, not down."
                                },
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "Which number is the greatest: 5,420, 5,240, 5,402, 5,042?",
                                "question_type": "multiple_choice",
                                "options": ["A) 5,240", "B) 5,402", "C) 5,420", "D) 5,042"],
                                "correct_answer": "C) 5,420",
                                "explanation": "All have 5 thousands. Compare hundreds: 5,420 and 5,402 have 4 hundreds. In tens: 2 tens > 0 tens. So 5,420 is greatest.",
                                "step_by_step_solution": [
                                    "Step 1: Thousands are all 5.",
                                    "Step 2: Hundreds: 4 > 2 > 0.",
                                    "Step 3: Between 5420 and 5402: 2 tens > 0 tens. Greatest = 5420."
                                ],
                                "difficulty": "medium",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] What is 8,000 - 3,500?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "4500",
                                "explanation": "8,000 - 3,500 = 4,500.",
                                "step_by_step_solution": [
                                    "Step 1: 80 hundreds - 35 hundreds = 45 hundreds = 4,500."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "What Roman numeral represents the number 7?",
                                "question_type": "multiple_choice",
                                "options": ["A) IV", "B) VI", "C) VII", "D) VIII"],
                                "correct_answer": "C) VII",
                                "explanation": "V (5) + II (2) = VII (7).",
                                "step_by_step_solution": [
                                    "Step 1: V = 5.",
                                    "Step 2: 5 + 2 = 7, written as VII."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    },
                    {
                        "title": "Multiplication Forge",
                        "instructions": "Multiply multi-digit numbers and solve sharing division problems at the forge.",
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
                                "prompt": "Calculate: 24 × 3 =",
                                "question_type": "multiple_choice",
                                "options": ["A) 62", "B) 72", "C) 82", "D) 64"],
                                "correct_answer": "B) 72",
                                "explanation": "3 × 4 = 12 (write 2, carry 1). 3 × 2 = 6, 6 + 1 = 7. Product = 72.",
                                "step_by_step_solution": [
                                    "Step 1: 3 × 4 ones = 12 ones = 1 ten and 2 ones.",
                                    "Step 2: 3 × 2 tens = 6 tens. 6 + 1 = 7 tens.",
                                    "Step 3: Total = 72."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is 45 ÷ 5?",
                                "question_type": "multiple_choice",
                                "options": ["A) 7", "B) 8", "C) 9", "D) 10"],
                                "correct_answer": "C) 9",
                                "explanation": "5 × 9 = 45, so 45 ÷ 5 = 9.",
                                "step_by_step_solution": [
                                    "Step 1: Think: what times 5 is 45? 5 × 9 = 45.",
                                    "Step 2: 45 ÷ 5 = 9."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] Solve: 32 × 4 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "128",
                                "explanation": "32 × 4 = 128.",
                                "step_by_step_solution": [
                                    "Step 1: 4 × 2 = 8.",
                                    "Step 2: 4 × 30 = 120.",
                                    "Step 3: 120 + 8 = 128."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "A box contains 6 rows of chocolates with 8 chocolates in each row. How many chocolates are in the box?",
                                "question_type": "multiple_choice",
                                "options": ["A) 42", "B) 48", "C) 54", "D) 56"],
                                "correct_answer": "B) 48",
                                "explanation": "6 × 8 = 48 chocolates.",
                                "step_by_step_solution": [
                                    "Step 1: Multiply rows by items: 6 × 8 = 48."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "If 56 books are packed equally into 7 cartons, how many books are in each carton?",
                                "question_type": "multiple_choice",
                                "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
                                "correct_answer": "C) 8",
                                "explanation": "56 ÷ 7 = 8 books per carton.",
                                "step_by_step_solution": [
                                    "Step 1: 7 × 8 = 56.",
                                    "Step 2: Therefore, 56 ÷ 7 = 8."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] Calculate: 15 × 6 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "90",
                                "explanation": "15 × 6 = 90.",
                                "step_by_step_solution": [
                                    "Step 1: 10 × 6 = 60.",
                                    "Step 2: 5 × 6 = 30.",
                                    "Step 3: 60 + 30 = 90."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "What is the remainder when 27 is divided by 4?",
                                "question_type": "multiple_choice",
                                "options": ["A) 1", "B) 2", "C) 3", "D) 0"],
                                "correct_answer": "C) 3",
                                "explanation": "4 × 6 = 24. 27 - 24 = 3 remainder.",
                                "step_by_step_solution": [
                                    "Step 1: 27 ÷ 4 = 6 with a remainder.",
                                    "Step 2: 4 × 6 = 24.",
                                    "Step 3: 27 - 24 = 3 remainder."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] A bus can carry 45 passengers. How many total passengers can 4 identical buses carry?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "180",
                                "explanation": "45 × 4 = 180 passengers.",
                                "step_by_step_solution": [
                                    "Step 1: 40 × 4 = 160.",
                                    "Step 2: 5 × 4 = 20.",
                                    "Step 3: 160 + 20 = 180."
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
                "title": "Fractions of Wholes & Collections",
                "description": "Understand unit fractions, halves, thirds, fourths, and compare like fractions.",
                "learning_objectives": [
                    "Identify numerator and denominator in common fractions",
                    "Represent fractions using shaded shapes and sets of objects",
                    "Compare fractions with the same denominator"
                ],
                "grade": 3,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Fraction Village",
                        "instructions": "Distribute bread, divide gardens, and compare portions in Fraction Village.",
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
                                "prompt": "In the fraction 3/5, what is the numerator?",
                                "question_type": "multiple_choice",
                                "options": ["A) 3", "B) 5", "C) 8", "D) 2"],
                                "correct_answer": "A) 3",
                                "explanation": "The top number in a fraction is the numerator. In 3/5, the numerator is 3.",
                                "step_by_step_solution": [
                                    "Step 1: Fraction is written as Numerator / Denominator.",
                                    "Step 2: Top number = 3."
                                ],
                                "common_mistakes": {
                                    "5": "5 is the bottom number, which is called the denominator."
                                },
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "A pizza is cut into 8 equal slices. Ali eats 3 slices. What fraction of the pizza did Ali eat?",
                                "question_type": "multiple_choice",
                                "options": ["A) 3/5", "B) 3/8", "C) 5/8", "D) 1/8"],
                                "correct_answer": "B) 3/8",
                                "explanation": "Ali ate 3 out of 8 equal slices, which is 3/8.",
                                "step_by_step_solution": [
                                    "Step 1: Total equal parts = 8 (denominator).",
                                    "Step 2: Parts eaten = 3 (numerator).",
                                    "Step 3: Fraction = 3/8."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "Which fraction is greater: 4/7 or 2/7?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2/7", "B) 4/7", "C) They are equal", "D) Cannot be compared"],
                                "correct_answer": "B) 4/7",
                                "explanation": "When denominators are the same, the fraction with the larger numerator is greater: 4 > 2, so 4/7 > 2/7.",
                                "step_by_step_solution": [
                                    "Step 1: Denominators are both 7.",
                                    "Step 2: Compare numerators: 4 > 2.",
                                    "Step 3: 4/7 is greater."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] What is 1/4 of 24?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "6",
                                "explanation": "24 ÷ 4 = 6.",
                                "step_by_step_solution": [
                                    "Step 1: Divide 24 into 4 equal groups.",
                                    "Step 2: 24 / 4 = 6."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "What is 2/6 + 3/6?",
                                "question_type": "multiple_choice",
                                "options": ["A) 5/12", "B) 5/6", "C) 1/6", "D) 6/6"],
                                "correct_answer": "B) 5/6",
                                "explanation": "Keep the common denominator (6) and add numerators: 2 + 3 = 5. So 5/6.",
                                "step_by_step_solution": [
                                    "Step 1: Add numerators: 2 + 3 = 5.",
                                    "Step 2: Keep denominator: 6.",
                                    "Step 3: Result = 5/6."
                                ],
                                "common_mistakes": {
                                    "5/12": "Do NOT add the denominators! Keep the denominator 6."
                                },
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "Which of these fractions is a unit fraction?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2/3", "B) 3/4", "C) 1/5", "D) 4/5"],
                                "correct_answer": "C) 1/5",
                                "explanation": "A unit fraction has a numerator of 1. Here, 1/5 is a unit fraction.",
                                "step_by_step_solution": [
                                    "Step 1: A unit fraction represents one equal part: numerator is 1.",
                                    "Step 2: 1/5 is the unit fraction."
                                ],
                                "difficulty": "easy",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] Solve: 7/9 - 4/9. Enter the numerator of the resulting fraction (e.g. for 3/9, enter 3):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "3",
                                "explanation": "7/9 - 4/9 = (7 - 4)/9 = 3/9. The numerator is 3.",
                                "step_by_step_solution": [
                                    "Step 1: 7 - 4 = 3.",
                                    "Step 2: Numerator is 3."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "A garden has 10 flowers. 3 are red, 4 are yellow, and 3 are white. What fraction of the flowers are yellow?",
                                "question_type": "multiple_choice",
                                "options": ["A) 3/10", "B) 4/10", "C) 7/10", "D) 4/7"],
                                "correct_answer": "B) 4/10",
                                "explanation": "4 out of 10 flowers are yellow, which is 4/10.",
                                "step_by_step_solution": [
                                    "Step 1: Yellow flowers = 4.",
                                    "Step 2: Total flowers = 10.",
                                    "Step 3: Fraction = 4/10."
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
        "title": "Geometry Gardens",
        "description": "Walk among line segments, right angles, perimeter pathways, and market bar graphs.",
        "grade": 3,
        "icon": "flag",
        "theme_color": "violet",
        "display_order": 2,
        "topics": [
            {
                "title": "Lines, Angles & Perimeter",
                "description": "Lines, rays, line segments, right angles, and perimeter of rectilinear shapes.",
                "learning_objectives": [
                    "Distinguish between line, line segment, and ray",
                    "Identify right angles as square corners",
                    "Calculate perimeter of polygons by summing side lengths"
                ],
                "grade": 3,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Lines & Perimeter Pavilion",
                        "instructions": "Measure geometric boundaries and locate square corners around the garden pavilion.",
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
                                "prompt": "What geometric figure has two endpoints and a fixed length?",
                                "question_type": "multiple_choice",
                                "options": ["A) Line", "B) Line segment", "C) Ray", "D) Angle"],
                                "correct_answer": "B) Line segment",
                                "explanation": "A line segment starts at one point and ends at another point with definite length.",
                                "step_by_step_solution": [
                                    "Step 1: Line goes on forever in both directions.",
                                    "Step 2: Ray has one endpoint.",
                                    "Step 3: Line segment has two endpoints."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "How many degrees are in a right angle?",
                                "question_type": "multiple_choice",
                                "options": ["A) 45°", "B) 90°", "C) 180°", "D) 360°"],
                                "correct_answer": "B) 90°",
                                "explanation": "A right angle is exactly 90 degrees, forming a square corner.",
                                "step_by_step_solution": [
                                    "Step 1: A square corner is a right angle.",
                                    "Step 2: A right angle measures 90 degrees."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] A triangle has sides of length 5 cm, 7 cm, and 9 cm. What is its perimeter in cm?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "21",
                                "explanation": "Perimeter = 5 + 7 + 9 = 21 cm.",
                                "step_by_step_solution": [
                                    "Step 1: Add all outer sides: 5 + 7 + 9 = 21 cm."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "A square garden has sides of length 6 meters. What is the perimeter of the garden?",
                                "question_type": "multiple_choice",
                                "options": ["A) 12 m", "B) 18 m", "C) 24 m", "D) 36 m"],
                                "correct_answer": "C) 24 m",
                                "explanation": "A square has 4 equal sides. Perimeter = 4 × 6 = 24 meters.",
                                "step_by_step_solution": [
                                    "Step 1: Perimeter of square = 4 × side.",
                                    "Step 2: 4 × 6 = 24 m."
                                ],
                                "common_mistakes": {
                                    "36 m": "36 is the area (6 × 6), not the perimeter."
                                },
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "What geometric figure starts at an endpoint and extends endlessly in one direction?",
                                "question_type": "multiple_choice",
                                "options": ["A) Ray", "B) Line segment", "C) Circle", "D) Angle"],
                                "correct_answer": "A) Ray",
                                "explanation": "A ray has one fixed starting point and continues infinitely in one direction (like a sunbeam).",
                                "step_by_step_solution": [
                                    "Step 1: One endpoint + infinite extension = Ray."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "[Numeric Entry] prompt": "[Numeric Entry] A rectangle has length 8 cm and width 3 cm. What is its perimeter in cm?",
                                "prompt": "[Numeric Entry] A rectangle has length 8 cm and width 3 cm. What is its perimeter in cm?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "22",
                                "explanation": "Perimeter = 2 × (length + width) = 2 × (8 + 3) = 2 × 11 = 22 cm.",
                                "step_by_step_solution": [
                                    "Step 1: 8 + 3 = 11.",
                                    "Step 2: 11 × 2 = 22 cm."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "Which shape contains at least one right angle?",
                                "question_type": "multiple_choice",
                                "options": ["A) A right-angled triangle", "B) A circle", "C) An equilateral triangle", "D) An oval"],
                                "correct_answer": "A) A right-angled triangle",
                                "explanation": "A right-angled triangle contains exactly one 90-degree right angle.",
                                "step_by_step_solution": [
                                    "Step 1: By definition, a right-angled triangle has one 90° angle."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] A regular pentagon has 5 equal sides. If its perimeter is 35 cm, what is the length of one side in cm?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "7",
                                "explanation": "35 ÷ 5 = 7 cm per side.",
                                "step_by_step_solution": [
                                    "Step 1: A regular pentagon has 5 equal sides.",
                                    "Step 2: Side = 35 / 5 = 7 cm."
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
                "title": "Currency Word Problems & Bar Graphs",
                "description": "Pakistani currency operations, purchase calculations, and interpreting bar graphs.",
                "learning_objectives": [
                    "Solve multi-step money word problems in Pakistani Rupees",
                    "Calculate total bills and change given in PKR",
                    "Read and interpret simple vertical and horizontal bar graphs"
                ],
                "grade": 3,
                "display_order": 2,
                "missions": [
                    {
                        "title": "The Merchant's Graph",
                        "instructions": "Help the village merchant balance transaction ledgers and read sales bar charts.",
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
                                "prompt": "Usman buys a geometry box for Rs. 140 and a pen for Rs. 45. What is the total bill?",
                                "question_type": "multiple_choice",
                                "options": ["A) Rs. 175", "B) Rs. 185", "C) Rs. 195", "D) Rs. 180"],
                                "correct_answer": "B) Rs. 185",
                                "explanation": "140 + 45 = 185 Rupees.",
                                "step_by_step_solution": [
                                    "Step 1: 140 + 45 = 185."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Faiza buys items worth Rs. 320 and hands a Rs. 500 note to the cashier. How much change does she receive?",
                                "question_type": "multiple_choice",
                                "options": ["A) Rs. 160", "B) Rs. 180", "C) Rs. 220", "D) Rs. 280"],
                                "correct_answer": "B) Rs. 180",
                                "explanation": "500 - 320 = 180 Rupees.",
                                "step_by_step_solution": [
                                    "Step 1: 500 - 320 = 180."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] You have 3 notes of Rs. 100 and 4 notes of Rs. 50. What is your total amount of money in Rupees?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "500",
                                "explanation": "(3 × 100) + (4 × 50) = 300 + 200 = 500 Rupees.",
                                "step_by_step_solution": [
                                    "Step 1: 3 × 100 = 300.",
                                    "Step 2: 4 × 50 = 200.",
                                    "Step 3: 300 + 200 = 500."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "On a bar graph, the bar for Grade 3 shows 25 students, and the bar for Grade 4 shows 35 students. How many more students are in Grade 4 than Grade 3?",
                                "question_type": "multiple_choice",
                                "options": ["A) 5", "B) 10", "C) 15", "D) 60"],
                                "correct_answer": "B) 10",
                                "explanation": "35 - 25 = 10 students.",
                                "step_by_step_solution": [
                                    "Step 1: Grade 4 = 35.",
                                    "Step 2: Grade 3 = 25.",
                                    "Step 3: Difference = 35 - 25 = 10."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "A shopkeeper sells 15 books on Monday, 20 on Tuesday, and 25 on Wednesday. What is the total number of books sold over the three days?",
                                "question_type": "multiple_choice",
                                "options": ["A) 50", "B) 60", "C) 65", "D) 70"],
                                "correct_answer": "B) 60",
                                "explanation": "15 + 20 + 25 = 60 books.",
                                "step_by_step_solution": [
                                    "Step 1: 15 + 20 = 35.",
                                    "Step 2: 35 + 25 = 60."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] One storybook costs Rs. 80. How much do 5 identical storybooks cost in Rupees?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "400",
                                "explanation": "80 × 5 = 400 Rupees.",
                                "step_by_step_solution": [
                                    "Step 1: 80 × 5 = 400."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "On a library bar graph, the bars show: Science = 30, History = 15, Math = 40, Art = 25. Which category has the highest number of borrowed books?",
                                "question_type": "multiple_choice",
                                "options": ["A) Science", "B) History", "C) Math", "D) Art"],
                                "correct_answer": "C) Math",
                                "explanation": "Math has the tallest bar at 40.",
                                "step_by_step_solution": [
                                    "Step 1: Compare bar heights: 40 is greatest.",
                                    "Step 2: Category is Math."
                                ],
                                "difficulty": "easy",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] A family spent Rs. 1,450 on groceries and Rs. 750 on fruits. How much total money did they spend?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "2200",
                                "explanation": "1,450 + 750 = 2,200 Rupees.",
                                "step_by_step_solution": [
                                    "Step 1: 1,450 + 750 = 2,200."
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
