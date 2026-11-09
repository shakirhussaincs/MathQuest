from datetime import datetime
from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field, ConfigDict

class QuestionPublic(BaseModel):
    id: int
    prompt: str
    question_type: str  # "multiple_choice" or "numeric"
    options: Optional[List[str]] = None
    difficulty: str
    display_order: int

    model_config = ConfigDict(from_attributes=True)

class MissionDetailResponse(BaseModel):
    id: int
    topic_id: int
    topic_title: str
    world_id: int
    world_title: str
    title: str
    instructions: str
    category: str
    difficulty: str
    question_count: int
    xp_reward: int
    pass_percentage: int
    is_boss: bool
    unlock_condition: str
    is_unlocked: bool
    unlock_explanation: Optional[str] = None
    questions: List[QuestionPublic]

    model_config = ConfigDict(from_attributes=True)

class SubmitAnswerRequest(BaseModel):
    question_id: int
    submitted_answer: str = Field(..., min_length=1, max_length=200)

class RelatedPracticeRecommendation(BaseModel):
    mission_id: int
    title: str
    topic_title: str
    reason: str

class SubmitAnswerResponse(BaseModel):
    is_correct: bool
    submitted_answer: str
    correct_answer: str
    explanation: str
    step_by_step_solution: List[str] = []
    mistake_analysis: Optional[str] = None
    related_practice: Optional[RelatedPracticeRecommendation] = None
    xp_awarded: int
    total_xp: int
    message: str

class CompleteMissionResponse(BaseModel):
    mission_id: int
    mission_title: str
    score: int
    total_questions: int
    accuracy_percentage: float
    is_passed: bool
    bonus_xp_awarded: int
    total_mission_xp: int
    new_total_xp: int
    new_level: int
    new_rank_title: str
    badges_unlocked: List[dict]
    unlocked_missions: List[str] = []
    message: str
