import random
from copy import deepcopy


# Returns agents pool dict --> key: agent, value: list of private objects
def _create_agent_pool(parsed_problems):
    pool = {}
    for prob in parsed_problems:
        pool[prob] = []
        if len(parsed_problems[prob]['private_objects']) == 0:
            continue
        for i, priv_obj in enumerate(parsed_problems[prob]['private_objects']):
            pool[prob].append(priv_obj)
    return pool


# Check if given predicate is public
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


# Delete given private object from given problem
def _delete_from_private_list(priv_obj, problem):
    i = 0
    for obj in problem['private_objects']:
        if priv_obj[0] == obj[0]:
            break
        i += 1
    problem['private_objects'].pop(i)


def private_relaxation(parsed_problems):
    agents_pool = _create_agent_pool(parsed_problems)
    new_problems = parsed_problems
    while True:
        key_value = random.sample(agents_pool.items(), 1)[0]
        agent = key_value[0]
        agent_private_objects = key_value[1]

        # delete from pool
        del agents_pool[agent]

        new_problems = deepcopy(new_problems)

        # Loop over all private objects of the selected agent
        for selected_object in agent_private_objects:

            # add the new public object to all agents' public objects
            for prob in new_problems:
                new_problems[prob]['public_objects'].append(selected_object)

            # delete the new public objects from relevant agent's private objects
            _delete_from_private_list(selected_object, new_problems[agent])

            # update relevant init predicates
            for predicate in new_problems[agent]['init']:
                obj_name = selected_object[0]
                if _is_public_predicate(obj_name, predicate, new_problems[agent]):
                    for prob in new_problems:
                        if prob == agent:
                            continue
                        new_problems[prob]['init'].append(predicate)

            # update relevant goal predicates
            for predicate in new_problems[agent]['goal']['positive']:
                obj_name = selected_object[0]
                if _is_public_predicate(obj_name, predicate, new_problems[agent]):
                    for prob in new_problems:
                        if prob == agent:
                            continue
                        new_problems[prob]['goal']['positive'].append(predicate)

            for predicate in new_problems[agent]['goal']['negative']:
                obj_name = selected_object[0]
                if _is_public_predicate(obj_name, predicate, new_problems[agent]):
                    for prob in new_problems:
                        if prob == agent:
                            continue
                        new_problems[prob]['goal']['negative'].append(predicate)

        yield new_problems

        if len(agents_pool) == 0:
            break
