from api.gpt_manager import GPTManager
from api.gemini_manager import GeminiManager
import pandas as pd
import json

df = pd.read_csv("../test_pr_output.csv")
processed_data = []

def main():
    gpt = GPTManager()
    prompt = 'Test cases PRs can have different changes ["new", "maintenance", "refactor", "prettify"]. You will analyze patches. For new, maintenance and refactor, specify if is an unit test, integration test, e2e test, or api test. Your response should be in json format with keys: "id", "test_type", "pr_id", "is_processed", "test_case", "is_valid_patch". Test case refers to if is new, maintenance, refactor, or prettify. The test_type should be one of the following: "unit", "integration", "e2e", "api". The is_processed should be a boolean value. Only reteurn json format, do not add any text nor explanation. Make sure to validate the patch is valid. If is not valid, all other test cases related keys should be set to None, is processed still true. DO NOT ADD \ n or \ symbols in the json format.'
    index = 0
    while index <= 300:
        output = gpt.prompt(f"{prompt}. PR Id: {df['pr_id'].iloc[index]}. Patch: ```{df['patch'].iloc[index]}```. ID: {index}")
        output = json.loads(output)
        print("Initializing ", index)
        processed_data.append(json.loads(output['output'][1]['content'][0]['text']))
        #print("Result:", output['output'][1]['content'][0]['text'])
        print("Finished ", index)
        index += 1
    print(processed_data)
    with open("processed_data.txt", "w", encoding="utf-8") as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=2)
    response_df = pd.DataFrame(processed_data)
    response_df.to_csv("../gpt-responses.csv", index=False)

if __name__ == "__main__":
    main()