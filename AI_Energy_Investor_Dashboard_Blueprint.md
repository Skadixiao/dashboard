# AI & Energy Investor Dashboard

## 1. Project Overview

### 1.1 Project Goal

Build a personal investment dashboard focused on:

- Artificial intelligence
- Semiconductors
- Memory and storage
- Data centres
- Power infrastructure
- Energy markets
- Portfolio risk management

The dashboard should not merely collect financial news. Its purpose is to support investment decisions by answering three questions:

1. What upcoming events could affect my holdings?
2. Did the latest result beat or miss market expectations?
3. Does the new information strengthen, weaken, or invalidate my investment thesis?

---

## 2. Core Design Principles

### 2.1 Decision-Oriented

Every data point should help support one of the following actions:

- Buy
- Small Add
- Hold
- Wait for Earnings
- Do Not Add
- Review for Exit

### 2.2 Expectation Matters More Than Headline Growth

A company may report strong growth but still fall if the result is below market expectations.

The dashboard should therefore compare:

- Actual result vs consensus
- Guidance vs consensus
- New guidance vs previous guidance
- Current valuation vs historical valuation
- Current fundamentals vs original investment thesis

### 2.3 Official Sources First

Prioritise official and primary sources:

1. Company investor relations pages
2. SEC filings
3. Federal Reserve
4. US Bureau of Labor Statistics
5. US Bureau of Economic Analysis
6. US Energy Information Administration
7. Company earnings call transcripts
8. Reputable financial data providers
9. General financial news
10. Social media and market commentary

### 2.4 Avoid Information Overload

Do not collect every article or analyst opinion.

Only prioritise information that changes:

- Revenue expectations
- Earnings expectations
- Product timelines
- Capital expenditure
- Market demand
- Competitive position
- Regulation
- Valuation
- Portfolio risk
- Investment thesis

---

# 3. Dashboard Structure

The dashboard should contain six main modules:

1. Investor Calendar
2. Company Watchlist
3. Earnings Dashboard
4. Industry Dashboard
5. Energy Dashboard
6. Portfolio Risk Dashboard

---

# 4. Home Page Layout

## 4.1 Portfolio Summary

Display:

- Total portfolio value
- Total invested capital
- Cash balance
- Cash percentage
- Daily profit and loss
- Total unrealised profit and loss
- Largest individual position
- Largest theme exposure
- Number of upcoming high-risk events
- Portfolio percentage reporting earnings within the next 7 days
- Portfolio percentage exposed to semiconductor cycle
- Portfolio percentage exposed to interest-rate-sensitive growth stocks

Example:

| Metric | Value |
|---|---:|
| Portfolio Value | £12,500 |
| Cash Balance | £4,100 |
| Cash Percentage | 32.8% |
| Largest Position | AMD |
| Largest Theme | AI Compute |
| Earnings Exposure Next 7 Days | 24% |
| High-Priority Events Next 7 Days | 4 |

---

## 4.2 Upcoming Catalysts

Display the next 10 important events.

Example:

| Date | Event | Importance | Related Holdings | Action Required |
|---|---|---|---|---|
| Tomorrow | US CPI | Very High | AMD, MU, MRVL | Review rate-sensitive exposure |
| 3 Days | TSMC Monthly Revenue | High | AMD, NVDA, ASML | Check AI demand signal |
| 6 Days | AMD Earnings | Very High | AMD | Do not add before earnings |
| 13 Days | FOMC Decision | Very High | All growth holdings | Review cash and position sizes |

---

## 4.3 Watchlist Summary

Display one row per company.

Recommended columns:

| Field | Description |
|---|---|
| Ticker | Stock ticker |
| Company | Company name |
| Theme | AI Compute, Memory, Energy, etc. |
| Position Value | Current position value |
| Portfolio Weight | Percentage of portfolio |
| Average Cost | Average purchase cost |
| Current Price | Latest price |
| Unrealised P/L | Profit or loss |
| Next Earnings | Next earnings date |
| Days to Earnings | Countdown |
| Valuation Status | Expensive, Fair, Attractive, Deep Value |
| Thesis Status | Green, Amber, Red |
| Action Status | Buy, Hold, Wait, Review |
| Risk Flag | Earnings, valuation, regulation, competition |

---

## 4.4 AI and Semiconductor Indicators

Display:

- Hyperscaler capital expenditure trend
- AI server demand trend
- TSMC monthly revenue growth
- DRAM price trend
- NAND price trend
- HBM supply status
- Semiconductor equipment order trend
- Advanced packaging capacity trend
- AI accelerator product launch timeline
- Export control updates

---

## 4.5 Energy Indicators

Display:

- Brent crude oil
- WTI crude oil
- Henry Hub natural gas
- European natural gas
- UK wholesale electricity price
- European electricity price
- Carbon price
- US crude oil inventory
- US natural gas storage
- Data-centre power demand announcements
- Utility capital expenditure
- Transformer lead times
- Grid connection delays
- Nuclear restart announcements
- Power purchase agreements

---

## 4.6 News and Filings

Only include:

- Company official announcements
- Earnings releases
- 10-Q and 10-K filings
- 8-K filings
- Form 4 insider transactions
- Product delays
- Product launches
- Major contract wins
- Major customer changes
- Guidance changes
- Capital expenditure changes
- Export restrictions
- Regulation
- Senior management changes
- Mergers and acquisitions
- Major financing
- Large analyst earnings estimate revisions

Exclude low-value noise such as:

- Small target-price changes
- Unverified rumours
- Generic market commentary
- Repetitive social media opinions
- Articles without new information

---

# 5. Investor Calendar

## 5.1 Company Events

Track:

- Earnings date
- Earnings release time
- Pre-market or after-hours
- Earnings call time
- Investor Day
- Product launch
- Shareholder meeting
- Ex-dividend date
- Major conference presentation
- Regulatory decision
- SEC filing deadline
- Capital Markets Day
- Lock-up expiry
- Major contract renewal
- Product shipment date

Recommended fields:

| Field | Description |
|---|---|
| Event ID | Unique event identifier |
| Company | Related company |
| Ticker | Stock ticker |
| Event Type | Earnings, product launch, filing, etc. |
| Event Date | Date |
| Event Time | Time |
| Time Zone | Relevant time zone |
| Importance | Low, Medium, High, Very High |
| Related Holdings | Other affected companies |
| Market Expectation | Consensus or expected outcome |
| My Focus | Metrics to monitor |
| Pre-Event Action | Planned action before event |
| Post-Event Review | Review status after event |
| Source | Official source |
| Notes | Additional context |

Example:

```yaml
event: Micron Quarterly Earnings
ticker: MU
importance: Very High
market_expectation:
  revenue: TBD
  eps: TBD
  gross_margin: TBD
my_focus:
  - HBM revenue
  - DRAM pricing
  - NAND pricing
  - Inventory days
  - Gross margin
  - Next-quarter guidance
pre_event_action:
  - Do not chase price
  - Check current position against maximum size
post_event_action:
  - Update earnings table
  - Update memory cycle status
  - Review investment thesis
```

---

## 5.2 Macroeconomic Events

Track:

### Federal Reserve

- FOMC interest-rate decision
- Federal Reserve press conference
- Summary of Economic Projections
- Dot plot
- FOMC meeting minutes
- Major Federal Reserve speeches

### Inflation

- CPI
- Core CPI
- PCE
- Core PCE
- PPI

### Employment

- Nonfarm payrolls
- Unemployment rate
- Average hourly earnings
- Initial jobless claims
- JOLTS
- ADP employment report

### Growth and Activity

- GDP
- Retail sales
- Industrial production
- ISM Manufacturing
- ISM Services
- Consumer confidence
- Durable goods orders

### Rates and Liquidity

- US Treasury auctions
- US 2-year yield
- US 10-year yield
- Yield curve
- Dollar index
- Financial conditions

Recommended fields:

| Field | Description |
|---|---|
| Event | CPI, FOMC, NFP, etc. |
| Date | Release date |
| Time | Release time |
| Consensus | Market expectation |
| Previous | Previous release |
| Actual | Actual result |
| Surprise | Actual minus consensus |
| Market Reaction | Equity, bond and currency response |
| Portfolio Impact | Estimated impact |
| Notes | Interpretation |

---

# 6. Company Watchlist

## 6.1 Company Classification

Recommended themes:

### AI Compute

- NVIDIA
- AMD
- Intel
- AI accelerator companies
- Custom ASIC providers

### Memory and Storage

- Micron
- SanDisk-related storage companies
- DRAM manufacturers
- NAND manufacturers
- HBM supply-chain companies

### AI Networking and Connectivity

- Marvell
- Broadcom
- Arista Networks
- Optical networking companies

### Semiconductor Manufacturing

- TSMC
- ASML
- Applied Materials
- Lam Research
- KLA
- Advanced packaging suppliers

### Data-Centre Infrastructure

- Vertiv
- Eaton
- Schneider Electric
- Cooling companies
- UPS providers
- Transformer companies
- Switchgear companies

### Power and Energy

- Utilities
- Independent power producers
- Nuclear companies
- Natural gas companies
- LNG companies
- Grid equipment companies
- Energy storage companies

---

## 6.2 Company Master Table

Recommended fields:

| Field | Description |
|---|---|
| Company ID | Unique identifier |
| Ticker | Stock ticker |
| Company Name | Full company name |
| Sector | Sector |
| Theme | Investment theme |
| Sub-Theme | More detailed category |
| Currency | Trading currency |
| Exchange | Listing exchange |
| Position Value | Current holding value |
| Portfolio Weight | Portfolio percentage |
| Average Cost | Average purchase price |
| Current Price | Latest price |
| Market Cap | Current market capitalisation |
| Next Earnings | Next earnings date |
| Investor Relations URL | Official IR page |
| SEC CIK | SEC identifier |
| Primary Thesis | Main reason for owning |
| Key Catalyst | Main upside catalyst |
| Key Risk | Main downside risk |
| Maximum Position | Maximum allowed position |
| Normal Position | Normal target position |
| Initial Position | Initial position size |
| Thesis Status | Green, Amber, Red |
| Valuation Status | Expensive, Fair, Attractive, Deep Value |
| Action Status | Buy, Hold, Wait, Review |
| Last Thesis Review | Last review date |

---

# 7. Earnings Dashboard

## 7.1 Universal Earnings Metrics

Track:

- Revenue
- Revenue growth
- EPS
- Gross margin
- Operating margin
- Net margin
- Free cash flow
- Capital expenditure
- Operating cash flow
- Share repurchases
- Debt
- Net cash
- Next-quarter revenue guidance
- Full-year revenue guidance
- Next-quarter EPS guidance
- Full-year EPS guidance

For every metric, store:

- Actual
- Consensus
- Previous period
- Year-on-year change
- Quarter-on-quarter change
- Surprise percentage

Recommended structure:

| Metric | Actual | Consensus | Surprise | Previous Quarter | Previous Year |
|---|---:|---:|---:|---:|---:|
| Revenue |  |  |  |  |  |
| EPS |  |  |  |  |  |
| Gross Margin |  |  |  |  |  |
| Free Cash Flow |  |  |  |  |  |
| Capex |  |  |  |  |  |

---

## 7.2 AI Chip Company Metrics

For AMD, NVIDIA, Marvell and similar companies, track:

- Data-centre revenue
- AI accelerator revenue
- AI product backlog
- Cloud customer demand
- New product launch timing
- Product shipment timing
- Product yield
- Supply constraints
- Advanced packaging constraints
- Gross margin
- R&D expenditure
- Hyperscaler adoption
- China exposure
- Export restriction impact
- Customer concentration
- Market-share commentary

---

## 7.3 Memory Company Metrics

For Micron and related companies, track:

- DRAM bit shipments
- NAND bit shipments
- DRAM average selling price
- NAND average selling price
- HBM revenue
- HBM capacity
- HBM supply commitments
- Inventory days
- Gross margin
- Utilisation rate
- Capital expenditure
- Supply growth
- Demand growth
- PC demand
- Smartphone demand
- Data-centre demand
- Automotive demand
- Management cycle commentary

---

## 7.4 Memory Cycle Indicator

Suggested stages:

1. Oversupply
2. Destocking
3. Stabilisation
4. Price Recovery
5. Strong Demand
6. Capacity Expansion
7. Cycle Peak
8. Renewed Oversupply

Recommended fields:

| Field | Description |
|---|---|
| Current Stage | Current cycle stage |
| DRAM Price Trend | Rising, flat, falling |
| NAND Price Trend | Rising, flat, falling |
| Inventory Trend | Rising or falling |
| Utilisation Trend | Rising or falling |
| Capex Trend | Expanding or contracting |
| Demand Commentary | Management commentary |
| Supply Commentary | Management commentary |
| Confidence | Low, Medium, High |
| Last Updated | Review date |

---

# 8. Industry Dashboard

## 8.1 AI Demand Indicators

Track:

- Microsoft capital expenditure
- Amazon capital expenditure
- Alphabet capital expenditure
- Meta capital expenditure
- Oracle capital expenditure
- AI infrastructure commentary
- Cloud AI revenue
- AI server shipment forecasts
- GPU lead times
- AI accelerator demand
- Data-centre construction
- Data-centre electricity demand

---

## 8.2 Semiconductor Supply Indicators

Track:

- TSMC monthly revenue
- Foundry utilisation
- Advanced packaging capacity
- CoWoS capacity
- HBM capacity
- HBM yield
- Wafer pricing
- Semiconductor equipment orders
- Fab construction
- Industry capital expenditure
- Export controls
- Government subsidies
- Supply-chain disruptions

---

## 8.3 Competitive Landscape

For each company, store:

| Field | Description |
|---|---|
| Company | Main company |
| Competitor | Competitor |
| Product Area | GPU, CPU, networking, memory, etc. |
| Relative Strength | Stronger, similar, weaker |
| Market Share Trend | Rising, stable, falling |
| Key Competitive Event | Product launch or customer win |
| Risk Level | Low, Medium, High |
| Notes | Supporting detail |

Example:

```yaml
company: AMD
competitors:
  - NVIDIA
  - Intel
  - Custom ASIC providers
products:
  - MI-series accelerators
  - EPYC server CPUs
  - Ryzen CPUs
key_risks:
  - Slower AI accelerator adoption
  - Software ecosystem disadvantage
  - Hyperscaler custom chip competition
key_catalysts:
  - New accelerator launch
  - Major hyperscaler adoption
  - Data-centre market-share gain
```

---

# 9. Energy Dashboard

## 9.1 Commodity Data

Track:

- WTI crude oil
- Brent crude oil
- Henry Hub natural gas
- European natural gas
- LNG prices
- Coal prices
- Uranium prices
- Carbon prices
- UK wholesale electricity
- European wholesale electricity

For each series, store:

- Current price
- Daily change
- Weekly change
- Monthly change
- 52-week percentile
- Key driver
- Related holdings

---

## 9.2 Energy Calendar

Track:

- EIA crude oil inventory
- EIA natural gas storage
- OPEC meetings
- LNG facility updates
- Major refinery outages
- Nuclear restart decisions
- Utility earnings
- Capacity market auctions
- Power-market reforms
- Carbon policy changes
- Weather events
- Grid policy announcements

---

## 9.3 AI and Energy Intersection

Track:

- Hyperscaler power purchase agreements
- Data-centre power demand forecasts
- Data-centre locations
- Grid connection queues
- Transformer lead times
- Switchgear lead times
- Utility capital expenditure
- Nuclear power agreements
- Natural gas generation orders
- Gas turbine orders
- Grid reinforcement projects
- Transmission investment
- Distribution investment
- Behind-the-meter generation
- Battery storage projects
- Data-centre cooling demand

Recommended project table:

| Field | Description |
|---|---|
| Project | Project name |
| Company | Company involved |
| Location | Project location |
| Capacity | MW or GW |
| Energy Source | Nuclear, gas, renewable, grid |
| Project Type | Data centre, PPA, generation, grid |
| Announcement Date | Date |
| Expected Completion | Estimated completion |
| Investment Value | Project value |
| Related Stocks | Potential beneficiaries |
| Status | Proposed, approved, under construction, operational |
| Source | Official source |

---

# 10. Portfolio Risk Dashboard

## 10.1 Theme Exposure

Example:

| Theme | Exposure |
|---|---:|
| AI Compute | 25% |
| Memory Cycle | 18% |
| AI Networking | 12% |
| Semiconductor Equipment | 10% |
| Data-Centre Power | 8% |
| Other | 27% |

---

## 10.2 Risk Factor Exposure

Track:

- AI capital expenditure exposure
- Semiconductor cycle exposure
- Memory cycle exposure
- Interest-rate exposure
- China revenue exposure
- Taiwan supply-chain exposure
- Hyperscaler customer concentration
- Commodity price exposure
- Electricity price exposure
- Regulatory exposure
- High valuation exposure
- Earnings-event exposure

Example:

| Risk Factor | Portfolio Exposure | Risk Level |
|---|---:|---|
| AI Capex Slowdown | 48% | High |
| Semiconductor Cycle | 42% | High |
| Memory Cycle | 20% | Medium |
| China Export Restrictions | 31% | High |
| Rising Bond Yields | 65% | High |
| Data-Centre Power Growth | 14% | Medium |

---

## 10.3 Position Limits

For each stock:

| Field | Description |
|---|---|
| Initial Position | Starter position |
| Normal Position | Standard target |
| Maximum Position | Hard limit |
| Current Position | Current holding |
| Remaining Capacity | Maximum minus current |
| Add Condition | Required before adding |
| Stop Adding Condition | Condition that blocks adding |

Example:

```yaml
ticker: MU
initial_position: £50
normal_position: £200
maximum_position: £400
current_position: £215
add_conditions:
  - Valuation enters target range
  - HBM thesis remains intact
  - Gross margin trend remains positive
  - Inventory does not deteriorate
stop_adding_conditions:
  - Guidance cut
  - Inventory rises sharply
  - HBM orders weaken
  - Position exceeds maximum size
```

---

# 11. Decision Status System

## 11.1 Valuation Status

Use four levels:

- Expensive
- Fair
- Attractive
- Deep Value

Valuation should consider:

- Forward P/E
- EV/EBITDA
- Price-to-sales
- Free-cash-flow yield
- Historical valuation range
- Peer valuation
- Growth expectations
- Current cycle stage

Do not classify a stock as cheap only because it has fallen from its previous high.

---

## 11.2 Thesis Status

### Green

The investment thesis remains intact.

Examples:

- Revenue growth remains strong
- Market share is stable or improving
- Product launch remains on schedule
- Gross margin remains healthy
- Demand outlook remains positive

### Amber

There is a meaningful risk that requires confirmation.

Examples:

- Growth is slowing
- Guidance is cautious
- Pricing is weakening
- Inventory is rising
- Product adoption is below expectations

### Red

The core thesis is broken.

Examples:

- Major product failure
- Sustained customer loss
- Structural margin decline
- Severe guidance cuts
- Market-share collapse
- Regulatory restriction removes a major market
- Management credibility deteriorates

---

## 11.3 Action Status

Use:

- Buy
- Small Add
- Hold
- Wait for Earnings
- Do Not Add
- Review for Exit

Action should depend on:

- Valuation
- Thesis status
- Position size
- Upcoming catalysts
- Portfolio concentration
- Market expectations
- Risk limits

---

# 12. News Priority System

## Level 1: Immediate Review

- Earnings and guidance
- 8-K filings
- FOMC decisions
- CPI
- PCE
- Nonfarm payrolls
- Export restrictions
- Product delays
- Major customer capex cuts
- CEO or CFO departure
- Major merger or acquisition
- Major financing
- Large regulatory decision

## Level 2: Review the Same Day

- Competitor earnings
- Major estimate revisions
- Industry pricing changes
- Important product launch
- Hyperscaler capital expenditure changes
- EIA energy data
- Major contract win
- Major insider transaction

## Level 3: Weekly Review

- General financial news
- Small target-price changes
- Generic market commentary
- Social media discussions
- Technical analysis
- Minor product updates

---

# 13. Alerts and Notifications

Recommended alerts:

- Earnings in 7 days
- Earnings in 1 day
- Earnings released
- Earnings call completed
- FOMC in 1 day
- CPI in 1 day
- PCE in 1 day
- New 8-K filed
- New 10-Q or 10-K filed
- Guidance raised
- Guidance cut
- CEO or CFO change
- Product delay
- Major customer capex change
- Position exceeds normal size
- Position exceeds maximum size
- Thesis not reviewed for 90 days
- Share price falls sharply without updated fundamentals
- Valuation enters target range
- Portfolio theme exposure exceeds limit
- More than 25% of portfolio reports earnings in one week

---

# 14. Minimum Viable Product

The first version should contain five core tables.

## 14.1 Companies

Contains:

- Ticker
- Company name
- Theme
- Position
- Average cost
- Maximum position
- Thesis
- Valuation status
- Thesis status
- Action status
- Next earnings date

## 14.2 Events

Contains:

- Date
- Event
- Type
- Importance
- Related companies
- Expected result
- Actual result
- Action required

## 14.3 Earnings

Contains:

- Company
- Quarter
- Revenue
- EPS
- Gross margin
- Guidance
- Consensus
- Surprise
- Market reaction

## 14.4 Investment Thesis

Contains:

- Company
- Why I own it
- Key catalysts
- Key risks
- Evidence supporting thesis
- Thesis invalidation conditions
- Last review date
- Current status

## 14.5 Portfolio Exposure

Contains:

- Company exposure
- Theme exposure
- Sector exposure
- Risk-factor exposure
- Earnings-event exposure
- Maximum position limits

---

# 15. Suggested Data Model

## 15.1 Tables

Suggested database tables:

```text
companies
positions
events
earnings
earnings_metrics
macro_events
industry_indicators
energy_indicators
investment_theses
thesis_reviews
news_items
sec_filings
alerts
portfolio_snapshots
theme_exposures
risk_exposures
```

---

## 15.2 Example Company Schema

```yaml
company_id: amd
ticker: AMD
company_name: Advanced Micro Devices
sector: Information Technology
theme: AI Compute
sub_theme: GPU and CPU
exchange: NASDAQ
currency: USD
position_value_gbp: 0
portfolio_weight: 0
average_cost: 0
normal_position_gbp: 200
maximum_position_gbp: 400
valuation_status: Fair
thesis_status: Green
action_status: Hold
next_earnings_date: null
primary_thesis: >
  AMD can gain share in data-centre CPUs and AI accelerators.
key_catalysts:
  - AI accelerator adoption
  - EPYC market-share gains
  - Hyperscaler customer wins
key_risks:
  - NVIDIA ecosystem advantage
  - Custom ASIC competition
  - Product execution
thesis_invalidation:
  - Sustained data-centre share loss
  - Repeated product delays
  - Material guidance deterioration
last_reviewed: null
```

---

## 15.3 Example Event Schema

```yaml
event_id: fomc_2026_01
event_type: FOMC
event_name: Federal Reserve Interest Rate Decision
event_date: null
event_time: null
timezone: America/New_York
importance: Very High
related_themes:
  - AI Compute
  - Semiconductors
  - Growth Stocks
consensus: null
previous: null
actual: null
portfolio_impact: High
pre_event_action:
  - Review cash percentage
  - Review high-valuation holdings
post_event_action:
  - Record bond yield reaction
  - Record semiconductor index reaction
source: Federal Reserve
```

---

# 16. Recommended Development Roadmap

## Phase 1: Manual MVP

Goal:

- Create the five core tables
- Enter current holdings manually
- Enter upcoming earnings manually
- Enter major macro events manually
- Add thesis and position limits
- Build a basic calendar view

Suggested tools:

- Markdown
- CSV
- Excel
- Google Sheets
- Notion
- SQLite

## Phase 2: Basic Automation

Automate:

- Stock prices
- Portfolio value
- Earnings dates
- Economic calendar
- SEC filing alerts
- Commodity prices
- Basic charts

Suggested tools:

- Python
- Pandas
- SQLite or PostgreSQL
- Streamlit
- Plotly
- Scheduled scripts
- Financial APIs

## Phase 3: Decision Engine

Add:

- Valuation scoring
- Thesis status scoring
- Event-risk scoring
- Position-limit warnings
- Theme concentration analysis
- Earnings-surprise analysis
- Memory cycle model
- AI capex tracker

## Phase 4: Advanced Intelligence

Add:

- Earnings call summarisation
- SEC filing change detection
- Automatic thesis updates
- News deduplication
- Competitor event mapping
- Portfolio scenario analysis
- AI and energy relationship analysis
- Natural-language portfolio queries

Example queries:

```text
Which of my holdings have earnings in the next 14 days?

Which companies are currently above my normal position size?

Which AI holdings are most exposed to rising bond yields?

Has Micron's investment thesis weakened since the last earnings report?

Which energy companies may benefit from data-centre power demand?

What changed in my portfolio risk this week?
```

---

# 17. Example Decision Output

The dashboard should produce decision-oriented summaries such as:

```text
AMD fell 5%.

The main driver appears to be lower market expectations for AI accelerator revenue.

The next major validation event is AMD's earnings report in six days.

The current position is already at 90% of the normal target size.

Recommendation: Wait for earnings before adding.

Key metrics to monitor:
- Data-centre revenue
- MI-series revenue
- Gross margin
- Hyperscaler adoption
- Next-quarter guidance
```

Another example:

```text
Micron's share price declined after weaker memory pricing expectations.

Current thesis status: Amber

Positive factors:
- HBM demand remains strong
- AI-related memory demand remains supportive

Risks:
- DRAM pricing is slowing
- Inventory may stop improving
- Industry capex may rise

Action: Do not add until the next pricing and inventory update.
```

---

# 18. Success Criteria

The dashboard is successful if it helps answer:

- What matters this week?
- Which events could move my holdings?
- Which holdings are too large?
- Which stocks are cheap for a good reason?
- Which investment theses are weakening?
- Which companies are benefiting from AI capital expenditure?
- Which energy companies benefit from data-centre power demand?
- What should I buy, hold, avoid adding to, or review for exit?
- What changed since the last earnings report?
- What changed in portfolio risk?

The final objective is not to predict every market move.

The objective is to make investment decisions more structured, evidence-based, consistent and less emotional.
