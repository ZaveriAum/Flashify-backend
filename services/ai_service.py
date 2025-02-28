from openai import OpenAI
from config import Config
from decorators import AuthDecorator
from services.flashcard_service import FlashCardService
from utils.error import AppError
import json
import PyPDF2
from docx import Document
from pptx import Presentation
from io import BytesIO

client = OpenAI(api_key=Config.OPENAI_KEY)

class AIService:

    @staticmethod
    @AuthDecorator.jwt_auth
    def generate_flashcards(text=None, file=None):
        try:
            if file:
                file_obj = file.get('file')
                
                if not file_obj:
                    raise ValueError("No file provided.")

                file_stream = BytesIO(file_obj.read())
                filename = file_obj.filename.lower()

                if filename.endswith('.pdf'):
                    text = AIService.extract_from_pdf(file_stream)
                elif filename.endswith('.docx'):
                    text = AIService.extract_from_docx(file_stream)
                elif filename.endswith('.pptx'):
                    text = AIService.extract_from_pptx(file_stream)
                elif filename.endswith('.txt'):
                    text = file_stream.getvalue().decode('utf-8')
                else:
                    raise ValueError("Unsupported file type")
            
            if not text:
                raise ValueError("Either topic, text, or file must be provided.")
            
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

            prompt=f"{base}\n{text}"
            
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                { "role": "user", "content": prompt },
                ],
                temperature=0
            );
            
            flashcards_json = response.choices[0].message.content.strip("```json\n").strip("```")
            return json.loads(flashcards_json)
        except Exception as e:
            print(e)
            raise AppError(getattr(e, 'message', 'Unknown Error'), getattr(e, 'statusCode', 400))

    @staticmethod
    @AuthDecorator.jwt_auth
    def interact_with_flashcard(folder_id, prompt=None):
        try:
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
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknown Error'), getattr(e, 'statusCode', 400))
    
    # File extraction methods
    @staticmethod
    def extract_from_pdf(file_stream):
        reader = PyPDF2.PdfReader(file_stream)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

    @staticmethod
    def extract_from_docx(file_stream):
        doc = Document(file_stream)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text

    @staticmethod
    def extract_from_pptx(file_stream):
        prs = Presentation(file_stream)
        text = ""
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    text += shape.text + "\n"
        return text