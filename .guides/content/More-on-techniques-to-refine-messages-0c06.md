You can guide the AI assistant effectively and enhance the overall quality of the generated content. Refining system messages is essential for achieving more accurate and useful responses from the ChatGPT API. You can increase efficiency of result By being specific, setting constraints, and offering context.

 In the travel example, we created a travel expert. Lets try setting some constraints and adding the context. Replace the previous message with the following in order to create constraint.
 System message with constraints:
```python

{"role": "system", "content": "You are a movie recommendation assistant. Only suggest movies rated PG-13 or lower."}
```
 {Try it!}(python3 temp.py 1)
In addition to defining the assistant's role as a movie recommendation assistant, this system message sets a constraint to only suggest movies rated PG-13 or lower.


Let's try an example offering context:
```python
{"role": "system", "content": "You are a history tutor. The student is currently studying the American Revolutionary War."}
```
{Try it!}(python3 temp.py 2)

This system message defines the assistant's role as a history tutor and provides context that the user is studying the American Revolutionary War, helping the AI to generate relevant responses.

### Ambiguous 

Ambiguous queries can lead to unclear or confusing AI-generated responses.

we will discuss strategies to recognize and handle ambiguous user queries, ensuring that the ChatGPT API generates clear and informative responses that accurately address user questions.

|||

Strategies for Handling Ambiguous Queries:

**Detect ambiguity**: Monitor user queries for potential ambiguity, vagueness, or lack of context that might result in unclear responses.
**Request clarification**: If a user query is ambiguous, program the AI assistant to ask for clarification or additional information before providing a response.
**Provide examples**: When responding to an ambiguous query, offer a range of examples or possibilities to cover different interpretations of the user's question.
**Refine system messages**: Modify system messages to guide the AI in handling ambiguous queries more effectively.
|||

Suppose you have the following ambiguous user query:

```python 
{"role": "user", "content": "What is the best way to cook it?"}

```

{Try it!}(python3 temp.py 3)

Handling Ambiguity:
```python
{"role": "system", "content": "You are a helpful assistant."}, 
 {"role": "user", "content": "What is the best way to cook it?"},  
{"role": "assistant", "content": "I need more information to provide a specific answer. What ingredient or dish are you referring to?"}
```
{Try it!}(python3 temp.py 4)

In this example, the AI assistant recognizes the ambiguity in the user's question and asks for clarification before attempting to provide a cooking method.

{Check It!|assessment}(multiple-choice-1339680802)
