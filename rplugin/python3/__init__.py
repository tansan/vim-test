# coding: utf-8

import neovim


@neovim.plugin
class NeoTest(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command('Helloworld')
    def echo(self):
        self.nvim.command("echo '[VIM-TEST] hello, world'")
