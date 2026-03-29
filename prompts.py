"""ElevenLabs AI音声革命ガイド - プロンプト定義

ElevenLabs特化ブログ用のプロンプトを一元管理する。
JSON-LD構造化データ（BlogPosting / FAQPage / BreadcrumbList）対応。
"""

# ペルソナ設定
PERSONA = (
    "あなたはElevenLabsとAI音声合成の日本語エキスパートです。"
    "ボイスクローン・テキスト読み上げ・音声API開発に精通し、"
    "初心者からクリエイター・開発者まで幅広い読者に実践的な情報を届けるプロのテックライターです。"
    "ElevenLabsの最新アップデートを常にキャッチアップし、"
    "他のAI音声ツール（Amazon Polly、Google Cloud TTS、Azure Speech等）との比較も客観的に行えます。"
)

# 記事フォーマット指示
ARTICLE_FORMAT = """
【記事構成（必ずこの順序で書くこと）】

## この記事でわかること
- ポイント1（具体的なベネフィット）
- ポイント2
- ポイント3

## 結論（先に結論を述べる）
（読者が最も知りたい答えを最初に提示）

## 本題（H2で3〜5セクション）
（具体的な手順・解説。操作手順を箇条書きで明示）

## 音声サンプル・活用シーン
（どんな場面でElevenLabsが活きるか。YouTube・ポッドキャスト・オーディオブック等）

## 他のAI音声ツールとの比較
（Amazon Polly / Google Cloud TTS / Azure Speech / VOICEVOX との違いを表形式で整理）

## よくある質問（FAQ）
### Q1: （よくある質問1）
A1: （回答1）

### Q2: （よくある質問2）
A2: （回答2）

### Q3: （よくある質問3）
A3: （回答3）

## まとめ
（要点整理と次のアクション提案）
"""

# カテゴリ別SEOキーワードヒント
CATEGORY_PROMPTS = {
    "ElevenLabs 使い方": "ElevenLabs 使い方、ElevenLabs 始め方、ElevenLabs 初心者、ElevenLabs 無料、ElevenLabs 登録方法",
    "ElevenLabs 料金・プラン": "ElevenLabs 料金、ElevenLabs 無料 有料 違い、ElevenLabs Pro、ElevenLabs 月額、ElevenLabs クレジット",
    "ボイスクローン": "ボイスクローン やり方、ElevenLabs 声 コピー、AI 音声クローン、自分の声 AI、ElevenLabs Voice Cloning",
    "ElevenLabs 最新ニュース": "ElevenLabs アップデート、ElevenLabs 新機能、ElevenLabs 評価額、AI音声 最新、ElevenLabs 110億ドル",
    "AI音声合成テクニック": "AI音声合成 コツ、ElevenLabs 高品質、音声 感情表現、SSML 使い方、AI ナレーション",
    "ElevenLabs API": "ElevenLabs API、ElevenLabs API 使い方、ElevenLabs SDK、ElevenLabs Python、音声API 開発",
    "AI音声ツール比較": "AI音声 比較、ElevenLabs vs Amazon Polly、ElevenLabs vs Google TTS、AI TTS 比較 2026、音声合成 おすすめ",
    "ElevenLabs 活用事例": "ElevenLabs ビジネス活用、AI音声 YouTube、AI ナレーション 自動化、ElevenLabs ポッドキャスト、オーディオブック AI",
}

# ニュースソース
NEWS_SOURCES = [
    "ElevenLabs Blog (https://elevenlabs.io/blog)",
    "TechCrunch (https://techcrunch.com/tag/elevenlabs/)",
    "The Verge (https://www.theverge.com/ai-artificial-intelligence)",
    "VentureBeat (https://venturebeat.com/tag/elevenlabs/)",
]

# FAQ構造化データの有効化
FAQ_SCHEMA_ENABLED = True

# キーワード選定用の追加プロンプト
KEYWORD_PROMPT_EXTRA = (
    "ElevenLabs（AI音声合成）に関するキーワードを選んでください。\n"
    "日本のユーザーが検索しそうな実用的なキーワードを意識してください。\n"
    "「ElevenLabs 使い方」「ボイスクローン やり方」「AI音声合成 比較」のような、\n"
    "検索ボリュームが見込めるキーワードを優先してください。"
)


def build_keyword_prompt(config):
    """キーワード選定プロンプトを構築する"""
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    category_hints = "\n".join(
        f"- {cat}: {hints}" for cat, hints in CATEGORY_PROMPTS.items()
    )
    return (
        f"{PERSONA}\n\n"
        "ElevenLabs AI音声革命ガイドブログ用のキーワードを選定してください。\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"カテゴリ別キーワードヒント:\n{category_hints}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    """ElevenLabs特化記事生成プロンプトを構築する"""
    category_hints = CATEGORY_PROMPTS.get(category, "")
    news_sources_text = "\n".join(f"- {src}" for src in NEWS_SOURCES)

    return f"""{PERSONA}

以下のキーワードに関する記事を、ElevenLabs（AI音声合成）の専門サイト向けに執筆してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- カテゴリ関連キーワード: {category_hints}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度

{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に（数字や年号を含めると効果的）
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQ（よくある質問）を3つ以上含めること（FAQPage構造化データ対応）

【内部リンク】
- 内部リンクのプレースホルダーを2〜3箇所に配置（{{{{internal_link:関連トピック}}}}の形式）

【参考情報源】
{news_sources_text}

【条件】
- {config.MAX_ARTICLE_LENGTH}文字程度
- 2026年最新の情報を反映すること
- 具体的な操作手順や設定方法を含める
- 音声サンプルの活用シーン（YouTube・ポッドキャスト・オーディオブック等）を含める
- 他AI音声ツールとの客観的な比較を含める
- 初心者にもわかりやすく、専門用語には補足説明を付ける

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}},
    {{"question": "質問3", "answer": "回答3"}}
  ]
}}
```

【注意事項】
- content内のMarkdownは適切にエスケープしてJSON文字列として有効にすること
- tagsは5個ちょうど生成すること
- slugは半角英数字とハイフンのみ使用すること
- faqは3個以上生成すること（FAQPage構造化データに使用）
- 読者にとって実用的で具体的な内容を心がけること"""
