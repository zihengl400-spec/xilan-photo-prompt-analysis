"""Validate complete UTF-8 prompt lengths against the unabridged example."""
import argparse
import json
from pathlib import Path


def count(text):
    return sum(not character.isspace() for character in text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('prompts', nargs='*', type=Path)
    args = parser.parse_args()
    baseline = Path(__file__).resolve().parents[1] / 'references' / 'full-example.txt'
    target = count(baseline.read_text(encoding='utf-8-sig'))
    report = {'baseline': target, 'minimum': target - 200, 'maximum': target + 200,
              'counting': 'Unicode non-whitespace characters, including punctuation',
              'results': []}
    passed = True
    for path in args.prompts:
        try:
            actual = count(path.read_text(encoding='utf-8-sig'))
            valid = abs(actual - target) <= 200
            report['results'].append({'path': str(path), 'count': actual,
                                      'difference': actual - target, 'passed': valid})
            passed = passed and valid
        except (OSError, UnicodeError) as error:
            report['results'].append({'path': str(path), 'passed': False, 'error': str(error)})
            passed = False
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
