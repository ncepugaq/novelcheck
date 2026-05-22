# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [('novelcheck', 'novelcheck'), ('ai_config.json', '.')]
binaries = []
hiddenimports = ['novelcheck', 'novelcheck.core', 'novelcheck.core.corrector', 'novelcheck.core.ad_detector', 'novelcheck.core.garbled', 'novelcheck.core.semantic', 'novelcheck.core.ai_corrector', 'novelcheck.core.engine', 'novelcheck.io', 'novelcheck.io.txt_handler', 'novelcheck.io.epub_handler', 'novelcheck.ui', 'novelcheck.ui.main_window', 'novelcheck.data', 'novelcheck.data.strings', 'jieba', 'pypinyin', 'ebooklib', 'bs4', 'chardet', 'lxml', 'openai']
tmp_ret = collect_all('jieba')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('pypinyin')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='NovelCheck',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
