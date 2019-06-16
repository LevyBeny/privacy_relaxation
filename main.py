from parse_problem import process_problems
from random_algo import private_relaxation
from shutil import copyfile
import os


def get_num_privates(parsed_problems):
    count = 0
    for prob in parsed_problems:
        count += len(parsed_problems[prob]['private_objects'])

    return count


def copy_domains(src_path, dest_path):
    directory = os.fsencode(src_path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if 'domain' in filename:
            copyfile(src_path + '/' + filename, dest_path + '/' + filename)


def write_problems(src_path, algo, domain, problem, num_relaxed, problems):
    new_dir = './privacy_relaxation/' + algo + '/' + domain + '/' + problem + '/' + num_relaxed
    os.makedirs(new_dir)

    copy_domains(src_path, new_dir)
    for prob in problems:
        with open(new_dir + '/' + prob, mode='w') as f:
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
                    f.write('\t(not ({} {} {}))\n'.format(init_pred[1][0], init_pred[1][1], init_pred[1][2]))
                else:
                    f.write('\t({} {} {})\n'.format(init_pred[0], init_pred[1], init_pred[2]))
            f.write(')\n')
            f.write('(:goal\n')
            f.write('\t(and\n')
            for goal_pred in problems[prob]['goal']['positive']:
                f.write('\t\t({} {} {})\n'.format(goal_pred[0], goal_pred[1], goal_pred[2]))
            for goal_pred in problems[prob]['goal']['negative']:
                f.write('\t\t(not ({} {} {}))\n'.format(goal_pred[0], goal_pred[1], goal_pred[2]))
            f.write('\t)\n)\n)\n')


dir_path = './benchmarks/logistics00-factored/probLOGISTICS-4-0'
planner_path = ''
parsed_problems = process_problems(dir_path)
for i, new_problems in enumerate(private_relaxation(parsed_problems)):
    new_dir = './privacy_relaxation/' + 'random' + '/' + 'logistics' + '/' + 'probLOGISTICS-4-0' + '/' + str(i+1)
    write_problems(dir_path, 'random', 'logistics', 'probLOGISTICS-4-0', str(i + 1), new_problems)
    res = os.popen('{} {}'.format(planner_path,new_dir)).read()
num_private = get_num_privates(parsed_problems)
print(num_private)
