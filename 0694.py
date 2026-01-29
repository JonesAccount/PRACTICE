val = {"resoursec": {"coal": 121, "iron": 50, "gold": 7}, "items": {"coin": 100, "exprience": 643837, "skill": "12 lvl"}, "info": {"id": 344553, "name": "Sam", "bonus": 555}}

val = {
    "resoursec": {"coal": 121, "iron": 50, "gold": 7},
    "items": {"coin": 100, "exprience": 643837, "skill": "12 lvl"},
    "info": {"id": 344553, "name": "Sam", "bonus": 555
    }
}

val = {
    "resoursec": {
        "coal": 121,
        "iron": 50,
        "gold": 7
    },
    "items": {
        "coin": 100,
        "exprience": 643837,
        "skill": "12 lvl"
    },
    "info": {
        "id": 344553,
        "name": "Sam",
        "bonus": 555
    }
}

val = dict(
    resoursec=dict(
        coal=121,
        iron=50,
        gold=7
                   ),
    items=dict(
        coin=100,
        exprience=643837,
        skill="12 lvl"
               ),
    info=dict(
        id=344553,
        name="Sam",
        bonus=555
    )
)

print(val["resoursec"]["iron"])
print(val)
