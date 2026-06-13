import os
from google import genai

def get_daily_content():
    client = genai.Client()
    
    prompt = (
        "Write a clever daily joke or pun specifically about DevOps engineering, CI/CD, "
        "Kubernetes, or cloud infrastructure. Keep it light and funny for a beginning engineer. "
        "Directly below the joke, provide a unique 'DevOps Skill of the Day' to focus on "
        "(e.g., a specific advanced Linux tool, an infrastructure-as-code optimization, a Git strategy, "
        "or a monitoring pattern) along with a 2-3 sentence explanation of its real-world value."
    )
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    return response.text

if __name__ == "__main__":
    print("--- Fetching Daily DevOps Briefing ---")
    daily_briefing = get_daily_content()
    
    # This prints the result directly into your GitHub Actions execution logs
    print(daily_briefing)
    print("---------------------------------------")