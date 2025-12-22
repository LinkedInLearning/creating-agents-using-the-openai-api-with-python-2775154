# PythonでOpenAI APIを使ったエージェントを作成する
LinkedInラーニングの「PythonでOpenAI APIを使ったエージェントを作成する」コース用のリポジトリです。このコースは[LinkedInラーニング][lil-course-url]で視聴できます。

![lil-thumbnail-url]

OpenAIのAPIはChat Completion APIからResponse APIに進化し、Agents SDKもリリースされました。これらの新しい技術とPythonのプログラムでより簡単に複雑なAIエージェントを作成できます。このコースではOpenAIのResponse APIの使い方を始め、Agents SDKを使ったエージェントの作り方を説明します。Agents SDKを使えば、PythonのプログラムでドキュメントやWeb検索、自作の関数を呼び出すエージェントを作り、それらのエージェントを連携させることも可能です。このコースで学習すれば、複雑な仕組みを組み合わせなくても、OpenAIの提供する環境だけで自分専用の高度なエージェントを作成できるようになるでしょう。

## Installing
- エクササイズファイルを使うにはOpenAI API keyが必要です。次のサイト取得してください。[platform.openai.com](https://platform.openai.com)
## GitHub Codespacesdで実行するには
1. CodeボタンをクリックしてCodespacesを選んでください。
3. 新規Codespaceを作成するか既存のCodespaceを選んでください。
4. .envファイルをrootフォルダに作成してください。
5. OPENAI_API_KEY=に続けて取得したOpenAI API keyを.envに記入してください。
6. .envファイルをGitHub上ではなく、Codespaceだけに置くことでOpenAI API keyの誤使用、盗用を避けます。
## Windowsで実行するには
- PowerShellで次のコマンドを実行する。
setx OPENAI_API_KEY "your_api_key_here"
- もしくはエクササイズファイル内のコードファイルと同じフォルダに.envファイルを配置してください。
- 詳細は次のページを参照してください。https://platform.openai.com/docs/quickstart

## GitHub Codespacesについて
プログラミング言語を学ぶ最良の方法は、実際にそれを使用することです。それがこのコースがGitHub Codespacesと統合されている理由です。GitHub Codespacesは、あなたが普段使っているIDEのすべての機能を提供するクラウド上の手軽な開発環境です。ローカルマシンのセットアップも必要ありません。 GitHub Codespacesを使えば、あなたが職場で使っている他のツールを使用しながら、どのパソコンからでもいつでもプログラミングの実践的な練習ができます。
5ｍ
## インストラクター

金宏和實

株式会社イーザー副社長、テクニカルライター


[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/creating-agents-using-the-openai-api-with-python
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4E0DAQFwyAFT9m_XEw/learning-public-crop_675_1200/B4EZs384BDIQAc-/0/1766170263978?e=2147483647&v=beta&t=Vv5BDNOAO_aFQ70IX79g8SpHjNnTkgkSRFLjlpoSgMM