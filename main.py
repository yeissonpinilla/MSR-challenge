from api.gpt_manager import GPTManager
import pandas as pd

df = pd.read_csv("../output.csv")

def main():
    gpt = GPTManager()
    prompt = 'Test cases PRs can have different changes ["new", "maintenance", "refactor", "prettify"]. For new, maintenance and refactor, specify if is an unit test, integration test, e2e test, or api test. Your response should be in json format with keys: "test_type", "pr_id", "is_processed". The test_type should be one of the following: "unit", "integration", "e2e", "api". The is_processed should be a boolean value.'
    output = gpt.prompt(f"{prompt}: ")
    print("Result:", output)

if __name__ == "__main__":
    main()