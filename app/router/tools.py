from fastapi import APIRouter
from app.utils import file

router = APIRouter()


@router.post("/tools/cleartmp")
async def clear_temp_folder():
    if file.clear_temp_folder():
        return 200, {"message": "Temp folder cleared"}
    else:
        return 500, {"message": "Failed to clear temp folder"}
