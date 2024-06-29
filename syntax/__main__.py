import click


@click.command()
def main():
    piped = ''
    with open('./templates/symbol-ngrams.txt', 'r') as file:
        piped = '|'.join([l.strip() for l in file])

    with open('./data/symbol-ngrams.txt', 'w') as file:
        file.write(piped)


def pipe_lines(lines: list[str]) -> str:
    piped = ''
    for line in lines:
        piped += line.strip() + '|'
    return piped


if __name__ == '__main__':
    main()
