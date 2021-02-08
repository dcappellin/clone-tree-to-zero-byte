import os
import click


def __get_files_tree(source):
    req_files = []
    for root, _, files in os.walk(source):
        for file in files:
            req_files.append(os.path.join(root, file))

    return req_files


@click.command()
@click.argument('source')
@click.argument('destination')
def clone_tree(source, destination):
    for idx, file in enumerate(__get_files_tree(source)):
        df = file.replace(source, destination)
        if not os.path.exists(os.path.dirname(df)):
            os.makedirs(os.path.dirname(df))
        with open(df, 'w') as zero_byte_file:
            zero_byte_file.write('')
            print(f'File #{idx} {df} created.')

    print(f'\nDirectory {source} successfully cloned into {destination} creating {idx} 0-byte files.')


if __name__ == '__main__':
    clone_tree()
