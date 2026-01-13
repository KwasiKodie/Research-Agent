from dotenv import load_dotenv
import os
import warnings
from crewai import Agent, Task, Crew
from IPython.display import display, Markdown

warnings.filterwarnings("ignore")
load_dotenv()

def main():
    planner = Agent(
        role="Content Planner",
        goal="Plan engaging and factually accurate content on {topic}",
        backstory=("You're working on planning a blog article "
                   "about the topic: {topic}. "
                   "You collect information that helps the audience learn something "
                   "and make informed decisions. "
                   "Your work is the basis for the Content Writer to write an article."),
        allow_delegation=False,
        verbose=True
    )

    writer = Agent(
        role="Content Writer",
        goal="Write insightful and factually accurate opinion piece about the topic: {topic}",
        backstory=("You're working on writing a new opinion piece about the topic: {topic}. "
                   "You base your writing on the Content Planner's outline and context. "
                   "You provide objective and impartial insights, and clearly label opinions."),
        allow_delegation=False,
        verbose=True
    )

    editor = Agent(
        role="Editor",
        goal="Edit a given blog post to align with the writing style of the organization.",
        backstory=("You are an editor who receives a blog post from the Content Writer. "
                   "You ensure journalistic best practices, balanced viewpoints, and tone."),
        allow_delegation=False,   # <-- boolean
        verbose=True
    )

    plan = Task(
        description=(
            "1. Prioritize the latest trends, key players, and noteworthy news on {topic}.\n"
            "2. Identify the target audience, considering their interests and pain points.\n"
            "3. Develop a detailed content outline including an introduction, key points, and a call to action.\n"
            "4. Include SEO keywords and relevant data or sources."
        ),
        expected_output=("A comprehensive content plan document with an outline, audience analysis, "
                         "SEO keywords, and resources."),
        agent=planner
    )

    write = Task(
        description=(
            "1. Use the content plan to craft a compelling blog post on {topic}.\n"
            "2. Incorporate SEO keywords naturally.\n"
            "3. Use engaging section titles.\n"
            "4. Structure: intro, insightful body, summarizing conclusion.\n"
            "5. Proofread for grammar and alignment with the brand voice."
        ),
        expected_output=("A well-written blog post in markdown format, ready for publication; "
                         "each section should have 2 or 3 paragraphs."),
        agent=writer
    )

    edit = Task(  # <-- define before Crew
        description="Proofread the blog post for grammar and alignment with the brand's voice.",
        expected_output=("A polished blog post in markdown format, ready for publication; "
                         "each section should have 2 or 3 paragraphs."),
        agent=editor
    )

    crew = Crew(
        agents=[planner, writer, editor],
        tasks=[plan, write, edit],
        verbose=2
    )

    result = crew.kickoff(inputs={"topic": "Artificial Intelligence In Cyber Security"})

    display(Markdown(result))  # or print(result) if not in a notebook

if __name__ == "__main__":
    main()
