# app/models/score.py

from dataclasses import dataclass

@dataclass
class ScoreResult:
    score: int
    notes: str