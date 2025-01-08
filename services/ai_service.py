from openai import OpenAI
from config import Config
from decorators.AuthDecorator import jwt_auth
from services.flashcard_service import FlashCardService
import json

client = OpenAI(api_key=Config.OPENAI_KEY)

class AIService:

    @staticmethod
    @jwt_auth
    def generate_flashcards(topic=None, text=None):
        base = """
            You are an advanced flashcard creator specializing in graduate and post-graduate level content. Your task is to generate 10 high-quality flashcards on the given topic. Follow these guidelines:

            1. Create exactly 10 flashcards.
            2. Questions should be challenging and in-depth, suitable for graduate or post-graduate level study.
            3. Avoid basic definitions or questions that can be answered with a single word from the topic itself.
            4. Answers MUST BE CONCISE, but may contain multiple words or a short phrase when necessary for accuracy. Answers MUST NOT BE MORE THAN 5 WORDS LONG.
            5. Ensure all answers are unique with no repetitions.
            6. Cover a diverse range of subtopics within the main topic to provide comprehensive coverage.
            7. Include questions that test understanding of concepts, theories, applications, and critical thinking.
            8. Avoid questions that can be answered with a simple "yes" or "no".

            Return the flashcards in the following JSON format:

            {
                "flashcards": [
                {
                    "question": "Detailed, challenging question related to the topic",
                    "answer": "Concise, accurate answer (can be a short phrase if needed)"
                }
                ]
            }

            Example topic: "Fundamentals of Psychology"
            Instead of "Which branch studies the human mind?", ask something like:
            Question: "What cognitive bias describes the tendency to search for or interpret information in a way that confirms one's preexisting beliefs?",
            Answer: "Confirmation bias"
        """
        if topic:
            prompt=f"{base}\n{topic}"
        elif text:
            prompt=f"{base}\n{text}"
        else:
            raise ValueError("Either topic or text must be provided.")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
            { "role": "user", "content": prompt },
            ],
            temperature=0
        );
        flashcards_json = response.choices[0].message.content.strip()
        print(json.loads(flashcards_json))
        return json.loads(flashcards_json)

    @staticmethod
    def interact_with_flashcard(folder_id, prompt=None):
        flashcards = FlashCardService.get_flashcards(folder_id)
        flashcards = [(flashcard["question"], flashcard["answer"]) for flashcard in flashcards]
        if not prompt:
            raise ValueError("Prompt empty.")
        else:
            prompt = f"""
            You role is off a profressor of well know Ivy League University\
            You are a chat bot nothing else\
            You will be provided with flashcards and your privous conversations with the user\
            Here are the flashcards
            {flashcards}
            Here is the context
            {prompt}
            Your task is to answer the question asked in the prompt or to do the task asked in the prompt\
            Never ever include flashcard questions, id, answer in the response you give
            The flash cards above are the context for the question asked below. You are tasked to answer the question in a way that is 
            understandable. Be very detailed and don't make any assumptions. What ever you are asked please be as thorough as possible.
            Don't repeat any flashcards. Just answer the question which is going to be asked.
            """
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
            { "role": "user", "content": prompt },
            ],
            temperature=0,
        );
        return response.choices[0].message.content
        