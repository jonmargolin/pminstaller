# -*- mode: python -*-

block_cipher = None
add_files=[('E:\\presetInstaller\\style.css','.'),
('E:\\presetInstaller\\Installer.png','.'),
('E:\\presetInstaller\\Installer2.png','.'),
('E:\\presetInstaller\\Installer3.png','.'),
('E:\\presetInstaller\\Installer4.png','.'),
('E:\\presetInstaller\\Installer4m.png','.'),
('E:\\presetInstaller\\Installer5.png','.'),
('E:\\presetInstaller\\Installer6.png','.'),
('E:\\presetInstaller\\pmlogo.jpg','.')

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
          exclude_binaries=True,
          name='testbar',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
             name='pminstaller',
			   icon='pmlogo.ico')
