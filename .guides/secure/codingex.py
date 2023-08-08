import os
import openai
import sys
sys.path.insert(1, '/home/codio/workspace')
import secret
openai.api_key=secret.api_key
from exerc import chatfunctions, user_experience

def test_chatfunctions():
    # Test with single prompt
    responses = chatfunctions(["What is the capital of France?"], 0.5, 100)
    assert isinstance(responses, list), "Output should be a list"
    assert len(responses) == 1, "List should contain one response"
    assert isinstance(responses[0], str), "Each response should be a string"

    # Test with multiple prompts
    prompts = ["Who is Elon Musk?", "What are some applications of AI?"]
    responses = chatfunctions(prompts, 0.7, 150)
    assert len(responses) == len(prompts), "Number of responses should equal number of prompts"

    print("All tests for chatfunctions() passed!")

def test_user_experience():
    # We can't predict exact AI response, but we can at least test that it runs without error
    try:
        user_experience("What is AI?", 0.7, 150)
        print("User experience test passed!")
    except Exception as e:
        print(f"User experience test failed with error: {e}")

test_chatfunctions()
test_user_experience()
