"""ElevenLabs AI音声革命ガイド - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "ElevenLabs AI音声革命ガイド"
BLOG_DESCRIPTION = "AI音声合成の革命児ElevenLabsの使い方・ボイスクローン・最新機能を毎日更新。評価額110億ドルの超成長AIツールを完全解説。"
BLOG_URL = "https://musclelove-777.github.io/elevenlabs-guide"
BLOG_TAGLINE = "ElevenLabsでAI音声合成の未来を切り拓く日本語情報サイト"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/elevenlabs-guide"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "ElevenLabs 使い方",
    "ElevenLabs 料金・プラン",
    "ボイスクローン",
    "ElevenLabs 最新ニュース",
    "AI音声合成テクニック",
    "ElevenLabs API",
    "AI音声ツール比較",
    "ElevenLabs 活用事例",
]

THEME = {
    "primary": "#000000",
    "accent": "#6366f1",
    "gradient_start": "#000000",
    "gradient_end": "#6366f1",
    "dark_bg": "#0a0a0a",
    "dark_surface": "#1a1a1a",
    "light_bg": "#f5f5f5",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 1
SCHEDULE_HOURS = [12]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "ElevenLabs": [
        {"service": "ElevenLabs", "url": "https://elevenlabs.io", "description": "ElevenLabsに登録する"},
    ],
    "ElevenLabs Pro": [
        {"service": "ElevenLabs Pro", "url": "https://elevenlabs.io/pricing", "description": "ElevenLabs Proプラン"},
    ],
    "AI音声ツール": [
        {"service": "ElevenLabs", "url": "https://elevenlabs.io", "description": "ElevenLabsを無料で試す"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAI音声講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI音声関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI音声関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8095

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-HJLCFVY5TF"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
