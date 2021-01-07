import mac_say.gtts
import random

twords = [
    "pumpkin",
    "mitten",
    "velvet",
    "timid",
    "creek",
    "weekend",
    "muffin",
    "bread",
    "sunscreen",
    "butter",
    "feelings",
    "head",
    "chair",
    "human",
    "paint",
    "plain",
    "frozen",
    "clean",
    "balloon",
    "smooth",
    "afternoon",
    "hill",
    "soap",
    "woman",
    "cheap",
    "goat",
    "student",
    "toothbrush",
    "small",
    "night",
    "music",
    "wheat",
    "block",
    "bright",
    "warm",
    "wheel",
    "light",
    "yard",
    "better",
    "perfect",
    "spring",
    "heat",
    "summer",
    "flood",
    "weather",
    "address",
    "spinach",
    "teacher",
    "garden",
    "seashell",
    "conflict",
    "fright",
    "might",
    "slight",
    "thigh",
    "sigh",
    "high",
    "flight",
    "right",
    "sight",
    "tight",
    "which",
]
iwords = [
    "flash",
    "drum",
    "spot",
    "ship",
    "this",
    "that",
    "then",
    "drip",
    "quiz",
    "drop",
    "thin",
    "his",
    "with",
    "duck",
    "quack",
    "math",
    "track",
    "rock",
    "shut",
    "shot",
    "black",
    "light",
    "night",
    "wish",
    "snack",
    "chin",
    "chick",
    "bath",
    "three",
    "back",
    "see",
    "feel",
    "thick",
    "green",
    "sick",
    "feet",
    "check",
    "when",
    "cape",
    "cap",
    "note",
    "boy",
    "coin",
    "feed",
    "joy",
    "stand",
]

words = twords

print(f"{len(words)} total weights")

correct = 0
total = 0
random.shuffle(words)
for word in words:
    student_answer = ""
    while student_answer == "":
        mac_say.gtts.say("en", word)
        student_answer = input().strip()

    if student_answer == str(word):
        print("correct")
        correct += 1
    else:
        print(f"incorrect. correct answer is: {word}")
    total += 1

    print(f"{correct} correct out of {total}: ({correct / total * 100:.00f}% correct)")
