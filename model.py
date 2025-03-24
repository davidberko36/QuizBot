from sentence_transformers import SentenceTransformer, util

class AnswerVerifier:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name) # This loads the model

    # verifies the answer by comparing it to an already known answer and checking similarity
    def verify_answer(self, correct_answer:str, user_answer:str, threshold:float=0.8) -> bool:
        correct_embedding = self.model.encode(correct_answer)
        user_embedding = self.model.encode(user_answer)

        similarity_score = util.cos_sim(correct_embedding, user_embedding).item()

        return similarity_score >= threshold, similarity_score
