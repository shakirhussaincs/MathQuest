from sqlalchemy.orm import Session
from app.models.curriculum import World, Topic, Mission, Question
from app.models.gamification import Badge

from app.services.curriculum_data.grade1 import GRADE_1_WORLDS
from app.services.curriculum_data.grade2 import GRADE_2_WORLDS
from app.services.curriculum_data.grade3 import GRADE_3_WORLDS
from app.services.curriculum_data.grade4 import GRADE_4_WORLDS
from app.services.curriculum_data.grade5 import GRADE_5_WORLDS
from app.services.curriculum_data.grade6 import GRADE_6_WORLDS
from app.services.curriculum_data.grade7 import GRADE_7_WORLDS
from app.services.curriculum_data.grade8 import GRADE_8_WORLDS
from app.services.curriculum_data.grade9 import GRADE_9_WORLDS
from app.services.curriculum_data.grade10 import GRADE_10_WORLDS
from app.services.curriculum_data.grade11_12 import GRADE_11_12_WORLDS

ALL_CURRICULUM_WORLDS = (
    GRADE_1_WORLDS +
    GRADE_2_WORLDS +
    GRADE_3_WORLDS +
    GRADE_4_WORLDS +
    GRADE_5_WORLDS +
    GRADE_6_WORLDS +
    GRADE_7_WORLDS +
    GRADE_8_WORLDS +
    GRADE_9_WORLDS +
    GRADE_10_WORLDS +
    GRADE_11_12_WORLDS
)

STANDARD_BADGES = [
    {
        "code": "first_steps",
        "name": "First Steps",
        "description": "Completed your first mathematics mission.",
        "icon": "footprints",
        "category": "milestone",
        "criteria_description": "Complete 1 mission"
    },
    {
        "code": "algebra_explorer",
        "name": "Algebra Explorer",
        "description": "Mastered missions in the Algebra Kingdom.",
        "icon": "shield",
        "category": "algebra",
        "criteria_description": "Complete 3 Algebra Kingdom missions"
    },
    {
        "code": "accuracy_star",
        "name": "Accuracy Star",
        "description": "Demonstrated high precision by achieving 80% or higher accuracy.",
        "icon": "star",
        "category": "mastery",
        "criteria_description": "Score >= 80% accuracy in any mission"
    },
    {
        "code": "practice_champion",
        "name": "Practice Champion",
        "description": "Consistently practised across 5 study sessions.",
        "icon": "flame",
        "category": "streak",
        "criteria_description": "Complete missions across 5 distinct sessions"
    },
    {
        "code": "boss_victor",
        "name": "Boss Victor",
        "description": "Conquered a high-difficulty world Boss Challenge.",
        "icon": "trophy",
        "category": "boss",
        "criteria_description": "Successfully complete a Boss Challenge mission"
    }
]

def seed_curriculum_and_badges(db: Session):
    """
    Idempotently seeds complete grade-wise curriculum (Grades 1–12) and achievement badges
    aligned with the National Curriculum of Pakistan (NCP) 2022–23.
    
    Guarantees:
    - Zero duplicate records on repeated execution.
    - Preserves existing Grade 11 and 12 curriculum exactly.
    - Preserves student attempts, progress records, XP, and streak logs without destructive resets.
    """
    # 1. Seed Badges Idempotently
    for b_data in STANDARD_BADGES:
        existing_badge = db.query(Badge).filter(Badge.code == b_data["code"]).first()
        if not existing_badge:
            db.add(Badge(**b_data))
    db.flush()

    # 2. Seed Worlds, Topics, Missions, and Questions Idempotently
    for w_data in ALL_CURRICULUM_WORLDS:
        world = db.query(World).filter(
            World.title == w_data["title"],
            World.grade == w_data["grade"]
        ).first()

        if not world:
            world = World(
                title=w_data["title"],
                description=w_data["description"],
                grade=w_data["grade"],
                icon=w_data.get("icon", "compass"),
                theme_color=w_data.get("theme_color", "emerald"),
                display_order=w_data.get("display_order", 1),
                unlock_condition=w_data.get("unlock_condition", "grade_match"),
                is_active=True
            )
            db.add(world)
            db.flush()

        for t_data in w_data.get("topics", []):
            topic = db.query(Topic).filter(
                Topic.world_id == world.id,
                Topic.title == t_data["title"]
            ).first()

            if not topic:
                topic = Topic(
                    world_id=world.id,
                    title=t_data["title"],
                    description=t_data.get("description"),
                    learning_objectives=t_data.get("learning_objectives", []),
                    grade=t_data.get("grade", world.grade),
                    display_order=t_data.get("display_order", 1)
                )
                db.add(topic)
                db.flush()

            for m_data in t_data.get("missions", []):
                mission = db.query(Mission).filter(
                    Mission.topic_id == topic.id,
                    Mission.title == m_data["title"]
                ).first()

                unlock_cond = m_data.get("unlock_condition", "always")
                if unlock_cond.startswith("requires_mission:"):
                    target_title = unlock_cond.split(":", 1)[1]
                    if not target_title.isdigit():
                        req_m = db.query(Mission).filter(Mission.title == target_title).first()
                        if req_m:
                            unlock_cond = f"requires_mission:{req_m.id}"

                if not mission:
                    mission = Mission(
                        topic_id=topic.id,
                        title=m_data["title"],
                        instructions=m_data["instructions"],
                        category=m_data.get("category", "practice"),
                        difficulty=m_data.get("difficulty", "easy"),
                        question_count=len(m_data.get("questions", [])),
                        xp_reward=m_data.get("xp_reward", 20),
                        pass_percentage=m_data.get("pass_percentage", 60),
                        unlock_condition=unlock_cond,
                        display_order=m_data.get("display_order", 1),
                        is_boss=m_data.get("is_boss", False),
                        is_active=True
                    )
                    db.add(mission)
                    db.flush()
                else:
                    # Update unlock condition if needed to ensure correct ID linking
                    if unlock_cond != mission.unlock_condition:
                        mission.unlock_condition = unlock_cond
                        db.flush()

                for q_data in m_data.get("questions", []):
                    question = db.query(Question).filter(
                        Question.mission_id == mission.id,
                        Question.prompt == q_data["prompt"]
                    ).first()

                    if not question:
                        question = Question(
                            mission_id=mission.id,
                            prompt=q_data["prompt"],
                            question_type=q_data.get("question_type", "multiple_choice"),
                            options=q_data.get("options"),
                            correct_answer=q_data["correct_answer"],
                            explanation=q_data["explanation"],
                            step_by_step_solution=q_data.get("step_by_step_solution"),
                            common_mistakes=q_data.get("common_mistakes"),
                            difficulty=q_data.get("difficulty", "easy"),
                            tolerance=q_data.get("tolerance", 0.01),
                            display_order=q_data.get("display_order", 1),
                            is_active=True
                        )
                        db.add(question)

    db.commit()
