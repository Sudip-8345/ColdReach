# ColdReach
ColdReach is a dynamic cold email generator that creates tailored outreach messages using job descriptions and portfolio links. Ideal for job seekers, freelancers, and networkers to craft professional, personalized emails in seconds.
![ColdReach Screenshot](https://github.com/Sudip-8345/ColdReach/blob/00c87f6663cf45af6f9a9fe01522968225bd783d/Image/Screenshot%20(11).png?raw=true)
## Architechture Diagram
![ColdReach Screenshot](https://github.com/codebasics/project-genai-cold-email-generator/blob/6dfa167d62d61eaf407046cd3d3634ecc0a9d4f8/imgs/architecture.png?raw=true)
## Set up
1. To get started we first need to get an API_KEY from here: ![https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens). Inside app/.env update the value of GROQ_API_KEY with the API_KEY you created.
2. To get started, first install the dependencies using:

 pip install -r requirements.txt

3. Run the streamlit app:

 streamlit run app/main.py
