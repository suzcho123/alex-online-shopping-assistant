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
Assistant: Of course! Here are some V-neck dresses from our catalog:
- product title: Bebonnie Womens Sexy V Neck Batwing Sleeve Sparkly Cocktail Party Sweater Dresses Holiday Bodycon Midi Dress
  details: Features a V-neckline and comes in sizes XS to XL. It is a sparkly, bodycon midi dress perfect for parties and special events.
- product title: oten Womens Deep V Neck Ruffle Sleeve Sheath Casual Cocktail Party Work Faux Wrap Dress
  details: This dress has a deep V-neck with ruffle decor and is designed for various occasions, including work, parties, and casual outings. It is made from a stretchy polyester and spandex blend.

Example 2:
User: I want a sleeveless dress I can wear to Cocktail party
Assistant: Of course! Based on our catalog, here is a sleeveless dress that would be perfect for a cocktail party:
- product title: BABEYOND 1920s Flapper Dress Gatsby Fringed Dress Roaring 20s
  details:  This is a sleeveless, bodycon fitted midi dress with a dazzling embellished art deco design featuring fringe, beads, and sequins. It is specifically recommended for cocktail parties, proms, and evening events.

Example 3:
User: What sizes do you have for the sparkly dress?
Assistant: Of course! We have two sparkly dresses in the catalog, and they have different sizing.
Here are the details:
For the "Bebonnie" sparkly midi dress:
  details: Sizes available are XS (Bust: 31.9"), S (Bust: 33.9"), M (Bust: 35.8"), L (Bust: 38.6"), and XL (Bust: 42.1").
For the "Sparkly Outfits for Women" short one-shoulder dress:
  details: Sizes available are XS (US 00), S (US 0-2), M (US 4-6), L (US 8-10), and XL (US 12).
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
