from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CommentCreate(BaseModel):
    """Схема для создания комментария."""

    user_name: str = Field(..., min_length=1, max_length=255)
    content: str = Field(..., min_length=1)


class CommentSchema(BaseModel):
    """Схема комментария из БД."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    task_id: int
    user_name: str
    content: str
    created_at: datetime
    updated_at: datetime