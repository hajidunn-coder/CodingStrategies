# Deep-dive record schema — write one JSON file per video to data/deep/<id>.json
{
 "id": "<video id>", "url": "...", "creator": "...",
 "title": "one line, what the video is actually about (not the clickbait)",
 "category": "one of: agent-architecture | claude-code-workflow | plugins-skills | vibe-coding-infra | security-legal | design-ui | ai-product-tool | business-with-ai | model-news | learning-resource | other",
 "tools": [ {"name": "...", "kind": "product|repo|skill|plugin|api|model|course|site", "where_seen": "transcript|screen|caption", "detail": "url/handle/command if shown, else short"} ],
 "claims": ["specific claims with numbers or specifics, as stated"],
 "how_to_steps": ["the actual steps the creator shows, in order"],
 "on_screen_only": ["text, UI, URLs, repo names, prompts visible in frames but NOT said in the transcript"],
 "cta": "what the creator asks (comment X / DM / link in bio / none)",
 "relevance": {"score": 1-5, "why": "for a solo founder building apps and businesses with Claude Code, veteran, time-poor"},
 "implement_score": {"score": 1-5, "why": "is this worth actually doing in our own apps/workflow; what it would take"},
 "verify": ["questions a researcher must check before trusting this (does the tool exist, cost, maintained, hype?)"]
}
