import json
from lxml import etree
import sys


def search(node):
    node_child = node['questionData']
    G = ''
    for key, value in node_child.items():
        if key.endswith('Content') and value:
            G = key
            ncn = node_child[key]
    div = etree.HTML(ncn['title'])
    title = div.xpath('//text()')[0]
    answer = []

    # type => fillInTheBlanksQuestionContent
    if G.startswith('fillIn'):
        answer = ncn['answerList']
        return {'title': title, 'answer': answer}

    # type => singleChoiceQuestionContent 
    # or multipleChoiceQuestionContent
    # or trueOrFalseQuestionContent
    choicesA = ncn['choicesAnswers']
    for x in choicesA:
        eachContent = etree.HTML(x['content']).xpath('//text()')[0]
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
