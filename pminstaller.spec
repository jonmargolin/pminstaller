# -*- mode: python -*-
block_cipher = None
add_files=[('C:\\Users\jonma\\PycharmProjects\\installer\\style.css','.'),
('C:\\Users\jonma\\PycharmProjects\\installer\\Installer.png','.'),
('C:\\Users\jonma\\PycharmProjects\\installer\\Installer2.png','.'),
('C:\\Users\jonma\\PycharmProjects\\installer\\Installer3.png','.'),
('C:\\Users\jonma\\PycharmProjects\\installer\\Installer4.png','.'),
('C:\\Users\jonma\\PycharmProjects\\installer\\Installer4m.png','.'),
('C:\\Users\jonma\\PycharmProjects\\installer\\Installer5.png','.'),
('C:\\Users\jonma\\PycharmProjects\\installer\\Installer6.png','.'),
('C:\\Users\jonma\\PycharmProjects\\installer\\pmlogo.jpg','.')

]

a = Analysis(['testbar.py'],
             pathex=['C:\\Users\jonma\\PycharmProjects\\installer'],
             binaries=[],
             datas=add_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pminstaller',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='pmlogo.ico')
