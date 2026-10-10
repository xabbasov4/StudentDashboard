from typing import List, Dict, Any, Tuple
from config import GRADE_BOUNDARIES

def calculate_grade(score: float) -> str:
    """Tələbənin topladığı bala görə Grade hərfini təyin edir."""
    if score >= GRADE_BOUNDARIES['A']:
        return 'A'
    elif score >= GRADE_BOUNDARIES['B']:
        return 'B'
    elif score >= GRADE_BOUNDARIES['C']:
        return 'C'
    elif score >= GRADE_BOUNDARIES['D']:
        return 'D'
    else:
        return 'F'

def calculate_statistics(students: List[Tuple[int, str, float]]) -> Dict[str, Any]:
    """Tələbə siyahısına əsasən statistik göstəriciləri hesablayır."""
    if not students:
        return {
            "total_students": 0,
            "average_score": 0.0,
            "highest_score": 0.0,
            "lowest_score": 0.0
        }

    scores = [student[2] for student in students]
    
    return {
        "total_students": len(scores),
        "average_score": round(sum(scores) / len(scores), 1),
        "highest_score": max(scores),
        "lowest_score": min(scores)
    }