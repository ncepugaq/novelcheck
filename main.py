"""
NovelCheck - Novel Text Intelligent Proofreading Tool

Main entry point
"""
import sys
import os
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    print('NovelCheck v1.0.0')
    print('Checking imports...')

    try:
        import PySide6
        import jieba
        import pypinyin
        import ebooklib
        import chardet
        import lxml
        from bs4 import BeautifulSoup
        print('All imports OK')
    except ImportError as e:
        print(f'ERROR: Missing dependency - {e}')
        print('Please run: pip install -r requirements.txt')
        print('Or double-click setup.bat')
        input('Press Enter to exit...')
        return 1

    try:
        from PySide6.QtWidgets import QApplication, QMessageBox
        from PySide6.QtGui import QFont
    except Exception as e:
        print(f'ERROR: Failed to import PySide6: {e}')
        traceback.print_exc()
        input('Press Enter to exit...')
        return 1

    print('Starting GUI...')

    try:
        app = QApplication(sys.argv)
        app.setApplicationName('NovelCheck')
        app.setOrganizationName('NovelCheck')
        app.setStyle('Fusion')

        font = QFont('Microsoft YaHei', 10)
        if not font.exactMatch():
            font = QFont('SimSun', 10)
        app.setFont(font)

        from novelcheck.ui.main_window import MainWindow
        window = MainWindow()
        window.show()
        print('GUI started successfully')
    except Exception as e:
        print(f'ERROR: Failed to start GUI: {e}')
        traceback.print_exc()
        try:
            QMessageBox.critical(
                None, 'NovelCheck - Startup Error',
                f'Failed to start:\n\n{str(e)}\n\n'
                'Please ensure all dependencies are installed.\n'
                'Run: pip install -r requirements.txt'
            )
        except Exception:
            pass
        input('Press Enter to exit...')
        return 1

    return app.exec()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print(f'FATAL ERROR: {e}')
        traceback.print_exc()
        input('Press Enter to exit...')
        sys.exit(1)
