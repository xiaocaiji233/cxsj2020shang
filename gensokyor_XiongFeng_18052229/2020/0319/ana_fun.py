import issues_process
import release_process
import nltk_process
import time_pieces_generate
import devide_issues
import dictionary_generate


def get_all_resources(issues_path: str, release_path: str):
    issues = issues_process.issues_process(issues_path)
    times = time_pieces_generate.port(release_path)
