import os
from shutil import copyfile


# Returns the number of private objects in the given problem
def get_num_privates(parsed_problems):
    count = 0
    for prob in parsed_problems:
        count += len(parsed_problems[prob]['private_objects'])

    return count


# Copy all the domain files from src to dest
def copy_domains(src_path, dest_path):
    directory = os.fsencode(src_path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if 'domain' in filename:
            copyfile(src_path + '/' + filename, dest_path + '/' + filename)


# Write the given problem and domain files
def write_problems(src_path, dest_path, domain, problem, problems):
    if not os.path.isdir(dest_path):
        os.makedirs(dest_path)

    copy_domains(src_path, dest_path)

    for prob in problems:
        with open(dest_path + '/' + prob, mode='w') as f:
            f.write('(define (problem {}) (:domain {})\n'.format(problem, domain))
            f.write('(:objects\n')
            for pub_obj in problems[prob]['public_objects']:
                f.write('\t{} {} {}\n'.format(pub_obj[0], pub_obj[1], pub_obj[2]))
            f.write('\n')
            f.write('\t(:private\n')
            for priv_obj in problems[prob]['private_objects']:
                f.write('\t\t{} {} {}\n'.format(priv_obj[0], priv_obj[1], priv_obj[2]))
            f.write('\t)\n)\n')
            f.write('(:init\n')
            for init_pred in problems[prob]['init']:
                if init_pred[0] == 'not':
                    s = '\t(not ('
                    for t in init_pred:
                        s += t
                    s += ')'
                else:
                    s = '\t('
                    for t in init_pred:
                        s += t + ' '
                s = s[:-1]
                s += ')\n'
                f.write(s)
            f.write(')\n')
            f.write('(:goal\n')
            f.write('\t(and\n')
            for goal_pred in problems[prob]['goal']['positive']:
                s = '\t\t('
                for t in goal_pred:
                    s += t + ' '
                s = s[:-1]
                s += ')\n'
                f.write(s)
            for goal_pred in problems[prob]['goal']['negative']:
                s = '\t\t(not ('
                for t in goal_pred:
                    s += t + ' '
                s = s[:-1]
                s += '))\n'
                f.write(s)
            f.write('\t)\n)\n)\n')
