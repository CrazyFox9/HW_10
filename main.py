from flask import Flask
import utils

app = Flask(__name__)


@app.route('/')  # Главная страница с кандидатами
def page_main():
    candidate_list = utils.load_candidates("candidates.json")

    return utils.output_candidates(candidate_list)


@app.route('/candidate/<int:candidate_id>')  # Страница кандидата
def candidate(candidate_id):
    candidate_list = utils.load_candidates("candidates.json")
    candidate = utils.get_candidate_by_id(candidate_list, candidate_id)
    result = f"<img src={candidate['picture']}>"

    return result + utils.output_candidates([candidate])


@app.route('/skills/<candidate_skill>')  # Страница кандидатов с нужным скилом
def skills(candidate_skill):
    candidate_list = utils.load_candidates("candidates.json")
    return utils.output_candidates(utils.get_candidates_by_skill(candidate_list, candidate_skill))


app.run()
