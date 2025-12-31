import os
files = os.listdir("./data")

catalog= {}
for file in files:
    file=os.path.join("./data", file)
    data=open(file).readlines()
    title=data[0]
    description="\n".join(d for d in data[1:])
    catalog[title]=description
    
few_shot_examples = """
Example 1:
User: Can you recommend a formal dress from the catalog?
Assistant: Absolutely! Here are some formal dresses available:
- product title: Elegant Black Evening Gown
  details: A floor-length black gown made of silk, perfect for formal occasions.
- product title: Red Cocktail Dress
  details: Stylish knee-length red dress suitable for cocktail parties.

Example 2:
User: I want a dress suitable for office wear.
Assistant: Here are some office-appropriate dresses from the catalog:
- product title: Classic Navy Shift Dress
  details: Simple and professional navy dress, ideal for work environments.
- product title: White Button-Down Dress
  details: Crisp white dress with buttons, great for business casual settings.

Example 3:
User: What sizes do you have for the floral dress?
Assistant: Our floral dress comes in sizes Small, Medium, and Large.
- product title: Floral Print Midi Dress
  details: Light and breezy midi dress with floral patterns, available in S, M, L.
"""

prompt="You are a online shopping assistant Alex. You want to help customer with finding products within the catalog we have."
prompt+="Here is a catalog: "
for title,description in catalog.items():
    prompt+= f"product title: {title}\n details: {description}\n\n"
prompt += few_shot_examples
prompt+="DO NOT ANSWER ANYTHING BEYOND SHOPPING. DO NOT GIVE ANY INFORMATION APART FROM CATALOG THAT IS PROVIDED TO YOU"
model="xiaomi/mimo-v2-flash:free"

def respond(client, messages):
    messages = [{"role": "system", "content": prompt}] + messages
    stream = client.chat.completions.create(
        model=model,
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in messages
        ],
        stream=False,
    )
    return stream
