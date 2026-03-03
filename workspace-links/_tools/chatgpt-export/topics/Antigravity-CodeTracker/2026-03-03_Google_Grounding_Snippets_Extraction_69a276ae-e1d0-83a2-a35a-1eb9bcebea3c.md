---
type: chatgpt-export-conversation
topic: "Antigravity-CodeTracker"
title: "Google Grounding Snippets Extraction"
conversation_id: "69a276ae-e1d0-83a2-a35a-1eb9bcebea3c"
imported_at_utc: "2026-03-03T05:32:15+00:00"
turn_count: 3
chars: 2628
topic_score: 1
---

# Google Grounding Snippets Extraction

- topic: `Antigravity-CodeTracker`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-001.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/69a276ae-e1d0-83a2-a35a-1eb9bcebea3c_Google_Grounding_Snippets_Extraction.txt`
- conversation_id: `69a276ae-e1d0-83a2-a35a-1eb9bcebea3c`
- matched_keywords: log
- card: [[workspace-links/_catalog/cards/Antigravity-CodeTracker|실행 로그·코드 추적 허브]]

## Summary
https://dejan.ai/blog/what-extraction-method-is-google-using-to-build-grounding-snippets/

## Transcript

## 1. user

https://dejan.ai/blog/what-extraction-method-is-google-using-to-build-grounding-snippets/

## 2. assistant

search("https://dejan.ai/blog/what-extraction-method-is-google-using-to-build-grounding-snippets/")

## 3. assistant

Here’s a clear breakdown of what extraction method Google is using to build *grounding snippets* (based on the **DEJAN AI reverse-engineering analysis**): citeturn0search0turn0view0

### 🧠 1. **Extractive Summarization (Sentence-Level Selection)**
Google’s grounding snippet pipeline does **extractive summarization**, meaning it doesn’t create new text — it picks *actual sentences* from the webpage that are most relevant to the user’s query (as opposed to generating paraphrased or abstractive summaries). citeturn0search0

- **Unit of extraction:** individual sentences. citeturn0view0  
- The algorithm scores each sentence against the query and selects the highest-scoring ones. citeturn0search0  
- These sentences become the *grounding snippet* that the model uses as factual context. citeturn0search0

### 🔍 2. **Query-Focused Scoring**
Sentences aren’t chosen arbitrarily — they’re ranked by how semantically relevant they are to the *specific query* that was issued. citeturn0view0  
That means:

- A long article can yield **different snippets** for different sub-queries. citeturn0search0  
- Sections unrelated to the query (even if on the same page) are often skipped entirely. citeturn0view0

### 📍 3. **Bias Toward Lead/Semantically Strong Content**
Two key biases were observed:

- **Lead/positional bias:** opening paragraphs tend to be extracted even if they aren’t the most directly relevant. citeturn0view0  
- **“Noise” elements** like headers, table of contents entries, and structural markers can be treated as sentences and scored alongside prose. citeturn0view0

### 📊 4. **Confidence Scoring**
Each extracted sentence (chunk) gets a *confidence score* — typically ranging from 0.1 to 1.0 — indicating how strongly it’s considered relevant to the grounding task. citeturn0view0

### 📘 5. **Pipeline Integration**
Once all snippets are extracted from selected source pages:

1. They’re bundled together as grounding context.
2. This grounding context is sent to the model with the user’s query.
3. The model generates an answer *grounded* in these selected sentences. citeturn0search0

👉 **Key takeaway:** Google uses a *query-aware, extractive summarization method* that picks and scores individual sentences from web pages to construct the factual context (“grounding snippets”) used in AI search answers. citeturn0search0
