In ChatGPT API interactions, you can fine-tune the AI's output by adjusting parameters like **temperature** and **max tokens**. We will delve into the significance of these parameters, learn how they affect the generated responses, and explore techniques to control the creativity and length of AI outputs. By understanding, experimenting, and fine-tuning these parameters, you can effectively customize the ChatGPT API's responses to match your specific use case.

Lets refresh our definitions for Temperature and Max Tokens.

| Temperature | Max tokens  |
|---------|----------|
| This parameter influences the randomness and creativity of the AI's responses. A higher temperature (e.g., 0.8) results in more diverse and creative outputs, while a lower temperature (e.g., 0.2) leads to more focused and deterministic responses. | This parameter sets an arbitrary limit on the length of the AI-generated response. By defining max tokens, you can control the response length to ensure it fits within a desired range. However, setting max tokens too low might result in incomplete or nonsensical responses.  |

Lets try writing an example, token and max tokens are extra variable that we can add during our API call. 

```python 
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are some creative ways to reuse plastic bottles?"}
    ],
  temperature=0.6,
  max_tokens=50
)

print(response['choices'][0]['message']['content'])
```


{Try it!}(python3 maxtokens.py)

In this example, the temperature is set to 0.6, striking a balance between creativity and coherence. The max tokens parameter is set to 50, limiting the response length without making it too short.



|||
Techniques for Adjusting Temperature and Max Tokens:

1. **Experiment with temperature values**: Test various temperature settings to find the best balance between creativity and coherence for your specific use case.
2. **Set appropriate max tokens**: Determine an ideal response length for your application, and set max tokens accordingly. Be cautious of setting it too low, as it may truncate the output and hinder comprehension.
3. **Iterate and fine-tune**: Continuously test and adjust these parameters based on generated responses to optimize AI outputs for your needs.

|||


There is also a [playground](https://platform.openai.com/playground?mode=chat) available on the main OpenAI website to help with  visualizing the tools. 

Additionally, we can include the `n` parameter to generate multiple responses given different temperatures and tokens.

``` python
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's a good book to read on a rainy day?"}
    ],
  n=3,
  temperature=0.7
)
```
{Try it!}(python3 maxtokens.py 2)

In this example, the API generates three alternative completions for the user query, providing a range of book suggestions. You can then choose the most fitting response based on your criteria or user preferences. Remember we can use the following code to better visualize.

```python
for i in (response["choices"]):
  print(i["message"]['content'].strip()) 
  print(" ////////")
```


{Try it!}(python3 maxtokens.py 3)

{Check It!|assessment}(multiple-choice-349844694)
