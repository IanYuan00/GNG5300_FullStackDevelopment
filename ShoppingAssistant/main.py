from agent.shopping_agent import process_user_input

def main():
    print("Welcome to the AI-powered Shopping Assistant!")
    
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        # 使用 AI 处理用户输入
        response = process_user_input(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()
