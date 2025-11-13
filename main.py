from api.gpt_manager import GPTManager

def main():
    gpt = GPTManager()
    
    output = gpt.prompt("users")
    print("Result:", output)

if __name__ == "__main__":
    main()