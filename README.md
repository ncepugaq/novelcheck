# NovelCheck

利用 AI 纠正小说错别字及删除广告的桌面应用程序。

##  功能特性

- **错别字识别与修正**：精确识别中文常见错别字并给出修改建议，支持形近字、音近字、成语等场景
- **广告文字检测与删除**：自动识别并移除嵌入在正文中的广告内容（如"奇书网"、"笔趣阁"等）
- **乱码清理**：检测并删除文本中的乱码字符和无意义符号
- **语义错误纠正**：识别人物名称混淆等上下文相关错误
- **AI 智能校对**：支持调用本地 Ollama 模型或云端 AI API 进行智能纠错
- **多格式支持**：支持 `.txt` 和 `.epub` 格式的文件导入与导出
- **图形界面**：基于 PySide6 开发的简洁桌面 UI，支持原文与结果左右对比

## ? 快速开始

### 环境要求

- Windows 10/11
- Python 3.10+

### 安装依赖

```powershell
pip install -r requirements.txt
```

### 运行程序

```powershell
python main.py
```

或双击 `run.bat`

## ? 使用说明

### 导入文件

点击 **导入文件** 按钮（快捷键 `Ctrl+O`），选择您的小说文件。

### 开始纠错

点击 **开始纠错** 按钮（快捷键 `Ctrl+R`），软件将依次执行：
1. 清理乱码字符
2. 检测并删除广告内容
3. 识别并修正错别字
4. 检查语义错误

### 查看结果

纠错完成后，左侧显示原文，右侧显示纠错后的文本。问题位置会以不同颜色高亮标记。

### 导出文件

点击 **导出结果** 按钮（快捷键 `Ctrl+S`），保存纠错后的文本。

## ? AI 校对配置

NovelCheck 支持两种 AI 模式：

| 模式 | 说明 |
|------|------|
| **本地 (Ollama)** | 使用本地运行的 Ollama 模型，无需 API Key |
| **云端 API** | 使用兼容 OpenAI API 的云端服务（如 OpenAI、DeepSeek 等） |

支持的模型类型：
- **中文原生模型**：Qwen、Yi、DeepSeek、豆包等
- **多语言模型**：Gemma、Llama 等（自动切换英文提示模板）
- **推理模型**：DeepSeek-R1、QwQ、Qwen3、o1 等（自动优化超时和 token 配置）

## ? 打包为可执行文件

```powershell
pip install pyinstaller
pyinstaller NovelCheck.spec
```

打包完成后，可执行文件位于 `dist\NovelCheck.exe`

##  运行测试

```powershell
python test.py
```

## ? 许可证

本项目采用 [Apache-2.0 License](LICENSE)。
