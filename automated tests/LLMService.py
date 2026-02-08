import os
from openai import OpenAI

class LLMService:
    def __init__(self):
        self.token = os.environ["GITHUB_TOKEN"]
        self.endpoint = "https://models.github.ai/inference"
        self.model = "openai/gpt-4.1"
        self.client = OpenAI(
            base_url=self.endpoint,
            api_key=self.token,
        )

    def chat(self, system_prompt, user_prompt, temperature=1.0, top_p=1.0):
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature,
            top_p=top_p,
            model=self.model
        )
        return response.choices[0].message.content

if __name__ == "__main__":
    llm = LLMService()
    answer = llm.chat(
        system_prompt="You are a helpful assistant.",
        user_prompt="What is the capital of France?"
    )
    print(answer)

