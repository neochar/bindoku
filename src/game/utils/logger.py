from datetime import datetime
from io import StringIO
from pathlib import Path

from game.utils.path import get_path


def cleanup_logs():
    import os
    import shutil

    path = get_path('../log/')
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            file_log(0, 'error', 'Failed to delete %s. Reason: %s' % (file_path, e))


def file_log(i, prefix='tick', key=None, data=None):
    s = StringIO()

    if data is not None:
        for row in data:
            print(row, file=s)
    else:
        print('None', file=s)

    path = get_path(f'../log')
    Path(path).mkdir(parents=True, exist_ok=True)

    with open(f'{path}/{prefix}-{i}.log', 'a') as f:
        f.write(datetime.now().strftime('%d.%m.%Y %H:%M:%S') + '\n')
        if key is not None:
            f.write(f'[{key}]\n')
        f.write(s.getvalue())
        f.write('\n')
        f.write('\n')
