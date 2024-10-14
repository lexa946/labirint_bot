hero_info = """
Твой персонаж:
💪 <b>Мастерство</b>: {skill}
❤️ <b>Выносливость</b>: {stamina}
🍀 <b>Удачливость</b>: {luck}
💰 <b>Золото</b>: {gold}
🍗 <b>Привалы</b>: {provision}
☠️ <b>Мерт</b>: {has_died}
🎒 <b>Рюкзак</b>: {inventory}
"""

stuff_info = """
<b>{stuff_name}</b>: {stuff_description}| {is_active}

"""

dice_dict = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}


protect_phrase= [
    "уклонился", "парировал", "отразил",
]
atack_phrase = [
    "промахнулся",
]