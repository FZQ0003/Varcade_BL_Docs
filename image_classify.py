#!/usr/bin/python3

import os
import shutil


def main():
    path = './source/images'
    files_list = os.listdir(path)
    for filename in files_list:
        name_list = filename.split('_')
        if len(name_list) > 1:
            path_tmp = path
            for name in name_list[0:-1]:
                path_tmp += '/' + name
                if not os.path.exists(path_tmp):
                    os.makedirs(path_tmp)
            os.rename(
                path + '/' + filename,
                path_tmp + '/' + name_list[-1]
            )


if __name__ == "__main__":
    main()
    print('Done!')
