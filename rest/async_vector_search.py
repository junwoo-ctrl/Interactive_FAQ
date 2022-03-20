from fastapi import APIRouter

from rest.knn_pool import KnnPool

router = APIRouter()
knn_pool = KnnPool()


@router.get("/search_knn/async_vector_search", tags=["knn", "brute_force"])
async def search_knn_vectors(requested_sentence: str):
    ret = knn_pool.search_similar_questions([requested_sentence])
    return {
        "query_result": ret,
    }
