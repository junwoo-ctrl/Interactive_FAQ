import torch
import numpy as np

from sklearn.neighbors import NearestNeighbors
from transformers import AutoTokenizer, AutoModel


class KnnPool:
    
    def __init__(self):
        vectors = np.load("./practice/embedding_vectors.npy")
        self.questions = [ele.replace("\n", "") for ele in open("./practice/question_sentences.txt", "r").readlines()]
        self.answers = [ele.replace("\n", "") for ele in open("./practice/answer_sentences.txt", "r").readlines()]
        
        self.embedding_model = AutoModel.from_pretrained("bespin-global/klue-sentence-roberta-base")
        self.tokenizer = AutoTokenizer.from_pretrained("bespin-global/klue-sentence-roberta-base")
        self.vector_pool = NearestNeighbors(
            n_neighbors=10,
            algorithm="kd_tree",
            metric="euclidean",
        ).fit(vectors)
        
    def mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0] #First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    
    def get_embedded_vectors(self, query_sentences):
        
        encoded_input = self.tokenizer(query_sentences, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            model_output = self.embedding_model(**encoded_input)
        
        sentence_embeddings = self.mean_pooling(model_output, encoded_input["attention_mask"])
        return sentence_embeddings

    def search_similar_questions(self, sentence):
        
        vector = self.get_embedded_vectors(sentence)
        distances, indices = self.vector_pool.kneighbors(vector)
        similar_scores = distances[0].tolist()
        similar_points = indices[0].tolist()
        
        ret = list()
        for idx, ele in enumerate(similar_points):
            rec = {
                "question": self.questions[ele],
                "answer": self.answers[ele],
                "score": similar_scores[idx],
            }
            ret.append(rec)
        return ret
