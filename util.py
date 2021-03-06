"""
This module defines additional functions.
"""

import copy
import data_manager


"""
from this place we add functions from sprint#2 (sql)
"""

def check_if_vote(table,  id, vote):

    sql_condition = {"id": int(id)}
    row_to_edit = data_manager.get_from_table_condition(table, sql_condition)[0]
    votes_no = int(row_to_edit["vote_number"])
    if vote == "vote_down":
        votes_no -= 1
    elif vote == "vote_up":
        votes_no += 1
    data_to_update = {"vote_number" : str(votes_no)}
    data_manager.update_data_in_table(table, data_to_update, sql_condition)


"""
FUNCTIONS FROM SPRINT#1
"""
def change_time_format(datafile):
    """
    Takes list of dicts and changes time format for more human friendly.
    Should be used only when passing data to html
    """
    datafile_with_dates = copy.deepcopy(datafile)

    if type(datafile_with_dates) != list:
        list(datafile_with_dates)

    for single_dict in datafile_with_dates:
        single_dict["submission_time"] = single_dict["submission_time"].strftime("%d %m %Y, %H:%M")

    return datafile_with_dates






#TODO: DELETE UTLILS FUNCTION->CSV AFTER UPDATE ALL TO SQL

def find_answers_by_question(question_id: str, answers_file: list) -> list:
    """
    Finds answers(list) for selected question_id
    param: question_id: str
    param: answers_file: list
    returns list of answers: list
    if there is no question with given id, returns empty list
    """

    return [single_answer for single_answer in answers_file if single_answer["question_id"] == question_id]


def find_index_of_dict_by_id(dict_list, given_id):
    index_number = 0
    for dictionary in dict_list:
        if dictionary["id"] == given_id:
            return index_number

        index_number += 1
    return None


def purge_answer_list(answers, question_id):
    """
    Takes a list of dictionaries and returns other
    list without those related to given question_id
    """

    purged_answers = []
    for answer in answers:
        if answer["question_id"] != str(question_id):
            purged_answers.append(answer)
    return purged_answers

def proper_capitalization(string):

    return string[0].capitalize() + string[1:] if string else ""


def get_single_row(data, searched_id):
    """ takes single row from database """

    # TODO: What this function is for?

    return [row for row in data if row["id"] == int(searched_id)][0]

"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
SQL FUNCTIONS SHOULD BE ADDED ON TOP!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""