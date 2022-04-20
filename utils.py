import json


def load_candidates(path):
    """ Загружает из файла JSON кандидатов и возвращает их """

    with open(path, "r", encoding="utf=8") as file:
        candidates = json.load(file)
        return candidates


def output_candidates(candidates_list):
    """
    Выводит список кандидатов в формате:
    Имя кандидата:
    Позиция кандидата:
    Навыки:
    """

    result = "<pre>"
    for candidate in candidates_list:
        result += (
            f"Имя кандидата: {candidate['name']}\n"
            f"Позиция кандидата: {candidate['position']}\n"
            f"Навыки: {candidate['skills']}\n\n"
        )
    result += "<pre>"
    return result


def get_candidate_by_id(candidates_list, candidate_id):
    """ Возвращает кандидата по его id """

    for candidate in candidates_list:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_skill(candidates_list, candidate_skill):
    """ Возвращает список кандидатов по наличию скилов """

    result = []
    for candidate in candidates_list:
        candidate_skills = candidate["skills"].lower().split(", ")
        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)
    return result
