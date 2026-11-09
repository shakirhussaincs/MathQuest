from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.curriculum import World, Topic, Mission, MissionCategory, DifficultyLevel
from app.services.auth_service import get_current_user, require_admin

router = APIRouter(prefix="/worlds", tags=["Mathematics Worlds & Curriculum"])

# Admin request schemas
class CreateWorldRequest(BaseModel):
    title: str = Field(..., min_length=2, max_length=100)
    description: str = Field(..., min_length=5, max_length=500)
    grade: int = Field(..., ge=1, le=12)
    icon: Optional[str] = "compass"
    theme_color: Optional[str] = "emerald"
    display_order: Optional[int] = 1

class CreateTopicRequest(BaseModel):
    title: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = None
    learning_objectives: Optional[List[str]] = []
    display_order: Optional[int] = 1

class CreateMissionRequest(BaseModel):
    title: str = Field(..., min_length=2, max_length=150)
    instructions: str
    category: Optional[MissionCategory] = MissionCategory.PRACTICE
    difficulty: Optional[DifficultyLevel] = DifficultyLevel.EASY
    question_count: Optional[int] = 5
    xp_reward: Optional[int] = 20
    is_boss: Optional[bool] = False
    display_order: Optional[int] = 1

@router.get("/")
def list_worlds(
    grade: Optional[int] = Query(None, ge=1, le=12),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Returns mathematics worlds filtered by student's grade or query parameter (FR-07, FR-08).
    - Grade 11: Algebra Kingdom, Trigonometry Island
    - Grade 12: Calculus Tower, Statistics City
    """
    target_grade = grade or current_user.grade or 11
    worlds = db.query(World)\
               .filter(World.grade == target_grade, World.is_active == True)\
               .order_by(World.display_order)\
               .all()
    
    result = []
    for w in worlds:
        topics = db.query(Topic).filter(Topic.world_id == w.id).order_by(Topic.display_order).all()
        missions_count = db.query(Mission)\
                           .join(Topic, Mission.topic_id == Topic.id)\
                           .filter(Topic.world_id == w.id, Mission.is_active == True)\
                           .count()
        result.append({
            "id": w.id,
            "title": w.title,
            "description": w.description,
            "grade": w.grade,
            "icon": w.icon,
            "theme_color": w.theme_color,
            "display_order": w.display_order,
            "topics_count": len(topics),
            "missions_count": missions_count,
            "topics_preview": [t.title for t in topics]
        })
    return result

@router.get("/{world_id}")
def get_world_details(
    world_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Returns the comprehensive realm view: topics, descriptions, learning objectives,
    and mission categorisation (Concept Exploration, Practice, Boss Challenge).
    """
    world = db.query(World).filter(World.id == world_id, World.is_active == True).first()
    if not world:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="World not found.")

    topics = db.query(Topic).filter(Topic.world_id == world.id).order_by(Topic.display_order).all()
    
    topics_data = []
    for t in topics:
        missions = db.query(Mission)\
                     .filter(Mission.topic_id == t.id, Mission.is_active == True)\
                     .order_by(Mission.display_order)\
                     .all()
        topics_data.append({
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "learning_objectives": t.learning_objectives or [],
            "missions": [
                {
                    "id": m.id,
                    "title": m.title,
                    "instructions": m.instructions,
                    "category": m.category,
                    "difficulty": m.difficulty,
                    "question_count": m.question_count,
                    "xp_reward": m.xp_reward,
                    "is_boss": m.is_boss
                }
                for m in missions
            ]
        })

    return {
        "id": world.id,
        "title": world.title,
        "description": world.description,
        "grade": world.grade,
        "icon": world.icon,
        "theme_color": world.theme_color,
        "topics": topics_data
    }

# ----------------- Administrator Content Management Endpoints -----------------

@router.post("/", status_code=status.HTTP_201_CREATED)
def admin_create_world(
    world_in: CreateWorldRequest,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):
    """FR-58: Administrator creates a new learning world."""
    world = World(
        title=world_in.title,
        description=world_in.description,
        grade=world_in.grade,
        icon=world_in.icon or "compass",
        theme_color=world_in.theme_color or "emerald",
        display_order=world_in.display_order or 1,
        is_active=True
    )
    db.add(world)
    db.commit()
    db.refresh(world)
    return {"message": "World created successfully.", "world": {"id": world.id, "title": world.title}}

@router.post("/{world_id}/topics", status_code=status.HTTP_201_CREATED)
def admin_create_topic(
    world_id: int,
    topic_in: CreateTopicRequest,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):
    """FR-58: Administrator adds a curriculum topic to a world."""
    world = db.query(World).filter(World.id == world_id).first()
    if not world:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="World not found.")

    topic = Topic(
        world_id=world.id,
        title=topic_in.title,
        description=topic_in.description,
        learning_objectives=topic_in.learning_objectives,
        grade=world.grade,
        display_order=topic_in.display_order or 1
    )
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return {"message": "Topic added successfully.", "topic": {"id": topic.id, "title": topic.title}}

@router.post("/topics/{topic_id}/missions", status_code=status.HTTP_201_CREATED)
def admin_create_mission(
    topic_id: int,
    mission_in: CreateMissionRequest,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):
    """FR-58: Administrator adds a mission to a topic."""
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found.")

    mission = Mission(
        topic_id=topic.id,
        title=mission_in.title,
        instructions=mission_in.instructions,
        category=mission_in.category.value if mission_in.category else MissionCategory.PRACTICE.value,
        difficulty=mission_in.difficulty.value if mission_in.difficulty else DifficultyLevel.EASY.value,
        question_count=mission_in.question_count or 5,
        xp_reward=mission_in.xp_reward or 20,
        is_boss=mission_in.is_boss or False,
        display_order=mission_in.display_order or 1,
        is_active=True
    )
    db.add(mission)
    db.commit()
    db.refresh(mission)
    return {"message": "Mission added successfully.", "mission": {"id": mission.id, "title": mission.title}}
