# 💳 FinPrompt: Local LLM for Secure Financial Querying

> *No cloud = no breach risk. Privacy-first financial assistant.*

![FinPrompt Desktop App](docs/screenshots/main-window.png)
*Figure 1: FinPrompt Desktop Application Main Window*

## Overview

FinPrompt is a privacy-first financial assistant that lets users ask questions about their local bank CSV/exported data. All processing happens on-device using a local LLM—no data ever leaves your device.

## Key Features

- **🔒 100% Local**: All processing on-device, no cloud dependency
- **💬 Natural Language**: Ask questions in plain English
- **📊 CSV Support**: Works with exported bank statements
- **🛡️ PII Protection**: Automatically redacts sensitive data
- **📱 Desktop App**: Built with Tauri for native performance

## User Interface & Experience

### Main Application Window

![Main Window](docs/screenshots/main-window.png)
*Figure 2: FinPrompt Main Interface*

#### **Application Header**
- **Title Bar**: "FinPrompt - Privacy-First Financial Assistant"
- **Menu Bar**: File, Edit, View, Help menus
- **Window Controls**: Minimize, maximize, close (native OS styling)

#### **Left Sidebar - Data Management**

![Data Management](docs/screenshots/data-management.png)
*Figure 3: Data Import and Management Panel*

- **Import Section**:
  - Large "Import CSV" button with file icon
  - Drag-and-drop area with dashed border
  - Supported formats: CSV, TSV, Excel
  - File size indicator

- **Data Summary Card**:
  - **Total Transactions**: Large number with icon
  - **Date Range**: "Jan 1, 2024 - Dec 31, 2024"
  - **Total Amount**: "$XX,XXX.XX" with currency symbol
  - **Account Count**: Number of accounts
  - **Privacy Badge**: "🔒 All data processed locally"

- **Data Status Indicator**:
  - Green dot: Data loaded and ready
  - Yellow dot: Processing/analyzing
  - Red dot: Error or no data

#### **Main Content Area - Chat Interface**

![Chat Interface](docs/screenshots/chat-interface.png)
*Figure 4: Natural Language Query Interface*

- **Chat Header**:
  - "Ask me anything about your finances" subtitle
  - Privacy indicator: "🔒 Processing locally - No data leaves your device"

- **Message History**:
  - **User Messages**: Right-aligned, blue background (#3498db)
  - **Assistant Messages**: Left-aligned, light gray background (#f5f5f5)
  - **System Messages**: Centered, yellow background for warnings/errors

- **Message Format**:
  - **User Query**: Plain text in message bubble
  - **Assistant Response**:
    - Natural language answer
    - **Data Highlights**: Bold numbers and key facts
    - **Visualizations**: Inline charts for spending patterns
    - **Source Reference**: "Based on 1,234 transactions"

- **Example Conversation**:
  ```
  User: "What's my spending on restaurants this month?"
  
  Assistant: "Based on your transaction data, you spent 
  $847.32 on restaurants this month, which is 23% higher 
  than last month. Here are your top restaurants:
  
  • Restaurant A: $234.50 (8 visits)
  • Restaurant B: $189.20 (5 visits)
  • Restaurant C: $156.80 (4 visits)
  
  [Bar chart showing monthly comparison]
  ```

#### **Input Area** (Bottom)

![Input Area](docs/screenshots/input-area.png)
*Figure 5: Query Input with Suggestions*

- **Text Input Field**:
  - Large, multi-line text area
  - Placeholder: "Ask about your finances... (e.g., 'Show unusual subscriptions')"
  - Auto-resize based on content
  - Character counter (optional)

- **Quick Action Buttons** (Above input):
  - "💰 Spending Summary"
  - "📊 Monthly Trends"
  - "🚨 Unusual Activity"
  - "💳 Top Merchants"

- **Send Button**:
  - Blue button with send icon
  - Disabled while processing
  - Loading spinner when querying LLM

- **Privacy Indicator**:
  - Small text: "Processing locally - No internet required"
  - Lock icon

#### **Right Sidebar - Insights Panel** (Optional)

![Insights Panel](docs/screenshots/insights-panel.png)
*Figure 6: Financial Insights and Visualizations*

- **Quick Stats Cards**:
  - **Total Spending**: This month vs. last month
  - **Average Transaction**: Amount with trend
  - **Top Category**: Spending category with percentage

- **Visualizations**:
  - **Spending by Category**: Pie chart or bar chart
  - **Monthly Trend**: Line chart
  - **Transaction Distribution**: Histogram

- **Insights List**:
  - Auto-generated insights:
    - "You spent 15% more on dining this month"
    - "Unusual subscription detected: $9.99/month"
    - "Large transaction: $500 on [Merchant]"

### Data Import Dialog

![Import Dialog](docs/screenshots/import-dialog.png)
*Figure 7: CSV Import Interface*

- **File Selection**:
  - Native file picker
  - File type filters: CSV, TSV, Excel
  - Recent files list

- **Preview Section**:
  - Table preview of first 10 rows
  - Column detection
  - Data type inference (date, amount, description)

- **Column Mapping**:
  - Map CSV columns to:
    - Date
    - Amount
    - Description
    - Category
    - Account

- **PII Redaction Options**:
  - Checkboxes for:
    - Redact account numbers
    - Redact merchant names (optional)
    - Redact transaction IDs

- **Import Button**: 
  - "Import & Analyze" button
  - Progress bar during import
  - Success message on completion

### Settings Window

![Settings](docs/screenshots/settings.png)
*Figure 8: Application Settings*

- **LLM Configuration**:
  - Provider selection (Ollama/LM Studio)
  - Model dropdown
  - Base URL input
  - Test connection button

- **Privacy Settings**:
  - "Process all data locally" (always enabled)
  - "Auto-redact PII" toggle
  - "Clear data on exit" option

- **Display Settings**:
  - Theme selection (Light/Dark)
  - Font size
  - Date format

### Response Visualizations

![Visualizations](docs/screenshots/visualizations.png)
*Figure 9: Inline Charts and Graphs*

When the assistant provides numerical answers, visualizations appear inline:

- **Bar Charts**: For category comparisons
- **Line Charts**: For trends over time
- **Pie Charts**: For spending distribution
- **Tables**: For detailed breakdowns

All charts are interactive (hover for details, click to expand).

### Design System

#### **Color Palette**
- **Primary**: Blue (#3498db) for actions and links
- **Background**: White (#ffffff) for main area
- **Sidebar**: Light gray (#f5f5f5)
- **User Messages**: Blue (#3498db)
- **Assistant Messages**: Light gray (#f5f5f5)
- **Success**: Green (#27ae60)
- **Warning**: Orange (#f39c12)
- **Error**: Red (#e74c3c)

#### **Typography**
- **Headings**: System font, bold, 18-24px
- **Body**: System font, regular, 14-16px
- **Code/Data**: Monospace, 13px
- **Messages**: System font, 15px

#### **Spacing**
- **Padding**: 16px standard
- **Card Margin**: 8px
- **Input Padding**: 12px

### Responsive Behavior

- **Window Resize**: Panels adjust proportionally
- **Minimum Width**: 800px
- **Minimum Height**: 600px
- **Full Screen**: Maximizes content area

## Installation

```bash
git clone https://github.com/yksanjo/finprompt.git
cd finprompt
npm install
npm run tauri dev
```

## Usage

### 1. Import Your Bank Data

- Click "Import CSV" or drag and drop a file
- Map columns in the import dialog
- Review preview and confirm import

### 2. Ask Questions

Type natural language questions like:
- "Show me unusual subscriptions"
- "What's my spending on restaurants this month?"
- "Find transactions over $500"
- "Compare this month's spending to last month"
- "What are my top 5 spending categories?"

### 3. Get Instant Answers

The assistant processes your query locally and provides:
- Direct answers with numbers
- Visualizations when relevant
- Insights and recommendations
- Source references

## Screenshots

### Generating Screenshots

1. **Build and run the app**:
   ```bash
   npm run tauri dev
   ```

2. **Import sample data**: Use a test CSV file

3. **Ask questions**: Interact with the interface

4. **Capture screenshots**:
   - Use OS screenshot tools
   - Or use automated tools like Playwright for Tauri apps

### Required Screenshots

- `main-window.png` - Full application window
- `data-management.png` - Import and data summary
- `chat-interface.png` - Query interface with conversation
- `import-dialog.png` - CSV import dialog
- `settings.png` - Settings window
- `visualizations.png` - Charts and graphs in responses

## API Usage (Programmatic)

```python
from finprompt import FinPrompt

fp = FinPrompt()
fp.load_csv("transactions.csv")
answer = fp.query("What's my total spending?")
print(answer)
```

## Privacy & Security

- **100% Local Processing**: All LLM queries run on your device
- **No Network Required**: Works completely offline
- **PII Redaction**: Automatic redaction of sensitive data
- **No Telemetry**: Zero tracking or analytics
- **Open Source**: Fully auditable code

## License

MIT License
