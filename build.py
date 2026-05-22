"""
NovelCheck Build Script

Use PyInstaller to package as Windows executable
"""
import os
import sys
import subprocess
import shutil


def build():
    """Build executable program"""
    print('=' * 60)
    print('NovelCheck Build Script')
    print('=' * 60)

    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    print('\n[1/3] Checking dependencies...')
    deps_ok = True
    dep_list = [
        ('PySide6', 'PySide6'),
        ('jieba', 'jieba'),
        ('pypinyin', 'pypinyin'),
        ('ebooklib', 'ebooklib'),
        ('bs4', 'beautifulsoup4'),
        ('chardet', 'chardet'),
        ('lxml', 'lxml'),
    ]
    for mod, name in dep_list:
        try:
            __import__(mod)
            print(f'   {name:20s} OK')
        except ImportError:
            print(f'   {name:20s} NOT INSTALLED')
            deps_ok = False

    if not deps_ok:
        print('\n   Please run: pip install -r requirements.txt')
        return False

    print('\n[2/3] Cleaning old builds...')
    for d in ['build', 'dist']:
        if os.path.exists(d):
            try:
                shutil.rmtree(d)
                print(f'   Cleaned {d} directory')
            except Exception as e:
                print(f'   Failed to clean {d} directory: {e}')

    spec_file = os.path.join(project_dir, 'NovelCheck.spec')
    if os.path.exists(spec_file):
        try:
            os.remove(spec_file)
            print(f'   Deleted old spec file')
        except Exception:
            pass

    print('\n[3/3] Building (this may take a few minutes)...')
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--name=NovelCheck',
        '--windowed',
        '--onefile',
        '--clean',
        '--add-data', f'novelcheck{os.pathsep}novelcheck',
        '--add-data', f'ai_config.json{os.pathsep}.',
        '--hidden-import', 'novelcheck',
        '--hidden-import', 'novelcheck.core',
        '--hidden-import', 'novelcheck.core.corrector',
        '--hidden-import', 'novelcheck.core.ad_detector',
        '--hidden-import', 'novelcheck.core.garbled',
        '--hidden-import', 'novelcheck.core.semantic',
        '--hidden-import', 'novelcheck.core.ai_corrector',
        '--hidden-import', 'novelcheck.core.engine',
        '--hidden-import', 'novelcheck.io',
        '--hidden-import', 'novelcheck.io.txt_handler',
        '--hidden-import', 'novelcheck.io.epub_handler',
        '--hidden-import', 'novelcheck.ui',
        '--hidden-import', 'novelcheck.ui.main_window',
        '--hidden-import', 'novelcheck.data',
        '--hidden-import', 'novelcheck.data.strings',
        '--hidden-import', 'jieba',
        '--hidden-import', 'pypinyin',
        '--hidden-import', 'ebooklib',
        '--hidden-import', 'bs4',
        '--hidden-import', 'chardet',
        '--hidden-import', 'lxml',
        '--hidden-import', 'openai',
        '--collect-all', 'jieba',
        '--collect-all', 'pypinyin',
        'main.py',
    ]

    try:
        result = subprocess.run(cmd, capture_output=False)
        if result.returncode == 0:
            exe_path = os.path.join(project_dir, 'dist', 'NovelCheck.exe')
            if os.path.exists(exe_path):
                size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                print(f'\nBuild successful!')
                print(f'Executable: {exe_path}')
                print(f'File size:  {size_mb:.1f} MB')
                return True
            else:
                print('\nBuild completed, but exe file not found. Check error output above.')
                return False
        else:
            print('\nBuild failed (exit code: {}). Check error messages above.'.format(result.returncode))
            return False
    except Exception as e:
        print(f'\nError during build: {e}')
        return False


if __name__ == '__main__':
    success = build()
    if not success:
        input('\nPress Enter to exit...')
        sys.exit(1)
