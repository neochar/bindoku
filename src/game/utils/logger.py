from datetime import datetime
from io import StringIO


def cleanup_logs():
    import os, shutil
    folder = '../log/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            file_log(0, 'error', 'Failed to delete %s. Reason: %s' % (file_path, e))


def file_log(move, prefix='move', key=None, data=None):
    s = StringIO()

    if data is not None:
        for row in data:
            print(row, file=s)
    else:
        print('None', file=s)

    with open(f'../log/{prefix}-{move}.log', 'a') as f:
        f.write(datetime.now().strftime('%d.%m.%Y %H:%M:%S') + '\n')
        f.write(f'[{key}]\n')
        f.write(s.getvalue())
        f.write('\n')
        f.write('\n')
