import json
import sys


def search(node):
    node_child = node['questionData']
    ncn = list(v for k,
               v in node_child.items() if k.endswith('Content') and v)[0]
    title = ncn['title'].replace('<p>', '').replace('</p>', '')
    choicesA = ncn['choicesAnswers']
    answer = []
    for x in choicesA:
        eachContent = x['content'].replace('<p>', '').replace('</p>', '')
        if x['correct']:
            answer.append(f'√ {eachContent}')
        else:
            answer.append(f'× {eachContent}')
    return {'title': title, 'answer': answer}


def func(filename):
    contGet = ''
    with open(filename+'.json', 'r', encoding='utf-8') as f:
        content = json.loads(f.read())
        node_list = content['result']['nodes']
        num = 1
        for node in node_list:
            eachGet = search(node)
            words = f"{num}.{eachGet['title']}\n" + \
                '\n'.join(eachGet['answer'])
            num += 1
            contGet = contGet + words + '\n\n'
        with open(filename+'.txt', 'w', encoding='utf-8') as f:
            f.write(contGet)


if __name__ == "__main__":
    filename = sys.argv[1]
    print('Begining(￣o￣) . z Z)')
    func(filename)
    print('Finishedヾ(•ω•`)o')
