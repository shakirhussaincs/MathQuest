# Grade 7 Mathematics Curriculum Data — Federal NCP 2022-23
# Strands: Numbers and Operations, Algebra, Commercial Arithmetic, Geometry & Probability

GRADE_7_WORLDS = [
    {
        "title": "Rational Realm",
        "description": "Harness the power of laws of exponents, polynomial operations, and algebraic factorization.",
        "grade": 7,
        "icon": "layers",
        "theme_color": "teal",
        "display_order": 1,
        "topics": [
            {
                "title": "Rational Numbers & Laws of Indices",
                "description": "Properties of rational numbers, exponent laws (product, quotient, power), and scientific notation.",
                "learning_objectives": [
                    "Perform operations with positive and negative rational numbers",
                    "Apply the laws of exponents (aᵐ · aⁿ = aᵐ⁺ⁿ, (aᵐ)ⁿ = aᵐⁿ, a⁰ = 1)",
                    "Express numbers in standard scientific notation"
                ],
                "grade": 7,
                "display_order": 1,
                "missions": [
                    {
                        "title": "Laws of Exponents Sanctum",
                        "instructions": "Simplify exponential expressions and convert standard forms in the ancient sanctum.",
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
                                "prompt": "Simplify: 2³ × 2⁴ =",
                                "question_type": "multiple_choice",
                                "options": ["A) 2⁷", "B) 2¹²", "C) 4⁷", "D) 4¹²"],
                                "correct_answer": "A) 2⁷",
                                "explanation": "Product law of exponents: aᵐ × aⁿ = aᵐ⁺ⁿ. So 2³ × 2⁴ = 2³⁺⁴ = 2⁷.",
                                "step_by_step_solution": [
                                    "Step 1: Same base: add exponents.",
                                    "Step 2: 3 + 4 = 7.",
                                    "Step 3: 2³ × 2⁴ = 2⁷ (128)."
                                ],
                                "common_mistakes": {
                                    "2¹²": "Do not multiply the exponents when multiplying bases; add them!"
                                },
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is the value of 5⁰?",
                                "question_type": "multiple_choice",
                                "options": ["A) 0", "B) 1", "C) 5", "D) Undefined"],
                                "correct_answer": "B) 1",
                                "explanation": "Any non-zero number raised to the power of zero equals 1: a⁰ = 1.",
                                "step_by_step_solution": [
                                    "Step 1: Zero exponent rule: a⁰ = 1 for any a ≠ 0.",
                                    "Step 2: 5⁰ = 1."
                                ],
                                "common_mistakes": {
                                    "0": "A number raised to power 0 is 1, not 0."
                                },
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "Simplify: (3²)³ =",
                                "question_type": "multiple_choice",
                                "options": ["A) 3⁵", "B) 3⁶", "C) 3⁸", "D) 3⁹"],
                                "correct_answer": "B) 3⁶",
                                "explanation": "Power of a power law: (aᵐ)ⁿ = aᵐⁿ. So (3²)³ = 3²ˣ³ = 3⁶.",
                                "step_by_step_solution": [
                                    "Step 1: Multiply the powers: 2 × 3 = 6.",
                                    "Step 2: (3²)³ = 3⁶."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] Evaluate: 7⁵ ÷ 7³ = (Enter the simplified numerical value):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "49",
                                "explanation": "7⁵ ÷ 7³ = 7⁵⁻³ = 7² = 49.",
                                "step_by_step_solution": [
                                    "Step 1: Quotient rule: subtract exponents: 5 - 3 = 2.",
                                    "Step 2: 7² = 49."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "Express 450,000 in standard scientific notation:",
                                "question_type": "multiple_choice",
                                "options": ["A) 45 × 10⁴", "B) 4.5 × 10⁵", "C) 4.5 × 10⁶", "D) 0.45 × 10⁶"],
                                "correct_answer": "B) 4.5 × 10⁵",
                                "explanation": "Move the decimal 5 places to the left: 450,000 = 4.5 × 10⁵.",
                                "step_by_step_solution": [
                                    "Step 1: Scientific notation form: a × 10ⁿ where 1 ≤ a < 10.",
                                    "Step 2: 450,000 = 4.5 × 10⁵."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "Simplify: (2a³b²) × (3a²b⁴) =",
                                "question_type": "multiple_choice",
                                "options": ["A) 6a⁵b⁶", "B) 5a⁵b⁶", "C) 6a⁶b⁸", "D) 6a⁵b⁸"],
                                "correct_answer": "A) 6a⁵b⁶",
                                "explanation": "Multiply coefficients: 2 × 3 = 6. Add exponents for like bases: a³⁺² = a⁵, b²⁺⁴ = b⁶. Total = 6a⁵b⁶.",
                                "step_by_step_solution": [
                                    "Step 1: Coefficients: 2 × 3 = 6.",
                                    "Step 2: a terms: a³ · a² = a⁵.",
                                    "Step 3: b terms: b² · b⁴ = b⁶.",
                                    "Step 4: Result = 6a⁵b⁶."
                                ],
                                "difficulty": "hard",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] What is the reciprocal of 4/7 as a decimal (rounded to 2 decimal places)?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "1.75",
                                "explanation": "Reciprocal of 4/7 is 7/4 = 1.75.",
                                "step_by_step_solution": [
                                    "Step 1: Flip numerator and denominator: 7/4.",
                                    "Step 2: 7 ÷ 4 = 1.75."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "Evaluate: (-2)⁴ =",
                                "question_type": "multiple_choice",
                                "options": ["A) -16", "B) 16", "C) -8", "D) 8"],
                                "correct_answer": "B) 16",
                                "explanation": "A negative number raised to an EVEN power is positive: (-2) × (-2) × (-2) × (-2) = +16.",
                                "step_by_step_solution": [
                                    "Step 1: (-2) × (-2) = +4.",
                                    "Step 2: (+4) × (-2) = -8.",
                                    "Step 3: (-8) × (-2) = +16."
                                ],
                                "difficulty": "medium",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Polynomial Operations & Factorization",
                "description": "Adding, subtracting, and expanding polynomials, common factor factoring, and equations.",
                "learning_objectives": [
                    "Add, subtract, and multiply algebraic expressions",
                    "Factorize expressions by taking out common factors and by grouping",
                    "Solve multi-step linear equations involving brackets and fractions"
                ],
                "grade": 7,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Polynomial Forge",
                        "instructions": "Expand binomial products and factor algebraic expressions at the forge.",
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
                                "prompt": "Expand the product: 3x(2x - 5)",
                                "question_type": "multiple_choice",
                                "options": ["A) 6x² - 15", "B) 6x² - 15x", "C) 5x² - 15x", "D) 6x - 15"],
                                "correct_answer": "B) 6x² - 15x",
                                "explanation": "Distribute 3x: 3x × 2x = 6x², and 3x × (-5) = -15x. Product = 6x² - 15x.",
                                "step_by_step_solution": [
                                    "Step 1: 3x × 2x = 6x².",
                                    "Step 2: 3x × (-5) = -15x.",
                                    "Step 3: Combine = 6x² - 15x."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "Factorize completely: 12x + 18",
                                "question_type": "multiple_choice",
                                "options": ["A) 6(2x + 3)", "B) 3(4x + 6)", "C) 2(6x + 9)", "D) 6x(2 + 3)"],
                                "correct_answer": "A) 6(2x + 3)",
                                "explanation": "The highest common factor of 12 and 18 is 6. Factor out 6: 6(2x + 3).",
                                "step_by_step_solution": [
                                    "Step 1: HCF of 12x and 18 is 6.",
                                    "Step 2: 12x / 6 = 2x.",
                                    "Step 3: 18 / 6 = 3. Factored form = 6(2x + 3)."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "Expand: (x + 3)(x + 4) =",
                                "question_type": "multiple_choice",
                                "options": ["A) x² + 7x + 12", "B) x² + 12x + 7", "C) x² + 7", "D) x² + 12"],
                                "correct_answer": "A) x² + 7x + 12",
                                "explanation": "FOIL method: x² + 4x + 3x + 12 = x² + 7x + 12.",
                                "step_by_step_solution": [
                                    "Step 1: First: x × x = x².",
                                    "Step 2: Outside: x × 4 = 4x.",
                                    "Step 3: Inside: 3 × x = 3x.",
                                    "Step 4: Last: 3 × 4 = 12.",
                                    "Step 5: Combine like terms: 4x + 3x = 7x. Total = x² + 7x + 12."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "Factorize by grouping: ax + ay + bx + by",
                                "question_type": "multiple_choice",
                                "options": ["A) (a + b)(x + y)", "B) (a + x)(b + y)", "C) (ax + by)(a + b)", "D) ab(x + y)"],
                                "correct_answer": "A) (a + b)(x + y)",
                                "explanation": "Group: a(x + y) + b(x + y) = (a + b)(x + y).",
                                "step_by_step_solution": [
                                    "Step 1: Group pairs: (ax + ay) + (bx + by).",
                                    "Step 2: Factor out common terms: a(x + y) + b(x + y).",
                                    "Step 3: Factor out binomial (x + y): (a + b)(x + y)."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] Solve for x:  3(x - 2) = 2(x + 4). Enter the value of x:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "14",
                                "explanation": "3x - 6 = 2x + 8 => 3x - 2x = 8 + 6 => x = 14.",
                                "step_by_step_solution": [
                                    "Step 1: Expand brackets: 3x - 6 = 2x + 8.",
                                    "Step 2: Subtract 2x: x - 6 = 8.",
                                    "Step 3: Add 6: x = 14."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "Factorize: 4x²y - 8xy²",
                                "question_type": "multiple_choice",
                                "options": ["A) 4xy(x - 2y)", "B) 4x(xy - 2y²)", "C) 2xy(2x - 4y)", "D) 4y(x² - 2xy)"],
                                "correct_answer": "A) 4xy(x - 2y)",
                                "explanation": "HCF is 4xy: 4xy(x - 2y).",
                                "step_by_step_solution": [
                                    "Step 1: Common factor of 4 and 8 is 4.",
                                    "Step 2: Common variables: x¹ and y¹.",
                                    "Step 3: 4xy(x - 2y)."
                                ],
                                "difficulty": "hard",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] If 2x/3 + 5 = 11, find the value of x:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "9",
                                "explanation": "2x/3 = 11 - 5 = 6 => 2x = 18 => x = 9.",
                                "step_by_step_solution": [
                                    "Step 1: Subtract 5: 2x/3 = 6.",
                                    "Step 2: Multiply by 3: 2x = 18.",
                                    "Step 3: Divide by 2: x = 9."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "Expand the difference of squares: (2x - 3)(2x + 3) =",
                                "question_type": "multiple_choice",
                                "options": ["A) 4x² - 6", "B) 4x² - 9", "C) 4x² + 9", "D) 2x² - 9"],
                                "correct_answer": "B) 4x² - 9",
                                "explanation": "(a - b)(a + b) = a² - b² = (2x)² - (3)² = 4x² - 9.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: (a - b)(a + b) = a² - b².",
                                    "Step 2: (2x)² - 3² = 4x² - 9."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    },
                    {
                        "title": "Linear Equations Citadel",
                        "instructions": "Master equations with variables on both sides, brackets, and fractional coefficients.",
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
                                "prompt": "Solve for x:  5x - 7 = 3x + 11",
                                "question_type": "multiple_choice",
                                "options": ["A) 7", "B) 8", "C) 9", "D) 10"],
                                "correct_answer": "C) 9",
                                "explanation": "5x - 3x = 11 + 7 => 2x = 18 => x = 9.",
                                "step_by_step_solution": [
                                    "Step 1: 5x - 3x = 18.",
                                    "Step 2: 2x = 18 => x = 9."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "[Numeric Entry] Solve for y:  4(y - 3) = 20. Enter the value of y:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "8",
                                "explanation": "y - 3 = 20 / 4 = 5 => y = 5 + 3 = 8.",
                                "step_by_step_solution": [
                                    "Step 1: Divide by 4: y - 3 = 5.",
                                    "Step 2: y = 8."
                                ],
                                "difficulty": "easy",
                                "tolerance": 0.01,
                                "display_order": 2
                            },
                            {
                                "prompt": "Solve for m:  (m + 4) / 3 = 5",
                                "question_type": "multiple_choice",
                                "options": ["A) 11", "B) 15", "C) 19", "D) 9"],
                                "correct_answer": "A) 11",
                                "explanation": "m + 4 = 5 × 3 = 15 => m = 15 - 4 = 11.",
                                "step_by_step_solution": [
                                    "Step 1: Multiply by 3: m + 4 = 15.",
                                    "Step 2: m = 11."
                                ],
                                "difficulty": "medium",
                                "display_order": 3
                            },
                            {
                                "prompt": "[Numeric Entry] If 3(2x - 1) = 4x + 7, what is the value of x?",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "5",
                                "explanation": "6x - 3 = 4x + 7 => 2x = 10 => x = 5.",
                                "step_by_step_solution": [
                                    "Step 1: 6x - 3 = 4x + 7.",
                                    "Step 2: 2x = 10 => x = 5."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 4
                            },
                            {
                                "prompt": "The perimeter of a rectangle is 34 cm. If its length is 5 cm more than its width w, what is its width?",
                                "question_type": "multiple_choice",
                                "options": ["A) 5 cm", "B) 6 cm", "C) 7 cm", "D) 8 cm"],
                                "correct_answer": "B) 6 cm",
                                "explanation": "2(w + w + 5) = 34 => 2(2w + 5) = 34 => 2w + 5 = 17 => 2w = 12 => w = 6 cm.",
                                "step_by_step_solution": [
                                    "Step 1: 2(2w + 5) = 34.",
                                    "Step 2: 2w + 5 = 17.",
                                    "Step 3: 2w = 12 => w = 6 cm."
                                ],
                                "difficulty": "hard",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] Solve for p:  2p/5 - 3 = 1. Enter the value of p:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "10",
                                "explanation": "2p/5 = 4 => 2p = 20 => p = 10.",
                                "step_by_step_solution": [
                                    "Step 1: 2p/5 = 4.",
                                    "Step 2: 2p = 20 => p = 10."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "A number increased by its half equals 18. What is the number?",
                                "question_type": "multiple_choice",
                                "options": ["A) 9", "B) 12", "C) 14", "D) 16"],
                                "correct_answer": "B) 12",
                                "explanation": "x + x/2 = 18 => (3/2)x = 18 => x = 18 × 2 / 3 = 12.",
                                "step_by_step_solution": [
                                    "Step 1: 1.5x = 18.",
                                    "Step 2: x = 18 / 1.5 = 12."
                                ],
                                "difficulty": "hard",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] Solve for k:  5 - 2(k - 4) = -1. Enter the value of k:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "7",
                                "explanation": "5 - 2k + 8 = -1 => 13 - 2k = -1 => 2k = 14 => k = 7.",
                                "step_by_step_solution": [
                                    "Step 1: 13 - 2k = -1.",
                                    "Step 2: 2k = 14 => k = 7."
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
        "title": "Commercial & Circle City",
        "description": "Calculate commercial profit, loss, Zakat, and discover circular mensuration and probability.",
        "grade": 7,
        "icon": "landmark",
        "theme_color": "cyan",
        "display_order": 2,
        "topics": [
            {
                "title": "Financial Mathematics (Profit, Loss, Zakat & Tax)",
                "description": "Cost price, selling price, percentage profit/loss, discount, Zakat (2.5%), and simple interest.",
                "learning_objectives": [
                    "Calculate profit, loss, and their percentage values",
                    "Compute Zakat on wealth at the rate of 2.5%",
                    "Calculate simple interest using I = (P × R × T) / 100"
                ],
                "grade": 7,
                "display_order": 1,
                "missions": [
                    {
                        "title": "The Financial Exchange",
                        "instructions": "Audit market transactions, compute Zakat dues, and calculate commercial interest.",
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
                                "prompt": "An article bought for Rs. 500 was sold for Rs. 600. What is the profit percentage?",
                                "question_type": "multiple_choice",
                                "options": ["A) 15%", "B) 20%", "C) 25%", "D) 10%"],
                                "correct_answer": "B) 20%",
                                "explanation": "Profit = 600 - 500 = Rs. 100. Profit % = (100 / 500) × 100% = 20%.",
                                "step_by_step_solution": [
                                    "Step 1: Profit = Selling Price - Cost Price = 600 - 500 = 100.",
                                    "Step 2: Profit % = (Profit / Cost Price) × 100.",
                                    "Step 3: (100 / 500) × 100% = 20%."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "What is the official rate of Zakat payable on wealth exceeding Nisab?",
                                "question_type": "multiple_choice",
                                "options": ["A) 2%", "B) 2.5%", "C) 5%", "D) 10%"],
                                "correct_answer": "B) 2.5%",
                                "explanation": "In Pakistan and Islamic jurisprudence, Zakat is calculated at the rate of 2.5% (or 1/40th) of qualifying wealth.",
                                "step_by_step_solution": [
                                    "Step 1: Zakat rate = 2.5% = 1/40."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] Calculate the Zakat payable on cash savings of Rs. 200,000 at the rate of 2.5%:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "5000",
                                "explanation": "Zakat = 2.5% of 200,000 = (2.5 / 100) × 200,000 = 5,000 Rupees.",
                                "step_by_step_solution": [
                                    "Step 1: 200,000 / 40 = 5,000 Rupees (or 200,000 × 0.025 = 5,000)."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "A shirt marked at Rs. 1,200 is sold at a 15% discount. What is the selling price of the shirt?",
                                "question_type": "multiple_choice",
                                "options": ["A) Rs. 1,000", "B) Rs. 1,020", "C) Rs. 1,050", "D) Rs. 1,080"],
                                "correct_answer": "B) Rs. 1,020",
                                "explanation": "Discount = 15% of 1,200 = 180. Sale price = 1,200 - 180 = Rs. 1,020.",
                                "step_by_step_solution": [
                                    "Step 1: Discount = 0.15 × 1200 = 180.",
                                    "Step 2: Sale price = 1200 - 180 = Rs. 1,020."
                                ],
                                "difficulty": "medium",
                                "display_order": 4
                            },
                            {
                                "prompt": "[Numeric Entry] Calculate the simple interest on a principal of Rs. 10,000 at 8% per annum for 3 years:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "2400",
                                "explanation": "I = (P × R × T) / 100 = (10,000 × 8 × 3) / 100 = 2,400 Rupees.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: I = PRT / 100.",
                                    "Step 2: (10,000 × 8 × 3) / 100 = 240,000 / 100 = 2,400."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 5
                            },
                            {
                                "prompt": "A merchant suffered a 10% loss on selling an item for Rs. 450. What was the cost price of the item?",
                                "question_type": "multiple_choice",
                                "options": ["A) Rs. 490", "B) Rs. 500", "C) Rs. 520", "D) Rs. 550"],
                                "correct_answer": "B) Rs. 500",
                                "explanation": "Selling price = 90% of Cost Price. 0.90 × CP = 450 => CP = 450 / 0.90 = Rs. 500.",
                                "step_by_step_solution": [
                                    "Step 1: SP = CP × (1 - Loss% / 100).",
                                    "Step 2: 450 = CP × 0.90.",
                                    "Step 3: CP = 450 / 0.90 = 500."
                                ],
                                "common_mistakes": {
                                    "Rs. 495": "Do not add 10% of the selling price; percentage loss is always based on the cost price!"
                                },
                                "difficulty": "hard",
                                "display_order": 6
                            },
                            {
                                "prompt": "[Numeric Entry] Calculate the property tax at 2% on a house assessed at Rs. 1,500,000:",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "30000",
                                "explanation": "Tax = 2% of 1,500,000 = (2 / 100) × 1,500,000 = 30,000 Rupees.",
                                "step_by_step_solution": [
                                    "Step 1: Tax = 0.02 × 1,500,000 = 30,000."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 7
                            },
                            {
                                "prompt": "An investment of Rs. 25,000 earned Rs. 5,000 in simple interest over 2 years. What was the annual interest rate?",
                                "question_type": "multiple_choice",
                                "options": ["A) 8%", "B) 10%", "C) 12%", "D) 15%"],
                                "correct_answer": "B) 10%",
                                "explanation": "R = (100 × I) / (P × T) = (100 × 5,000) / (25,000 × 2) = 500,000 / 50,000 = 10%.",
                                "step_by_step_solution": [
                                    "Step 1: R = (100 × I) / (P × T).",
                                    "Step 2: R = (100 × 5,000) / (25,000 × 2) = 500,000 / 50,000 = 10%."
                                ],
                                "difficulty": "hard",
                                "display_order": 8
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Circle Mensuration & Probability",
                "description": "Circumference and area of circles, triangle congruence criteria, and theoretical probability.",
                "learning_objectives": [
                    "Calculate circumference (2πr) and area (πr²) of circles",
                    "Apply triangle congruence criteria (SSS, SAS, ASA, RHS)",
                    "Calculate theoretical probability of simple events"
                ],
                "grade": 7,
                "display_order": 2,
                "missions": [
                    {
                        "title": "Circle & Probability Plaza",
                        "instructions": "Measure circular fountains and predict chance outcomes in the central plaza.",
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
                                "prompt": "What is the circumference of a circle with radius 7 cm? (Use π = 22/7)",
                                "question_type": "multiple_choice",
                                "options": ["A) 22 cm", "B) 44 cm", "C) 88 cm", "D) 154 cm"],
                                "correct_answer": "B) 44 cm",
                                "explanation": "Circumference = 2πr = 2 × (22/7) × 7 = 44 cm.",
                                "step_by_step_solution": [
                                    "Step 1: Formula: C = 2πr.",
                                    "Step 2: C = 2 × (22/7) × 7 = 44 cm."
                                ],
                                "difficulty": "easy",
                                "display_order": 1
                            },
                            {
                                "prompt": "A fair six-sided die is rolled. What is the probability of rolling an even number?",
                                "question_type": "multiple_choice",
                                "options": ["A) 1/6", "B) 1/3", "C) 1/2", "D) 2/3"],
                                "correct_answer": "C) 1/2",
                                "explanation": "Even outcomes: {2, 4, 6} (3 outcomes). Total outcomes = 6. Probability = 3/6 = 1/2.",
                                "step_by_step_solution": [
                                    "Step 1: Even numbers on a die: 2, 4, 6 (3 numbers).",
                                    "Step 2: Total faces: 6.",
                                    "Step 3: P = 3/6 = 1/2."
                                ],
                                "difficulty": "easy",
                                "display_order": 2
                            },
                            {
                                "prompt": "[Numeric Entry] What is the area of a circle with radius 7 cm in cm²? (Use π = 22/7):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "154",
                                "explanation": "Area = πr² = (22/7) × 7 × 7 = 22 × 7 = 154 cm².",
                                "step_by_step_solution": [
                                    "Step 1: Formula: A = πr².",
                                    "Step 2: A = (22/7) × 49 = 154 cm²."
                                ],
                                "difficulty": "medium",
                                "tolerance": 0.01,
                                "display_order": 3
                            },
                            {
                                "prompt": "Which congruence criterion states that two triangles are congruent if three sides of one triangle are equal to three sides of another?",
                                "question_type": "multiple_choice",
                                "options": ["A) SAS", "B) ASA", "C) SSS", "D) RHS"],
                                "correct_answer": "C) SSS",
                                "explanation": "SSS stands for Side-Side-Side congruence.",
                                "step_by_step_solution": [
                                    "Step 1: Three equal sides = SSS (Side-Side-Side)."
                                ],
                                "difficulty": "easy",
                                "display_order": 4
                            },
                            {
                                "prompt": "A bag contains 5 red balls, 3 blue balls, and 2 green balls. A ball is drawn at random. What is the probability of drawing a blue ball?",
                                "question_type": "multiple_choice",
                                "options": ["A) 1/5", "B) 3/10", "C) 1/2", "D) 3/7"],
                                "correct_answer": "B) 3/10",
                                "explanation": "Total balls = 5 + 3 + 2 = 10. Blue balls = 3. P(blue) = 3/10.",
                                "step_by_step_solution": [
                                    "Step 1: Total = 5 + 3 + 2 = 10.",
                                    "Step 2: Favorable = 3.",
                                    "Step 3: P = 3/10."
                                ],
                                "difficulty": "medium",
                                "display_order": 5
                            },
                            {
                                "prompt": "[Numeric Entry] What is the diameter of a circle whose circumference is 88 cm? (Use π = 22/7):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "28",
                                "explanation": "C = πd => 88 = (22/7) × d => d = (88 × 7) / 22 = 4 × 7 = 28 cm.",
                                "step_by_step_solution": [
                                    "Step 1: C = πd.",
                                    "Step 2: d = C / π = 88 / (22/7) = (88 × 7) / 22 = 28 cm."
                                ],
                                "difficulty": "hard",
                                "tolerance": 0.01,
                                "display_order": 6
                            },
                            {
                                "prompt": "If a card is drawn at random from a standard deck of 52 cards, what is the probability of drawing an Ace?",
                                "question_type": "multiple_choice",
                                "options": ["A) 1/52", "B) 1/13", "C) 1/4", "D) 4/13"],
                                "correct_answer": "B) 1/13",
                                "explanation": "There are 4 Aces in a deck of 52 cards: 4/52 = 1/13.",
                                "step_by_step_solution": [
                                    "Step 1: 4 aces in 52 cards.",
                                    "Step 2: 4/52 = 1/13."
                                ],
                                "difficulty": "medium",
                                "display_order": 7
                            },
                            {
                                "prompt": "[Numeric Entry] A circular track has a radius of 14 meters. How many meters does an athlete run in 1 complete lap? (Use π = 22/7):",
                                "question_type": "numeric",
                                "options": None,
                                "correct_answer": "88",
                                "explanation": "1 lap = Circumference = 2πr = 2 × (22/7) × 14 = 2 × 22 × 2 = 88 meters.",
                                "step_by_step_solution": [
                                    "Step 1: C = 2 × (22/7) × 14 = 88 m."
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
