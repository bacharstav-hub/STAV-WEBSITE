# -*- coding: utf-8 -*-
"""
i18n.py — Internationalization module (English / Hebrew).

Pure-Python module (no Streamlit imports) so it can be unit-tested in isolation.

Public API:
    LANGUAGES            : display-name -> language code mapping for the UI selector
    t(key, lang)         : translate a UI string key
    instrument_name(...) : localized display name for a ticker
    is_rtl(lang)         : True for right-to-left languages
    BASE_CSS / RTL_CSS   : style blocks injected by app.py
"""

from __future__ import annotations

from typing import Dict

LANGUAGES: Dict[str, str] = {
    "English": "en",
    "עברית": "he",
}

RTL_LANGS = {"he"}


def is_rtl(lang: str) -> bool:
    return lang in RTL_LANGS


# --------------------------------------------------------------------------- #
# UI strings
# --------------------------------------------------------------------------- #
_T: Dict[str, Dict[str, str]] = {
    # ---- global / chrome ----
    "app_title": {
        "en": "Macro & Equity Analytics Dashboard",
        "he": "דשבורד אנליטיקות מאקרו ומניות",
    },
    "app_caption": {
        "en": "Daily macro pulse, sector capital flows and an aggressive-movers stock scanner — powered by Yahoo Finance.",
        "he": "דופק מאקרו יומי, זרימות הון סקטוריאליות וסורק מניות אגרסיביות — מבוסס נתוני Yahoo Finance.",
    },
    "language_label": {"en": "Language / שפה", "he": "שפה / Language"},
    "refresh_button": {"en": "Refresh data", "he": "רענון נתונים"},
    "last_updated": {"en": "Last updated", "he": "עדכון אחרון"},
    "disclaimer": {
        "en": "For research & education only. Not investment advice.",
        "he": "המידע להמחשה ולמחקר בלבד ואינו מהווה ייעוץ השקעות.",
    },
    "tab_macro": {
        "en": "📊 Daily Macro Pulse & Sector Flows",
        "he": "📊 דופק מאקרו וזרימות סקטוריאליות",
    },
    "tab_scanner": {
        "en": "🔥 Aggressive Stock Scanner",
        "he": "🔥 סורק מניות אגרסיביות",
    },
    # ---- landing page (app.py) ----
    "nav_hint": {
        "en": "Navigate between pages from the sidebar, or use the shortcuts below.",
        "he": "נווטו בין העמודים דרך סרגל הצד, או השתמשו בקיצורי הדרך שלמטה.",
    },
    "home_pages_header": {"en": "Dashboard pages", "he": "עמודי הדשבורד"},
    "home_macro_desc": {
        "en": "Global indices snapshot, VIX volatility regimes, US yield curve, "
              "commodities/FX and Sector Capital Flow Momentum across 1D / 5D / 1M horizons.",
        "he": "תמונת מצב של מדדים גלובליים, משטרי תנודתיות VIX, עקום התשואות האמריקאי, "
              "סחורות ומט\"ח, ומומנטום זרימות הון סקטוריאליות באופקי יום / שבוע / חודש.",
    },
    "home_scanner_desc": {
        "en": "Automated engine detecting aggressive movers: ROC, RVOL vs 20-day average "
              "volume and ATR expansion — with a filterable leaderboard and stock deep-dive.",
        "he": "מנוע אוטומטי לזיהוי תנועות אגרסיביות: ROC, נפח יחסי מול ממוצע 20 ימים "
              "והתרחבות ATR — כולל לוח מובילים ניתן לסינון וצלילה למניה בודדת.",
    },
    "open_macro": {"en": "Open Macro Analysis →", "he": "← לניתוח המאקרו"},
    "open_scanner": {"en": "Open Stock Screener →", "he": "← לסורק המניות"},
    "home_snapshot_title": {"en": "Quick market snapshot", "he": "תמונת שוק מהירה"},
    "top_inflow_label": {"en": "Top sector inflow", "he": "כניסת ההון המובילה"},
    "data_error": {
        "en": "Failed to load market data from Yahoo Finance. Please refresh in a moment.",
        "he": "שגיאה בטעינת נתוני שוק מ-Yahoo Finance. נסו לרענן בעוד רגע.",
    },
    "no_data": {"en": "No data available.", "he": "אין נתונים זמינים."},
    "loading_macro": {"en": "Loading macro data…", "he": "טוען נתוני מאקרו…"},
    "loading_scan": {
        "en": "Scanning the universe… this can take up to a minute on first run",
        "he": "סורק את יקום המניות… הריצה הראשונה עשויה לקחת עד דקה",
    },

    # ---- company screener page (Finviz-style) ----
    "tab_screener2": {"en": "🏢 Company Screener", "he": "🏢 סורק חברות"},
    "home_screener2_desc": {
        "en": "Finviz-style fundamental screener over the whole US market: filter by sector, "
              "market cap, P/E and dividend — then deep-dive into company profile, management, "
              "financial statements and an optional Gemini AI analysis.",
        "he": "סורק פונדמנטלי בסגנון Finviz על כל השוק האמריקאי: סינון לפי סקטור, שווי שוק, "
              "מכפיל רווח ודיבידנד — עם צלילה לפרופיל החברה, ההנהלה, הדוחות הכספיים "
              "וניתוח AI אופציונלי של Gemini.",
    },
    "open_screener2": {"en": "Open Company Screener →", "he": "← לסורק החברות"},
    "screener2_caption": {
        "en": "Server-side Yahoo Finance screener over the whole US market. Pick filters, "
              "then select any result (or type a ticker) for a full company deep-dive.",
        "he": "סורק צד-שרת של Yahoo Finance על כל השוק האמריקאי. בחרו מסננים, ואז בחרו "
              "תוצאה (או הקלידו טיקר) לצלילה מלאה לחברה.",
    },
    "filters_title": {"en": "🔍 Screening filters", "he": "🔍 מסנני סריקה"},
    "f_sector": {"en": "Sector", "he": "סקטור"},
    "f_all": {"en": "All", "he": "הכל"},
    "f_min_cap": {"en": "Min market cap", "he": "שווי שוק מינימלי"},
    "f_max_pe": {"en": "Max P/E (TTM)", "he": "מכפיל רווח מקסימלי"},
    "f_min_div": {"en": "Min dividend yield (%)", "he": "תשואת דיבידנד מינימלית (%)"},
    "f_sort": {"en": "Sort by", "he": "מיון לפי"},
    "sort_cap": {"en": "Market cap", "he": "שווי שוק"},
    "sort_pe": {"en": "P/E", "he": "מכפיל רווח"},
    "sort_div": {"en": "Dividend yield", "he": "תשואת דיבידנד"},
    "sort_chg": {"en": "Daily change", "he": "שינוי יומי"},
    "sort_vol": {"en": "Volume", "he": "מחזור"},
    "results_title": {"en": "Screener results", "he": "תוצאות הסריקה"},
    "screener_failed": {
        "en": "Yahoo screener is unavailable right now — try again shortly.",
        "he": "סורק Yahoo אינו זמין כרגע — נסו שוב בעוד רגע.",
    },
    "col_company": {"en": "Company", "he": "חברה"},
    "col_cap_b": {"en": "Cap ($B)", "he": "שווי ($B)"},
    "col_pe_t": {"en": "P/E (TTM)", "he": "מכפיל רווח"},
    "col_pe_f": {"en": "Fwd P/E", "he": "מכפיל עתידי"},
    "col_eps": {"en": "EPS (TTM)", "he": "רווח למניה"},
    "col_div_pct": {"en": "Div %", "he": "דיבידנד %"},
    "col_chg": {"en": "Change %", "he": "שינוי %"},
    "col_vol_m": {"en": "Volume (M)", "he": "מחזור (M)"},
    "deep_dive_title": {"en": "🔎 Company Deep-Dive", "he": "🔎 צלילה לחברה"},
    "select_company": {"en": "Select a company from the results", "he": "בחרו חברה מהתוצאות"},
    "or_type_ticker": {"en": "Or type any ticker", "he": "או הקלידו טיקר כלשהו"},
    "f_industry": {"en": "Industry (sub-sector)", "he": "תעשייה (תת-סקטור)"},
    "go_deepdive": {
        "en": "Open Company Deep-Dive for these results →",
        "he": "← לצלילה לחברה עבור התוצאות האלה",
    },
    "deepdive_hint": {
        "en": "Search any listed stock by ticker or company name — the whole market, not a fixed list.",
        "he": "חפשו כל מניה נסחרת לפי טיקר או שם חברה — כל השוק, לא רשימה סגורה.",
    },
    "search_label": {
        "en": "Search any stock (ticker or name)",
        "he": "חפשו כל מניה (טיקר או שם חברה)",
    },
    "search_help": {
        "en": "Covers the entire market — every listed stock, from mega caps down past $200M. Type and press Enter.",
        "he": "מכסה את כל השוק — כל מניה נסחרת, ממגה-קאפ ועד הרבה מתחת ל-$200M שווי שוק. הקלידו ולחצו Enter.",
    },
    "search_pick": {"en": "Matches", "he": "התאמות"},
    "search_no_results": {
        "en": "No matches found — check the spelling.",
        "he": "לא נמצאו התאמות — בדקו את האיות.",
    },
    "uni_screen": {"en": "Last screener results", "he": "תוצאות הסריקה האחרונות"},
    "no_screener_results_yet": {
        "en": "No screener results in this session yet — run the Company Screener first, or just type a ticker.",
        "he": "אין עדיין תוצאות סריקה בסשן הזה — הריצו קודם את סורק החברות, או פשוט הקלידו טיקר.",
    },
    "profile_unavailable": {
        "en": "Company profile unavailable for this ticker.",
        "he": "פרופיל החברה אינו זמין עבור הטיקר הזה.",
    },
    "profile_employees": {"en": "Employees", "he": "עובדים"},
    "profile_country": {"en": "Country", "he": "מדינה"},
    "profile_website": {"en": "Website", "he": "אתר החברה"},
    "profile_industry": {"en": "Industry", "he": "תעשייה"},
    "business_summary": {"en": "📄 Business summary", "he": "📄 תקציר עסקי"},
    "management_title": {"en": "👔 Management & Officers", "he": "👔 הנהלה ונושאי משרה"},
    "col_name": {"en": "Name", "he": "שם"},
    "col_title": {"en": "Title", "he": "תפקיד"},
    "col_age": {"en": "Age", "he": "גיל"},
    "col_pay": {"en": "Total pay ($)", "he": "שכר כולל ($)"},
    "ratios_title": {"en": "Key ratios & valuation", "he": "יחסים פיננסיים והערכת שווי"},
    "r_pb": {"en": "P/B", "he": "מכפיל הון"},
    "r_roe": {"en": "ROE", "he": "תשואה על ההון"},
    "r_margin": {"en": "Profit margin", "he": "שולי רווח נקי"},
    "r_op_margin": {"en": "Operating margin", "he": "שולי רווח תפעולי"},
    "r_rev_growth": {"en": "Revenue growth (YoY)", "he": "צמיחת הכנסות (שנתי)"},
    "r_target": {"en": "Analyst target", "he": "יעד אנליסטים"},
    "r_recommendation": {"en": "Recommendation", "he": "המלצה"},
    "r_beta": {"en": "Beta", "he": "בטא"},
    "financials_title": {
        "en": "📑 Financial Statements (annual)",
        "he": "📑 דוחות כספיים (שנתיים)",
    },
    "stmt_income": {"en": "📈 Income Statement", "he": "📈 דוח רווח והפסד"},
    "stmt_balance": {"en": "🏦 Balance Sheet", "he": "🏦 מאזן"},
    "stmt_cash": {"en": "💵 Cash Flow", "he": "💵 תזרים מזומנים"},
    "stmt_income_q": {"en": "Quarterly income statement", "he": "דוח רווח והפסד רבעוני"},
    "values_in_millions": {
        "en": "Values in $ millions (EPS in $).",
        "he": "הערכים במיליוני דולרים (רווח למניה בדולרים).",
    },
    "full_statement": {"en": "Full statement", "he": "הדוח המלא"},
    "financials_unavailable": {
        "en": "Financial statements unavailable for this ticker.",
        "he": "דוחות כספיים אינם זמינים עבור הטיקר הזה.",
    },
    "ai_title": {"en": "🤖 AI Analysis (Gemini)", "he": "🤖 ניתוח AI (Gemini)"},
    "ai_key_label": {
        "en": "Gemini API key — get one free at aistudio.google.com/apikey",
        "he": "מפתח API של Gemini — מקבלים חינם ב-aistudio.google.com/apikey",
    },
    "ai_key_configured": {
        "en": "🔑 A Gemini API key is configured on the server — analyses are ready to run. "
              "The key is never sent to the browser.",
        "he": "🔑 מפתח Gemini מוגדר בצד השרת — הניתוחים מוכנים להפעלה. "
              "המפתח לעולם לא נשלח לדפדפן.",
    },
    "ai_generate": {"en": "✨ Generate analysis", "he": "✨ הפקת ניתוח"},
    "ai_error": {
        "en": "Gemini request failed — check the API key and try again.",
        "he": "הבקשה ל-Gemini נכשלה — בדקו את המפתח ונסו שוב.",
    },
    "ai_disclaimer": {
        "en": "AI-generated content — verify before making decisions.",
        "he": "תוכן שנוצר על ידי בינה מלאכותית — יש לאמת לפני קבלת החלטות.",
    },

    # ---- options scanner page (credit spreads) ----
    "tab_options_scanner": {"en": "🧮 Options Scanner", "he": "🧮 סורק אופציות"},
    "open_options_scanner": {
        "en": "Options / Credit-Spread Scanner →",
        "he": "← סורק אופציות ומרווחי אשראי",
    },
    "opt_scan_caption": {
        "en": "Finds symbols whose option premium is relatively expensive (high IV Rank / "
              "Percentile) — the raw material for high-probability credit spreads in small accounts.",
        "he": "מאתר סימבולים שהפרמיה שלהם יקרה יחסית (IV Rank / Percentile גבוהים) — "
              "חומר הגלם למרווחי אשראי בהסתברות גבוהה בחשבונות קטנים.",
    },
    "opt_method_note": {
        "en": "Methodology: current IV is the live at-the-money IV from the ~30-DTE option chain. "
              "Yahoo provides no historical IV, so Rank/Percentile compare it against the past "
              "year's realized-volatility distribution (rolling 21-session, annualized) — a "
              "volatility-risk-premium reading: high = options priced rich vs actual movement.",
        "he": "מתודולוגיה: ה-IV הנוכחי הוא IV חי בכסף משרשרת האופציות בפקיעה של כ-30 יום. "
              "ל-Yahoo אין IV היסטורי, ולכן ה-Rank/Percentile מחושבים מול התפלגות התנודתיות "
              "בפועל של השנה האחרונה (חלון 21 ימים, שנתי) — קריאת פרמיית סיכון תנודתיות: "
              "גבוה = אופציות מתומחרות ביוקר ביחס לתנועה האמיתית.",
    },
    "opt_min_rank": {
        "en": "Min IV Rank / Percentile (%)",
        "he": "IV Rank / Percentile מינימלי (%)",
    },
    "opt_candidates": {"en": "Candidates", "he": "מועמדות"},
    "opt_richest": {"en": "Richest premium", "he": "הפרמיה היקרה ביותר"},
    "opt_chain_failed": {
        "en": "Option chain unavailable for:",
        "he": "שרשרת אופציות לא זמינה עבור:",
    },
    "col_cur_iv": {"en": "IV (30D ATM)", "he": "IV ‏(30 יום ATM)"},
    "col_hv30": {"en": "HV 30D", "he": "תנודתיות בפועל 30 יום"},
    "col_iv_hv": {"en": "IV / HV", "he": "IV / HV"},
    "col_iv_rank": {"en": "IV Rank", "he": "IV Rank"},
    "col_iv_pctile": {"en": "IV Percentile", "he": "IV Percentile"},
    "col_exp_move": {"en": "1σ move 30D ($)", "he": "תנועת 1σ ל-30 יום ($)"},
    "col_exp_move_pct": {"en": "1σ move (%)", "he": "תנועת 1σ (%)"},
    "col_dte": {"en": "DTE", "he": "ימים לפקיעה"},
    "opt_rank_chart": {
        "en": "IV Rank by symbol (threshold marked)",
        "he": "IV Rank לפי סימבול (הסף מסומן)",
    },
    "opt_card_title": {"en": "📇 Symbol card", "he": "📇 כרטיס סימבול"},
    "opt_pick_symbol": {"en": "Pick a symbol", "he": "בחרו סימבול"},
    "opt_range": {
        "en": "Expected 1σ range (30D)",
        "he": "טווח 1σ צפוי (30 יום)",
    },
    "opt_hv_chart": {
        "en": "Realized volatility (1Y) vs current IV",
        "he": "תנודתיות בפועל (שנה) מול IV נוכחי",
    },
    "opt_cur_iv_line": {"en": "Current IV", "he": "IV נוכחי"},
    "strat_title": {"en": "💡 Suggested Strategies", "he": "💡 אסטרטגיות מומלצות"},
    "strat_note": {
        "en": "Defined-risk premium-selling structures with short strikes at ~1σ, priced from the "
              "live chain at bid/ask mid, per 1 contract (×100 shares). The ⭐ pick follows the "
              "price-trend bias vs the 20-day average.",
        "he": "מבני מכירת פרמיה בסיכון מוגדר עם סטרייקים מכורים סביב 1σ, מתומחרים מהשרשרת החיה "
              "לפי אמצע Bid/Ask, לחוזה אחד (×100 מניות). הבחירה המסומנת ב-⭐ נגזרת מהטיית "
              "המגמה מול ממוצע 20 הימים.",
    },
    "strat_bull_put": {"en": "Bull Put Spread", "he": "מרווח פוט שורי (Bull Put)"},
    "strat_bear_call": {"en": "Bear Call Spread", "he": "מרווח קול דובי (Bear Call)"},
    "strat_iron_condor": {"en": "Iron Condor", "he": "איירון קונדור (Iron Condor)"},
    "strat_recommended": {"en": "Recommended", "he": "מומלצת"},
    "bias_label": {"en": "Trend bias", "he": "הטיית מגמה"},
    "bias_up": {"en": "Bullish — above the 20-day MA", "he": "שורית — מעל ממוצע 20 ימים"},
    "bias_down": {"en": "Bearish — below the 20-day MA", "he": "דובית — מתחת לממוצע 20 ימים"},
    "bias_neutral": {"en": "Neutral — near the 20-day MA", "he": "ניטרלית — סביב ממוצע 20 הימים"},
    "strat_action": {"en": "Action", "he": "פעולה"},
    "strat_sell": {"en": "SELL", "he": "מכירה"},
    "strat_buy": {"en": "BUY", "he": "קנייה"},
    "strat_type": {"en": "Type", "he": "סוג"},
    "strat_type_put": {"en": "Put", "he": "פוט"},
    "strat_type_call": {"en": "Call", "he": "קול"},
    "strat_strike": {"en": "Strike", "he": "סטרייק"},
    "strat_mid": {"en": "Premium (mid)", "he": "פרמיה (אמצע)"},
    "strat_credit": {"en": "Net credit", "he": "קרדיט נטו"},
    "strat_max_profit": {"en": "Max profit", "he": "רווח מקסימלי"},
    "strat_max_loss": {"en": "Max loss", "he": "הפסד מקסימלי"},
    "strat_breakeven": {"en": "Breakeven", "he": "נקודת איזון"},
    "strat_pop": {"en": "Est. prob. of profit", "he": "הסתברות רווח משוערת"},
    "strat_width": {"en": "Width", "he": "רוחב"},
    "strat_rr": {"en": "Risk per $1 of reward", "he": "סיכון על כל $1 רווח"},
    "strat_unavailable": {
        "en": "Not enough liquid strikes around the 1σ range to price strategies for this expiry.",
        "he": "אין מספיק סטרייקים נזילים סביב טווח ה-1σ לתמחור אסטרטגיות בפקיעה הזו.",
    },
    "strat_indicative": {
        "en": "⏸️ Indicative prices (last trades — market closed / premarket). Re-check with live quotes before trading.",
        "he": "⏸️ מחירים אינדיקטיביים (עסקאות אחרונות — השוק סגור / פרה-מרקט). יש לבדוק מול ציטוטים חיים לפני ביצוע.",
    },
    "strat_disclaimer": {
        "en": "Educational illustration at mid prices — real fills, fees and assignment risk differ. "
              "Options involve substantial risk. Not investment advice.",
        "he": "המחשה לימודית לפי מחירי אמצע — ביצוע בפועל, עמלות וסיכון הקצאה שונים. "
              "אופציות כרוכות בסיכון מהותי. אינו ייעוץ השקעות.",
    },

    # ---- options flow page (OI / volume strike distribution) ----
    "tab_flow": {"en": "📊 Options Flow", "he": "📊 זרימת אופציות"},
    "open_flow": {
        "en": "Options Flow (OI / Volume by strike) →",
        "he": "← זרימת אופציות (OI / נפח לפי סטרייק)",
    },
    "flow_caption": {
        "en": "Where puts and calls concentrate by strike — spot support/resistance and gamma "
              "walls. Interactive: zoom, hover, and toggle Open Interest ↔ Volume.",
        "he": "היכן מרוכזים הפוטים והקולים לפי סטרייק — רמות תמיכה/התנגדות וקירות גמא. "
              "אינטראקטיבי: זום, ריחוף, ומעבר בין Open Interest ל-Volume.",
    },
    "flow_ticker": {"en": "Ticker", "he": "טיקר"},
    "flow_expiry": {"en": "Expiration", "he": "תאריך פקיעה"},
    "flow_metric": {"en": "Metric", "he": "מדד"},
    "flow_oi": {"en": "Open Interest", "he": "פוזיציות פתוחות (OI)"},
    "flow_volume": {"en": "Volume", "he": "נפח (Volume)"},
    "flow_calls": {"en": "Calls", "he": "קולים"},
    "flow_puts": {"en": "Puts", "he": "פוטים"},
    "flow_strike": {"en": "Strike", "he": "סטרייק"},
    "flow_spot": {"en": "Spot", "he": "מחיר נוכחי"},
    "flow_no_options": {
        "en": "No listed options for this ticker (small caps often have none). Try SPY, QQQ, AAPL…",
        "he": "אין אופציות נסחרות לטיקר הזה (לחברות קטנות לרוב אין). נסו SPY, QQQ, AAPL…",
    },
    "flow_chain_failed": {
        "en": "Could not load the option chain for this expiry — try another, or refresh.",
        "he": "טעינת שרשרת האופציות לפקיעה הזו נכשלה — נסו פקיעה אחרת או רעננו.",
    },
    "flow_oi_zero_note": {
        "en": "Open Interest is 0 across this chain right now (Yahoo updates OI overnight from the "
              "OCC — it reads 0 on weekends / some off-hours). Showing Volume instead.",
        "he": "ה-Open Interest אפס בכל השרשרת כרגע (Yahoo מעדכן OI בלילה מ-OCC — בסופ\"ש "
              "ובחלק משעות המסחר הוא מציג 0). מוצג Volume במקום.",
    },
    "flow_summary_call_oi": {"en": "Total call OI", "he": "סך OI קולים"},
    "flow_summary_put_oi": {"en": "Total put OI", "he": "סך OI פוטים"},
    "flow_summary_pcr": {"en": "Put/Call ratio (OI)", "he": "יחס פוט/קול (OI)"},
    "flow_max_pain": {"en": "Max-pain strike", "he": "סטרייק Max-Pain"},
    "flow_surface_header": {
        "en": "🗺️ Open-Interest surface — all expiries at once",
        "he": "🗺️ מפת פוזיציות פתוחות — כל הפקיעות במבט אחד",
    },
    "flow_surface_title": {
        "en": "Open Interest — strike × expiry",
        "he": "פוזיציות פתוחות — סטרייק × פקיעה",
    },
    "flow_surface_unavailable": {
        "en": "Open-interest surface unavailable right now.",
        "he": "מפת הפוזיציות הפתוחות אינה זמינה כרגע.",
    },

    # ---- portfolio page ----
    "tab_portfolio": {"en": "💼 My Portfolio", "he": "💼 התיק שלי"},
    "portfolio_caption": {
        "en": "Track your positions: weights, unrealized P&L, Beta, Sharpe ratio and full risk analytics per holding.",
        "he": "מעקב אחר הפוזיציות שלך: משקל מהתיק, רווח/הפסד, בטא, יחס שארפ ואנליטיקת סיכון מלאה לכל החזקה.",
    },
    "home_portfolio_desc": {
        "en": "Enter your positions (ticker, shares, entry price) and get portfolio weights, "
              "P&L, Beta, Sharpe, volatility, drawdown and correlations.",
        "he": "הזינו את הפוזיציות שלכם (טיקר, כמות מניות, מחיר כניסה) וקבלו משקלים מהתיק, "
              "רווח/הפסד, בטא, שארפ, תנודתיות, Drawdown וקורלציות.",
    },
    "open_portfolio": {"en": "Open My Portfolio →", "he": "← לתיק שלי"},
    "subtab_port_overview": {"en": "📊 Overview", "he": "📊 סקירה"},
    "subtab_port_metrics": {"en": "📋 Position Metrics", "he": "📋 מדדי פוזיציות"},
    "subtab_port_risk": {"en": "⚖️ Risk & Performance", "he": "⚖️ סיכון וביצועים"},
    "subtab_port_edit": {"en": "➕ Edit Positions", "he": "➕ עריכת פוזיציות"},
    "positions_editor_help": {
        "en": "Add / edit / delete rows below, then click Save. Duplicate tickers are merged "
              "into one lot (weighted-average entry price). Prices in USD.",
        "he": "הוסיפו, ערכו או מחקו שורות בטבלה ולחצו על שמירה. טיקרים כפולים מאוחדים "
              "לפוזיציה אחת (מחיר כניסה ממוצע משוקלל). המחירים בדולר.",
    },
    "col_shares": {"en": "Shares", "he": "כמות מניות"},
    "col_entry": {"en": "Entry price", "he": "מחיר כניסה"},
    "save_portfolio": {"en": "💾 Save portfolio", "he": "💾 שמירת התיק"},
    "portfolio_saved": {"en": "Portfolio saved.", "he": "התיק נשמר בהצלחה."},
    "save_failed": {
        "en": "Could not write the portfolio file to disk.",
        "he": "שמירת קובץ התיק לדיסק נכשלה.",
    },
    "invalid_rows_dropped": {
        "en": "Some rows were invalid and skipped:",
        "he": "חלק מהשורות לא היו תקינות ודולגו:",
    },
    "empty_portfolio": {
        "en": "Your portfolio is empty — add positions in the editor below and click Save.",
        "he": "התיק ריק — הוסיפו פוזיציות בטבלה למטה ולחצו על שמירה.",
    },
    "fetch_failed_tickers": {
        "en": "No market data found for:",
        "he": "לא נמצאו נתוני שוק עבור:",
    },
    "positions_count": {"en": "Positions", "he": "מספר פוזיציות"},
    "total_value": {"en": "Total value", "he": "שווי כולל"},
    "total_cost": {"en": "Cost basis", "he": "עלות כוללת"},
    "total_pnl": {"en": "Unrealized P&L", "he": "רווח/הפסד לא ממומש"},
    "daily_pnl": {"en": "Daily P&L", "he": "רווח/הפסד יומי"},
    "port_beta": {"en": "Portfolio Beta (weighted)", "he": "בטא של התיק (משוקלל)"},
    "port_realized_beta": {"en": "Realized Beta (1Y)", "he": "בטא בפועל (שנה)"},
    "port_sharpe": {"en": "Portfolio Sharpe (1Y)", "he": "שארפ של התיק (שנה)"},
    "port_vol": {"en": "Annualized volatility", "he": "תנודתיות שנתית"},
    "port_maxdd": {"en": "Max drawdown (1Y)", "he": "ירידה מקסימלית (שנה)"},
    "col_weight": {"en": "% of portfolio", "he": "% מהתיק"},
    "col_mkt_value": {"en": "Market value", "he": "שווי שוק"},
    "col_pnl": {"en": "P&L $", "he": "רווח/הפסד $"},
    "col_pnl_pct": {"en": "P&L %", "he": "רווח/הפסד %"},
    "col_day_chg": {"en": "Day %", "he": "% יומי"},
    "col_beta": {"en": "Beta (1Y)", "he": "בטא (שנה)"},
    "col_sharpe": {"en": "Sharpe (1Y)", "he": "שארפ (שנה)"},
    "col_vol_ann": {"en": "Volatility (ann.)", "he": "תנודתיות שנתית"},
    "col_maxdd": {"en": "Max DD (1Y)", "he": "ירידה מקס' (שנה)"},
    "col_dist_52w": {"en": "vs 52W high", "he": "מול שיא 52 שבועות"},
    "alloc_pie_title": {"en": "Portfolio allocation", "he": "הקצאת התיק"},
    "pnl_bar_title": {"en": "Unrealized P&L by position", "he": "רווח/הפסד לפי פוזיציה"},
    "perf_vs_spy_title": {
        "en": "Portfolio vs SPY — 1 year (normalized to 100)",
        "he": "התיק מול SPY — שנה אחורה (מנורמל ל-100)",
    },
    "corr_title": {
        "en": "Correlation matrix of holdings (daily returns, 1Y)",
        "he": "מטריצת קורלציה בין ההחזקות (תשואות יומיות, שנה)",
    },
    "portfolio_label": {"en": "Portfolio", "he": "התיק שלי"},
    "rf_note": {
        "en": "Risk-free rate used for Sharpe (13-week T-bill):",
        "he": "ריבית חסרת סיכון לחישוב שארפ (אג\"ח ארה\"ב 13 שבועות):",
    },

    # ---- macro sub-tabs (navigation within the Macro Analysis page) ----
    "subtab_pulse": {"en": "🫀 Pulse", "he": "🫀 דופק"},
    "subtab_indices": {"en": "🌍 Indices", "he": "🌍 מדדים"},
    "subtab_vol": {"en": "🌪️ Volatility", "he": "🌪️ תנודתיות"},
    "subtab_rates": {"en": "🏦 Rates", "he": "🏦 ריביות"},
    "subtab_commod": {"en": "🛢️ Commodities", "he": "🛢️ סחורות"},
    "subtab_fx": {"en": "💱 Dollar & FX", "he": "💱 דולר ומט\"ח"},
    "subtab_crypto": {"en": "₿ Crypto", "he": "₿ קריפטו"},
    "subtab_sectors": {"en": "🔄 Sectors", "he": "🔄 סקטורים"},
    "subtab_options": {"en": "🎯 Options", "he": "🎯 אופציות"},

    # ---- macro tab: options data ----
    "sec_term": {"en": "VIX Term Structure", "he": "מבנה עקום ה-VIX"},
    "term_contango": {
        "en": "Contango — normal risk appetite ✓",
        "he": "קונטנגו — תיאבון סיכון תקין ✓",
    },
    "term_backwardation": {
        "en": "Backwardation — near-term stress ⚠️",
        "he": "בקוורדציה — לחץ בטווח הקצר ⚠️",
    },
    "term_flat": {"en": "Flat curve", "he": "עקום שטוח"},
    "term_slope": {"en": "3M / 1M slope", "he": "שיפוע 3 חודשים / חודש"},
    "term_chart_title": {
        "en": "VIX term structure — today vs. one week ago",
        "he": "מבנה עקום ה-VIX — היום מול לפני שבוע",
    },
    "term_1w_ago": {"en": "1 week ago", "he": "לפני שבוע"},
    "sec_tail": {
        "en": "Tail Risk & Bond Volatility (SKEW / MOVE)",
        "he": "סיכון זנב ותנודתיות אג\"ח (SKEW / MOVE)",
    },
    "skew_low": {"en": "Low tail-risk pricing", "he": "תמחור סיכון זנב נמוך"},
    "skew_moderate": {"en": "Moderate tail-risk pricing", "he": "תמחור סיכון זנב בינוני"},
    "skew_high": {"en": "Elevated tail-risk pricing", "he": "תמחור סיכון זנב גבוה"},
    "skew_chart_title": {
        "en": "SKEW index — last 6 months",
        "he": "מדד SKEW — שישה חודשים אחרונים",
    },
    "sec_pcr": {
        "en": "Put/Call Ratios & Implied Volatility (live chains)",
        "he": "יחסי פוט/קול וסטיית תקן גלומה (שרשראות חיות)",
    },
    "options_note": {
        "en": "Put/Call ratios, ATM IV and the open-interest profile are computed live from the "
              "nearest listed SPY / QQQ option expiry (≥5 days out, to avoid 0-DTE noise).",
        "he": "יחסי פוט/קול, סטיית תקן גלומה ופרופיל הפוזיציות הפתוחות מחושבים בזמן אמת "
              "מהפקיעה הקרובה של אופציות SPY / QQQ (לפחות 5 ימים קדימה, להימנעות מרעש 0-DTE).",
    },
    "options_unavailable": {
        "en": "Options chain data is unavailable right now.",
        "he": "נתוני שרשרת האופציות אינם זמינים כרגע.",
    },
    "pcr_vol_label": {"en": "P/C ratio (volume)", "he": "יחס פוט/קול (מחזור)"},
    "pcr_oi_label": {"en": "P/C ratio (open interest)", "he": "יחס פוט/קול (OI)"},
    "atm_iv_label": {"en": "ATM implied volatility", "he": "סטיית תקן גלומה (ATM)"},
    "pcr_fear": {
        "en": "Heavy put buying — hedging / fear",
        "he": "קניית פוטים כבדה — גידור / פחד",
    },
    "pcr_neutral": {"en": "Neutral positioning", "he": "פוזיציה ניטרלית"},
    "pcr_greed": {
        "en": "Call-heavy — risk appetite / complacency",
        "he": "עודף קולים — תיאבון סיכון / שאננות",
    },
    "sec_oi": {
        "en": "Open Interest Profile — nearest expiry",
        "he": "פרופיל פוזיציות פתוחות — פקיעה קרובה",
    },
    "oi_calls": {"en": "Calls OI", "he": "קולים (OI)"},
    "oi_puts": {"en": "Puts OI", "he": "פוטים (OI)"},
    "spot_label": {"en": "Spot", "he": "מחיר נוכחי"},
    "expiry_label": {"en": "Expiry", "he": "פקיעה"},

    # ---- macro tab: pulse ----
    "pulse_title": {"en": "Daily Macro Pulse", "he": "דופק מאקרו יומי"},
    "pulse_gauge_title": {"en": "Risk Appetite Score", "he": "מדד תיאבון הסיכון"},
    "pulse_risk_on": {"en": "RISK-ON 🟢", "he": "🟢 תיאבון סיכון (Risk-On)"},
    "pulse_risk_off": {"en": "RISK-OFF 🔴", "he": "🔴 בריחה מסיכון (Risk-Off)"},
    "pulse_mixed": {"en": "MIXED / NEUTRAL 🟡", "he": "🟡 מעורב / ניטרלי"},
    "pulse_breadth": {"en": "Index breadth (1D)", "he": "רוחב מדדים (יומי)"},
    "pulse_vix_comp": {"en": "VIX momentum", "he": "מומנטום VIX"},
    "pulse_sector_comp": {"en": "Sector breadth (1D)", "he": "רוחב סקטורים (יומי)"},

    # ---- macro tab: volatility ----
    "sec_vol": {"en": "Volatility & Risk Regime", "he": "משטר תנודתיות וסיכון"},
    "vix_1y_pct": {"en": "1Y percentile", "he": "אחוזון שנתי"},
    "regime_calm": {"en": "Calm", "he": "רגוע"},
    "regime_normal": {"en": "Normal", "he": "נורמלי"},
    "regime_elevated": {"en": "Elevated", "he": "מוגבר"},
    "regime_stress": {"en": "High stress", "he": "לחץ גבוה"},
    "regime_crisis": {"en": "Crisis", "he": "משבר"},
    "vix_chart_title": {
        "en": "VIX — last 6 months with regime bands",
        "he": "VIX — שישה חודשים אחרונים עם רצועות משטר",
    },

    # ---- macro tab: rates ----
    "sec_rates": {"en": "Rates & Yield Curve", "he": "ריביות ועקום התשואות"},
    "curve_metric": {"en": "10Y – 3M spread", "he": "מרווח 10 שנים – 3 חודשים"},
    "curve_inverted": {"en": "Inverted curve ⚠️", "he": "עקום הפוך ⚠️"},
    "curve_flat": {"en": "Flat curve", "he": "עקום שטוח"},
    "curve_normal": {"en": "Normal curve", "he": "עקום נורמלי"},
    "curve_chart_title": {
        "en": "US Treasury curve — today vs. 1M / 6M / 1Y ago",
        "he": "עקום התשואות האמריקאי — היום מול חודש / חצי שנה / שנה אחורה",
    },
    "curve_today": {"en": "Today", "he": "היום"},
    "curve_1m_ago": {"en": "1 month ago", "he": "לפני חודש"},
    "curve_6m_ago": {"en": "6 months ago", "he": "לפני חצי שנה"},
    "curve_1y_ago": {"en": "1 year ago", "he": "לפני שנה"},
    "tnx_history_title": {
        "en": "US 10-Year yield — last 12 months",
        "he": "תשואת אג\"ח 10 שנים — 12 חודשים אחרונים",
    },
    "chg_1m": {"en": "Δ 1 month", "he": "Δ חודש"},
    "chg_6m": {"en": "Δ 6 months", "he": "Δ חצי שנה"},
    "chg_1y": {"en": "Δ 1 year", "he": "Δ שנה"},

    # ---- central bank policy rates ----
    "sec_cbanks": {
        "en": "🏛️ Central Bank Policy Rates",
        "he": "🏛️ ריביות בנקים מרכזיים",
    },
    "cbanks_note": {
        "en": "Official policy rates from the BIS central-bank policy rates dataset "
              "(cross-checked against the ECB's own API), refreshed hourly. Each card's "
              "'Last move' is when that bank last CHANGED its rate — often months ago, "
              "because a rate that hasn't moved is not out of date.",
        "he": "ריביות רשמיות ממאגר ריביות הבנקים המרכזיים של ה-BIS (מאומת מול ה-API הרשמי "
              "של ה-ECB), מתעדכן כל שעה. ה'מהלך האחרון' בכל כרטיס הוא מתי הבנק שינה את הריבית "
              "לאחרונה — לרוב לפני חודשים, כי ריבית שלא זזה אינה ריבית לא-מעודכנת.",
    },
    "cbanks_asof": {
        "en": "Rates current as of",
        "he": "הריביות נכונות לתאריך",
    },
    "cbanks_failed": {
        "en": "Central bank rates are unavailable right now.",
        "he": "נתוני ריביות הבנקים המרכזיים אינם זמינים כרגע.",
    },
    "cb_as_of": {"en": "As of", "he": "נכון ל-"},
    "cb_override_title": {"en": "✏️ Manual rate update", "he": "✏️ עדכון ריבית ידני"},
    "cb_override_note": {
        "en": "If a rate decision was just announced and the BIS feed hasn't caught up yet, "
              "set the new rate here. The override applies only while it is newer than the "
              "source, and expires automatically once BIS updates. Overridden rates are "
              "marked with ✏️.",
        "he": "אם התקבלה החלטת ריבית וה-BIS עדיין לא התעדכן, עדכנו כאן את הריבית החדשה. "
              "העדכון תקף רק כל עוד הוא חדש יותר מהמקור, ופג אוטומטית ברגע שה-BIS מתעדכן. "
              "ריבית מעודכנת ידנית מסומנת ב-✏️.",
    },
    "cb_override_rate": {"en": "New rate (%)", "he": "ריבית חדשה (%)"},
    "cb_override_date": {"en": "Effective date", "he": "תאריך תחולה"},
    "cb_override_save": {"en": "Save update", "he": "שמירת עדכון"},
    "cb_override_saved": {"en": "Saved.", "he": "נשמר בהצלחה."},
    "cbanks_history_title": {
        "en": "Policy rates — last 3 years (click legend to toggle banks)",
        "he": "ריביות מוניטריות — 3 שנים אחרונות (לחיצה על המקרא מציגה/מסתירה בנק)",
    },
    "cb_last_change": {"en": "Last move", "he": "מהלך אחרון"},
    "cb_rate_col": {"en": "Policy rate", "he": "ריבית"},
    "cb_bank_col": {"en": "Central bank", "he": "בנק מרכזי"},
    "cb_IL": {"en": "Israel — Bank of Israel", "he": "ישראל — בנק ישראל"},
    "cb_US": {"en": "United States — Fed", "he": "ארה\"ב — הפדרל ריזרב"},
    "cb_XM": {"en": "Euro Area — ECB", "he": "גוש האירו — ECB"},
    "cb_GB": {"en": "United Kingdom — BoE", "he": "בריטניה — בנק אוף אינגלנד"},
    "cb_JP": {"en": "Japan — BoJ", "he": "יפן — בנק אוף יפן"},
    "cb_CH": {"en": "Switzerland — SNB", "he": "שווייץ — SNB"},
    "cb_CA": {"en": "Canada — BoC", "he": "קנדה — בנק אוף קנדה"},
    "cb_AU": {"en": "Australia — RBA", "he": "אוסטרליה — RBA"},
    "cb_CN": {"en": "China — PBoC", "he": "סין — הבנק העממי"},
    "maturity": {"en": "Maturity", "he": "טווח לפדיון"},
    "yield_pct": {"en": "Yield (%)", "he": "תשואה (%)"},

    # ---- macro tab: snapshots ----
    "sec_indices": {"en": "Global Indices Snapshot", "he": "מדדים גלובליים — תמונת מצב"},
    "sec_commod": {"en": "Commodities", "he": "סחורות"},
    "sec_fx": {
        "en": "US Dollar vs Major Currencies",
        "he": "הדולר מול המטבעות המובילים",
    },
    "sec_crypto": {"en": "Leading Cryptocurrencies", "he": "מטבעות הקריפטו המובילים"},
    "fx_note": {
        "en": "In USD/XXX pairs (shekel, yen, yuan, rupee…) a rise = stronger dollar; "
              "in EUR/USD, GBP/USD, AUD/USD and NZD/USD a rise = weaker dollar.",
        "he": "בזוגות דולר/מטבע (שקל, ין, יואן, רופי...) עלייה = דולר מתחזק; "
              "באירו/דולר, ליש\"ט/דולר, אוסטרלי/דולר וניו-זילנדי/דולר עלייה = דולר נחלש.",
    },
    "crypto_note": {
        "en": "The list is dynamic: the top coins by LIVE market cap (stablecoins and "
              "staked/wrapped derivatives excluded), refreshed every 6 hours.",
        "he": "הרשימה דינמית: המטבעות המובילים לפי שווי שוק חי (ללא סטייבלקוינים "
              "ונגזרות staked/wrapped), מתעדכנת כל 6 שעות.",
    },
    "horizon_table": {
        "en": "Returns by horizon (1D / 5D / 1M)",
        "he": "תשואות לפי אופק (יומי / שבועי / חודשי)",
    },
    "hist_title": {"en": "📈 Historical chart", "he": "📈 גרף היסטורי"},
    "hist_pick": {"en": "Pick an instrument", "he": "בחרו מכשיר"},
    "hist_period": {"en": "Period", "he": "תקופה"},
    "hist_ret": {"en": "Return over the period", "he": "תשואה בתקופה"},
    "hist_range": {"en": "Low–High", "he": "שפל–שיא"},
    "col_asset": {"en": "Asset", "he": "נכס"},
    "col_price": {"en": "Price", "he": "מחיר"},
    "col_1d": {"en": "1D %", "he": "% יומי"},
    "col_5d": {"en": "5D %", "he": "% 5 ימים"},
    "col_1m": {"en": "1M %", "he": "% חודש"},
    "indices_chart_title": {
        "en": "Index performance by horizon",
        "he": "ביצועי מדדים לפי אופק זמן",
    },

    # ---- macro tab: sector flows ----
    "sec_sectors": {
        "en": "Sector Rotation & Capital Flows",
        "he": "רוטציה סקטוריאלית וזרימות הון",
    },
    "flow_explain": {
        "en": "Flow Score = momentum blend (50% 1D, 30% 5D, 20% 1M cross-sectional z-scores) × √(relative dollar volume). "
              "A high positive score = capital is aggressively rotating IN; a deep negative score = capital is rotating OUT.",
        "he": "ציון הזרימה = שילוב מומנטום (50% יומי, 30% שבועי, 20% חודשי — ציוני תקן רוחביים) × שורש הנפח הדולרי היחסי. "
              "ציון חיובי גבוה = הון זורם פנימה באגרסיביות; ציון שלילי עמוק = הון בורח החוצה.",
    },
    "money_map_header": {
        "en": "🗺️ Money Map — where capital is trading",
        "he": "🗺️ מפת הכסף — היכן ההון נסחר",
    },
    "money_map_note": {
        "en": "Each tile is a sector; SIZE = dollar volume traded today (how much capital is changing hands), "
              "COLOR = today's move (green in / red out). Big & green = money flowing in with conviction.",
        "he": "כל אריח הוא סקטור; הגודל = המחזור הדולרי היום (כמה הון מחליף ידיים), "
              "הצבע = התנועה היומית (ירוק = פנימה / אדום = החוצה). גדול וירוק = הון נכנס בביטחון.",
    },
    "money_map_horizon": {"en": "Color by", "he": "צביעה לפי"},
    "hz_1d": {"en": "1-day move", "he": "תנועה יומית"},
    "hz_5d": {"en": "5-day move", "he": "תנועה שבועית"},
    "hz_1m": {"en": "1-month move", "he": "תנועה חודשית"},
    "hz_flow": {"en": "Flow Score", "he": "ציון זרימה"},
    "map_vol_label": {"en": "$ traded today", "he": "מחזור דולרי היום"},
    "rrg_header": {
        "en": "🎯 Sector Rotation Graph (RRG) — the flow direction",
        "he": "🎯 גרף רוטציה סקטוריאלית (RRG) — כיוון הזרימה",
    },
    "rrg_note": {
        "en": "Each sector's relative strength vs SPY (X) against its momentum (Y). Rotation is clockwise: "
              "Improving → Leading → Weakening → Lagging. The trail shows the last few weeks' direction — "
              "a sector heading up-right is attracting flow; down-left is bleeding it.",
        "he": "העוצמה היחסית של כל סקטור מול SPY (ציר X) מול המומנטום שלו (ציר Y). הרוטציה עם כיוון השעון: "
              "משתפר ← מוביל ← נחלש ← מפגר. השובל מראה את הכיוון בשבועות האחרונים — "
              "סקטור שנע ימינה-למעלה מושך הון; שמאלה-למטה מאבד אותו.",
    },
    "rrg_ratio_axis": {"en": "Relative Strength (vs SPY)", "he": "עוצמה יחסית (מול SPY)"},
    "rrg_mom_axis": {"en": "Relative Momentum", "he": "מומנטום יחסי"},
    "rrg_leading": {"en": "Leading", "he": "מוביל"},
    "rrg_weakening": {"en": "Weakening", "he": "נחלש"},
    "rrg_lagging": {"en": "Lagging", "he": "מפגר"},
    "rrg_improving": {"en": "Improving", "he": "משתפר"},
    "heatmap_title": {
        "en": "Sector returns heatmap by horizon",
        "he": "מפת חום — תשואות סקטוריאליות לפי אופק",
    },
    "flowbar_title": {
        "en": "Capital Flow Score (momentum × relative volume)",
        "he": "ציון זרימת הון (מומנטום × נפח יחסי)",
    },
    "flow_score_col": {"en": "Flow Score", "he": "ציון זרימה"},
    "rvol_col": {"en": "RVOL ($)", "he": "נפח יחסי ($)"},
    "rank_col": {"en": "Rank", "he": "דירוג"},
    "excess_col": {"en": "1D vs SPY %", "he": "% יומי מול SPY"},
    "inflow_caption": {"en": "🟢 Strongest capital inflow:", "he": "🟢 כניסת ההון החזקה ביותר:"},
    "outflow_caption": {"en": "🔴 Strongest capital outflow:", "he": "🔴 יציאת ההון החזקה ביותר:"},

    # ---- scanner tab ----
    "scan_title": {
        "en": "Aggressive Movers & Unusual Volume Scanner",
        "he": "סורק תנועות אגרסיביות ונפחים חריגים",
    },
    "scan_caption": {
        "en": "Automated engine detecting stocks with abnormal daily volatility, volume surges (RVOL) and ATR expansion.",
        "he": "מנוע אוטומטי המזהה מניות עם תנודתיות יומית חריגה, קפיצות נפח (RVOL) והתרחבות ATR.",
    },
    "scan_settings": {"en": "⚙️ Scan settings & filters", "he": "⚙️ הגדרות סריקה וסינון"},
    "extra_tickers": {
        "en": "Extra tickers (comma-separated)",
        "he": "טיקרים נוספים (מופרדים בפסיק)",
    },
    "extra_tickers_help": {
        "en": "Add your own tickers to the scan universe, e.g. TEVA, NICE, CHKP",
        "he": "הוסיפו טיקרים משלכם ליקום הסריקה, לדוגמה: TEVA, NICE, CHKP",
    },
    "min_price": {"en": "Min price ($)", "he": "מחיר מינימלי ($)"},
    "min_rvol": {"en": "Min RVOL", "he": "RVOL מינימלי"},
    "min_roc": {"en": "Min |daily ROC| (%)", "he": "|ROC יומי| מינימלי (%)"},
    "direction": {"en": "Direction", "he": "כיוון"},
    "dir_all": {"en": "All", "he": "הכל"},
    "dir_up": {"en": "Gainers only", "he": "עולות בלבד"},
    "dir_down": {"en": "Losers only", "he": "יורדות בלבד"},
    "top_n": {"en": "Max results", "he": "מספר תוצאות מקסימלי"},
    "scanned_label": {"en": "Stocks scanned", "he": "מניות נסרקו"},
    "matches_label": {"en": "Passed filters", "he": "עברו סינון"},
    "top_rvol_label": {"en": "Highest RVOL", "he": "שיא RVOL"},
    "top_mover_label": {"en": "Sharpest move", "he": "התנועה החדה ביותר"},
    "leaderboard_title": {"en": "Dynamic Leaderboard", "he": "לוח מובילים דינמי"},
    "no_results": {
        "en": "No stocks match the current filters — try loosening the thresholds.",
        "he": "אין תוצאות העונות לסינון הנוכחי — נסו להקל את הספים.",
    },
    "col_ticker": {"en": "Ticker", "he": "טיקר"},
    "col_signal": {"en": "Signal", "he": "אות"},
    "col_roc1": {"en": "ROC 1D %", "he": "ROC יומי %"},
    "col_roc5": {"en": "ROC 5D %", "he": "ROC 5 ימים %"},
    "col_gap": {"en": "Gap %", "he": "גאפ %"},
    "col_rvol": {"en": "RVOL (20D)", "he": "RVOL (20 ימים)"},
    "col_atr_pct": {"en": "ATR %", "he": "ATR %"},
    "col_atr_exp": {"en": "ATR expansion", "he": "התרחבות ATR"},
    "col_dollar_vol": {"en": "$ Volume (M)", "he": "מחזור דולרי (מיליונים)"},
    "col_score": {"en": "Aggression Score", "he": "ציון עוצמה"},
    "col_dist_high": {"en": "vs 20D high %", "he": "% מול שיא 20 ימים"},
    "signal_breakout_up": {"en": "Breakout ↑ 🚀", "he": "פריצה למעלה 🚀"},
    "signal_breakdown": {"en": "Breakdown ↓ 📉", "he": "שבירה למטה 📉"},
    "signal_volume_surge": {"en": "Volume surge 🔊", "he": "התפרצות נפח 🔊"},
    "signal_vol_expansion": {"en": "Volatility expansion ⚡", "he": "התרחבות תנודתיות ⚡"},
    "signal_momentum_up": {"en": "Momentum ↑", "he": "מומנטום חיובי ↑"},
    "signal_momentum_down": {"en": "Momentum ↓", "he": "מומנטום שלילי ↓"},
    "signal_active": {"en": "Active", "he": "פעילה"},
    "scatter_title": {
        "en": "Activity map: daily ROC vs RVOL (bubble = $ volume)",
        "he": "מפת פעילות: ROC יומי מול RVOL (גודל בועה = מחזור דולרי)",
    },
    "gainers_title": {"en": "Top gainers (daily ROC)", "he": "עולות מובילות (ROC יומי)"},
    "losers_title": {"en": "Top losers (daily ROC)", "he": "יורדות מובילות (ROC יומי)"},
    "drill_title": {"en": "🔎 Stock Deep-Dive", "he": "🔎 צלילה למניה"},
    "drill_select": {"en": "Pick a stock from the results", "he": "בחרו מניה מהתוצאות"},
    "drill_price": {"en": "Last price", "he": "מחיר אחרון"},
    "drill_change": {"en": "Daily change", "he": "שינוי יומי"},
    "drill_rvol": {"en": "RVOL (20D)", "he": "RVOL (20 ימים)"},
    "drill_atr": {"en": "ATR (14)", "he": "ATR (14)"},
    "drill_avg_vol": {"en": "Avg volume (20D)", "he": "נפח ממוצע (20 ימים)"},
    "candle_title": {"en": "6-month candlestick chart", "he": "גרף נרות — 6 חודשים"},
    "vol_axis": {"en": "Volume", "he": "נפח"},
    "ma20": {"en": "MA-20", "he": "ממוצע נע 20"},
}


def t(key: str, lang: str = "en") -> str:
    """Translate a UI string. Falls back to English, then to the raw key."""
    entry = _T.get(key)
    if entry is None:
        return key
    return entry.get(lang) or entry.get("en") or key


# --------------------------------------------------------------------------- #
# Metric explanations — shown as a small clickable "?" next to every data
# point (st.metric help= / column_config help=). Keyed h_<concept>.
# --------------------------------------------------------------------------- #
_H: Dict[str, Dict[str, str]] = {
    # ---- macro: pulse ----
    "h_pulse_score": {
        "en": "Composite risk-appetite score (-100…+100) blending index breadth, inverted VIX momentum and sector breadth. Above +20 = Risk-On, below -20 = Risk-Off.",
        "he": "ציון תיאבון סיכון משוקלל (100-…100+) המשלב רוחב מדדים, מומנטום VIX הפוך ורוחב סקטורים. מעל 20+ = תיאבון סיכון, מתחת ל-20- = בריחה מסיכון.",
    },
    "h_pulse_breadth": {
        "en": "Average 1-day return of the global indices, squashed to a -100…+100 scale. Positive = equity markets broadly green today.",
        "he": "התשואה היומית הממוצעת של המדדים הגלובליים, מכווצת לסקאלה של 100-…100+. חיובי = השווקים ירוקים באופן רחב היום.",
    },
    "h_pulse_vix_comp": {
        "en": "Inverted 1-day VIX momentum: VIX falling = positive contribution (risk-on), VIX spiking = negative (risk-off).",
        "he": "מומנטום VIX יומי הפוך: ‏VIX יורד = תרומה חיובית (תיאבון סיכון), ‏VIX מזנק = שלילית (בריחה מסיכון).",
    },
    "h_pulse_sector_comp": {
        "en": "Share of the 11 sectors that are up today, rescaled to -100…+100. Shows how broad the move is beneath the index level.",
        "he": "שיעור הסקטורים (מתוך 11) שעולים היום, בסקאלה של 100-…100+. מראה כמה רחבה התנועה מתחת לפני השטח של המדד.",
    },
    "h_index_card": {
        "en": "Last close and 1-day change of the index.",
        "he": "שער הסגירה האחרון והשינוי היומי של המדד.",
    },
    # ---- macro: volatility ----
    "h_vix": {
        "en": "The option market's expected S&P 500 volatility over the next 30 days. Below 14 = calm, 20-28 = elevated, above 40 = crisis.",
        "he": "התנודתיות הצפויה של S&P 500 ל-30 הימים הקרובים, כפי שמתומחרת בשוק האופציות. מתחת ל-14 = רוגע, 20–28 = מוגבר, מעל 40 = משבר.",
    },
    "h_vix_pctile": {
        "en": "Where today's VIX sits vs the past year: 0% = calmest day of the year, 100% = most fearful.",
        "he": "מיקום ה-VIX הנוכחי ביחס לשנה האחרונה: ‏0% = היום הרגוע ביותר, ‏100% = המפוחד ביותר.",
    },
    "h_vol_family": {
        "en": "Implied-volatility index for this asset class (same construction as the VIX). Rising = the market is paying more for protection.",
        "he": "מדד תנודתיות גלומה לנכס הזה (באותה מתודולוגיה של ה-VIX). עלייה = השוק משלם יותר על הגנות.",
    },
    # ---- macro: rates ----
    "h_curve_spread": {
        "en": "10-year minus 3-month Treasury yield. Negative (inverted) has preceded most US recessions; a steep positive slope = healthy growth expectations.",
        "he": "תשואת 10 שנים פחות 3 חודשים. שלילי (עקום הפוך) הקדים את רוב המיתונים בארה\"ב; שיפוע חיובי תלול = ציפיות צמיחה בריאות.",
    },
    "h_tnx": {
        "en": "The 10-year US Treasury yield — the world's benchmark 'risk-free' rate that anchors valuations of all risk assets.",
        "he": "תשואת אג\"ח ארה\"ב ל-10 שנים — ריבית הבסיס העולמית שמעגנת את התמחור של כל נכסי הסיכון.",
    },
    "h_chg_bp": {
        "en": "Change in the 10-year yield over this horizon, in basis points (100bp = 1%). Rising = tightening financial conditions.",
        "he": "השינוי בתשואת ה-10 שנים באופק הזה, בנקודות בסיס (100bp = ‏1%). עלייה = הידוק התנאים הפיננסיים.",
    },
    "h_cb_rate": {
        "en": "The official policy rate set by this central bank — the anchor for deposits, mortgages and credit in that economy. The delta shows the bank's most recent move. ✏️ = manual update not yet in the BIS feed.",
        "he": "הריבית הרשמית שקובע הבנק המרכזי — העוגן לפיקדונות, משכנתאות ואשראי באותה כלכלה. הדלתא מציגה את המהלך האחרון. ✏️ = עדכון ידני שעדיין לא נקלט ב-BIS.",
    },
    # ---- macro: commodities / fx / crypto ----
    "h_commodity": {
        "en": "Last price and 1-day change. Commodities reflect inflation pressure, global growth and supply dynamics.",
        "he": "מחיר אחרון ושינוי יומי. סחורות משקפות לחצי אינפלציה, צמיחה גלובלית ודינמיקת היצע.",
    },
    "h_dxy": {
        "en": "Weighted value of the dollar against six major currencies — the global benchmark for dollar strength. Rising DXY tightens conditions for risk assets and emerging markets.",
        "he": "שווי משוקלל של הדולר מול שישה מטבעות מרכזיים — הבנצ'מרק העולמי לעוצמת הדולר. ‏DXY עולה מהדק תנאים לנכסי סיכון ולשווקים מתעוררים.",
    },
    "h_fx": {
        "en": "Exchange rate and 1-day change. For USD/XXX pairs a rise = stronger dollar; for EUR/USD, GBP/USD and AUD/USD a rise = weaker dollar.",
        "he": "שער החליפין והשינוי היומי. בזוגות דולר/מטבע עלייה = דולר מתחזק; באירו/דולר, ליש\"ט/דולר ואוסטרלי/דולר עלייה = דולר נחלש.",
    },
    "h_crypto": {
        "en": "Last price in USD and 1-day change. Crypto trades 24/7 — a leading real-time gauge of global risk appetite and liquidity.",
        "he": "מחיר אחרון בדולרים ושינוי יומי. קריפטו נסחר 24/7 — מד מוביל בזמן אמת לתיאבון הסיכון והנזילות הגלובלית.",
    },
    # ---- macro: sector flows ----
    "h_ret_horizon": {
        "en": "Total price return over this horizon.",
        "he": "תשואת המחיר הכוללת באופק הזה.",
    },
    "h_excess": {
        "en": "Today's return minus SPY's — relative strength vs the broad market.",
        "he": "התשואה היומית פחות תשואת SPY — עוצמה יחסית מול השוק הרחב.",
    },
    "h_rvol_sector": {
        "en": "Today's dollar volume vs its 20-day average. Above 1 = more capital transacting in this sector than usual.",
        "he": "המחזור הדולרי היום ביחס לממוצע 20 ימים. מעל 1 = עובר בסקטור יותר הון מהרגיל.",
    },
    "h_flow_score": {
        "en": "Momentum blend (50% 1D, 30% 5D, 20% 1M z-scores) × √relative volume. High positive = capital rotating IN aggressively; deep negative = rotating OUT.",
        "he": "שילוב מומנטום (50% יומי, 30% שבועי, 20% חודשי — ציוני תקן) × שורש הנפח היחסי. חיובי גבוה = הון נכנס באגרסיביות; שלילי עמוק = הון בורח.",
    },
    "h_rank": {
        "en": "Position in today's capital-flow ranking (1 = strongest inflow).",
        "he": "מיקום בדירוג זרימת ההון היומי (1 = הכניסה החזקה ביותר).",
    },
    # ---- macro: options ----
    "h_term_point": {
        "en": "Expected S&P 500 volatility over this horizon, from option prices.",
        "he": "התנודתיות הצפויה של S&P 500 לאופק הזה, לפי מחירי האופציות.",
    },
    "h_term_slope": {
        "en": "VIX 3M ÷ VIX 1M − 1. Positive (contango) = normal conditions; negative (backwardation) = near-term panic priced above the future — a classic stress signal.",
        "he": "‏VIX ל-3 חודשים חלקי VIX לחודש, פחות 1. חיובי (קונטנגו) = מצב תקין; שלילי (בקוורדציה) = פאניקה בטווח הקצר מעל העתיד — איתות לחץ קלאסי.",
    },
    "h_skew": {
        "en": "The price of crash insurance in deep out-of-the-money S&P puts. Above 140 = elevated demand for tail-risk hedges.",
        "he": "מחיר ביטוח הקריסה באופציות פוט עמוקות מחוץ לכסף על S&P. מעל 140 = ביקוש גבוה לגידור סיכון זנב.",
    },
    "h_move": {
        "en": "The bond market's 'VIX' — implied volatility of US Treasuries. High MOVE destabilizes pricing across all assets.",
        "he": "ה'VIX' של שוק האג\"ח — תנודתיות גלומה של אג\"ח ארה\"ב. ‏MOVE גבוה מערער את התמחור בכל הנכסים.",
    },
    "h_pcr_vol": {
        "en": "Puts traded ÷ calls traded today (nearest expiry). Above 1 = hedging/fear; below 0.7 = complacency/greed.",
        "he": "מחזור פוטים חלקי מחזור קולים היום (פקיעה קרובה). מעל 1 = גידור/פחד; מתחת ל-0.7 = שאננות/חמדנות.",
    },
    "h_pcr_oi": {
        "en": "Puts ÷ calls in open positions — the slower, positioning-based version of the put/call ratio.",
        "he": "פוטים חלקי קולים בפוזיציות הפתוחות — הגרסה האיטית, מבוססת-הפוזיציות, של יחס הפוט/קול.",
    },
    "h_atm_iv": {
        "en": "Implied volatility at-the-money — the option market's expected move for this underlying until expiry (annualized).",
        "he": "סטיית תקן גלומה בכסף — התנועה שהשוק מצפה לה בנכס עד הפקיעה (במונחים שנתיים).",
    },
    # ---- scanner ----
    "h_scanned": {
        "en": "Number of stocks fetched and analyzed in this scan.",
        "he": "מספר המניות שנשלפו ונותחו בסריקה הזו.",
    },
    "h_matches": {
        "en": "Stocks that passed your current filters.",
        "he": "מניות שעברו את הסינון הנוכחי שלך.",
    },
    "h_top_rvol": {
        "en": "The stock trading at the highest multiple of its normal volume right now.",
        "he": "המניה שנסחרת כעת במכפלה הגבוהה ביותר של הנפח הרגיל שלה.",
    },
    "h_top_mover": {
        "en": "The largest absolute daily move in the scanned universe.",
        "he": "התנועה היומית החדה ביותר (בערך מוחלט) ביקום הסריקה.",
    },
    "h_roc1": {
        "en": "Rate of Change — today's % move vs yesterday's close.",
        "he": "‏Rate of Change — השינוי היומי באחוזים מול סגירת אתמול.",
    },
    "h_roc5": {
        "en": "% move over the last 5 trading days.",
        "he": "השינוי באחוזים ב-5 ימי המסחר האחרונים.",
    },
    "h_gap": {
        "en": "Today's open vs yesterday's close — the overnight repricing (news, earnings).",
        "he": "פתיחת היום מול סגירת אתמול — תמחור-הלילה מחדש (חדשות, דוחות).",
    },
    "h_rvol20": {
        "en": "Today's volume ÷ 20-day average volume. 2x+ = unusual interest; 3x+ = event-driven activity.",
        "he": "נפח היום חלקי ממוצע 20 ימים. פי 2 ומעלה = עניין חריג; פי 3 ומעלה = אירוע מניע.",
    },
    "h_atr_pct": {
        "en": "Average True Range (14d) as % of price — the stock's 'normal' daily movement.",
        "he": "‏ATR ל-14 ימים כאחוז מהמחיר — התנועה היומית ה'נורמלית' של המניה.",
    },
    "h_atr_exp": {
        "en": "Today's true range ÷ ATR(14). Above 1.8 = a genuine volatility-expansion day.",
        "he": "טווח התנועה של היום חלקי ATR(14). ‏מעל 1.8 = יום התרחבות תנודתיות אמיתי.",
    },
    "h_dist_high20": {
        "en": "Distance from the 20-day closing high. Positive = trading above it (breakout territory).",
        "he": "המרחק משיא הסגירה של 20 הימים. חיובי = נסחרת מעליו (טריטוריית פריצה).",
    },
    "h_dollar_vol": {
        "en": "Price × shares traded today, in $ millions — the actual capital changing hands.",
        "he": "מחיר × כמות מניות שנסחרו היום, במיליוני דולרים — ההון שבאמת מחליף ידיים.",
    },
    "h_score": {
        "en": "Cross-sectional percentile composite: 40% |daily ROC| + 35% RVOL + 25% ATR expansion. 90+ = among today's most aggressive movers.",
        "he": "ציון אחוזוני משוקלל מול כל היקום: ‏40% |ROC יומי| + ‏35% RVOL + ‏25% התרחבות ATR. ‏90+ = מהאגרסיביות של היום.",
    },
    "h_signal": {
        "en": "Automatic classification of what drives the move: breakout, volume surge, volatility expansion or momentum.",
        "he": "סיווג אוטומטי של מקור התנועה: פריצה, התפרצות נפח, התרחבות תנודתיות או מומנטום.",
    },
    "h_avg_vol": {
        "en": "Average daily share volume over the past 20 sessions.",
        "he": "נפח המסחר היומי הממוצע ב-20 הימים האחרונים.",
    },
    # ---- options scanner ----
    "h_cur_iv": {
        "en": "At-the-money implied volatility from the ~30-day chain — the annualized move the option market is pricing right now.",
        "he": "סטיית התקן הגלומה בכסף מהשרשרת של כ-30 יום — התנועה השנתית שהשוק מתמחר כרגע.",
    },
    "h_hv30": {
        "en": "Realized (historical) volatility of the last 21 sessions, annualized — how much the stock ACTUALLY moved.",
        "he": "התנודתיות בפועל של 21 הימים האחרונים, במונחים שנתיים — כמה המניה באמת זזה.",
    },
    "h_iv_hv": {
        "en": "IV ÷ HV. Above 1 = options priced richer than realized movement — the volatility risk premium a credit-spread seller collects.",
        "he": "‏IV חלקי HV. מעל 1 = האופציות מתומחרות ביוקר ביחס לתנועה בפועל — פרמיית הסיכון שמוכר מרווחי אשראי גובה.",
    },
    "h_iv_rank": {
        "en": "Where current IV sits between the 52-week volatility low and high (0–100). Above 40 = premium relatively expensive → favorable for selling credit spreads.",
        "he": "מיקום ה-IV הנוכחי בין השפל לשיא של התנודתיות ב-52 השבועות האחרונים (0–100). מעל 40 = פרמיה יקרה יחסית ← סביבה נוחה למכירת מרווחי אשראי.",
    },
    "h_iv_pctile": {
        "en": "% of the last 252 trading days with volatility below the current IV. High percentile = premium richer than usual, robust to one-off spikes.",
        "he": "אחוז הימים מתוך 252 האחרונים שבהם התנודתיות הייתה נמוכה מה-IV הנוכחי. אחוזון גבוה = פרמיה יקרה מהרגיל, ועמיד לזינוקים חד-פעמיים.",
    },
    "h_exp_move": {
        "en": "Price × IV × √(30/365) — the one-standard-deviation expected move over ~30 days (~68% probability the stock stays inside). Selling spreads beyond this range = high-probability setups.",
        "he": "מחיר × IV × ‏√(30/365) — תנועת סטיית תקן אחת ל-30 יום (סיכוי ~68% שהמניה תישאר בטווח). מכירת מרווחים מעבר לטווח הזה = עסקאות בהסתברות גבוהה.",
    },
    "h_dte": {
        "en": "Days to the expiry used for the IV reading (closest to 30).",
        "he": "מספר הימים לפקיעה שממנה נלקח ה-IV (הקרובה ביותר ל-30).",
    },
    "h_flow_pcr": {
        "en": "Total put open interest ÷ total call open interest for this expiry. Above 1 = more downside protection open; below 1 = call-heavy.",
        "he": "סך ה-OI של הפוטים חלקי סך ה-OI של הקולים בפקיעה הזו. מעל 1 = יותר הגנה על ירידות; מתחת ל-1 = עודף קולים.",
    },
    "h_max_pain": {
        "en": "The strike at which the total dollar value of all in-the-money options is smallest — where the most option buyers 'lose'. Price often gravitates toward it near expiry.",
        "he": "הסטרייק שבו הערך הדולרי הכולל של כל האופציות בתוך הכסף הוא הקטן ביותר — היכן שרוב קוני האופציות 'מפסידים'. המחיר נוטה להימשך אליו סמוך לפקיעה.",
    },
    "h_strat_credit": {
        "en": "Premium received when opening the spread (mid prices, per contract = ×100 shares). Kept in full if the spread expires worthless.",
        "he": "הפרמיה שמתקבלת בפתיחת המרווח (מחירי אמצע, לחוזה = ×100 מניות). נשמרת במלואה אם המרווח פוקע חסר ערך.",
    },
    "h_strat_max_profit": {
        "en": "The full credit — earned when the stock finishes on the profitable side of the short strike at expiry.",
        "he": "מלוא הקרדיט — מתקבל כשהמניה מסיימת בצד הרווחי של הסטרייק המכור בפקיעה.",
    },
    "h_strat_max_loss": {
        "en": "Strike width minus the credit, capped by the long protective leg. Size your position from THIS number.",
        "he": "רוחב הסטרייקים פחות הקרדיט, מוגבל על ידי הרגל הקנויה המגינה. את גודל הפוזיציה גוזרים מהמספר הזה.",
    },
    "h_strat_breakeven": {
        "en": "The expiry price where P/L is exactly zero — beyond it the trade loses.",
        "he": "מחיר הפקיעה שבו הרווח/הפסד מתאפס בדיוק — מעבר לו העסקה מפסידה.",
    },
    "h_strat_pop": {
        "en": "Rough estimate from the 1σ expected move (normal approximation): probability the stock finishes on the profitable side. Not a guarantee.",
        "he": "אומדן גס מהתנועה הצפויה של 1σ (קירוב נורמלי): ההסתברות שהמניה תסיים בצד הרווחי. לא הבטחה.",
    },

    # ---- portfolio ----
    "h_total_value": {
        "en": "Sum of all positions at current market prices.",
        "he": "סך כל הפוזיציות במחירי השוק הנוכחיים.",
    },
    "h_daily_pnl": {
        "en": "Today's change in portfolio value, in $ and as % of yesterday's value.",
        "he": "השינוי היומי בשווי התיק, בדולרים וכאחוז מהשווי של אתמול.",
    },
    "h_total_pnl": {
        "en": "Market value minus cost basis — unrealized, before taxes and fees.",
        "he": "שווי שוק פחות עלות הקנייה — לא ממומש, לפני מס ועמלות.",
    },
    "h_positions_count": {
        "en": "Number of holdings currently in the portfolio.",
        "he": "מספר ההחזקות בתיק כרגע.",
    },
    "h_port_beta": {
        "en": "Value-weighted average of position betas. 1 = moves like the S&P 500; 1.5 = 50% more volatile than the market.",
        "he": "ממוצע משוקלל-שווי של הבטא של הפוזיציות. ‏1 = זז כמו S&P 500; ‏1.5 = תנודתי ב-50% יותר מהשוק.",
    },
    "h_port_sharpe": {
        "en": "Risk-adjusted return: (annual return − risk-free) ÷ volatility, computed on 1y of your current holdings. Above 1 = good, above 2 = excellent.",
        "he": "תשואה מותאמת סיכון: (תשואה שנתית פחות ריבית חסרת סיכון) חלקי התנודתיות, על שנה של ההחזקות הנוכחיות. מעל 1 = טוב, מעל 2 = מצוין.",
    },
    "h_port_vol": {
        "en": "Annualized standard deviation of daily portfolio returns — how bumpy the ride is.",
        "he": "סטיית התקן השנתית של תשואות התיק היומיות — כמה מטלטלת הנסיעה.",
    },
    "h_port_maxdd": {
        "en": "Worst peak-to-trough decline of the portfolio value curve over the past year.",
        "he": "הירידה החדה ביותר משיא לשפל בעקומת שווי התיק בשנה האחרונה.",
    },
    "h_realized_beta": {
        "en": "Beta measured on the actual daily portfolio-value curve vs SPY — confirms the weighted estimate.",
        "he": "בטא שנמדדה על עקומת שווי התיק בפועל מול SPY — מאמתת את האומדן המשוקלל.",
    },
    "h_weight": {
        "en": "This position's share of total portfolio value — your concentration risk at a glance.",
        "he": "חלקה של הפוזיציה מסך שווי התיק — סיכון הריכוזיות שלך במבט אחד.",
    },
    "h_mkt_value": {
        "en": "Shares × current price.",
        "he": "כמות המניות × המחיר הנוכחי.",
    },
    "h_pnl": {
        "en": "Unrealized profit/loss in dollars: shares × (price − entry).",
        "he": "רווח/הפסד לא ממומש בדולרים: כמות × (מחיר נוכחי פחות מחיר כניסה).",
    },
    "h_pnl_pct": {
        "en": "Current price vs your entry price, in %.",
        "he": "המחיר הנוכחי מול מחיר הכניסה שלך, באחוזים.",
    },
    "h_day_chg": {
        "en": "Today's % move of this holding.",
        "he": "התנועה היומית של ההחזקה באחוזים.",
    },
    "h_beta": {
        "en": "Sensitivity to S&P 500 moves (1y daily data). 1 = market-like; above 1 = amplifies market moves; below 1 = defensive.",
        "he": "רגישות לתנועות S&P 500 (נתונים יומיים, שנה). ‏1 = כמו השוק; מעל 1 = מגביר את תנועות השוק; מתחת ל-1 = דפנסיבי.",
    },
    "h_sharpe_stock": {
        "en": "This stock's risk-adjusted return over the past year: excess return ÷ volatility.",
        "he": "התשואה מותאמת הסיכון של המניה בשנה האחרונה: תשואה עודפת חלקי תנודתיות.",
    },
    "h_vol_ann": {
        "en": "Annualized volatility of daily returns over the past year.",
        "he": "התנודתיות השנתית של התשואות היומיות בשנה האחרונה.",
    },
    "h_maxdd_stock": {
        "en": "Worst peak-to-trough decline of this stock over the past year.",
        "he": "הירידה החדה ביותר משיא לשפל של המניה בשנה האחרונה.",
    },
    "h_dist_52w": {
        "en": "Distance from the 52-week high. Near 0% = at highs; deeply negative = far below them.",
        "he": "המרחק משיא 52 השבועות. קרוב ל-0% = בשיאים; שלילי עמוק = רחוק מהם.",
    },
    "h_entry": {
        "en": "Your average purchase price for this position.",
        "he": "מחיר הקנייה הממוצע שלך בפוזיציה.",
    },
    "h_shares": {
        "en": "Number of shares you hold.",
        "he": "כמות המניות שבבעלותך.",
    },
    # ---- screener / deep dive ----
    "h_mcap": {
        "en": "Market capitalization = share price × shares outstanding. Mega ≥ $200B, large ≥ $10B, mid ≥ $2B.",
        "he": "שווי שוק = מחיר המניה × מספר המניות. מגה ≥ ‏$200B, גדולה ≥ ‏$10B, בינונית ≥ ‏$2B.",
    },
    "h_pe_t": {
        "en": "Price ÷ trailing 12-month earnings per share. Lower = cheaper vs current earnings — compare within the same sector.",
        "he": "מחיר חלקי הרווח למניה ב-12 החודשים האחרונים. נמוך = זול יותר ביחס לרווחים — יש להשוות בתוך אותו סקטור.",
    },
    "h_pe_f": {
        "en": "Price ÷ next-year expected EPS — how the market prices future earnings. Well below trailing P/E = strong growth expected.",
        "he": "מחיר חלקי הרווח הצפוי לשנה הבאה — איך השוק מתמחר את הרווחים העתידיים. נמוך משמעותית מהמכפיל הנוכחי = צפי לצמיחה חזקה.",
    },
    "h_eps": {
        "en": "Earnings per share over the trailing 12 months.",
        "he": "הרווח למניה ב-12 החודשים האחרונים.",
    },
    "h_div": {
        "en": "Annual dividend ÷ share price — the cash yield of holding the stock.",
        "he": "הדיבידנד השנתי חלקי מחיר המניה — תשואת המזומן על ההחזקה.",
    },
    "h_chg_daily": {
        "en": "Today's % change.",
        "he": "השינוי היומי באחוזים.",
    },
    "h_vol_shares": {
        "en": "Shares traded today, in millions.",
        "he": "מניות שנסחרו היום, במיליונים.",
    },
    "h_pb": {
        "en": "Price ÷ book value per share. Below 1 = trading under accounting equity value; interpret alongside ROE.",
        "he": "מחיר חלקי ההון העצמי למניה. מתחת ל-1 = נסחרת מתחת לשווי ההון בספרים; יש לפרש יחד עם ה-ROE.",
    },
    "h_roe": {
        "en": "Return on Equity: net income ÷ shareholders' equity — how efficiently the company turns capital into profit.",
        "he": "תשואה על ההון: רווח נקי חלקי ההון העצמי — כמה יעיל התרגום של הון לרווח.",
    },
    "h_margin": {
        "en": "Net profit margin: net income ÷ revenue.",
        "he": "שולי רווח נקי: רווח נקי חלקי הכנסות.",
    },
    "h_rev_growth": {
        "en": "Year-over-year revenue growth.",
        "he": "צמיחת ההכנסות ביחס לשנה שעברה.",
    },
    "h_target": {
        "en": "Average 12-month price target of covering analysts.",
        "he": "יעד המחיר הממוצע ל-12 חודשים של האנליסטים המסקרים.",
    },
    "h_recommendation": {
        "en": "Consensus analyst rating (Strong Buy → Sell).",
        "he": "המלצת הקונצנזוס של האנליסטים (קנייה חזקה ← מכירה).",
    },
    "h_employees": {
        "en": "Full-time employees — a scale indicator.",
        "he": "מספר העובדים במשרה מלאה — אינדיקציית גודל.",
    },
    "h_top_inflow": {
        "en": "The sector with the strongest capital-flow score right now.",
        "he": "הסקטור עם ציון זרימת ההון החזק ביותר כרגע.",
    },
}


# --------------------------------------------------------------------------- #
# Data-source attribution — appended in parentheses to every metric tooltip.
# --------------------------------------------------------------------------- #
_SRC: Dict[str, Dict[str, str]] = {
    "yahoo": {
        "en": "(Source: Yahoo Finance)",
        "he": "(מקור הנתונים: Yahoo Finance)",
    },
    "cboe": {
        "en": "(Source: CBOE index, via Yahoo Finance)",
        "he": "(מקור: מדד CBOE, דרך Yahoo Finance)",
    },
    "chain": {
        "en": "(Computed live from Yahoo Finance option chains)",
        "he": "(מחושב בזמן אמת משרשראות האופציות של Yahoo Finance)",
    },
    "calc": {
        "en": "(Formula computed by this app on Yahoo Finance price data — method described above)",
        "he": "(נוסחה שמחושבת באפליקציה על נתוני Yahoo Finance — דרך החישוב מתוארת למעלה)",
    },
    "bis": {
        "en": "(Source: BIS central-bank policy rates dataset; manual updates marked ✏️)",
        "he": "(מקור: מאגר ריביות הבנקים המרכזיים של ה-BIS; עדכונים ידניים מסומנים ✏️)",
    },
    "user": {
        "en": "(Source: your own input)",
        "he": "(מקור: הזנה ידנית שלך)",
    },
}

# every tooltip key -> its data-source tag
_H_SRC: Dict[str, str] = {
    # macro pulse (own composite formulas)
    "h_pulse_score": "calc", "h_pulse_breadth": "calc",
    "h_pulse_vix_comp": "calc", "h_pulse_sector_comp": "calc",
    "h_index_card": "yahoo",
    # volatility
    "h_vix": "cboe", "h_vix_pctile": "calc", "h_vol_family": "cboe",
    # rates
    "h_curve_spread": "calc", "h_tnx": "cboe", "h_chg_bp": "calc",
    "h_cb_rate": "bis",
    # commodities / fx / crypto
    "h_commodity": "yahoo", "h_dxy": "yahoo", "h_fx": "yahoo",
    "h_crypto": "yahoo",
    # sector flows (own formulas)
    "h_ret_horizon": "calc", "h_excess": "calc", "h_rvol_sector": "calc",
    "h_flow_score": "calc", "h_rank": "calc",
    # options (macro tab)
    "h_term_point": "cboe", "h_term_slope": "calc", "h_skew": "cboe",
    "h_move": "yahoo", "h_pcr_vol": "chain", "h_pcr_oi": "chain",
    "h_atm_iv": "chain",
    # stock scanner (own formulas)
    "h_scanned": "calc", "h_matches": "calc", "h_top_rvol": "calc",
    "h_top_mover": "calc", "h_roc1": "calc", "h_roc5": "calc",
    "h_gap": "calc", "h_rvol20": "calc", "h_atr_pct": "calc",
    "h_atr_exp": "calc", "h_dist_high20": "calc", "h_dollar_vol": "calc",
    "h_score": "calc", "h_signal": "calc", "h_avg_vol": "calc",
    # options scanner
    "h_cur_iv": "chain", "h_hv30": "calc", "h_iv_hv": "calc",
    "h_iv_rank": "calc", "h_iv_pctile": "calc", "h_exp_move": "calc",
    "h_dte": "chain",
    # options flow
    "h_flow_pcr": "chain", "h_max_pain": "calc",
    # strategy suggestions
    "h_strat_credit": "chain", "h_strat_max_profit": "calc",
    "h_strat_max_loss": "calc", "h_strat_breakeven": "calc",
    "h_strat_pop": "calc",
    # portfolio
    "h_total_value": "calc", "h_daily_pnl": "calc", "h_total_pnl": "calc",
    "h_positions_count": "user", "h_port_beta": "calc",
    "h_port_sharpe": "calc", "h_port_vol": "calc", "h_port_maxdd": "calc",
    "h_realized_beta": "calc", "h_weight": "calc", "h_mkt_value": "calc",
    "h_pnl": "calc", "h_pnl_pct": "calc", "h_day_chg": "calc",
    "h_beta": "calc", "h_sharpe_stock": "calc", "h_vol_ann": "calc",
    "h_maxdd_stock": "calc", "h_dist_52w": "calc",
    "h_entry": "user", "h_shares": "user",
    # company screener / deep dive (raw Yahoo fundamentals)
    "h_mcap": "yahoo", "h_pe_t": "yahoo", "h_pe_f": "yahoo",
    "h_eps": "yahoo", "h_div": "yahoo", "h_chg_daily": "yahoo",
    "h_vol_shares": "yahoo", "h_pb": "yahoo", "h_roe": "yahoo",
    "h_margin": "yahoo", "h_rev_growth": "yahoo", "h_target": "yahoo",
    "h_recommendation": "yahoo", "h_employees": "yahoo",
    "h_top_inflow": "calc",
}


def h(key: str, lang: str = "en") -> str:
    """
    Explanation text for a metric (st help tooltips), with the data source
    appended in parentheses. '' when the key is unknown.
    """
    entry = _H.get(key)
    if entry is None:
        return ""
    base = entry.get(lang) or entry.get("en") or ""
    src = _SRC.get(_H_SRC.get(key, ""))
    if base and src:
        return f"{base}\n\n{src.get(lang) or src['en']}"
    return base


# --------------------------------------------------------------------------- #
# Localized instrument names (tickers -> display names)
# --------------------------------------------------------------------------- #
INSTRUMENT_NAMES: Dict[str, Dict[str, str]] = {
    "en": {
        # indices
        "^GSPC": "S&P 500", "^NDX": "Nasdaq 100", "^IXIC": "Nasdaq Composite",
        "^DJI": "Dow Jones",
        "^RUT": "Russell 2000", "^GDAXI": "DAX (Germany)", "^FTSE": "FTSE 100 (UK)",
        "^N225": "Nikkei 225 (Japan)", "^HSI": "Hang Seng (HK)", "^TA125.TA": "TA-125 (Israel)",
        # volatility
        "^VIX": "VIX (S&P 500)", "^VXN": "VXN (Nasdaq-100)",
        "^OVX": "OVX (Crude Oil)", "^GVZ": "GVZ (Gold)",
        # options-derived indices
        "^VIX9D": "VIX 9-Day", "^VIX3M": "VIX 3-Month", "^VIX6M": "VIX 6-Month",
        "^SKEW": "SKEW (Tail Risk)", "^MOVE": "MOVE (Bond Volatility)",
        # yields
        "^IRX": "US 13-Week Bill", "^FVX": "US 5-Year Note",
        "^TNX": "US 10-Year Note", "^TYX": "US 30-Year Bond",
        # commodities
        "GC=F": "Gold", "SI=F": "Silver", "HG=F": "Copper",
        "PL=F": "Platinum", "PA=F": "Palladium", "ALI=F": "Aluminum",
        "CL=F": "WTI Crude", "BZ=F": "Brent Crude", "NG=F": "Natural Gas",
        "URA": "Uranium (URA ETF)",
        "ZW=F": "Wheat", "ZC=F": "Corn", "ZS=F": "Soybeans",
        "SB=F": "Sugar", "KC=F": "Coffee", "CC=F": "Cocoa", "CT=F": "Cotton",
        "LIT": "Lithium (LIT ETF)", "NTR": "Fertilizers (Nutrien)",
        # dollar & fx
        "DX-Y.NYB": "US Dollar Index", "ILS=X": "USD/ILS (Shekel)",
        "EURUSD=X": "EUR/USD", "GBPUSD=X": "GBP/USD", "JPY=X": "USD/JPY",
        "CHF=X": "USD/CHF", "CAD=X": "USD/CAD", "AUDUSD=X": "AUD/USD",
        "NZDUSD=X": "NZD/USD", "CNY=X": "USD/CNY", "INR=X": "USD/INR",
        "KRW=X": "USD/KRW", "SGD=X": "USD/SGD", "MXN=X": "USD/MXN",
        "BRL=X": "USD/BRL", "ZAR=X": "USD/ZAR", "TRY=X": "USD/TRY",
        "SEK=X": "USD/SEK", "NOK=X": "USD/NOK", "PLN=X": "USD/PLN",
        # crypto (dynamic list — common tops named; others use screener names)
        "BTC-USD": "Bitcoin", "ETH-USD": "Ethereum", "SOL-USD": "Solana",
        "XRP-USD": "XRP (Ripple)", "BNB-USD": "BNB", "DOGE-USD": "Dogecoin",
        "TRX-USD": "TRON", "ADA-USD": "Cardano", "LINK-USD": "Chainlink",
        "AVAX-USD": "Avalanche", "LTC-USD": "Litecoin", "XLM-USD": "Stellar",
        "DOT-USD": "Polkadot", "SHIB-USD": "Shiba Inu",
        # sectors
        "XLK": "Technology", "XLF": "Financials", "XLE": "Energy",
        "XLV": "Health Care", "XLY": "Consumer Discretionary",
        "XLP": "Consumer Staples", "XLI": "Industrials", "XLB": "Materials",
        "XLU": "Utilities", "XLRE": "Real Estate", "XLC": "Communication Services",
        "SPY": "S&P 500 ETF (benchmark)",
    },
    "he": {
        # indices
        "^GSPC": "S&P 500", "^NDX": "נאסד\"ק 100", "^IXIC": "נאסד\"ק (מורכב)",
        "^DJI": "דאו ג'ונס",
        "^RUT": "ראסל 2000", "^GDAXI": "דאקס (גרמניה)", "^FTSE": "פוטסי 100 (בריטניה)",
        "^N225": "ניקיי 225 (יפן)", "^HSI": "האנג סנג (הונג קונג)", "^TA125.TA": "ת\"א 125 (ישראל)",
        # volatility
        "^VIX": "מדד הפחד VIX", "^VXN": "VXN (נאסד\"ק 100)",
        "^OVX": "OVX (נפט)", "^GVZ": "GVZ (זהב)",
        # options-derived indices
        "^VIX9D": "VIX 9 ימים", "^VIX3M": "VIX 3 חודשים", "^VIX6M": "VIX 6 חודשים",
        "^SKEW": "SKEW (סיכון זנב)", "^MOVE": "MOVE (תנודתיות אג\"ח)",
        # yields
        "^IRX": "אג\"ח ארה\"ב 13 שבועות", "^FVX": "אג\"ח ארה\"ב 5 שנים",
        "^TNX": "אג\"ח ארה\"ב 10 שנים", "^TYX": "אג\"ח ארה\"ב 30 שנה",
        # commodities
        "GC=F": "זהב", "SI=F": "כסף", "HG=F": "נחושת",
        "PL=F": "פלטינה", "PA=F": "פלדיום", "ALI=F": "אלומיניום",
        "CL=F": "נפט WTI", "BZ=F": "נפט ברנט", "NG=F": "גז טבעי",
        "URA": "אורניום (תעודת סל URA)",
        "ZW=F": "חיטה", "ZC=F": "תירס", "ZS=F": "סויה",
        "SB=F": "סוכר", "KC=F": "קפה", "CC=F": "קקאו", "CT=F": "כותנה",
        "LIT": "ליתיום (תעודת סל LIT)", "NTR": "דשנים (Nutrien)",
        # dollar & fx
        "DX-Y.NYB": "מדד הדולר", "ILS=X": "דולר/שקל",
        "EURUSD=X": "אירו/דולר", "GBPUSD=X": "ליש\"ט/דולר", "JPY=X": "דולר/ין יפני",
        "CHF=X": "דולר/פרנק שוויצרי", "CAD=X": "דולר/דולר קנדי",
        "AUDUSD=X": "דולר אוסטרלי/דולר", "NZDUSD=X": "דולר ניו-זילנדי/דולר",
        "CNY=X": "דולר/יואן סיני", "INR=X": "דולר/רופי הודי",
        "KRW=X": "דולר/וון קוריאני", "SGD=X": "דולר/דולר סינגפורי",
        "MXN=X": "דולר/פזו מקסיקני", "BRL=X": "דולר/ריאל ברזילאי",
        "ZAR=X": "דולר/ראנד דרום-אפריקאי", "TRY=X": "דולר/לירה טורקית",
        "SEK=X": "דולר/כתר שוודי", "NOK=X": "דולר/כתר נורווגי",
        "PLN=X": "דולר/זלוטי פולני",
        # crypto (dynamic list — common tops named; others use screener names)
        "BTC-USD": "ביטקוין", "ETH-USD": "אתריום", "SOL-USD": "סולאנה",
        "XRP-USD": "ריפל (XRP)", "BNB-USD": "BNB", "DOGE-USD": "דוג'קוין",
        "TRX-USD": "טרון (TRON)", "ADA-USD": "קרדאנו", "LINK-USD": "צ'יינלינק",
        "AVAX-USD": "אבלאנץ'", "LTC-USD": "לייטקוין", "XLM-USD": "סטלר",
        "DOT-USD": "פולקאדוט", "SHIB-USD": "שיבא אינו",
        # sectors
        "XLK": "טכנולוגיה", "XLF": "פיננסים", "XLE": "אנרגיה",
        "XLV": "בריאות", "XLY": "צריכה מחזורית", "XLP": "צריכה בסיסית",
        "XLI": "תעשייה", "XLB": "חומרי גלם", "XLU": "שירותים ציבוריים",
        "XLRE": "נדל\"ן", "XLC": "תקשורת",
        "SPY": "תעודת סל S&P 500 (בנצ'מרק)",
    },
}


# Yahoo screener sector names (exact filter values) -> localized labels
YAHOO_SECTOR_NAMES: Dict[str, Dict[str, str]] = {
    "en": {
        "Technology": "Technology",
        "Financial Services": "Financial Services",
        "Healthcare": "Healthcare",
        "Consumer Cyclical": "Consumer Cyclical",
        "Consumer Defensive": "Consumer Defensive",
        "Energy": "Energy",
        "Industrials": "Industrials",
        "Basic Materials": "Basic Materials",
        "Utilities": "Utilities",
        "Real Estate": "Real Estate",
        "Communication Services": "Communication Services",
    },
    "he": {
        "Technology": "טכנולוגיה",
        "Financial Services": "שירותים פיננסיים",
        "Healthcare": "בריאות",
        "Consumer Cyclical": "צריכה מחזורית",
        "Consumer Defensive": "צריכה בסיסית",
        "Energy": "אנרגיה",
        "Industrials": "תעשייה",
        "Basic Materials": "חומרי גלם",
        "Utilities": "שירותים ציבוריים",
        "Real Estate": "נדל\"ן",
        "Communication Services": "תקשורת",
    },
}


def yahoo_sector_label(sector: str, lang: str = "en") -> str:
    """Localized label for a Yahoo screener sector name."""
    return YAHOO_SECTOR_NAMES.get(lang, {}).get(sector) or sector


def instrument_name(ticker: str, lang: str = "en", default: str = "") -> str:
    """Localized display name for a ticker, with graceful fallbacks."""
    name = INSTRUMENT_NAMES.get(lang, {}).get(ticker)
    if name:
        return name
    name = INSTRUMENT_NAMES["en"].get(ticker)
    if name:
        return name
    return default or ticker


# --------------------------------------------------------------------------- #
# CSS injected by app.py
# --------------------------------------------------------------------------- #
BASE_CSS = """
<style>
/* tighter, more professional layout */
div.block-container { padding-top: 2.2rem; padding-bottom: 2rem; }
[data-testid="stMetric"] {
    background: rgba(128, 128, 128, 0.08);
    border: 1px solid rgba(128, 128, 128, 0.18);
    border-radius: 10px;
    padding: 10px 14px;
}
[data-testid="stMetricLabel"] { font-size: 0.82rem; }
h3 { margin-top: 0.6rem; }
</style>
"""

RTL_CSS = """
<style>
/* Right-to-left layout for Hebrew */
div.block-container { direction: rtl; text-align: right; }
[data-testid="stSidebar"] { direction: rtl; text-align: right; }
[data-testid="stMetric"] { direction: rtl; text-align: right; }
/* keep numeric metric values readable (numbers are LTR by nature) */
[data-testid="stMetricValue"], [data-testid="stMetricDelta"] { direction: ltr; text-align: right; }
/* tables and charts stay LTR internally for readability */
[data-testid="stDataFrame"] { direction: ltr; }
.js-plotly-plot { direction: ltr; }
[data-testid="stExpander"] summary { direction: rtl; text-align: right; }
</style>
"""
