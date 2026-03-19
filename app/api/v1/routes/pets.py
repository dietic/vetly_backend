from fastapi import APIRouter, Depends


router = APIRouter()


@router.get("/")
def get_my_pets(db: Session = Depends(get_db), current_owner_id: int):
