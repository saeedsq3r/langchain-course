from langchain_core.prompts import PromptTemplate


# template
template = PromptTemplate(
    template= """
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Explanation Lenght: {lenght_input}
    1. Mathematical Detials:
        - Include relevent mathematical equation if present in paper.
        - Explain the mathematical concepts using dimple, intuitive code snippets where applicable.
    2. Analogies:
        - Use relatable analogies to simplify complex ideas.
    If certain information is not availabel in the paper, respond with: "Insuffient information available" instead of guessing.
    Ensure the summary is clear, accurate, and aligned with the provided style and lenght.
""",
input_variables= ['paper_input','style_input', 'lenght_input'],
validate_template=True
)

template.save('template.json')