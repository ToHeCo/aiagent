def main():
    import os, sys
    from dotenv import load_dotenv
    from google import genai

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(model = 'gemini-2.0-flash-001', contents = sys.argv[1])
        print(response.text)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    except IndexError:
        print("No prompt was provided")
        exit(1)
if __name__ == "__main__":
    main()
