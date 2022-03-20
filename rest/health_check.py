from fastapi import APIRouter, Response


router = APIRouter()


@router.get("/search_knn" + "/monitor/health_check", tags=["healthcheck"])
async def health_check():
    return Response(status_code=200)
