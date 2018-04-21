# -*- mode: python -*-

block_cipher = None
add_files=[('E:\\presetInstaller\\style.css','.'),
('E:\\presetInstaller\\update\\Installer.png','.'),
('E:\\presetInstaller\\update\\Installer2.png','.'),
('E:\\presetInstaller\\update\\Installer3.png','.'),
('E:\\presetInstaller\\update\\Installer4.png','.'),
('E:\\presetInstaller\\update\\Installer4m.png','.'),
('E:\\presetInstaller\\update\\Installer5.png','.'),
('E:\\presetInstaller\\update\\Installer6.png','.'),
('E:\\presetInstaller\\update\\pmlogo.jpg','.')

]

a = Analysis(['testbar.py'],
             pathex=['E:\\presetInstaller\\update'],
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
          console=False,
          icon='pmlogo.ico')
