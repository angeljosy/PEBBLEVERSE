from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)


# ============================================================
# BASIC DATA
# ============================================================

names = [
    "Gerald", "Martha", "Kevin", "Blumbus",
    "Rockbert", "Susan", "Dwayne", "Pebbleton",
    "Greg", "Rocky", "Barbara", "Steve",
    "Pebble James", "Rocky Jr", "Mabel",
    "Boulder Bob", "Tiny", "Chunky", "Dusty",
    "Professor Rock"
]

personalities = [
    "Grumpy",
    "Dramatic",
    "Nosy",
    "Introvert",
    "Overconfident",
    "Suspicious",
    "Friendly",
    "Lazy",
    "Judgmental"
]

moods = [
    "Happy",
    "Bored",
    "Annoyed",
    "Confused",
    "Suspicious",
    "Peaceful",
    "Dramatic",
    "Existential"
]

actions = [
    "Doing absolutely nothing",
    "Rolling slightly",
    "Staring at another pebble",
    "Avoiding everyone",
    "Thinking about nothing",
    "Moving unnecessarily",
    "Having an existential crisis",
    "Judging another pebble",
    "Waiting for something",
    "Pretending to be busy"
]


# ============================================================
# PEBBLE CREATION
# ============================================================

pebbles = []

for i in range(30):

    pebble = {
        "id": i + 1,

        "name": random.choice(names) + " " + str(i + 1),

        "personality": random.choice(personalities),

        "mood": random.choice(moods),

        "action": random.choice(actions),

        "age": random.randint(1, 100),

        "favorite_number": random.randint(1, 100),

        "x": random.randint(5, 90),

        "y": random.randint(5, 90),

        "gossip": 0,

        "money": random.randint(10, 500),

        "crime_count": 0,

        "status": "Active",

        "partner": None,

        "achievement": None
    }

    pebbles.append(pebble)


# ============================================================
# GOVERNMENT
# ============================================================

government = {
    "president": random.choice(pebbles)["name"],
    "vice_president": random.choice(pebbles)["name"],
    "minister_nothing": random.choice(pebbles)["name"],
    "minister_rolling": random.choice(pebbles)["name"],
    "minister_gossip": random.choice(pebbles)["name"]
}


# ============================================================
# USELESS LAWS
# ============================================================

laws = [

    "Every pebble must stare at another pebble for 3 seconds.",

    "Rolling more than 5 centimeters requires government permission.",

    "Thinking about moving without actually moving is encouraged.",

    "Gossip must be completely unreliable.",

    "Nobody is allowed to accomplish anything.",

    "Pebbles must maintain a respectful distance from suspicious pebbles.",

    "Standing still for too long is considered suspicious.",

    "The number 7 is temporarily illegal.",

    "All arguments must be about absolutely nothing.",

    "Pebbles must pretend they have somewhere to go.",

    "Looking productive without actually working is encouraged.",

    "Being unnecessarily dramatic is completely legal."
]


# ============================================================
# CRIMES
# ============================================================

crimes = [

    "Illegal Rolling",

    "Suspicious Standing",

    "Unauthorized Staring",

    "Excessive Doing Nothing",

    "Gossip Without Permission",

    "Moving Without Purpose",

    "Thinking Too Loudly",

    "Standing in the Wrong Place",

    "Being Suspicious",

    "Stealing Absolutely Nothing"
]


# ============================================================
# COURT
# ============================================================

court_cases = []

court_verdicts = [

    "Guilty of absolutely nothing",

    "Not guilty because nobody cares",

    "Sentence: 3 minutes of standing still",

    "Case dismissed due to lack of purpose",

    "Guilty of suspicious behavior",

    "Warning issued for unnecessary movement"
]


# ============================================================
# RELATIONSHIPS
# ============================================================

relationship_types = [

    "Friends",

    "Best Friends",

    "Enemies",

    "Suspicious Partners",

    "Secret Friends",

    "Professional Rivals",

    "Unexpected Allies",

    "People Who Pretend Not To Know Each Other"
]

relationships = []


# ============================================================
# MARRIAGES
# ============================================================

marriages = []


# ============================================================
# GOSSIP
# ============================================================

gossip_templates = [

    "{a} thinks {b} is acting suspicious today.",

    "{a} heard that {b} has been standing still for too long.",

    "{a} says {b} secretly likes {c}.",

    "{a} thinks {b} is avoiding everyone.",

    "{a} heard that {b} moved for absolutely no reason.",

    "{a} believes {b} is hiding something.",

    "{a} says {b} thinks they are the most important pebble.",

    "{a} suspects {b} has a secret friendship with {c}.",

    "{a} thinks {b} has been behaving strangely.",

    "{a} claims {b} started everything.",

    "{a} heard that {b} is planning something.",

    "{a} thinks {b} spends too much time with {c}.",

    "{a} says {b} cannot be trusted.",

    "{a} believes {b} is secretly judging everyone."
]

gossip_history = []


def create_gossip():

    speaker, target, third = random.sample(pebbles, 3)

    template = random.choice(gossip_templates)

    message = template.format(
        a=speaker["name"],
        b=target["name"],
        c=third["name"]
    )

    reliability = random.randint(5, 95)

    if reliability >= 75:
        level = "CONFIRMED"

    elif reliability >= 50:
        level = "RUMOR"

    elif reliability >= 25:
        level = "SUSPICIOUS"

    else:
        level = "WILD SPECULATION"

    speaker["gossip"] += 1

    gossip = {
        "speaker": speaker["name"],
        "message": message,
        "level": level,
        "reliability": reliability,
        "time": datetime.now().strftime("%H:%M:%S")
    }

    gossip_history.insert(0, gossip)

    if len(gossip_history) > 30:
        gossip_history.pop()

    return gossip


# ============================================================
# EVENTS
# ============================================================

events = [

    "A suspicious amount of nothing happened.",

    "Two pebbles stood unusually close.",

    "Someone started a pointless argument.",

    "The civilization experienced complete silence.",

    "Someone looked at someone else.",

    "A pebble rolled for absolutely no reason.",

    "Nobody knows what happened.",

    "A pebble has been standing still for 47 minutes.",

    "The council discussed absolutely nothing.",

    "Everyone decided to do nothing.",

    "The government announced that nothing will change.",

    "A pebble forgot why it moved.",

    "Someone was caught thinking.",

    "The economy experienced absolutely no growth.",

    "A historic moment occurred and nobody noticed.",

    "Someone achieved absolutely nothing.",

    "A pebble became unnecessarily famous."
]

event_history = []


def create_event():

    message = random.choice(events)

    importance = random.randint(1, 100)

    impacts = [

        "None",

        "Absolutely nothing",

        "No measurable impact",

        "Everyone ignored it",

        "The pebbles continued doing nothing"
    ]

    event = {

        "message": message,

        "importance": importance,

        "impact": random.choice(impacts),

        "time": datetime.now().strftime("%H:%M:%S")
    }

    event_history.insert(0, event)

    if len(event_history) > 20:
        event_history.pop()

    return event


# ============================================================
# RELATIONSHIP GENERATOR
# ============================================================

def create_relationship():

    if len(pebbles) < 2:
        return None

    existing_pairs = {
        tuple(sorted([r["a"], r["b"]]))
        for r in relationships
    }

    possible_pairs = []

    for i in range(len(pebbles)):

        for j in range(i + 1, len(pebbles)):

            a = pebbles[i]

            b = pebbles[j]

            pair = tuple(
                sorted([a["name"], b["name"]])
            )

            if pair not in existing_pairs:

                possible_pairs.append((a, b))

    if possible_pairs:

        a, b = random.choice(possible_pairs)

    else:

        a, b = random.sample(pebbles, 2)

    relationship = {

        "a": a["name"],

        "b": b["name"],

        "type": random.choice(
            relationship_types
        ),

        "time": datetime.now().strftime("%H:%M:%S")
    }

    relationships.insert(
        0,
        relationship
    )

    if len(relationships) > 30:
        relationships.pop()

    return relationship


# ============================================================
# MARRIAGE GENERATOR
# ============================================================

def create_marriage():

    available = [

        p for p in pebbles

        if p["partner"] is None
    ]

    if len(available) < 2:
        return None

    a, b = random.sample(
        available,
        2
    )

    a["partner"] = b["name"]

    b["partner"] = a["name"]

    marriage = {

        "a": a["name"],

        "b": b["name"],

        "message":
            f"{a['name']} and {b['name']} "
            f"are now married for absolutely no reason.",

        "time":
            datetime.now().strftime("%H:%M:%S")
    }

    marriages.insert(
        0,
        marriage
    )

    if len(marriages) > 20:
        marriages.pop()

    return marriage


# ============================================================
# INITIAL CIVILIZATION
# ============================================================

for _ in range(8):

    create_relationship()


for _ in range(3):

    create_marriage()


# ============================================================
# CRIME GENERATOR
# ============================================================

def create_crime():

    suspect = random.choice(pebbles)

    crime = random.choice(crimes)

    suspect["crime_count"] += 1

    case = {

        "suspect": suspect["name"],

        "crime": crime,

        "verdict":
            random.choice(court_verdicts),

        "time":
            datetime.now().strftime("%H:%M:%S")
    }

    court_cases.insert(
        0,
        case
    )

    if len(court_cases) > 20:
        court_cases.pop()

    return case


# ============================================================
# ACHIEVEMENTS
# ============================================================

achievements = [

    "Moved 1 centimeter",

    "Did absolutely nothing",

    "Gossiped successfully",

    "Stared at another pebble",

    "Survived another day",

    "Avoided responsibility",

    "Won an argument about nothing",

    "Became unnecessarily suspicious",

    "Rolled without permission",

    "Thought about doing something",

    "Successfully wasted time",

    "Accomplished absolutely nothing"
]


def create_achievement():

    pebble = random.choice(pebbles)

    achievement = random.choice(
        achievements
    )

    pebble["achievement"] = achievement

    return {

        "pebble": pebble["name"],

        "achievement": achievement
    }


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ============================================================
# PEBBLES
# ============================================================

@app.route("/pebbles")
def get_pebbles():

    for pebble in pebbles:

        if pebble["status"] == "Active":

            pebble["x"] += random.randint(
                -3,
                3
            )

            pebble["y"] += random.randint(
                -3,
                3
            )

            pebble["x"] = max(
                5,
                min(90, pebble["x"])
            )

            pebble["y"] = max(
                5,
                min(90, pebble["y"])
            )

            if random.random() < 0.3:

                pebble["mood"] = random.choice(
                    moods
                )

            if random.random() < 0.4:

                pebble["action"] = random.choice(
                    actions
                )

    return jsonify(pebbles)


# ============================================================
# GOSSIP
# ============================================================

@app.route("/gossip")
def get_gossip():

    create_gossip()

    return jsonify(
        gossip_history[:10]
    )


# ============================================================
# EVENT
# ============================================================

@app.route("/event")
def get_event():

    return jsonify(
        create_event()
    )


# ============================================================
# STATISTICS
# ============================================================

@app.route("/stats")
def get_stats():

    active = len([

        p for p in pebbles

        if p["status"] == "Active"
    ])

    moving = random.randint(
        4,
        min(12, active)
    )

    doing_nothing = active - moving

    total_gossip = sum(

        p["gossip"]

        for p in pebbles
    )

    total_crimes = sum(

        p["crime_count"]

        for p in pebbles
    )

    return jsonify({

        "population": active,

        "total_population":
            len(pebbles),

        "moving": moving,

        "doing_nothing":
            max(0, doing_nothing),

        "gossip":
            total_gossip,

        "crimes":
            total_crimes,

        "relationships":
            len(relationships),

        "marriages":
            len(marriages),

        "money":
            sum(
                p["money"]
                for p in pebbles
            ),

        "progress":
            "0.0001%",

        "purpose":
            "NONE"
    })


# ============================================================
# GOVERNMENT
# ============================================================

@app.route("/government")
def get_government():

    return jsonify(
        government
    )


# ============================================================
# LAWS
# ============================================================

@app.route("/laws")
def get_laws():

    return jsonify(
        laws
    )


# ============================================================
# COURT
# ============================================================

@app.route("/court")
def get_court():

    create_crime()

    return jsonify(
        court_cases[:10]
    )


# ============================================================
# RELATIONSHIPS
# ============================================================

@app.route("/relationships")
def get_relationships():

    if random.random() < 0.65:

        create_relationship()

    return jsonify(
        relationships[:10]
    )


# ============================================================
# MARRIAGES
# ============================================================

@app.route("/marriages")
def get_marriages():

    if random.random() < 0.15:

        create_marriage()

    return jsonify(
        marriages[:10]
    )


# ============================================================
# ACHIEVEMENTS
# ============================================================

@app.route("/achievement")
def get_achievement():

    return jsonify(
        create_achievement()
    )


# ============================================================
# HISTORY
# ============================================================

@app.route("/history")
def get_history():

    history = []

    history.extend(
        event_history
    )

    for gossip in gossip_history:

        history.append({

            "message":
                gossip["message"],

            "time":
                gossip["time"]
        })

    history.sort(

        key=lambda x: x["time"],

        reverse=True
    )

    return jsonify(
        history[:20]
    )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )
