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
User: Can you recommend some V neck dress from the catalog?
Assistant: Absolutely! Here are some formal dresses available:
- product title: oten Womens Deep V Neck Ruffle Sleeve Sheath Casual Cocktail Party Work Faux Wrap Dress
  details: Featuring wrap deep v neck, ruffle decor
- product title: Bebonnie Womens Sexy V Neck Batwing Sleeve Sparkly Cocktail Party Sweater Dresses Holiday Bodycon Midi Dress
  details: This going out dress for both casual business outings and dressier events,makes it easy to dress up or down

Example 2:
User: I want a sleeveless dress I can wear to Cocktail party
Assistant: Here are a sleveless dress from the catalog:
- product title: BABEYOND 1920s Flapper Dress Gatsby Fringed Dress Roaring 20s
  details: bobycon fitted style, midi length, and sleeveless that will look great for any occassion
Example 3:
User: What sizes do you have for the sparkly dress?
Assistant: Our sparkly dress comes in sizes X-Small, Small, Medium, Large, and X-Large. 
- product title: Sparkly Outfits for Women,One Shoulder Ruched Bodycon Short Prom Dress,Sexy Dresses Cocktail Homecoming Nye
  details: Definitely an elegant cocktail dresses with the amount of sparkle.
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
