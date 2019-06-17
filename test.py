from parse_problem import process_problems
from random_algo import private_relaxation
from utils import *
import os

# CONFIG
domain_name = 'logistics'
domain_path = './benchmarks/logistics00-factored'
algo = 'random'
planner_path = 'C:/Users/User/source/ma-strips/bin/Debug/GPPP.exe'

# Loop over all problems in given domain
for problem_dir in os.listdir(os.fsencode(domain_path)):
    problem_name = os.fsdecode(problem_dir)
    problem_name = 'probLOGISTICS-11-1'
    original_problem_path = domain_path + '/' + problem_name
    parsed_problems = process_problems(original_problem_path)

    print("Working on problem {}...".format(problem_name))

    # Copy original problem
    new_problem_path = './privacy_relaxation/' + algo + '/' + domain_name + '/' + problem_name + '/0'
    write_problems(original_problem_path, new_problem_path, domain_name, problem_name, parsed_problems)

    # # Run Planner on original problem
    # res = os.popen('{} {}'.format(planner_path, new_problem_path)).read()

    # Each iteration is relaxing a privacy by the relaxing algorithm
    for i, new_problems in enumerate(private_relaxation(parsed_problems)):
        new_problem_path = './privacy_relaxation/' + algo + '/' + domain_name + '/' + problem_name + '/' + str(i + 1)

        # Write the new relaxed problem and domain files
        write_problems(original_problem_path, new_problem_path, domain_name, problem_name, new_problems)

        # Run planner on new relaxed problem
        res = os.popen('{} {}'.format(planner_path, new_problem_path)).read()

    # result_file_path = './results/' + problem_name + '.txt'
    # copyfile('./Results.txt', result_file_path)
    # os.remove('./Results.txt')
