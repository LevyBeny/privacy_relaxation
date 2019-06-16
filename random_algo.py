import random
from copy import deepcopy


def _create_private_pool(parsed_problems):
    pool = {}
    for prob in parsed_problems:
        for i, priv_obj in enumerate(parsed_problems[prob]['private_objects']):
            pool[str(priv_obj)] = (prob, priv_obj)
    return pool


def _is_public_predicate(obj_name, predicate, problem):
    if predicate[0] == 'not':
        _predicate = predicate[1]
    else:
        _predicate = predicate

    if obj_name not in _predicate:
        return False

    for priv_obj in problem['private_objects']:
        if priv_obj[0] in _predicate:
            return False

    return True


def _delete_from_private_list(priv_obj, problem):
    i = 0
    for obj in problem['private_objects']:
        if priv_obj[0] == obj[0]:
            break
        i += 1
    problem['private_objects'].pop(i)


def private_relaxation(parsed_problems):
    private_pool = _create_private_pool(parsed_problems)
    new_problems = parsed_problems
    while True:
        key_value = random.sample(private_pool.items(), 1)[0]
        pool_key = key_value[0]
        problem_name = key_value[1][0]
        selected_object = key_value[1][1]

        # delete from pool
        del private_pool[pool_key]

        new_problems = deepcopy(new_problems)

        # add the new public object to all agents' public objects
        for prob in new_problems:
            new_problems[prob]['public_objects'].append(selected_object)

        # delete the new public object from relevant agent's private objects
        _delete_from_private_list(selected_object,new_problems[problem_name])

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

        yield new_problems

        if len(private_pool) == 0:
            break
