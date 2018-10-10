from jinja2 import Template
import json

def get_skill_by_id(skills, skid):
    for sk in skills:
        if sk["id"] == skid:
            return sk
    return None

def has_skill(plr, sk):
    for plr_sk in plr["skills"]:
        if sk["id"] == plr_sk["id"]:
            return True
    return False

def compute_grade(plr, skills):
    if has_skill(plr, get_skill_by_id(skills, 0)):
        plr["level_name"] = "Professor"
        return 
    
    plr["level_name"] = "Ghost"
    
    classroom_skills = [sk for sk in skills if sk["type"] == "Classroom"]
    for cls_sk in classroom_skills:
        if not has_skill(plr, cls_sk):
            return
    
    plr["level_name"] = "Newbie"
    
    if plr["xp"] >= 50 and has_skill(plr, get_skill_by_id(skills, 5)) and \
    has_skill(plr, get_skill_by_id(skills, 8)) and has_skill(plr, get_skill_by_id(skills, 9)):
        plr["level_name"] = "Iniciado"
    else:
        return 
    
    if plr["xp"] >= 80 and has_skill(plr, get_skill_by_id(skills, 6)):
        plr["level_name"] = "Competente"
    else:
        return
    
    if plr["xp"] >= 150 and (has_skill(plr, get_skill_by_id(skills, 13)) or
                             has_skill(plr, get_skill_by_id(skills, 17)) or
                             has_skill(plr, get_skill_by_id(skills, 18))):
        plr["level_name"] = "Mestre"
    else:
        return
    
    if plr["xp"] >= 250 and (has_skill(plr, get_skill_by_id(skills, 14)) or
                             has_skill(plr, get_skill_by_id(skills, 17)) or
                             has_skill(plr, get_skill_by_id(skills, 18))):
        plr["level_name"] = "Grão-Mestre"
    

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
        plr["raw_img"] += "?sanitize=true"
        plr["xp"] = 0

        plr["skills"] = []
        for ach in achievement_per_player[plr["uuid"]]:
            skill = get_skill_by_id(skills, ach["skill_id"])
            plr["xp"] += skill["xp_value"]
            plr["skills"].append(skill.copy())
        
        plr["skills"].sort(key=lambda t: t["id"])
        compute_grade(plr, skills)
        
    out = player_list_page.render(players=players)
    with open('docs/players.html', 'w') as f:
        f.write(out) 

    sorted_skills = sorted(skills, key=lambda x: x['type'])

    out = skill_list_page.render(skills=sorted_skills)
    with open('docs/skills.html', 'w') as f:
        f.write(out) 

