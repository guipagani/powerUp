from powerup.browser_script import BroswerScript

open = BroswerScript()

open.command_press('win')
open.command_write('chrome')
open.command_press('enter')
open.command_press('tab')
open.command_press('tab')
open.command_press('tab')
open.command_press('tab')
open.command_press('enter')

login = BroswerScript()

login.command_write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
login.command_press('enter')
