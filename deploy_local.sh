#!/bin/bash

# ----------------------------------------
# 功能介绍
# 将代码库中的配置文件复制到指定位置
# ----------------------------------------
cp vimrc ~/.vimrc
cp bash_profile ~/.bash_profile
cp tmux.conf ~/.tmux.conf
cp gitconfig ~/.gitconfig
cp -Rf vim/* ~/.vim/
cp -f Templates/* ~/Templates/

echo "if you are using Ubuntu, romove ~/.bash_profile"

