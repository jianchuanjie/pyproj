# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\PyCharm2016.3.1\\pyproj\\Transitive_closure\\tk.py'],
             pathex=['D:\\PyCharm2016.3.1\\pyproj'],
             binaries=None,
             datas=None,
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
          name='tk',
          debug=False,
          strip=False,
          upx=True,
          console=True )
