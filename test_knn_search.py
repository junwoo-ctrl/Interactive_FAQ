
from typing import List
import numpy as np
from sklearn.neighbors import NearestNeighbors

from transformers import AutoTokenizer, AutoModel
import torch


def get_configuration():
    vectors = np.load("./practice/embedding_vectors.npy")
    questions = [ele.replace("\n", "") for ele in open("./practice/question_sentences.txt", "r").readlines()]
    answers = [ele.replace("\n", "") for ele in open("./practice/answer_sentences.txt", "r").readlines()]
    return vectors, questions, answers


def train_knn(vectors, questions):
    knn = NearestNeighbors(
        n_neighbors=10,
        algorithm="kd_tree",
        metric="euclidean"
    ).fit(vectors)
    return knn


def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def get_embedded_vectors(query_sentences: List[str]):
    
    tokenizer = AutoTokenizer.from_pretrained("bespin-global/klue-sentence-roberta-base")
    model = AutoModel.from_pretrained("bespin-global/klue-sentence-roberta-base")
    
    encoded_input = tokenizer(query_sentences, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        model_output = model(**encoded_input)
    
    sentence_embeddings = mean_pooling(model_output, encoded_input["attention_mask"])
    return sentence_embeddings


if __name__ == "__main__":
    
    vectors, questions, answers = get_configuration()
    vector_pool = train_knn(vectors, questions)
    
    sample_sentence = ["이사를 가면 배송지를 어떻게 해야 하나요"]
    sample_vector = get_embedded_vectors(sample_sentence)
    
    distances, indices = vector_pool.kneighbors(
        sample_vector
    )
    similar_questions = [questions[idx] for idx in indices[0]]
    similar_answers = [answers[idx] for idx in indices[0]]

    print("query sentence: ",  sample_sentence)
    print("similar questions: ", similar_questions)
    print("similar_answers: ", similar_answers)
    
    
