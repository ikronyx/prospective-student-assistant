# ------------------------------------------------------------
# University Application Assistant – Streamlit App (Full‑Scale)
# Author: ChatGPT (OpenAI) | License: MIT
# ------------------------------------------------------------
"""
A one‑stop prompt generator that helps students craft high‑impact
questions for free ChatGPT, covering:
 • Personal / Statement of Purpose
 • SOP editing
 • Program search & comparison
 • Recommendation letters
 • Application timeline planning
 • Scholarship search
 • IELTS practice
 • Résumé review
 • Ready‑made prompt library
Design theme: black / dark‑grey UI with red action buttons.
"""

from datetime import date, timedelta
from textwrap import dedent

import streamlit as st

# --------------------------- Page Config ---------------------------
st.set_page_config(
    page_title="University Application Assistant",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --------------------------- Custom CSS ---------------------------
CUSTOM_CSS = """
<style>
    /* ----- Global colours ----- */
    html, body, [class*="stApp"], .block-container {
        background-color: #121212;
        color: #F0F0F0;
    }
    /* ----- Sidebar ----- */
    section[data-testid="stSidebar"] > div:first-child {
        background-color: #1E1E1E;
    }
    /* ----- Headers ----- */
    h1, h2, h3, h4 { color: #E0E0E0; }
    /* ----- Buttons ----- */
    div.stButton > button {
        background-color: #B80000;
        color: #FFFFFF;
        border: 1px solid #B80000;
        border-radius: 6px;
        padding: 0.4rem 1rem;
        transition: 0.2s ease;
    }
    div.stButton > button:hover {
        background-color: #E50914;
        border-color: #E50914;
        color: #FFFFFF;
    }
    div.stDownloadButton > button {
        background-color: #333333 !important;
        color: #FFFFFF !important;
        border-radius: 6px !important;
    }
    div.stDownloadButton > button:hover {
        background-color: #444444 !important;
        color: #FFFFFF !important;
    }
    /* ----- Code blocks ----- */
    pre code {
        background-color: #262626;
        color: #F8F8F2;
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --------------------------- Helper Functions ---------------------------

def personal_statement_prompt(name: str, country: str, degree: str, field: str,
                              background: str, passion: str, goals: str) -> str:
    return dedent(f"""
    Write a personal statement for a {degree} program in {field}. I am {name} from {country}. 
    My background is: {background}.
    I am passionate about {passion}.
    My future goals are: {goals}.
    Make the tone academic, ambitious, and authentic.
    """)

def edit_sop_prompt(draft: str) -> str:
    return dedent(f"""
    Improve the following Statement of Purpose to make it more concise, 
    goal‑oriented, and engaging while retaining my voice:
    ---
    {draft}
    ---
    """)

def program_search_prompt(field: str, degree: str, gpa: float, countries: str,
                           constraints: str) -> str:
    return dedent(f"""
    List top‑ranked English‑language {degree} programs in {field} located in {countries}. 
    I have a GPA of {gpa}. {constraints}
    Include tuition (local & international) and scholarship information.
    """)

def reco_letter_prompt(relationship: str, achievements: str, field: str, degree: str) -> str:
    return dedent(f"""
    Draft a recommendation letter for a student applying to a {degree} in {field}. 
    The recommender is their {relationship}. Highlight these achievements: {achievements}.
    Keep the tone professional and supportive.
    """)

def timeline_prompt(intake: str, tests: str) -> str:
    return dedent(f"""
    Create a 6‑month application plan for the {intake} intake. Include {tests}, 
    SOP drafting, recommendation letters, transcript requests, and submission deadlines.
    """)

def scholarship_prompt(field: str, destination: str, level: str, nationality: str) -> str:
    return dedent(f"""
    List international scholarships for {nationality} students applying to {level} programs in {field} in {destination}. 
    Include award amount and eligibility criteria.
    """)

def ielts_prompt(task: str) -> str:
    return dedent(f"""
    Generate an IELTS Academic {task} practice question with a band‑9 sample answer. 
    Then provide feedback for common mistakes that would reduce the score to band 6.
    """)

def resume_review_prompt(text: str, field: str) -> str:
    return dedent(f"""
    Review my résumé below for an application to a {field} program. 
    Make it more academic and achievement‑focused while keeping it concise:
    ---
    {text}
    ---
    """)

def prompt_library() -> str:
    """Static markdown for the prompt library."""
    return dedent("""
    ## 📚 Quick‑Copy Prompt Library

    **Personal Statement / SOP**
    ```
    Write a personal statement for a Master’s in Computer Science. I am a Sri Lankan student with a BSc in IT, GPA 3.7, and two years' software‑engineering experience. Emphasize my AI interests.
    ```

    **SOP Editing**
    ```
    Improve the following SOP to strengthen clarity and flow while retaining my voice: <paste SOP>
    ```

    **Program Finder**
    ```
    List top‑ranked MSc programs in Data Science in Canada or Germany for international students with GPA 3.5+. Include tuition and scholarship info.
    ```

    **Recommendation Letter**
    ```
    Draft a recommendation letter for a student applying to an MSc in Finance. Recommender: internship supervisor from ABC Bank.
    ```

    **Timeline Planner**
    ```
    Create a 6‑month plan for applying to UK universities for the Fall 2026 intake. Include IELTS, SOP, LoR, and finance prep.
    ```

    **Scholarship Search**
    ```
    List full‑tuition scholarships for Asian students applying to Public Policy degrees in Europe.
    ```

    **IELTS Practice**
    ```
    Give me an IELTS Writing Task 2 question on climate change plus a band‑9 sample essay.
    ```

    **Résumé Review**
    ```
    Make this résumé more academic and achievement‑oriented for an MSc in Biomedical Engineering: <paste résumé>
    ```
    """)

# --------------------------- Sidebar Navigation ---------------------------
PAGES = [
    "Personal Statement",
    "Edit SOP",
    "Program Finder",
    "Recommendation Letter",
    "Timeline Planner",
    "Scholarship Search",
    "IELTS Practice",
    "Résumé Review",
    "Prompt Library",
]

selection = st.sidebar.radio("Select a module", PAGES)

# --------------------------- Main Content ---------------------------

st.title("🎓 University Application Assistant")

if selection == "Personal Statement":
    st.subheader("Generate a Personal Statement Prompt")
    name = st.text_input("Your Name")
    country = st.text_input("Your Country of Citizenship")
    degree = st.selectbox("Target Degree", ["Bachelor's", "Master's", "PhD", "MBA"])
    field = st.text_input("Field of Study (e.g., Data Science)")
    background = st.text_area("Academic & Work Background")
    passion = st.text_area("Why are you passionate about this field?")
    goals = st.text_area("Future Career or Academic Goals")

    if st.button("Generate Prompt"):
        prompt = personal_statement_prompt(name, country, degree, field, background, passion, goals)
        st.success("Prompt generated! Copy & use in ChatGPT (Free).")
        st.code(prompt, language="markdown")
        st.download_button("📥 Download Prompt as .txt", prompt, file_name="personal_statement_prompt.txt")

elif selection == "Edit SOP":
    st.subheader("SOP Editing Prompt")
    draft = st.text_area("Paste your existing SOP draft here")
    if st.button("Generate Edit Prompt"):
        prompt = edit_sop_prompt(draft)
        st.success("Prompt generated! Copy & use in ChatGPT (Free).")
        st.code(prompt, language="markdown")
        st.download_button("📥 Download Prompt as .txt", prompt, file_name="edit_sop_prompt.txt")

elif selection == "Program Finder":
    st.subheader("Program Search Prompt")
    field = st.text_input("Field of Study")
    degree = st.selectbox("Degree Level", ["Bachelor's", "Master's", "PhD", "MBA"])
    gpa = st.number_input("Your GPA (on 4.0 scale)", min_value=0.0, max_value=4.0, value=3.0, step=0.1)
    countries = st.text_input("Preferred Countries (comma‑separated)")
    constraints = st.text_area("Other Constraints (e.g., budget, scholarships, duration)")
    if st.button("Generate Prompt"):
        prompt = program_search_prompt(field, degree, gpa, countries, constraints)
        st.success("Prompt generated! Copy & use in ChatGPT (Free).")
        st.code(prompt, language="markdown")
        st.download_button("📥 Download Prompt as .txt", prompt, file_name="program_search_prompt.txt")

elif selection == "Recommendation Letter":
    st.subheader("Recommendation Letter Draft Prompt")
    relationship = st.text_input("Your relationship to recommender (e.g., Professor, Manager)")
    achievements = st.text_area("Key Achievements & Qualities to Highlight")
    field = st.text_input("Field of Study (e.g., Finance)")
    degree = st.selectbox("Degree Level", ["Bachelor's", "Master's", "PhD", "MBA"])
    if st.button("Generate Prompt"):
        prompt = reco_letter_prompt(relationship, achievements, field, degree)
        st.success("Prompt generated! Copy & use in ChatGPT (Free).")
        st.code(prompt, language="markdown")
        st.download_button("📥 Download Prompt as .txt", prompt, file_name="reco_letter_prompt.txt")

elif selection == "Timeline Planner":
    st.subheader("Application Timeline Prompt")
    intake = st.text_input("Target Intake (e.g., Fall 2026)")
    tests = st.text_input("Standardized Tests (e.g., IELTS, GRE)")
    if st.button("Generate Prompt"):
        prompt = timeline_prompt(intake, tests)
        st.success("Prompt generated! Copy & use in ChatGPT (Free).")
        st.code(prompt, language="markdown")
        st.download_button("📥 Download Prompt as .txt", prompt, file_name="timeline_prompt.txt")

elif selection == "Scholarship Search":
    st.subheader("Scholarship Search Prompt")
    field = st.text_input("Field of Study (e.g., Public Health)")
    destination = st.text_input("Destination Country/Region (e.g., Europe)")
    level = st.selectbox("Program Level", ["Bachelor's", "Master's", "PhD", "MBA"])
    nationality = st.text_input("Your Nationality (e.g., Sri Lankan)")
    if st.button("Generate Prompt"):
        prompt = scholarship_prompt(field, destination, level, nationality)
        st.success("Prompt generated! Copy & use in ChatGPT (Free).")
        st.code(prompt, language="markdown")
        st.download_button("📥 Download Prompt as .txt", prompt, file_name="scholarship_prompt.txt")

elif selection == "IELTS Practice":
    st.subheader("IELTS Practice Prompt")
    task = st.selectbox("Select Task", ["Writing Task 1", "Writing Task 2", "Speaking Part 2 Cue Card"])
    if st.button("Generate Prompt"):
        prompt = ielts_prompt(task)
        st.success("Prompt generated! Copy & use in ChatGPT (Free).")
        st.code(prompt, language="markdown")
        st.download_button("📥 Download Prompt as .txt", prompt, file_name="ielts_prompt.txt")

elif selection == "Résumé Review":
    st.subheader("Résumé Review Prompt")
    resume_text = st.text_area("Paste your résumé/CV text here")
    field = st.text_input("Field of Study (e.g., Biomedical Engineering)")
    if st.button("Generate Prompt"):
        prompt = resume_review_prompt(resume_text, field)
        st.success("Prompt generated! Copy & use in ChatGPT (Free).")
        st.code(prompt, language="markdown")
        st.download_button("📥 Download Prompt as .txt", prompt, file_name="resume_review_prompt.txt")

elif selection == "Prompt Library":
    st.subheader("Quick‑Copy Prompt Library")
    st.markdown(prompt_library())

# --------------------------- Footer ---------------------------

st.markdown("""
---
© 2025 • University Application Assistant. Prompt engineering powered by ChatGPT (free tier).
""")
