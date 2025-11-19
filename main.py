from api.gpt_manager import GPTManager
import pandas as pd
import json

df = pd.read_csv("../output.csv")

def main():
    gpt = GPTManager()
    prompt = 'Test cases PRs can have different changes ["new", "maintenance", "refactor", "prettify"]. You will analyze patches. For new, maintenance and refactor, specify if is an unit test, integration test, e2e test, or api test. Your response should be in json format with keys: "id", "test_type", "pr_id", "is_processed", "test_case", "is_valid_patch". Test case refers to if is new, maintenance, refactor, or prettify. The test_type should be one of the following: "unit", "integration", "e2e", "api". The is_processed should be a boolean value. Only reteurn json format, do not add any text nor explanation. Make sure to validate the patch is valid. If is not valid, all other test cases related keys should be set to None, is processed still true. DO NOT ADD \ n or \ symbols in the json format.'
    index = 1
    while index <= 1:
        output = gpt.prompt(f"{prompt}. PR Id: {df['pr_id'].iloc[index]}. Patch: {df['patch'].iloc[index]}. ID: {index}")
        output = json.loads(output)
        print("PATCH: ", df['patch'].iloc[index])
        print("Result:", output['output'][1]['content'][0]['text'])
        index += 1

if __name__ == "__main__":
    main()