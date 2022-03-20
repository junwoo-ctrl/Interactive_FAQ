import os
from clize import run
from typing import List

from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np


def get_faq_sentences():
    
    practice_path  = './practice'    
    filelist = [ele for ele in os.listdir(practice_path) if 'txt' in ele]
    
    question_table = list()
    answer_table = list()
    for filename in filelist:
        filepath = os.path.join(practice_path, filename)
        
        corpus_list = open(filepath, 'r').readlines()
        corpus_list = [ele.replace("\n", "") for ele in corpus_list]
        
        for idx, corpus in enumerate(corpus_list):
            if idx % 2 == 0:
                continue
            
            temp_raws = corpus.split("답변")
            question_table.append(temp_raws[0])
            answer_table.append(temp_raws[1])
    return {'questions': question_table, 'answers': answer_table}


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
    
    faq_sentences = get_faq_sentences()
    
    question_sentences = faq_sentences["questions"]
    answer_sentences = faq_sentences["answers"]
    embedding_sentences = get_embedded_vectors(question_sentences)
    
    
    with open("./practice/question_sentences.txt", "w") as f:
        for question in question_sentences:
            f.write("%s\n" % question)
            
    with open("./practice/answer_sentences.txt", "w") as f:
        for answer in answer_sentences:
            f.write("%s\n" % answer)
            
    np.save("./practice/embedding_vectors", embedding_sentences)
