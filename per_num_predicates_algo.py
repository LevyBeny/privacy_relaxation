import random
from copy import deepcopy


# Returns for given agent and private object the number of predicates that will turn public
def _get_num_predicates(priv_obj, problem_name, problems):
    res = 0
    for predicate in problems[problem_name]['init']:
        obj_name = priv_obj[0]
        if _is_public_predicate(obj_name, predicate, problems[problem_name]):
            res += 1
    return res


# Retrieve the next private object to make public
def _get_next_object(problems):
    max_num_predicates = -1
    max_object = None
    max_prob = None
    for prob in problems:
        for priv_obj in problems[prob]['private_objects']:
            num_predicates = _get_num_predicates(priv_obj, prob, problems)
            if num_predicates > max_num_predicates:
                max_num_predicates = num_predicates
                max_object = priv_obj
                max_prob = prob
    return max_num_predicates, max_prob, max_object


# Check if given agent's private predicate can turn public if you turn given object public
def _is_public_predicate(obj_name, predicate, problem):
    if predicate[0] == 'not':
        _predicate = predicate[1]
    else:
        _predicate = predicate

    if obj_name not in _predicate:
        return False

    for priv_obj in problem['private_objects']:
        if priv_obj[0] in _predicate and obj_name not in priv_obj:
            return False

    return True


# Delete given private object fron the given agent's problem
def _delete_from_private_list(priv_obj, problem):
    i = 0
    for obj in problem['private_objects']:
        if priv_obj[0] == obj[0]:
            break
        i += 1
    problem['private_objects'].pop(i)


# Generator for creating the problem with the relaxed privacy
def private_relaxation(parsed_problems):
    new_problems = parsed_problems
    i = 1
    while True:
        num_predicates, problem_name, selected_object = _get_next_object(new_problems)

        # Stopping condition
        if problem_name is None:
            break

        new_problems = deepcopy(new_problems)

        # add the new public object to all agents' public objects
        for prob in new_problems:
            new_problems[prob]['public_objects'].append(selected_object)

        # delete the new public object from relevant agent's private objects
        _delete_from_private_list(selected_object, new_problems[problem_name])

        # update relevant init predicates
        for predicate in new_problems[problem_name]['init']:
            obj_name = selected_object[0]
            if _is_public_predicate(obj_name, predicate, new_problems[problem_name]):
                for prob in new_problems:
                    if prob == problem_name:
                        continue
                    new_problems[prob]['init'].append(predicate)

        # update relevant goal predicates
        for predicate in new_problems[problem_name]['goal']['positive']:
            obj_name = selected_object[0]
            if _is_public_predicate(obj_name, predicate, new_problems[problem_name]):
                for prob in new_problems:
                    if prob == problem_name:
                        continue
                    new_problems[prob]['goal']['positive'].append(predicate)

        for predicate in new_problems[problem_name]['goal']['negative']:
            obj_name = selected_object[0]
            if _is_public_predicate(obj_name, predicate, new_problems[problem_name]):
                for prob in new_problems:
                    if prob == problem_name:
                        continue
                    new_problems[prob]['goal']['negative'].append(predicate)

        iteration_name = str(i) + '_' + str(num_predicates) + '_' + selected_object[0]
        i += 1
        yield iteration_name, new_problems
