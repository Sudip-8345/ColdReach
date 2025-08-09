import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatOpenAI(
            openai_api_base="https://router.huggingface.co/v1",
            openai_api_key=os.environ["HF_TOKEN"],
            model="openai/gpt-oss-120b:cerebras",
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
        You are an expert at writing professional cold emails for job outreach.
        Write a concise, personalized cold email to a hiring manager.

        Inputs:
        - Job Description: {job_description}
        - Portfolio/Project Links: {link_list}

        Requirements for the email:
        1. Start with a polite greeting and introduction of myself.
        2. Mention how my skills and experience align with the {job_description}.
        3. Reference my relevant projects or portfolio using the {link_list}.
        4. Keep the tone professional yet warm and confident.
        5. End with a clear call to action (e.g., request to connect, share resume, or schedule a meeting).
        6. Keep it within 150–200 words.
        7. no preamble

        """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("HF_TOKEN"))