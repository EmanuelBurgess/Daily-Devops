import os
from google import genai

def get_daily_content():
    client = genai.Client()
    
    prompt = (
        "You are a witty, elite DevOps compiler. Write a daily newsletter briefing for a senior infrastructure engineer "
        "using a clean layout and vibrant emojis. The response must follow this exact markdown structure:\n\n"
        "## ☕ Good Morning, Engineer!\n"
        "[Insert a clever, high-context DevOps joke or pun about CI/CD, Kubernetes, Docker, or cloud infrastructure here. Keep it sharp.]\n\n"
        "## 🛠️ Skill of the Day\n"
        "**[Skill Name]**\n"
        "[Provide a unique DevOps focus item—like an advanced Linux tool, infrastructure-as-code optimization, Git strategy, "
        "or monitoring pattern—followed by a 2-3 sentence practical explanation of its real-world value.]\n\n"
        "## 💡 Inspirational Tech Quote\n"
        "*[Insert a thought-provoking technology or engineering quote here]*\n\n"
        "## 📦 Meme of the Day\n"
        "![DevOps Meme](https://raw.githubusercontent.com/devops-memes/assets/main/meme.png)\n"
        "*(Note: Provide a real, publicly accessible image URL for a software engineering or DevOps comic, such as an xkcd, dilbert, or developer community asset link that fits the context)*"
    )
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    return response.text

if __name__ == "__main__":
    daily_briefing = get_daily_content()
    
    with open("briefing.md", "w", encoding="utf-8") as f:
        f.write(daily_briefing)
        
    print("Briefing written to briefing.md successfully.")