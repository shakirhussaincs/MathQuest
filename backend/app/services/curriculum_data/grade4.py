# Grade 4 Mathematics Curriculum Data — Federal NCP 2022-23
# Strands: Numbers and Operations, Geometry, Measurement & Data Handling

GRADE_4_WORLDS = [
    {
        "title": "Valley of Multiples",
        "description": "Scale peaks of prime numbers, cross LCM canyons, and discover decimal oases.",
        "grade": 4,
        "icon": "award",
        "theme_color": "purple",
        "display_order": 1,
        "topics": [
            {
                "title": "Large Numbers, Factors, Multiples & HCF/LCM",
                "description": "Numbers up to 100,000, prime and composite numbers, and calculating HCF and LCM.",
                "learning_objectives": [
                    "Read, write, and round numbers up to 100,000",
                    "Differentiate prime and composite numbers up to 50",
                    "Find the Highest Common Factor (HCF) and Lowest Common Multiple (LCM)"
                ],
                "grade": 4,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Prime Factor Peaks",
                        "instructions": "Decompose numbers into prime building blocks to unlock the mountain gates.",
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
                                "prompt": "Which of these numbers is a PRIME number?",
                                "question_type": "multiple_choice",
                                "options": ["A) 9", "B) 15", "C) 19", "D) 21"],
                                "correct_answer": "C) 19",
                                "explanation": "19 has only two factors: 1 and 19. Therefore, it is a prime number.",
                                "step_by_step_solution": [
                                    "Step 1: Check factors of 9: 1, 3, 9 (Composite).",
                                    "Step 2: Check factors of 15: 1, 3, 5, 15 (Composite).",
                                    "Step 3: Check factors of 19: only 1 and 19 (Prime)."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is the prime factorization of 24?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2 × 3 × 4", "B) 2 × 2 × 2 × 3", "C) 3 × 8", "D) 2 × 12"],
                                "correct_answer": "B) 2 × 2 × 2 × 3",
                                "explanation": "24 = 2 × 12 = 2 × 2 × 6 = 2 × 2 × 2 × 3 (or 2³ × 3). All factors must be prime.",
                                "step_by_step_solution": [
                                    "Step 1: 24 ÷ 2 = 12.",
                                    "Step 2: 12 ÷ 2 = 6.",
                                    "Step 3: 6 ÷ 2 = 3.",
                                    "Step 4: Prime factors = 2 × 2 × 2 × 3."
                                ],
                                "common_mistakes": {
                                    "2 × 3 × 4": "4 is not a prime number; it can be factored into 2 × 2."
                                },
                                "difficulty": "medium",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] What is the Highest Common Factor (HCF) of 12 and 18?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "6",
                                "explanation": "Factors of 12: 1, 2, 3, 4, 6, 12. Factors of 18: 1, 2, 3, 6, 9, 18. Common factors: 1, 2, 3, 6. The highest is 6.",
                                "step_by_step_solution": [
                                    "Step 1: 12 = 2 × 2 × 3.",
                                    "Step 2: 18 = 2 × 3 × 3.",
                                    "Step 3: Common prime factors = 2 × 3 = 6."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "What is the smallest prime number?",
                                "question_type": "multiple_choice",
                                "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
                                "correct_answer": "C) 2",
                                "explanation": "2 is the smallest prime number and the only even prime number. (1 is neither prime nor composite).",
                                "step_by_step_solution": [
                                    "Step 1: 1 is not prime because it has only one factor.",
                                    "Step 2: 2 has exactly two factors (1 and 2), so 2 is the smallest prime."
                                ],
                                "common_mistakes": {
                                    "1": "1 is neither prime nor composite by definition."
                                },
                                "difficulty": "easy",
                                "display_order": 4
                            },
                            {
                                "prompt": "Round 47,823 to the nearest thousand:",
                                "question_type": "multiple_choice",
                                "options": ["A) 47,000", "B) 47,800", "C) 48,000", "D) 50,000"],
                                "correct_answer": "C) 48,000",
                                "explanation": "Look at the hundreds digit (8). Since 8 ≥ 5, round the thousands up from 7 to 8: 48,000.",
                                "step_by_step_solution": [
                                    "Step 1: Target digit is 7 in thousands place.",
                                    "Step 2: Next digit is 8 (hundreds place).",
                                    "Step 3: 8 ≥ 5, so round up to 48,000."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] What is the HCF of 20 and 30?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "10",
                                "explanation": "20 = 2 × 2 × 5, 30 = 2 × 3 × 5. Common prime factors = 2 × 5 = 10.",
                                "step_by_step_solution": [
                                    "Step 1: Common divisors are 1, 2, 5, 10.",
                                    "Step 2: Greatest is 10."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "Which of these numbers is COMPOSITE?",
                                "question_type": "multiple_choice",
                                "options": ["A) 23", "B) 29", "C) 31", "D) 33"],
                                "correct_answer": "D) 33",
                                "explanation": "33 has factors 1, 3, 11, and 33, making it composite.",
                                "step_by_step_solution": [
                                    "Step 1: 33 = 3 × 11.",
                                    "Step 2: More than 2 factors means it is composite."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] How many factors does the number 16 have?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "5",
                                "explanation": "The factors of 16 are: 1, 2, 4, 8, 16. Total count is 5.",
                                "step_by_step_solution": [
                                    "Step 1: List factors: 1 × 16, 2 × 8, 4 × 4.",
                                    "Step 2: Distinct factors: 1, 2, 4, 8, 16.",
                                    "Step 3: Count = 5."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 8
                            }
                        ]
                    },
                    {
                        "title": "LCM Canyon",
                        "instructions": "Find common multiples to bridge the gaps across LCM Canyon.",
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
                                "prompt": "What is the Least Common Multiple (LCM) of 4 and 6?",
                                "question_type": "multiple_choice",
                                "options": ["A) 12", "B) 16", "C) 24", "D) 2"],
                                "correct_answer": "A) 12",
                                "explanation": "Multiples of 4: 4, 8, 12, 16... Multiples of 6: 6, 12, 18... Smallest common multiple is 12.",
                                "step_by_step_solution": [
                                    "Step 1: List multiples of 4: 4, 8, 12, 16, 20...",
                                    "Step 2: List multiples of 6: 6, 12, 18...",
                                    "Step 3: First common multiple is 12."
                                ],
                                "common_mistakes": {
                                    "24": "24 is a common multiple, but 12 is smaller (least common multiple)."
                                },
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "[Numeric Entry] What is the LCM of 3 and 5?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "15",
                                "explanation": "Since 3 and 5 are co-prime, their LCM is 3 × 5 = 15.",
                                "step_by_step_solution": [
                                    "Step 1: Multiples of 3: 3, 6, 9, 12, 15...",
                                    "Step 2: Multiples of 5: 5, 10, 15...",
                                    "Step 3: Smallest common is 15."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 2
                            },
                            {
                                "prompt": "What is the LCM of 8 and 12?",
                                "question_type": "multiple_choice",
                                "options": ["A) 16", "B) 24", "C) 48", "D) 96"],
                                "correct_answer": "B) 24",
                                "explanation": "8 = 2³, 12 = 2² × 3. LCM = 2³ × 3 = 8 × 3 = 24.",
                                "step_by_step_solution": [
                                    "Step 1: Multiples of 8: 8, 16, 24, 32...",
                                    "Step 2: Multiples of 12: 12, 24, 36...",
                                    "Step 3: LCM = 24."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "Two bells ring together. One rings every 4 minutes and the other rings every 5 minutes. After how many minutes will they ring together again?",
                                "question_type": "multiple_choice",
                                "options": ["A) 10 minutes", "B) 15 minutes", "C) 20 minutes", "D) 25 minutes"],
                                "correct_answer": "C) 20 minutes",
                                "explanation": "Find LCM(4, 5). Since 4 and 5 share no common factors, LCM = 4 × 5 = 20 minutes.",
                                "step_by_step_solution": [
                                    "Step 1: This is a Least Common Multiple problem.",
                                    "Step 2: LCM(4, 5) = 20.",
                                    "Step 3: They ring together after 20 minutes."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] Find the LCM of 6 and 9:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "18",
                                "explanation": "6 = 2 × 3, 9 = 3². LCM = 2 × 3² = 18.",
                                "step_by_step_solution": [
                                    "Step 1: Multiples of 6: 6, 12, 18, 24...",
                                    "Step 2: Multiples of 9: 9, 18, 27...",
                                    "Step 3: LCM = 18."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "If the HCF of two numbers is 4 and their LCM is 24, and one number is 8, what is the other number?",
                                "question_type": "multiple_choice",
                                "options": ["A) 6", "B) 12", "C) 16", "D) 18"],
                                "correct_answer": "B) 12",
                                "explanation": "Product of numbers = HCF × LCM. 8 × Other = 4 × 24 = 96. Other = 96 / 8 = 12.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: Product = HCF × LCM.",
                                    "Step 2: 8 × n = 4 × 24 = 96.",
                                    "Step 3: n = 96 / 8 = 12."
                                ],
                                "difficulty": "hard",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] What is the LCM of 10, 15, and 20?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "60",
                                "explanation": "10 = 2 × 5, 15 = 3 × 5, 20 = 2² × 5. LCM = 2² × 3 × 5 = 4 × 15 = 60.",
                                "step_by_step_solution": [
                                    "Step 1: Highest powers of prime factors: 2² = 4, 3¹ = 3, 5¹ = 5.",
                                    "Step 2: 4 × 3 × 5 = 60."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "Which pair of numbers has an LCM of 30?",
                                "question_type": "multiple_choice",
                                "options": ["A) 5 and 6", "B) 3 and 10", "C) 10 and 15", "D) All of the above"],
                                "correct_answer": "D) All of the above",
                                "explanation": "LCM(5, 6) = 30, LCM(3, 10) = 30, and LCM(10, 15) = 30. All pairs have LCM 30.",
                                "step_by_step_solution": [
                                    "Step 1: Check 5 and 6: LCM = 30.",
                                    "Step 2: Check 3 and 10: LCM = 30.",
                                    "Step 3: Check 10 and 15: LCM = 30.",
                                    "Step 4: Answer is All of the above."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Fractions Operations & Decimals",
                "description": "Addition and subtraction of unlike fractions, decimal place value, and conversions.",
                "learning_objectives": [
                    "Add and subtract fractions with unlike denominators",
                    "Convert between improper fractions and mixed numbers",
                    "Represent and operate with decimals up to two decimal places"
                ],
                "grade": 4,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Decimal Oasis",
                        "instructions": "Navigate unlike fractions, mixed numbers, and decimal additions at the desert oasis.",
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
                                "prompt": "What is 1/2 + 1/4?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2/6", "B) 3/4", "C) 2/4", "D) 1/8"],
                                "correct_answer": "B) 3/4",
                                "explanation": "Convert 1/2 to equivalent fraction 2/4. Then 2/4 + 1/4 = 3/4.",
                                "step_by_step_solution": [
                                    "Step 1: Find common denominator: 4.",
                                    "Step 2: 1/2 = 2/4.",
                                    "Step 3: 2/4 + 1/4 = 3/4."
                                ],
                                "common_mistakes": {
                                    "2/6": "Never add denominators together! Find a common denominator instead."
                                },
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Convert the improper fraction 7/3 to a mixed number:",
                                "question_type": "multiple_choice",
                                "options": ["A) 1 1/3", "B) 2 1/3", "C) 2 2/3", "D) 3 1/3"],
                                "correct_answer": "B) 2 1/3",
                                "explanation": "7 ÷ 3 = 2 with a remainder of 1. So 7/3 = 2 1/3.",
                                "step_by_step_solution": [
                                    "Step 1: Divide numerator by denominator: 7 ÷ 3 = 2 remainder 1.",
                                    "Step 2: Whole number is 2, remainder is numerator: 2 1/3."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "In the decimal 3.75, what is the value of the digit 7?",
                                "question_type": "multiple_choice",
                                "options": ["A) 7 tens", "B) 7 ones", "C) 7 tenths (0.7)", "D) 7 hundredths (0.07)"],
                                "correct_answer": "C) 7 tenths (0.7)",
                                "explanation": "The first digit after the decimal point is the tenths place, so 7 has value 7/10 = 0.7.",
                                "step_by_step_solution": [
                                    "Step 1: In 3.75: 3 is Ones, 7 is Tenths, 5 is Hundredths."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] Solve: 4.3 + 2.5 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "6.8",
                                "explanation": "Align decimal points: 4.3 + 2.5 = 6.8.",
                                "step_by_step_solution": [
                                    "Step 1: 3 tenths + 5 tenths = 8 tenths.",
                                    "Step 2: 4 ones + 2 ones = 6 ones. Sum = 6.8."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "What is 3/5 - 1/10?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2/5", "B) 5/10 (1/2)", "C) 2/10", "D) 1/2"],
                                "correct_answer": "B) 5/10 (1/2)",
                                "explanation": "3/5 = 6/10. 6/10 - 1/10 = 5/10 = 1/2.",
                                "step_by_step_solution": [
                                    "Step 1: Common denominator is 10.",
                                    "Step 2: 3/5 = 6/10.",
                                    "Step 3: 6/10 - 1/10 = 5/10 = 1/2."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "Which decimal is equivalent to the fraction 3/4?",
                                "question_type": "multiple_choice",
                                "options": ["A) 0.34", "B) 0.5", "C) 0.75", "D) 0.25"],
                                "correct_answer": "C) 0.75",
                                "explanation": "3 ÷ 4 = 0.75 (or 75/100).",
                                "step_by_step_solution": [
                                    "Step 1: 3/4 = (3 × 25) / (4 × 25) = 75/100 = 0.75."
                                ],
                                "difficulty": "medium",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] Calculate: 8.50 - 3.25 =",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "5.25",
                                "explanation": "8.50 - 3.25 = 5.25.",
                                "step_by_step_solution": [
                                    "Step 1: Align decimals: 8.50 - 3.25 = 5.25."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "A jug had 2.75 liters of juice. Hina poured out 1.20 liters. How much juice remains in the jug?",
                                "question_type": "multiple_choice",
                                "options": ["A) 1.45 liters", "B) 1.55 liters", "C) 1.65 liters", "D) 3.95 liters"],
                                "correct_answer": "B) 1.55 liters",
                                "explanation": "2.75 - 1.20 = 1.55 liters.",
                                "step_by_step_solution": [
                                    "Step 1: 5 - 0 = 5 hundredths.",
                                    "Step 2: 7 - 2 = 5 tenths.",
                                    "Step 3: 2 - 1 = 1 one. Result = 1.55 liters."
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
        "title": "Geometric Citadel",
        "description": "Construct angles with protractors, classify triangles, and compute area of fortresses.",
        "grade": 4,
        "icon": "shield",
        "theme_color": "fuchsia",
        "display_order": 2,
        "topics": [
            {
                "title": "Protractor Angles & Triangles",
                "description": "Measure angles (acute, right, obtuse, straight) and classify triangles by sides and angles.",
                "learning_objectives": [
                    "Classify angles as acute, right, obtuse, or straight",
                    "Measure angles using a protractor (0° to 180°)",
                    "Classify triangles as equilateral, isosceles, or scalene"
                ],
                "grade": 4,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Protractor Bastion",
                        "instructions": "Measure defenses using protractors and categorize triangles on the citadel ramparts.",
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
                                "prompt": "An angle that measures less than 90° is called:",
                                "question_type": "multiple_choice",
                                "options": ["A) An obtuse angle", "B) An acute angle", "C) A straight angle", "D) A right angle"],
                                "correct_answer": "B) An acute angle",
                                "explanation": "An acute angle measures between 0° and 90°.",
                                "step_by_step_solution": [
                                    "Step 1: Less than 90° = Acute.",
                                    "Step 2: Exactly 90° = Right.",
                                    "Step 3: Greater than 90° and less than 180° = Obtuse."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What type of angle measures 135°?",
                                "question_type": "multiple_choice",
                                "options": ["A) Acute", "B) Right", "C) Obtuse", "D) Straight"],
                                "correct_answer": "C) Obtuse",
                                "explanation": "Since 135° is between 90° and 180°, it is an obtuse angle.",
                                "step_by_step_solution": [
                                    "Step 1: 90° < 135° < 180° => Obtuse angle."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "A triangle with all 3 sides equal in length is called:",
                                "question_type": "multiple_choice",
                                "options": ["A) An isosceles triangle", "B) A scalene triangle", "C) An equilateral triangle", "D) A right triangle"],
                                "correct_answer": "C) An equilateral triangle",
                                "explanation": "An equilateral triangle has all 3 sides equal and all 3 angles equal to 60°.",
                                "step_by_step_solution": [
                                    "Step 1: 'Equi-lateral' means equal sides.",
                                    "Step 2: All 3 sides equal = Equilateral."
                                ],
                                "difficulty": "easy",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] What is the angle measurement (in degrees) of a straight line?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "180",
                                "explanation": "A straight angle measures exactly 180°.",
                                "step_by_step_solution": [
                                    "Step 1: Two right angles make a straight angle: 90° + 90° = 180°."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "A triangle has side lengths of 7 cm, 7 cm, and 4 cm. What type of triangle is it?",
                                "question_type": "multiple_choice",
                                "options": ["A) Equilateral", "B) Isosceles", "C) Scalene", "D) Right-angled"],
                                "correct_answer": "B) Isosceles",
                                "explanation": "An isosceles triangle has exactly 2 sides of equal length (here, two sides are 7 cm).",
                                "step_by_step_solution": [
                                    "Step 1: Count equal sides: 2 equal sides (7 cm and 7 cm).",
                                    "Step 2: Exactly 2 equal sides = Isosceles triangle."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "A triangle has side lengths of 5 cm, 8 cm, and 10 cm (all different). What type of triangle is it?",
                                "question_type": "multiple_choice",
                                "options": ["A) Equilateral", "B) Isosceles", "C) Scalene", "D) Regular"],
                                "correct_answer": "C) Scalene",
                                "explanation": "A scalene triangle has all three sides of different lengths.",
                                "step_by_step_solution": [
                                    "Step 1: All sides differ: 5 ≠ 8 ≠ 10.",
                                    "Step 2: All different = Scalene triangle."
                                ],
                                "difficulty": "medium",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] The sum of angles in any triangle is always constant. How many degrees do the angles in a triangle add up to?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "180",
                                "explanation": "The interior angles of any triangle always add up to 180°.",
                                "step_by_step_solution": [
                                    "Step 1: Angle sum of triangle = 180°."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "If two angles of a triangle are 50° and 70°, what is the third angle?",
                                "question_type": "multiple_choice",
                                "options": ["A) 50°", "B) 60°", "C) 70°", "D) 80°"],
                                "correct_answer": "B) 60°",
                                "explanation": "Sum of angles = 180°. 50° + 70° = 120°. Third angle = 180° - 120° = 60°.",
                                "step_by_step_solution": [
                                    "Step 1: 50° + 70° = 120°.",
                                    "Step 2: 180° - 120° = 60°."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Area, Perimeter & Time Units",
                "description": "Calculate area and perimeter of rectangles and convert units of time (hours, minutes, seconds).",
                "learning_objectives": [
                    "Derive and apply formulas for area (length × width) and perimeter",
                    "Convert between hours, minutes, and seconds",
                    "Interpret line graphs showing changes over time"
                ],
                "grade": 4,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Area & Time Garrison",
                        "instructions": "Measure floor plans and calculate patrol durations in the garrison quarters.",
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
                                "prompt": "What is the area of a rectangle with length 9 cm and width 4 cm?",
                                "question_type": "multiple_choice",
                                "options": ["A) 26 cm²", "B) 36 cm²", "C) 40 cm²", "D) 45 cm²"],
                                "correct_answer": "B) 36 cm²",
                                "explanation": "Area = length × width = 9 × 4 = 36 cm².",
                                "step_by_step_solution": [
                                    "Step 1: Formula for rectangle area: A = l × w.",
                                    "Step 2: A = 9 × 4 = 36 cm²."
                                ],
                                "common_mistakes": {
                                    "26 cm²": "26 is the perimeter 2(9 + 4), not the area."
                                },
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "How many minutes are in 3 hours?",
                                "question_type": "multiple_choice",
                                "options": ["A) 120 minutes", "B) 150 minutes", "C) 180 minutes", "D) 300 minutes"],
                                "correct_answer": "C) 180 minutes",
                                "explanation": "1 hour = 60 minutes. 3 hours = 3 × 60 = 180 minutes.",
                                "step_by_step_solution": [
                                    "Step 1: 1 hr = 60 min.",
                                    "Step 2: 3 × 60 = 180 minutes."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] A square room has sides of length 7 meters. What is the area of the room in square meters?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "49",
                                "explanation": "Area of square = side × side = 7 × 7 = 49 m².",
                                "step_by_step_solution": [
                                    "Step 1: Area = 7 × 7 = 49 m²."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "How many seconds are in 5 minutes?",
                                "question_type": "multiple_choice",
                                "options": ["A) 250 seconds", "B) 300 seconds", "C) 350 seconds", "D) 500 seconds"],
                                "correct_answer": "B) 300 seconds",
                                "explanation": "1 minute = 60 seconds. 5 minutes = 5 × 60 = 300 seconds.",
                                "step_by_step_solution": [
                                    "Step 1: 1 min = 60 sec.",
                                    "Step 2: 5 × 60 = 300 seconds."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "A rectangular courtyard has length 12 m and width 8 m. What is its perimeter?",
                                "question_type": "multiple_choice",
                                "options": ["A) 40 m", "B) 96 m", "C) 20 m", "D) 48 m"],
                                "correct_answer": "A) 40 m",
                                "explanation": "Perimeter = 2 × (12 + 8) = 2 × 20 = 40 meters.",
                                "step_by_step_solution": [
                                    "Step 1: P = 2(l + w).",
                                    "Step 2: P = 2(12 + 8) = 2(20) = 40 m."
                                ],
                                "common_mistakes": {
                                    "96 m": "96 is the area (12 × 8), not the perimeter."
                                },
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] If a film started at 2:15 PM and ended at 4:45 PM, how many minutes did the film last?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "150",
                                "explanation": "From 2:15 to 4:15 is 2 hours (120 min). From 4:15 to 4:45 is 30 min. 120 + 30 = 150 minutes.",
                                "step_by_step_solution": [
                                    "Step 1: 4:45 - 2:15 = 2 hours and 30 minutes.",
                                    "Step 2: (2 × 60) + 30 = 120 + 30 = 150 minutes."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "A rectangular field has an area of 72 m² and a width of 6 m. What is its length?",
                                "question_type": "multiple_choice",
                                "options": ["A) 10 m", "B) 11 m", "C) 12 m", "D) 14 m"],
                                "correct_answer": "C) 12 m",
                                "explanation": "Length = Area / width = 72 / 6 = 12 meters.",
                                "step_by_step_solution": [
                                    "Step 1: Area = length × width.",
                                    "Step 2: Length = 72 ÷ 6 = 12 m."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] A square carpet has a perimeter of 32 meters. What is the area of the carpet in square meters?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "64",
                                "explanation": "Side length = 32 / 4 = 8 m. Area = 8 × 8 = 64 m².",
                                "step_by_step_solution": [
                                    "Step 1: Side of square = Perimeter / 4 = 32 / 4 = 8 m.",
                                    "Step 2: Area = side × side = 8 × 8 = 64 m²."
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
