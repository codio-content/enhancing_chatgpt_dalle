System messages play a crucial role in guiding the AI assistant's behavior when interacting with the ChatGPT API. In this guide, we will explore the importance of refining system messages, techniques for crafting effective instructions, and examples to help you improve the quality of generated responses.


The system message sets the context and role for the AI assistant. It provides initial instructions on how the assistant should behave throughout the conversation. By carefully crafting system messages, you can ensure the AI understands the desired behavior, leading to more accurate and relevant responses.


|||

Techniques for Crafting Effective System Messages:

1. **Be specific**: Clearly define the assistant's role or expertise to set proper expectations for the conversation.
1. **Set constraints**: If necessary, provide limitations or rules that the assistant should follow when generating responses.
1. **Offer context**: Mention any relevant background information that could influence the assistant's understanding or responses.

|||

Lets try a few examples, First in order to interact with the API we need to get our libraries and our API key.
```python
import os
import openai
import secret
openai.api_key=secret.api_key
```
{Try it!}(python3 temp.py)

Now we are ready to use our API call which we will set equal to `response` so its easier for us to manipulate. 

```python
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a financial advisor."},
        {"role": "user", "content": "What are some tips for saving money?"},
        {"role": "assistant", "content": "Creating a budget, reducing expenses, and saving on utilities are some ways to save money."},
        {"role": "user", "content": "How do I create a budget?"}
    ]
)
```
{Try it!}(python3 temp.py 1)

We are going to use some slicing in order to make our response more legible. 
```python 
print(response['choices'][0]['message']['content'])
```

{Try it!}(python3 temp.py 2)

In the above example we are setting the AI as financial advisor. It provides initial instructions on how the assistant should behave throughout the conversation.

However, we can use more precision, with our tasks. Lets replace our message with the following.
```
{"role": "system", "content": "You are a travel expert specializing in European destinations."}
```
{Try it!}(python3 temp.py 3)

Explanation: This system message clearly defines the assistant's role as a travel expert and narrows down the expertise to European destinations, providing more focused guidance. Now if the user want to add something more specific, they can add it to the conversation. 

{Check It!|assessment}(multiple-choice-2744544990)
