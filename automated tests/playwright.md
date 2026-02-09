## Playwright Setup
Install Playwright via pip: `pip install playwright pytest-playwright`. Run `playwright install` to download browsers. Create `test_summarize_app.py` for the E2E test; assumes a local app at `http://localhost:3000` with `<input type="file" id="upload">` and `<button id="summarize">`. [browserstack](https://www.browserstack.com/guide/playwright-upload-file)

Prepare a test file `test-doc.txt` in your project root:
```
This is a sample document for testing summarization.
It contains multiple sentences to process.
```

## Test Example
```python
import os
from playwright.sync_api import Page, expect
import pytest

def test_upload_and_summarize(page: Page):
    page.goto("http://localhost:3000")
    
    # Upload document
    test_file = os.path.join(os.path.dirname(__file__), "test-doc.txt")
    page.locator("#upload").set_input_files(test_file)
    expect(page.locator("#upload-preview")).to_be_visible()  # Verify upload UI
    
    # Click summarize button
    page.locator("#summarize").click()
    
    # Wait and assert summary appears
    expect(page.locator("#summary")).to_be_visible()
    expect(page.locator("#summary")).to_contain_text("sample document")
```

Run with `pytest test_summarize_app.py -v --headed` (use `--headed` for visual debugging). [way2automation](https://www.way2automation.com/upload-a-file-using-playwright-python/)

## Key Steps Explained
- **File Upload**: Use `locator.set_input_files(path)` on `<input type="file">` - handles hidden inputs automatically. [playwright](https://playwright.dev/python/docs/input)
- **Interactions**: `locator.click()` auto-waits for visibility/actionability.
- **Assertions**: `expect(locator).to_be_visible()` or `to_contain_text()` retries until true or timeout.
- **Adapt Locators**: Replace `#upload`, `#summarize` with real selectors (e.g., `get_by_role("button", name="Summarize")`). [youtube](https://www.youtube.com/watch?v=Qf0qZtmTqcw)

## Running Tips
| Command | Purpose |
|---------|---------|
| `playwright test` | Run all tests with reports/videos. |
| `--headed --slow-mo=500` | Visible browser, slowed for demo. |
| `--trace on` | Record traces for debugging failed tests. | [playwright](https://playwright.dev/docs/test-reporters)

This tests the full user flow reliably across Chromium/Firefox/WebKit. [browserstack](https://www.browserstack.com/guide/playwright-upload-file)


# about playwright
# Complete Playwright Tutorial: File Upload & Summarize App Testing

## Detailed Introduction to Playwright
**Playwright** is Microsoft's open-source Node.js/Python library for **automating Chromium, Firefox, and WebKit browsers** with a single API. Launched in 2020, it powers E2E testing, scraping, and PDF generation for apps like Microsoft, Netflix, and Adobe. Unlike Selenium (WebDriver-based, flaky waits), Playwright uses **DevTools Protocol** for direct browser control - **auto-waiting** ensures elements are actionable before interacting, achieving **>99% reliability** without sleeps/polling. [playwright](https://playwright.dev)

**Core Strengths for Automated Testing**:
- **Reliable Execution**: Auto-waits for network, DOM, actions; retries assertions intelligently
- **Cross-Platform**: Tests Chrome/Edge, Firefox, Safari simultaneously (`project: chromium`)
- **Speed**: Parallel workers, trace viewer, video/screenshot artifacts
- **Modern Features**: Mobile emulation, geolocation, permissions, network mocking, shadow DOM
- **Languages**: Python (your preference), JS/TS, .NET, Java
- **CI/CD Ready**: GitHub Actions, Azure Pipelines (your Docker workflows)

**Automated Testing Use Cases**:
- **E2E Flows**: User journeys (login → upload → summarize → export)
- **Regression**: Visual diffs, snapshot testing
- **API/UI Mocking**: `page.route()` intercepts fetches
- **Component Testing**: Isolated React/Vue components [checklyhq](https://checklyhq.com/docs/learn/playwright/what-is-playwright)

**Your Fit**: As a Python/Docker/AI dev in edtech, Playwright tests GPU-accelerated summarize apps, student dashboards, and collaborative coding UIs reliably.

## Playwright & MCP: AI-Powered Automation
**Model Context Protocol (MCP)** is Playwright's 2025 extension bridging browsers to **LLMs/AI agents** (Copilot, Claude, Cursor). Run `npx @playwright/mcp` to start a **local server** exposing 20+ tools (navigate, click, screenshot, accessibility tree) via JSON-RPC.

**How MCP Enables Automated Testing**:
1. **No-Code Generation**: Prompt AI: "Test upload → summarize flow" → Explores app, generates pytest code
2. **Live Exploration**: AI calls `browser_navigate(url)`, `browser_click("Summarize")`, gets snapshots/state
3. **Self-Healing**: AI inspects ARIA/DOM, adapts locators to UI changes (e.g., `#upload` → `get_by_role("textbox")`)
4. **Validation Loop**: Run → Trace → Analyze failure → Fix/Retry autonomously
5. **Zero-Boilerplate**: English test plans → Executable scripts + CI YAML [testomat](https://testomat.io/blog/playwright-mcp-modern-test-automation-from-zero-to-hero/)

**MCP Workflow Example**:
```
# Terminal 1: npx playwright-mcp
# Terminal 2 (VS Code Copilot/Claude):
"Navigate localhost:3000, upload test-doc.txt, click Summarize, assert summary visible"
→ AI: Generates/runs test_summarize_app.py above
```

**Benefits for You**:
- **AI Edtech Apps**: Auto-test voice synthesis UIs, RAG chats, student uploads
- **Maintenance-Free**: MCP adapts to deployment changes (Docker updates)
- **Speed**: 10x faster test creation vs. manual scripting [youtube](https://www.youtube.com/watch?v=AaCj939XIQ4)

## Prerequisites & Setup
`pip install playwright pytest-playwright && playwright install`

## Test Example (Enhanced)
*(See previous response for full code with 10+ commands like `route()`, `evaluate()`, `get_by_role()`)*

## Command Reference & Running Tips
*(As in previous; includes `pause()`, traces, MCP server)*

This combo - Playwright reliability + MCP AI - revolutionizes your automated testing for AI/ML edtech projects! [testomat](https://testomat.io/blog/playwright-mcp-modern-test-automation-from-zero-to-hero/)