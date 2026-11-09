from sqlalchemy.orm import Session
from app.models.curriculum import World, Topic, Mission, Question, DifficultyLevel, MissionCategory
from app.models.gamification import Badge

def seed_curriculum_and_badges(db: Session):
    """
    Seeds verified curriculum worlds, topics, missions (MCQs & Numeric), and badges:
    Module 4: Topic-based missions, MCQs, Numeric answers, Easy/Med/Difficult,
    Boss Challenges, and Unlock conditions.
    """
    # 1. Seed Badges
    if db.query(Badge).first() is None:
        badges = [
            Badge(
                code="first_steps",
                name="First Steps",
                description="Completed your first mathematics mission.",
                icon="footprints",
                category="milestone",
                criteria_description="Complete 1 mission"
            ),
            Badge(
                code="algebra_explorer",
                name="Algebra Explorer",
                description="Mastered missions in the Algebra Kingdom.",
                icon="shield",
                category="algebra",
                criteria_description="Complete 3 Algebra Kingdom missions"
            ),
            Badge(
                code="accuracy_star",
                name="Accuracy Star",
                description="Demonstrated high precision by achieving 80% or higher accuracy.",
                icon="star",
                category="mastery",
                criteria_description="Score >= 80% accuracy in any mission"
            ),
            Badge(
                code="practice_champion",
                name="Practice Champion",
                description="Consistently practised across 5 study sessions.",
                icon="flame",
                category="streak",
                criteria_description="Complete missions across 5 distinct sessions"
            ),
            Badge(
                code="boss_victor",
                name="Boss Victor",
                description="Conquered a high-difficulty world Boss Challenge.",
                icon="trophy",
                category="boss",
                criteria_description="Successfully complete a Boss Challenge mission"
            )
        ]
        db.add_all(badges)
        db.commit()

    # 2. Seed Worlds, Topics, Missions, Questions
    if db.query(World).count() < 4:
        db.query(Question).delete()
        db.query(Mission).delete()
        db.query(Topic).delete()
        db.query(World).delete()
        db.commit()

        # =====================================================================
        # WORLD 1: Algebra Kingdom (Grade 11)
        # =====================================================================
        w1 = World(
            title="Algebra Kingdom",
            description="Embark through matrices, determinants, and polynomial equations in the royal algebraic realm.",
            grade=11,
            icon="compass",
            theme_color="emerald",
            display_order=1
        )
        db.add(w1)
        db.flush()

        t1_1 = Topic(
            world_id=w1.id,
            title="Matrices & Systems of Linear Equations",
            description="Fundamental matrix arithmetic, determinants, matrix inversions, and solving systems using Cramer's rule.",
            learning_objectives=[
                "Perform matrix addition, subtraction, and scalar multiplication",
                "Calculate determinants of 2x2 and 3x3 square matrices",
                "Solve systems of linear equations using Cramer's rule"
            ],
            grade=11,
            display_order=1
        )
        t1_2 = Topic(
            world_id=w1.id,
            title="Quadratic Equations & Complex Numbers",
            description="Root classification using the discriminant, complex number algebra, and factoring techniques.",
            learning_objectives=[
                "Determine the nature of roots using the discriminant b² - 4ac",
                "Execute complex number arithmetic (addition, multiplication, conjugates)",
                "Solve higher-degree polynomial equations by factoring"
            ],
            grade=11,
            display_order=2
        )
        db.add_all([t1_1, t1_2])
        db.flush()

        # Module 4 Example: Linear Equations Mission with 5 questions (MCQ + Numeric)
        m1_1 = Mission(
            topic_id=t1_1.id,
            title="Linear Equation Challenge",
            instructions="Solve each single-variable and matrix linear problem step-by-step. Complete all 5 questions with at least 60% accuracy to unlock the next challenge.",
            category=MissionCategory.CONCEPT_EXPLORATION.value,
            difficulty=DifficultyLevel.EASY.value,
            question_count=5,
            xp_reward=20,
            pass_percentage=60,
            unlock_condition="always",
            display_order=1,
            is_boss=False
        )
        db.add(m1_1)
        db.flush()

        # Mission 1_2 (Medium Difficulty, requires m1_1)
        m1_2 = Mission(
            topic_id=t1_1.id,
            title="Determinant Inversion Mastery",
            instructions="Compute determinants of 2x2 and 3x3 matrices. Identify singular matrices.",
            category=MissionCategory.PRACTICE.value,
            difficulty=DifficultyLevel.MEDIUM.value,
            question_count=3,
            xp_reward=25,
            pass_percentage=60,
            unlock_condition=f"requires_mission:{m1_1.id}",
            display_order=2,
            is_boss=False
        )
        # Mission 1_3 (Boss Challenge)
        m1_3 = Mission(
            topic_id=t1_2.id,
            title="Boss Challenge: The Polynomial Dragon",
            instructions="Prove your algebraic mastery by defeating the legendary Polynomial Dragon in this final trial.",
            category=MissionCategory.BOSS_CHALLENGE.value,
            difficulty=DifficultyLevel.BOSS.value,
            question_count=3,
            xp_reward=50,
            pass_percentage=60,
            unlock_condition="boss_topic_mastery",
            display_order=3,
            is_boss=True
        )
        db.add_all([m1_2, m1_3])
        db.flush()

        # Questions for Mission 1_1 (5 questions: 4 MCQ, 1 Numeric)
        db.add_all([
            Question(
                mission_id=m1_1.id,
                prompt="Solve for x:  3x + 5 = 20",
                question_type="multiple_choice",
                options=["A) 3", "B) 5", "C) 7", "D) 15"],
                correct_answer="B) 5",
                explanation="Subtract 5 from both sides: 3x = 15. Divide both sides by 3: x = 15/3 = 5.",
                step_by_step_solution=[
                    "Step 1 (Subtraction): Subtract 5 from both sides: 3x + 5 - 5 = 20 - 5  ==>  3x = 15",
                    "Step 2 (Division): Divide both sides by 3: (3x) / 3 = 15 / 3  ==>  x = 5",
                    "Step 3 (Verification): Check by substituting x = 5: 3(5) + 5 = 15 + 5 = 20 (Verified!)."
                ],
                common_mistakes={
                    "4": "If x = 4, substituting into the equation gives: 3(4) + 5 = 12 + 5 = 17 != 20. Make sure to subtract 5 from 20 before dividing by 3.",
                    "3": "If x = 3, substituting gives: 3(3) + 5 = 9 + 5 = 14 != 20.",
                    "7": "If x = 7, substituting gives: 3(7) + 5 = 26 != 20. Remember to subtract 5 from 20, rather than adding.",
                    "15": "15 is the intermediate value of 3x (since 20 - 5 = 15). Don't forget the second step: divide by 3 to find x!"
                },
                difficulty=DifficultyLevel.EASY.value,
                display_order=1
            ),
            Question(
                mission_id=m1_1.id,
                prompt="If 2x - 4 = 10, what is the value of x + 3?",
                question_type="multiple_choice",
                options=["A) 7", "B) 8", "C) 10", "D) 14"],
                correct_answer="C) 10",
                explanation="Solve for x: 2x = 14 => x = 7. Then evaluate x + 3 = 7 + 3 = 10.",
                difficulty=DifficultyLevel.EASY.value,
                display_order=2
            ),
            Question(
                mission_id=m1_1.id,
                prompt="Find the root of: 5(y - 2) = 3y + 6",
                question_type="multiple_choice",
                options=["A) 4", "B) 6", "C) 8", "D) 10"],
                correct_answer="C) 8",
                explanation="Expand left side: 5y - 10 = 3y + 6. Subtract 3y: 2y - 10 = 6. Add 10: 2y = 16 => y = 8.",
                difficulty=DifficultyLevel.EASY.value,
                display_order=3
            ),
            Question(
                mission_id=m1_1.id,
                prompt="Solve for z:  (z / 4) + 2 = 5",
                question_type="multiple_choice",
                options=["A) 8", "B) 10", "C) 12", "D) 16"],
                correct_answer="C) 12",
                explanation="Subtract 2: z/4 = 3. Multiply both sides by 4: z = 12.",
                difficulty=DifficultyLevel.EASY.value,
                display_order=4
            ),
            # NUMERIC ANSWER QUESTION (FR-15)
            Question(
                mission_id=m1_1.id,
                prompt="[Numeric Entry] Solve for k:  4k - 7 = 17. Enter the exact numerical value of k:",
                question_type="numeric",
                options=None,
                correct_answer="6",
                explanation="Add 7 to both sides: 4k = 24. Divide by 4: k = 24/4 = 6.",
                difficulty=DifficultyLevel.EASY.value,
                tolerance=0.01,
                display_order=5
            ),
            # Questions for Mission 1_2 (Medium)
            Question(
                mission_id=m1_2.id,
                prompt="Evaluate the determinant of matrix A = [[2, 3], [1, 4]]:",
                question_type="multiple_choice",
                options=["A) 5", "B) 8", "C) 11", "D) -5"],
                correct_answer="A) 5",
                explanation="Determinant |A| = (ad - bc) = (2 * 4) - (3 * 1) = 8 - 3 = 5.",
                difficulty=DifficultyLevel.MEDIUM.value,
                display_order=1
            ),
            Question(
                mission_id=m1_2.id,
                prompt="Which condition makes matrix [[k, 6], [2, 3]] singular (det = 0)?",
                question_type="multiple_choice",
                options=["A) k = 1", "B) k = 4", "C) k = 6", "D) k = 12"],
                correct_answer="B) k = 4",
                explanation="Singular means det = 0: (3k) - (6 * 2) = 0 => 3k = 12 => k = 4.",
                difficulty=DifficultyLevel.MEDIUM.value,
                display_order=2
            ),
            Question(
                mission_id=m1_2.id,
                prompt="[Numeric Entry] Compute the determinant of matrix [[7, 2], [5, 3]]:",
                question_type="numeric",
                options=None,
                correct_answer="11",
                explanation="det = (7 * 3) - (2 * 5) = 21 - 10 = 11.",
                difficulty=DifficultyLevel.MEDIUM.value,
                tolerance=0.01,
                display_order=3
            ),
            # Questions for Mission 1_3 (Boss Challenge)
            Question(
                mission_id=m1_3.id,
                prompt="What is the nature of the roots of 2x² - 4x + 2 = 0?",
                question_type="multiple_choice",
                options=["A) Real and distinct", "B) Real and equal", "C) Complex conjugates", "D) Irrationals"],
                correct_answer="B) Real and equal",
                explanation="Discriminant Δ = b² - 4ac = (-4)² - 4(2)(2) = 16 - 16 = 0. When Δ = 0, roots are real and equal.",
                difficulty=DifficultyLevel.BOSS.value,
                display_order=1
            ),
            Question(
                mission_id=m1_3.id,
                prompt="What is the product of (3 + 2i) and (3 - 2i)?",
                question_type="multiple_choice",
                options=["A) 5", "B) 9", "C) 13", "D) 13 - 12i"],
                correct_answer="C) 13",
                explanation="Difference of squares for complex conjugates: (3)² - (2i)² = 9 - 4(i²) = 9 - 4(-1) = 9 + 4 = 13.",
                difficulty=DifficultyLevel.BOSS.value,
                display_order=2
            ),
            Question(
                mission_id=m1_3.id,
                prompt="[Numeric Entry] Find the sum of the roots of the quadratic equation 3x² - 18x + 7 = 0:",
                question_type="numeric",
                options=None,
                correct_answer="6",
                explanation="Sum of roots for ax² + bx + c = 0 is -b/a = -(-18)/3 = 18/3 = 6.",
                difficulty=DifficultyLevel.BOSS.value,
                tolerance=0.01,
                display_order=3
            )
        ])

        # =====================================================================
        # WORLD 2: Trigonometry Island (Grade 11)
        # =====================================================================
        w2 = World(
            title="Trigonometry Island",
            description="Explore sinusoidal shores, unit circles, and compound angle mysteries across trigonometry.",
            grade=11,
            icon="mountain",
            theme_color="cyan",
            display_order=2
        )
        db.add(w2)
        db.flush()

        t2_1 = Topic(
            world_id=w2.id,
            title="Fundamental Trigonometric Identities",
            description="Ratios, Pythagorean identities, reciprocal relationships, and radian measures.",
            learning_objectives=[
                "Recall exact values for 0°, 30°, 45°, 60°, and 90°",
                "Apply the fundamental identity sin²θ + cos²θ = 1",
                "Convert between degree and radian measures"
            ],
            grade=11,
            display_order=1
        )
        db.add(t2_1)
        db.flush()

        m2_1 = Mission(
            topic_id=t2_1.id,
            title="Unit Circle Expedition",
            instructions="Identify exact circular function values on the unit circle.",
            category=MissionCategory.CONCEPT_EXPLORATION.value,
            difficulty=DifficultyLevel.EASY.value,
            question_count=2,
            xp_reward=20,
            pass_percentage=60,
            unlock_condition="always",
            display_order=1,
            is_boss=False
        )
        db.add(m2_1)
        db.flush()

        db.add_all([
            Question(
                mission_id=m2_1.id,
                prompt="What is the exact value of sin(30°)?",
                question_type="multiple_choice",
                options=["A) 1/2", "B) √3/2", "C) 1", "D) 0"],
                correct_answer="A) 1/2",
                explanation="By standard trigonometric ratios for special angles: sin(30°) = sin(π/6) = 1/2.",
                difficulty=DifficultyLevel.EASY.value,
                display_order=1
            ),
            Question(
                mission_id=m2_1.id,
                prompt="[Numeric Entry] Convert 180 degrees into radians as a multiple of π. Enter the coefficient of π (e.g. for 1π, enter 1):",
                question_type="numeric",
                options=None,
                correct_answer="1",
                explanation="180° = π radians, so the coefficient is 1.",
                difficulty=DifficultyLevel.EASY.value,
                tolerance=0.01,
                display_order=2
            )
        ])

        # =====================================================================
        # WORLD 3: Calculus Tower (Grade 12)
        # =====================================================================
        w3 = World(
            title="Calculus Tower",
            description="Ascend the towers of limits, differential calculus, and instantaneous rates of change.",
            grade=12,
            icon="castle",
            theme_color="purple",
            display_order=1
        )
        db.add(w3)
        db.flush()

        t3_1 = Topic(
            world_id=w3.id,
            title="Limits & Continuity",
            description="Approaching values, resolving indeterminate forms, and evaluating continuity at a point.",
            learning_objectives=[
                "Evaluate algebraic limits as x approaches finite values",
                "Resolve indeterminate 0/0 forms using factorization",
                "Test continuity using left-hand and right-hand limits"
            ],
            grade=12,
            display_order=1
        )
        db.add(t3_1)
        db.flush()

        m3_1 = Mission(
            topic_id=t3_1.id,
            title="Limit Evaluation Trial",
            instructions="Calculate limits as x approaches specified values using algebraic factorization.",
            category=MissionCategory.CONCEPT_EXPLORATION.value,
            difficulty=DifficultyLevel.EASY.value,
            question_count=2,
            xp_reward=20,
            pass_percentage=60,
            unlock_condition="always",
            display_order=1,
            is_boss=False
        )
        db.add(m3_1)
        db.flush()

        db.add_all([
            Question(
                mission_id=m3_1.id,
                prompt="Evaluate:  lim (x -> 3) of (x² - 9) / (x - 3)",
                question_type="multiple_choice",
                options=["A) 0", "B) 3", "C) 6", "D) Undefined"],
                correct_answer="C) 6",
                explanation="Factor the numerator: (x - 3)(x + 3) / (x - 3) = x + 3. Substitute x = 3: 3 + 3 = 6.",
                difficulty=DifficultyLevel.EASY.value,
                display_order=1
            ),
            Question(
                mission_id=m3_1.id,
                prompt="[Numeric Entry] Evaluate:  lim (x -> 4) of (2x + 5). Enter the exact value:",
                question_type="numeric",
                options=None,
                correct_answer="13",
                explanation="Direct substitution for continuous polynomial: 2(4) + 5 = 8 + 5 = 13.",
                difficulty=DifficultyLevel.EASY.value,
                tolerance=0.01,
                display_order=2
            )
        ])

        # =====================================================================
        # WORLD 4: Statistics City (Grade 12)
        # =====================================================================
        w4 = World(
            title="Statistics City",
            description="Navigate the urban districts of measures of dispersion, probability theory, and normal distributions.",
            grade=12,
            icon="chart",
            theme_color="amber",
            display_order=2
        )
        db.add(w4)
        db.flush()

        t4_1 = Topic(
            world_id=w4.id,
            title="Measures of Dispersion",
            description="Analysis of variance, standard deviation, quartiles, and range in grouped and ungrouped datasets.",
            learning_objectives=[
                "Calculate the range and interquartile range (IQR)",
                "Calculate sample variance and standard deviation",
                "Interpret spread of data around the mean"
            ],
            grade=12,
            display_order=1
        )
        db.add(t4_1)
        db.flush()

        m4_1 = Mission(
            topic_id=t4_1.id,
            title="The Variance Vault",
            instructions="Inspect frequency distributions and calculate measures of spread.",
            category=MissionCategory.CONCEPT_EXPLORATION.value,
            difficulty=DifficultyLevel.EASY.value,
            question_count=2,
            xp_reward=20,
            pass_percentage=60,
            unlock_condition="always",
            display_order=1,
            is_boss=False
        )
        db.add(m4_1)
        db.flush()

        db.add_all([
            Question(
                mission_id=m4_1.id,
                prompt="Given the data set: 2, 4, 4, 4, 5, 5, 7, 9. What is the sample range?",
                question_type="multiple_choice",
                options=["A) 5", "B) 7", "C) 4", "D) 9"],
                correct_answer="B) 7",
                explanation="Range = Maximum - Minimum = 9 - 2 = 7.",
                difficulty=DifficultyLevel.EASY.value,
                display_order=1
            ),
            Question(
                mission_id=m4_1.id,
                prompt="[Numeric Entry] If the variance of a dataset is 64, what is the standard deviation? Enter the exact number:",
                question_type="numeric",
                options=None,
                correct_answer="8",
                explanation="Standard deviation σ is the positive square root of variance: √64 = 8.",
                difficulty=DifficultyLevel.EASY.value,
                tolerance=0.01,
                display_order=2
            )
        ])

        db.commit()
