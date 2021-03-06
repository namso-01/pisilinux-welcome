#
#
#  Copyright 2016 Metehan Özbek <mthnzbk@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from setuptools import setup, find_packages
from os import listdir, system


langs = []
for file in listdir('languages'):
    if file.endswith('ts'):
        system('lrelease-qt5 languages/{}'.format(file))
        langs.append(('languages/{}'.format(file)).replace('.ts', '.qm'))


system('pyrcc5 welcome.qrc -o welcome/resource.py')

datas = [('/usr/share/applications', ['data/pisilinux-welcome.desktop']),
         ('/etc/skel/.config/autostart', ['data/pisilinux-welcome.desktop']),
         ('/usr/share/icons/hicolor/scalable/apps', ['images/pisilinux-welcome.svg']),
         ('/usr/share/welcome/languages', langs),
         ('/usr/share/welcome/data', ["data/pisilinux-2-0-kurulum-belgesi.pdf", "data/pisilinux-welcome.desktop"])]

setup(
    name = "pisilinux-welcome",
    scripts = ["pisilinux-welcome"],
    packages = find_packages(),
    version = "1.0",
    license = "GPLv3",
    description = "Pisi GNU/Linux welcome application",
    author = "Metehan Özbek",
    author_email = "mthnzbk@gmail.com",
    url = "https://github.com/PisiLinuxNew/pisilinux-welcome",
    keywords = ["PyQt5"],
    data_files = datas
)

