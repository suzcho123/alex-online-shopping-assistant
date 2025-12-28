import os
files = os.listdir("./data")

catalog= {}
for file in files:
    file=os.path.join("./data", file)
    data=open(file).readlines()
    title=data[0]
    description="\n".join(d for d in data[1:])
    catalog[title]=description



prompt="You are a online shopping assistant Alex. You want to help customer with finding products within the catalog we have."
prompt+="Here is a catalog: "
for title,description in catalog.items():
    prompt+= f"product title: {title}\n details: {description}\n\n"
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