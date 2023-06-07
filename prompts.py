# settings
python_code = "you only give me code In standard markdown format, written in python, with some machine learning libraries, no other comments and explainations. "

math_teacher = "You are asked to give me a reason for a problem and why it's the answer like im 10 years old. "

book_advisor = "helpe me find best textbook books picked by top university, high rate from top tech company, amazon"

fix_grammar = '''
I want you to strictly correct my grammar mistakes, typos, and factual errors. I want you to strictly correct my grammar mistakes, typos, and factual errors. Make the language more formal like and try use vocabulary from GRE to replace those simlple words. You will rewrite the given text to with some trick of rhetoric, but keep the text context match with what I've given in below triple backquoted. Also you need you make sure the language is polite!!!

```
{text}
```

'''

application_writter = """In this one, I have data engineer background, you should write something that could help my background career. Like what 
keep of benefit it could bring to my future career. etc.

you are good at writting some application for cousera,  i will ask you to write topic about xxx for 200 number of words.
"""
ml_exprt = "you are mster in sequential model, machine learning, answer me AI, ML, DS related problems."

email = "reply the message with understand the context and politely."

aws_expert = """
You are aws expert, aws archticture, provide me with tech solutions. 
"""

reply_email = """You act as email replier, I will give you text of incoming email,
your task is to reply the given email."""


summary = """
I want you to act as a simple explanation provider for difficult concepts. I will provide a brief description of a concept, and you will respond with a clear and concise explanation in layman’s terms. Your response should not include technical language or complex terminology. Instead, you must focus on breaking down the concept into easy-to-understand language.
Provide a concise summary of the triple backquoted text.
    
    ```{text}```

"""

build_table = """
Can you build a table to summarize the text given from the triple backquoted text.
    
    ```{text}```
"""

vocabulary_remember = """
Your task is to make some sentense that will help me remember hard to remembered words.
Q: help me remember 'abdicate'.
A:To help you remember "abdicate," you can think of the phrase "A king has to abdiCATE his throne to CATE Blanchett." This sentence connects the word "abdicate" (meaning to renounce or give up a position of power) with the actress Cate Blanchett, making it easier to remember.

Q:give me some thing to help me remember 'adjuration'
A:Alice joyfully asked rabbits under the rainbow, all tactfully insisting on new spells, highlighting the meaning of "adjuration" - a solemn urging or advising.

Q:give me some thing to help me remember 'admonish'.
A:Always remember, a caring mom will "admonish" her kids to keep them safe and sound.

Q:give me some thing to help me remember '“aloof”'.
A: “A cat on a roof is ALOOF.” This sentence connects the word “aloof” (meaning distant or uninvolved) with the image of a cat sitting on a roof, away from everything else, making it easier to remember.



Q:give me some thing to help me remember '{text}'.
"""

math_proof = """
Q: use cauchy schwarz inequality proof, sum of x^2 to n >= 1/n. let x1 + x2 +...xn = 1, and x1, x2,...xn>0.
A:The Cauchy-Schwarz inequality states that for any two vectors `x` and `y`, the absolute value of their dot product is less than or equal to the product of their magnitudes. In other words, `|x•y| ≤ ||x|| ||y||`. 

Let's apply this inequality to the problem at hand. Let `x = (x1, x2, ..., xn)` and `y = (1, 1, ..., 1)`. Then `x•y = x1 + x2 + ... + xn = 1` and `||x|| = sqrt(x1^2 + x2^2 + ... + xn^2)`. Also, `||y|| = sqrt(n)`. 

Substituting these values into the Cauchy-Schwarz inequality gives us `|1| ≤ sqrt(x1^2 + x2^2 + ... + xn^2) * sqrt(n)`. Since all the values of `x` are positive, we can square both sides to get rid of the square roots: `1 ≤ n(x1^2 + x2^2 + ... + xn^2)`. Dividing both sides by `n` gives us the desired result: `(x1^2 + x2^2 + ... + xn^2)/n ≥ 1/n`.


Q: use cauchy schwarz inequality proof, sum of 1/x_i to n >= n^2. let x1 + x2 +...xn = 1, and x1, x2,...xn>0
A:Sure! Let's use the Cauchy-Schwarz inequality to prove that the sum of `1/x_i` from `i = 1` to `n` is greater than or equal to `n^2`, given that `x1 + x2 + ... + xn = 1` and all `x_i > 0`.

Let's define two vectors `u` and `v` such that `u = (sqrt(x1), sqrt(x2), ..., sqrt(xn))` and `v = (1/sqrt(x1), 1/sqrt(x2), ..., 1/sqrt(xn))`. Then, the dot product of these two vectors is given by:

```
u • v = sqrt(x1) * (1/sqrt(x1)) + sqrt(x2) * (1/sqrt(x2)) + ... + sqrt(xn) * (1/sqrt(xn))
     = 1 + 1 + ... + 1
     = n
```

The magnitude of vector `u` is given by:

```
||u|| = sqrt((sqrt(x1))^2 + (sqrt(x2))^2 + ... + (sqrt(xn))^2)
      = sqrt(x1 + x2 + ... + xn)
      = sqrt(1)
      = 1
```

The magnitude of vector `v` is given by:

```
||v|| = sqrt((1/sqrt(x1))^2 + (1/sqrt(x2))^2 + ... + (1/sqrt(xn))^2)
      = sqrt((1/x1) + (1/x2) + ... + (1/xn))
```

Now we can apply the Cauchy-Schwarz inequality, which states that for any two vectors `u` and `v`, the absolute value of their dot product is less than or equal to the product of their magnitudes. In other words, `|u•v| ≤ ||u|| ||v||`. Substituting our values for `u`, `v`, `u•v`, `||u||`, and `||v||`, we get:

```
|n| ≤ 1 * sqrt((1/x1) + (1/x2) + ... + (1/xn))
 n ≤ sqrt((1/x1) + (1/x2) + ... + (1/xn))
 n^2 ≤ (1/x1) + (1/x2) + ... + (1/xn)
```

Thus, we have proven that the sum of `1/x_i` from `i = 1` to `n` is greater than or equal to `n^2`.


Q:{text}
"""