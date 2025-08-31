#!/usr/bin/env python3
"""Mad Libs program for CSP300 Assignment-2"""
def collect(prompts):
    values = {}
    for key, prompt in prompts:
        values[key] = input(f"{prompt}: ").strip() or "<missing>"
    return values

def build_story(data):
    return f"""
One {data['adjective1']} morning, I woke up and found a {data['animal']} in my room!
It started to {data['verb1']} around like it owned the place.
So, I decided to take it to {data['place']}, hoping someone there would help.

But instead, people just laughed because the {data['animal']} was wearing a {data['adjective2']} hat
and eating {data['food']} noisily.

Suddenly, it began to {data['verb2']} on top of a {data['object']},
and everyone, including my best friend {data['friend']}, joined in the fun.

That day was the most unforgettable adventure of my life!
"""

def main():
    prompts = [
        ("adjective1","Enter an adjective"),
        ("animal","Enter an animal"),
        ("verb1","Enter a verb"),
        ("place","Enter a place"),
        ("adjective2","Enter another adjective"),
        ("food","Enter a type of food"),
        ("verb2","Enter another verb"),
        ("friend","Enter a friend's name"),
        ("object","Enter an object")
    ]
    data = collect(prompts)
    print("\nHere’s your Mad Libs story:\n")
    print(build_story(data))

if __name__ == "__main__":
    main()
