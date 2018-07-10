from jinja2 import Template
import json

if __name__ == "__main__":
    with open('players/player_list_template.html') as f:
        player_list_page = Template(f.read())


    with open('skills/skills.html') as f:
        skill_list_page = Template(f.read())

    
    with open('players/player_list.json') as pfp:
        players = json.load(pfp)
    
    with open('skills/skill_list.json') as pfp:
        skills = json.load(pfp)
        for sk in skills:
            sk["raw_img"] = "https://raw.githubusercontent.com/igordsm/dev-aberto/master/skills/images/" + sk["badge"] + "?sanitize=true"

    with open('players/achievement_list.json') as pfp:
        achievement_list = json.load(pfp)
        
        achievement_per_player = {}
        for ach in achievement_list:
            if not ach["player_uuid"] in achievement_per_player:
                achievement_per_player[ach["player_uuid"]] = []
            achievement_per_player[ach["player_uuid"]].append(ach)

    for plr in players:
        plr["raw_img"] = 'https://github.com/igordsm/dev-aberto/raw/master/players/avatar_data/' + plr["avatar_image"]
        plr["xp"] = 0
        plr["level_name"] = "Newbie"

        plr["skills"] = []
        for ach in achievement_per_player[plr["uuid"]]:
            plr["xp"] += skills[ach["skill_id"]]["xp_value"]
            plr["skills"].append(skills[ach["skill_id"]].copy())
        
        # compute player level

    out = player_list_page.render(players=players)
    with open('docs/players.html', 'w') as f:
        f.write(out) 

    out = skill_list_page.render(skills=skills)
    with open('docs/skills.html', 'w') as f:
        f.write(out) 

