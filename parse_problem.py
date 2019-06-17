import os
import re


def scan_tokens(filename):
    with open(filename, 'r') as f:
        # Remove single line comments
        str = re.sub(r';.*$', '', f.read(), flags=re.MULTILINE).lower()
    # Tokenize
    stack = []
    list = []
    for t in re.findall(r'[()]|[^\s()]+', str):
        if t == '(':
            stack.append(list)
            list = []
        elif t == ')':
            if stack:
                l = list
                list = stack.pop()
                list.append(l)
            else:
                raise Exception('Missing open parentheses')
        else:
            list.append(t)
    if stack:
        raise Exception('Missing close parentheses')
    if len(list) != 1:
        raise Exception('Malformed expression')
    return list[0]


def parse_problem(problem_filename):
    tokens = scan_tokens(problem_filename)
    problem_dict = {}
    if type(tokens) is list and tokens.pop(0) == 'define':
        positive_goals = []
        negative_goals = []
        while tokens:
            group = tokens.pop(0)
            t = group[0]
            if t == 'problem':
                problem_name = group[-1]
                problem_dict['problem'] = problem_name
            elif t == ':domain':
                domain_name = group[-1]
                problem_dict['domain'] = domain_name
            # elif t == ':requirements':
            #     pass
            elif t == ':objects':
                group.pop(0)
                if group[-1][0] == ':private':
                    raw_objects = group[:-1]
                else:
                    raw_objects = group
                objects = []
                for i in range(0, len(raw_objects), 3):
                    objects.append(raw_objects[i:i+3])
                problem_dict['public_objects'] = objects
                if group[-1][0] == ':private':
                    raw_private_objects = group[-1][1:]
                    private_objects =[]
                    for i in range(0, len(raw_private_objects), 3):
                        private_objects.append(raw_private_objects[i:i+3])
                    problem_dict['private_objects'] = private_objects
                else:
                    problem_dict['private_objects'] = []
            elif t == ':init':
                group.pop(0)
                problem_dict['init'] = group
            elif t == ':goal':
                split_propositions(group[1], positive_goals, negative_goals, '', 'goals')
                problem_dict['goal'] = {}
                problem_dict['goal']['negative'] = negative_goals
                problem_dict['goal']['positive'] = positive_goals
            else:
                print(str(t) + ' is not recognized in problem')
    return problem_dict


def split_propositions(group, pos, neg, name, part):
    if not type(group) is list:
        raise Exception('Error with ' + name + part)
    if group[0] == 'and':
        group.pop(0)
    else:
        group = [group]
    for proposition in group:
        if proposition[0] == 'not':
            if len(proposition) != 2:
                raise Exception('Unexpected not in ' + name + part)
            neg.append(proposition[-1])
        else:
            pos.append(proposition)


# process and parse all problems from given path
def process_problems(dir_path):
    parsed_problems = {}

    for file in os.listdir(os.fsencode(dir_path)):
        filename = os.fsdecode(file)
        if 'domain' in filename:
            continue
        problem_dict = parse_problem(dir_path + '/' + filename)
        parsed_problems[filename] = problem_dict

    return parsed_problems




