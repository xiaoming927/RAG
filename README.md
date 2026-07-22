# KnowledgeBase-RAG-LLM-System
基于 Streamlit + LangChain 搭建的
**本地知识库 RAG 问答系统**
适合 AI 大模型入门、RAG 检索增强学习、简历项目展示

## ✨ 项目简介
本项目是一套
**轻量化、可快速部署的私有知识库问答系统**

<p align="center">
<img src="111.png" width="800">
</p>
<p align="center">项目运行效果图</p>
。
支持网页端上传自定义文档，自动向量化存入本地向量库，结合大模型实现
**私有内容 RAG 问答**
。

无需部署复杂后端，纯本地运行，适合初学者学习 RAG 完整链路：
文档上传 → 文本切分 → 向量入库 → 语义检索 → LLM 增强问答

## 🎯 核心功能
### 1. 知识库上传服务
-
 Streamlit 可视化网页上传 TXT 文本文件
-
 自动读取、解析文档内容
-
 智能文本切分（RecursiveCharacterTextSplitter）
-
 MD5 文件去重机制，避免重复入库
-
 Chroma 向量库本地持久化存储

### 2. RAG 智能问答服务
-
 仿 ChatGPT 对话 UI，流式思维链输出
- 基于私有知识库**检索增强回答**
，杜绝幻觉
-
 完整上下文记忆，支持多轮连续对话
-
 本地文件持久化存储聊天记录
-
 LangChain 标准 RAG 链路组装

### 3. 项目演示
-
 内置衣物尺码、材质保养、穿搭建议等业务测试数据
-
 可一键替换为任意行业私有知识库（办公、教育、运维、产品手册等）

## 🛠 技术栈
-
 前端框架：Streamlit
-
 大模型框架：LangChain
-
 大模型：通义千问 Qwen3-max
-
 嵌入模型：DashScope text-embedding-v4
-
 向量数据库：Chroma
-
 开发语言：Python

## 📁 项目结构
￼
KnowledgeBase-RAG-LLM-System/
├── app_upload.py # 知识库上传页面
├── app_chat.py # RAG 对话问答页面
├── knowledge_base.py # 文档解析、切分、去重、入库
├── rag.py # RAG 问答链路组装
├── vector_stores.py # 向量库初始化与检索封装
├── file_history_store.py # 对话历史持久化
├── config_data.py # 全局参数配置
├── requirements.txt # 项目依赖
└── assets/ # 素材与演示资源
plaintext
￼
￼
￼
## ⚙️ 环境部署
### 1. 安装依赖
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
￼
2. 环境变量配置
需要配置阿里百炼 Key 用于模型调用：
bash
￼
￼
运行
￼
￼
# Windows
set DASHSCOPE_API_KEY=
你的密钥

# Mac / Linux
export DASHSCOPE_API_KEY=
你的密钥
￼
可在 config_data.py 自定义：切片大小、检索数量、模型参数、向量库路径等。
🚀 快速启动
1. 启动知识库上传服务
bash
￼
￼
运行
￼
￼
streamlit run app_upload.py
￼
上传 .txt 私有文档，自动完成向量化入库。
2. 启动智能问答服务
bash
￼
￼
运行
￼
￼
streamlit run app_qa.py
￼
基于上传的私有知识库，进行精准 RAG 问答。
❓ 常见问题
Q1：上传文件后问答无对应内容
• 向量库存放路径不一致
• collection_name 集合名不统一
• 文件未成功写入、切片参数过大
Q2：回答卡顿、无流式输出
• 网络波动导致模型响应慢
• chunk 切片、检索 TopK 参数不合理
Q3：运行报错路径异常
优先检查 config_data.py 路径配置、环境变量是否配置成功。
💡 项目优化方向（可进阶升级）
• 接入 Rerank 重排序模型，大幅提升检索精度
• 支持 PDF / Word / Markdown 多格式文档解析
• 替换 Chroma 为 FAISS / Milvus 企业级向量库
• 增加用户登录、会话隔离
• 对接 LangGraph 实现智能体问答
• 增加问答日志统计、知识库管理后台
