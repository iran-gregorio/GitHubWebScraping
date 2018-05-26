import requests
import pandas as pd
import re
import os
from bs4 import BeautifulSoup
from element import Element
from multiprocessing import Pool
from argparse import ArgumentParser

BASE_URL = "https://github.com/"
out_dir = ""


def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')


def get_fileInfo(soup, element):
    elem = soup.select("div.file-info")[0]
    regexLines = re.findall(r"(\d+ line)", elem.get_text())
    regexBytes = re.findall(r"([\d+.]?\d+ [KMG]?B)", elem.get_text())

    if(regexLines):
        element.lines = int(regexLines[0].split()[0])

    if(regexBytes):
        bytes = 0
        bytesInfo = regexBytes[0].split()
        if bytesInfo[1] == "B":
            bytes = int(bytesInfo[0])
        elif bytesInfo[1] == "KB":
            bytes = int(float(bytesInfo[0]) * 1024)
        elif bytesInfo[1] == "MB":
            bytes = int(float(bytesInfo[0]) * (1024 ** 2))
        else:
            bytes = int(float(bytesInfo[0]) * (1024 ** 3))

        element.size = bytes

    element.isFile = True
    element.setExtensionFile()


def get_elementList(soup, level):
    result = []
    for elm in soup.select("tr.js-navigation-item a.js-navigation-open"):
        element = Element(elm['href'], elm['title'], level)
        if (element.title == "Go to parent directory"):
            continue
        soup = get_soup(BASE_URL + element.href[1:])
        childs = get_elementList(soup, level+1)
        if (len(childs) > 0):
            result.append(element)
            result = result + childs
        else:
            get_fileInfo(soup, element)
            result.append(element)
    return result


def process(repo):
    soup = get_soup(BASE_URL + repo)

    elementsRepo = get_elementList(soup, 0)

    totalLines = sum(e.lines for e in elementsRepo)
    totalSize = sum(e.size for e in elementsRepo)

    df = pd.DataFrame([(e.extensionFile, e.lines, e.size)
                       for e in elementsRepo if e.isFile],
                      columns=['extension', 'lines', 'size'])

    df = df.groupby(by='extension').sum()
    df = df.sort_values(by=['lines', 'size'], ascending=False)
    df.reset_index(level=0, inplace=True)

    df['lines'] = df.apply(lambda x: "{0} ({1:.2%})".format(
        x['lines'], x['lines'] / totalLines), axis=1)

    df['size'] = df.apply(lambda x: "{0} ({1:.2%})".format(
        x['size'], x['size'] / totalSize), axis=1)

    filename = out_dir + repo.replace('/', '-') + '.txt'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:

        file.write("Caminho: {0}\n".format(repo))
        file.write("Total de Linhas: {0}\n".format(totalLines))
        file.write("Total de Bytes: {0}\n\n".format(totalSize))

        df.to_string(buf=file, header=[
            'Extensão', 'Linhas', 'Bytes'], index=False, justify='center')

        file.write("\n\n[Project {0}]".format(repo))

        for elm in elementsRepo:
            if (elm.isFile):
                file.write("\n{0}|__ {1} ({2} linhas)".format(
                    ("|   " * elm.level), elm.title, elm.lines))
            else:
                file.write("\n{0}|__ [{1}]".format(
                    ("|   " * elm.level), elm.title))


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("-fi", "--file-input", dest="repoFile", help="Input file with repositores")
    parser.add_argument("-do", "--directory-output", dest="outDir", help="Output directory for result files")

    args = parser.parse_args()

    repoFile = args.repoFile
    out_dir = args.outDir

    with open(repoFile, 'r') as fileRepositores:
        repositores = fileRepositores.read().splitlines()

    with Pool(10) as p: 
        records = p.map(process, repositores)
    p.terminate()
    p.join()
