import type { LessonContent } from "../lessons";

export const CIB_LESSONS: Record<string, LessonContent> = {
  "cib-1-1": {
    id: "cib-1-1",
    title: "Market Types",
    content: `# Financial Market Types

Financial markets are the backbone of the global economy, providing the infrastructure for capital allocation, price discovery, and risk management. Understanding the different types of markets is the first step toward mastering corporate and investment banking.

## Equity Markets

Equity markets (also called stock markets) are where shares of publicly listed companies are bought and sold. Primary markets involve the issuance of new securities through Initial Public Offerings (IPOs) and follow-on offerings, while secondary markets facilitate the trading of existing securities between investors. Major equity exchanges include the NYSE, NASDAQ, London Stock Exchange, and Hong Kong Stock Exchange. Market capitalization — the total value of a company's outstanding shares — is the primary measure of a company's size in equity markets.

## Debt / Fixed Income Markets

Debt markets are significantly larger than equity markets globally. They include government bonds (Treasuries, Gilts, Bunds), corporate bonds (investment grade and high yield), municipal bonds, and money market instruments. When a company or government needs to borrow money, they issue bonds that pay periodic interest (coupons) and return the principal at maturity. The bond market is crucial for setting interest rates across the economy.

## Derivatives Markets

Derivatives are financial instruments whose value is derived from an underlying asset — such as stocks, bonds, commodities, or currencies. Common derivatives include options (rights to buy or sell), futures (obligations to buy or sell at a future date), swaps (exchanges of cash flows), and credit default swaps (insurance against default). Derivatives serve three primary purposes: hedging risk, speculation, and arbitrage. The notional value of the global derivatives market exceeds $600 trillion.

## Foreign Exchange (FX) Markets

The FX market is the largest and most liquid financial market in the world, with daily trading volume exceeding $7 trillion. Currencies are traded in pairs (e.g., EUR/USD), and the market operates 24 hours a day across major financial centers. FX markets are essential for international trade, investment, and central bank monetary policy.

## Commodities Markets

Commodities markets facilitate the trading of physical goods including energy (oil, natural gas), metals (gold, silver, copper), and agricultural products (wheat, corn, soybeans). These markets use both spot trading (immediate delivery) and futures contracts (future delivery at a predetermined price).`,
    videos: [
      { title: "How the Stock Market Works", url: "https://www.youtube.com/watch?v=p7HKvqRI_Bo", duration: "12:34" },
      { title: "Bond Market Explained", url: "https://www.youtube.com/watch?v=RfPnSUMlgKI", duration: "10:15" },
      { title: "Derivatives Explained in One Minute", url: "https://www.youtube.com/watch?v=Wjlw7ZpZVK4", duration: "8:42" },
    ],
    quiz: [
      {
        question: "Which market is the largest by daily trading volume?",
        options: ["Equity markets", "Bond markets", "Foreign exchange markets", "Commodities markets"],
        correct: 2,
      },
      {
        question: "What is the primary market?",
        options: [
          "Where existing securities are traded",
          "Where new securities are issued for the first time",
          "The largest stock exchange in a country",
          "A market for government bonds only",
        ],
        correct: 1,
      },
      {
        question: "What are derivatives?",
        options: [
          "Stocks issued by derivative companies",
          "Financial instruments whose value is derived from an underlying asset",
          "A type of government bond",
          "Currency exchange rates",
        ],
        correct: 1,
      },
    ],
  },

  "cib-1-2": {
    id: "cib-1-2",
    title: "Key Players",
    content: `# Key Players in Financial Markets

Understanding who participates in financial markets and their roles is critical for anyone entering corporate and investment banking. Each participant has distinct motivations, strategies, and regulatory requirements.

## Investment Banks

Investment banks are the intermediaries at the center of capital markets. They advise corporations on mergers and acquisitions (M&A), underwrite debt and equity securities, provide sales and trading services, and offer research coverage. Major investment banks (often called "bulge bracket") include Goldman Sachs, JPMorgan, Morgan Stanley, Bank of America, and Citigroup. These institutions have divisions covering Investment Banking Division (IBD), Sales & Trading (S&T), Asset Management, and Research.

## Buy-Side Institutions

The "buy side" includes institutions that buy and manage securities on behalf of their clients or their own portfolios. This category includes mutual funds (Fidelity, Vanguard), hedge funds (Bridgewater, Citadel), pension funds (CalPERS, Norway Government Pension Fund), insurance companies, and sovereign wealth funds. Buy-side firms are the primary customers of investment banks and rely on their research, execution capabilities, and deal origination.

## Central Banks and Regulators

Central banks like the Federal Reserve, European Central Bank, and Bank of England set monetary policy, manage interest rates, and act as lenders of last resort. Regulators such as the SEC (Securities and Exchange Commission), FCA (Financial Conduct Authority), and BaFin oversee market integrity, enforce disclosure requirements, and protect investors. Post-2008 regulations like Dodd-Frank and Basel III have significantly increased capital requirements and compliance obligations for banks.

## Corporations (Issuers)

Companies access financial markets to raise capital for growth, acquisitions, and operations. They issue equity (stocks) and debt (bonds, loans) and are the primary clients of investment banking advisory services. CFOs and treasury departments work closely with investment banks to optimize their capital structure, manage risk, and execute strategic transactions.

## Retail Investors and Market Infrastructure

Retail investors participate through brokerage accounts, retirement plans, and increasingly through commission-free platforms. Exchanges (NYSE, NASDAQ), clearinghouses (DTCC, LCH), and custodian banks provide the infrastructure that makes trading possible. Rating agencies (Moody's, S&P, Fitch) assess creditworthiness and play a pivotal role in debt markets.`,
    videos: [
      { title: "Investment Banking Explained in 5 Minutes", url: "https://www.youtube.com/watch?v=lKm4YPKR5SY", duration: "5:23" },
      { title: "Buy Side vs Sell Side Explained", url: "https://www.youtube.com/watch?v=J3SEvTg9kxs", duration: "7:45" },
    ],
    quiz: [
      {
        question: "Which of these is a 'buy-side' institution?",
        options: ["Goldman Sachs", "A hedge fund", "The NYSE", "Moody's"],
        correct: 1,
      },
      {
        question: "What is the primary role of investment banks?",
        options: [
          "Taking retail deposits",
          "Advising on deals and underwriting securities",
          "Setting interest rates",
          "Rating corporate bonds",
        ],
        correct: 1,
      },
    ],
  },

  "cib-2-1": {
    id: "cib-2-1",
    title: "Financial Statements",
    content: `# Financial Statements

Financial statements are the primary tool for understanding a company's financial health. Every investment banking analyst must be able to read, interpret, and model the three core financial statements fluently.

## The Income Statement (P&L)

The income statement shows a company's revenues, expenses, and profitability over a period. It starts with Revenue (top line) and subtracts Cost of Goods Sold (COGS) to arrive at Gross Profit. Then it deducts operating expenses (SG&A, R&D, D&A) to get Operating Income (EBIT). After interest and taxes, you reach Net Income (bottom line). Key metrics derived from the income statement include gross margin, operating margin, EBITDA margin, and EPS (earnings per share).

## The Balance Sheet

The balance sheet is a snapshot of a company's financial position at a point in time. It follows the fundamental equation: Assets = Liabilities + Shareholders' Equity. Current assets include cash, accounts receivable, and inventory. Non-current assets include PP&E (property, plant, and equipment), goodwill, and intangible assets. On the other side, current liabilities include accounts payable and short-term debt, while non-current liabilities include long-term debt and deferred taxes.

## The Cash Flow Statement

The cash flow statement reconciles net income to actual cash generated. It has three sections: Operating Activities (cash from core business — starts with net income and adjusts for non-cash items like depreciation), Investing Activities (capital expenditures, acquisitions, asset sales), and Financing Activities (debt issuance/repayment, equity issuance, dividends, share buybacks). Free Cash Flow (FCF) — typically calculated as operating cash flow minus capital expenditures — is one of the most important metrics in valuation.

## How the Three Statements Link

The three statements are interconnected. Net income from the income statement flows into retained earnings on the balance sheet and is the starting point for the cash flow statement. Capital expenditures on the cash flow statement increase PP&E on the balance sheet. Debt issuance increases both cash (balance sheet asset) and long-term debt (balance sheet liability). Understanding these linkages is fundamental to building financial models.

## Why This Matters in Banking

In investment banking, analysts build models that project all three statements forward. Whether you are valuing a company via DCF, assessing a target in an M&A transaction, or structuring a leveraged buyout, you need to understand how revenue growth, margin expansion, working capital changes, and capital structure decisions flow through the financial statements.`,
    videos: [
      { title: "Three Financial Statements Explained", url: "https://www.youtube.com/watch?v=PjFgJSmOxQc", duration: "15:20" },
      { title: "How the 3 Financial Statements Link Together", url: "https://www.youtube.com/watch?v=Kfx0MMsHaYQ", duration: "11:05" },
      { title: "Reading Financial Statements - Warren Buffett", url: "https://www.youtube.com/watch?v=deIRKc0I1jM", duration: "18:30" },
    ],
    codeExamples: [
      {
        language: "formula",
        code: `Income Statement Flow:
Revenue
- COGS
= Gross Profit
- SG&A, R&D
= EBITDA
- Depreciation & Amortization
= EBIT (Operating Income)
- Interest Expense
= EBT (Earnings Before Tax)
- Taxes
= Net Income`,
      },
      {
        language: "formula",
        code: `Free Cash Flow (FCF):
Operating Cash Flow
- Capital Expenditures (CapEx)
= Free Cash Flow

OR

Net Income
+ Depreciation & Amortization
- Changes in Working Capital
- Capital Expenditures
= Free Cash Flow`,
      },
    ],
    quiz: [
      {
        question: "What is the fundamental accounting equation?",
        options: [
          "Revenue - Expenses = Profit",
          "Assets = Liabilities + Equity",
          "Cash In - Cash Out = Net Cash",
          "EBIT - Taxes = Net Income",
        ],
        correct: 1,
      },
      {
        question: "Which section of the cash flow statement includes capital expenditures?",
        options: [
          "Operating Activities",
          "Investing Activities",
          "Financing Activities",
          "None — CapEx is only on the income statement",
        ],
        correct: 1,
      },
      {
        question: "How is Free Cash Flow typically calculated?",
        options: [
          "Net Income minus Dividends",
          "Revenue minus all expenses",
          "Operating Cash Flow minus CapEx",
          "EBITDA minus Taxes",
        ],
        correct: 2,
      },
    ],
  },

  "cib-2-2": {
    id: "cib-2-2",
    title: "Key Ratios",
    content: `# Key Financial Ratios

Financial ratios allow analysts to quickly assess a company's profitability, liquidity, leverage, and efficiency. In investment banking, ratios are used for benchmarking companies against peers, evaluating creditworthiness, and identifying potential investment opportunities.

## Profitability Ratios

Profitability ratios measure how effectively a company generates profit. Gross Margin (Gross Profit / Revenue) shows the markup on cost of goods. Operating Margin (EBIT / Revenue) reflects operational efficiency. Net Margin (Net Income / Revenue) captures overall profitability after all costs. EBITDA Margin is widely used in banking because it removes the effects of capital structure, tax jurisdiction, and accounting policies, making it ideal for comparing companies. Return on Equity (ROE = Net Income / Shareholders' Equity) and Return on Assets (ROA = Net Income / Total Assets) measure how well management uses capital.

## Leverage Ratios

Leverage ratios assess a company's debt burden and ability to service obligations. Debt-to-Equity (Total Debt / Total Equity) shows the balance between debt and equity financing. Net Debt / EBITDA is the most commonly used leverage metric in investment banking — a ratio of 3.0x means it would take three years of EBITDA to repay all net debt. Interest Coverage (EBIT / Interest Expense) measures the ability to pay interest obligations. In leveraged finance, these ratios determine loan covenants and credit ratings.

## Liquidity Ratios

Liquidity ratios measure short-term solvency. The Current Ratio (Current Assets / Current Liabilities) should generally be above 1.0. The Quick Ratio excludes inventory for a more conservative view. The Cash Ratio (Cash / Current Liabilities) is the strictest measure. Lenders and credit analysts pay close attention to these metrics when assessing default risk.

## Efficiency / Activity Ratios

Efficiency ratios measure how well a company manages its assets. Days Sales Outstanding (DSO = Receivables / Revenue x 365) shows how quickly a company collects payments. Days Inventory Outstanding (DIO = Inventory / COGS x 365) measures inventory turnover. Days Payable Outstanding (DPO = Payables / COGS x 365) shows how long a company takes to pay suppliers. The Cash Conversion Cycle (CCC = DSO + DIO - DPO) captures the entire working capital cycle and is critical for understanding cash flow dynamics.

## Valuation Multiples

While technically not accounting ratios, valuation multiples are essential in banking. Enterprise Value / EBITDA (EV/EBITDA) is the most widely used multiple for M&A and comparable analysis. Price / Earnings (P/E) is common for equity investors. Price / Book (P/B) is important for financial institutions. These multiples allow rapid comparison across companies and are the foundation of comparable company analysis.`,
    videos: [
      { title: "Financial Ratios Explained", url: "https://www.youtube.com/watch?v=aSP5JFgrfao", duration: "14:22" },
      { title: "Key Ratios for Stock Analysis", url: "https://www.youtube.com/watch?v=ARrNYyJEnFI", duration: "11:48" },
    ],
    codeExamples: [
      {
        language: "excel",
        code: `=== Key Ratio Formulas in Excel ===

Gross Margin:       =Gross_Profit / Revenue
EBITDA Margin:      =EBITDA / Revenue
Net Margin:         =Net_Income / Revenue
ROE:                =Net_Income / Shareholders_Equity
ROA:                =Net_Income / Total_Assets

Net Debt / EBITDA:  =(Total_Debt - Cash) / EBITDA
Interest Coverage:  =EBIT / Interest_Expense
Current Ratio:      =Current_Assets / Current_Liabilities

DSO:                =(Accounts_Receivable / Revenue) * 365
DIO:                =(Inventory / COGS) * 365
DPO:                =(Accounts_Payable / COGS) * 365
CCC:                =DSO + DIO - DPO`,
      },
    ],
    quiz: [
      {
        question: "What is the most commonly used leverage metric in investment banking?",
        options: ["Debt-to-Equity", "Net Debt / EBITDA", "Current Ratio", "Interest Coverage"],
        correct: 1,
      },
      {
        question: "What does the Cash Conversion Cycle measure?",
        options: [
          "How quickly a company converts revenue to profit",
          "The time it takes to convert inventory investments into cash from sales",
          "How fast a company can raise debt",
          "The ratio of cash to total assets",
        ],
        correct: 1,
      },
    ],
  },

  "cib-3-1": {
    id: "cib-3-1",
    title: "TVM Concepts",
    content: `# Time Value of Money

The Time Value of Money (TVM) is the most fundamental concept in all of finance. It states that a dollar today is worth more than a dollar in the future because of its potential to earn returns. Every valuation technique — DCF, LBO modeling, bond pricing — is built upon this principle.

## Present Value and Future Value

Future Value (FV) calculates what an investment today will be worth at a future date given a rate of return: FV = PV x (1 + r)^n. Present Value (PV) is the reverse — it tells you what a future cash flow is worth today: PV = FV / (1 + r)^n. The process of converting future values to present values is called discounting, and the rate used is called the discount rate. In corporate finance, the discount rate typically reflects the riskiness of the cash flows being valued.

## Compounding and Discounting

Compounding is the process by which an investment grows exponentially over time because returns are earned on both the original principal and accumulated interest. The frequency of compounding matters — annual, semi-annual, quarterly, monthly, or continuous compounding all produce different results. The formula for continuous compounding is FV = PV x e^(rt). Discounting is the inverse of compounding: it reduces future cash flows to their present-day equivalent.

## Annuities and Perpetuities

An annuity is a series of equal cash flows occurring at regular intervals. The present value of an annuity is PV = C x [(1 - (1 + r)^-n) / r], where C is the periodic cash flow. A perpetuity is an annuity that continues forever, with PV = C / r. A growing perpetuity (PV = C / (r - g)) is particularly important in finance because it is used to calculate the terminal value in DCF models — representing the value of a company's cash flows beyond the explicit forecast period.

## Net Present Value (NPV) and IRR

Net Present Value is the sum of all discounted cash flows minus the initial investment. A positive NPV means the project creates value. The Internal Rate of Return (IRR) is the discount rate that makes the NPV equal to zero — it represents the annualized return an investment generates. In investment banking, IRR is the primary metric for evaluating LBO returns. Both NPV and IRR are essential tools for capital budgeting and investment decision-making.

## Application in Banking

TVM concepts are used constantly in banking. Bond traders price bonds by discounting future coupon payments and principal repayment. Investment bankers build DCF models that discount projected free cash flows. Leveraged buyout models calculate IRR to determine whether a deal meets return thresholds. Loan officers use TVM to structure amortization schedules. Mastering these concepts is non-negotiable for a career in finance.`,
    videos: [
      { title: "Time Value of Money Explained", url: "https://www.youtube.com/watch?v=KGnCXnMUNbA", duration: "13:15" },
      { title: "NPV and IRR Explained Simply", url: "https://www.youtube.com/watch?v=N-lN5bMYPhE", duration: "9:50" },
      { title: "Present Value and Discounting", url: "https://www.youtube.com/watch?v=b6FnKmdUS3I", duration: "16:20" },
    ],
    codeExamples: [
      {
        language: "excel",
        code: `=== TVM Formulas in Excel ===

Future Value:             =PV * (1 + rate)^nper
                          =FV(rate, nper, pmt, pv)

Present Value:            =FV / (1 + rate)^nper
                          =PV(rate, nper, pmt, fv)

NPV:                      =NPV(rate, cashflow1, cashflow2, ...) + initial_investment

IRR:                      =IRR(values_range)

PV of Annuity:            =PV(rate, nper, -payment, 0)
PV of Perpetuity:         =Annual_CashFlow / Discount_Rate
PV of Growing Perpetuity: =CashFlow / (Discount_Rate - Growth_Rate)`,
      },
    ],
    quiz: [
      {
        question: "What does a positive NPV indicate?",
        options: [
          "The project will lose money",
          "The project creates value and should be accepted",
          "The discount rate is too high",
          "The cash flows are growing",
        ],
        correct: 1,
      },
      {
        question: "What is the formula for the present value of a perpetuity?",
        options: ["PV = C x (1 + r)^n", "PV = C / r", "PV = C x r", "PV = FV / (1 + r)^n"],
        correct: 1,
      },
      {
        question: "What is IRR?",
        options: [
          "The maximum interest rate on a loan",
          "The discount rate that makes NPV equal to zero",
          "The inflation-adjusted return rate",
          "The interest rate set by central banks",
        ],
        correct: 1,
      },
    ],
  },

  "cib-4-1": {
    id: "cib-4-1",
    title: "Bonds & Yields",
    content: `# Fixed Income: Bonds and Yields

Fixed income securities — primarily bonds — form the largest segment of global capital markets. Understanding bonds, yields, and interest rate dynamics is essential for anyone in corporate and investment banking.

## Bond Basics

A bond is a debt instrument where the issuer borrows money from investors and promises to pay periodic interest (coupons) and return the principal (face value or par value) at maturity. Bonds are issued by governments (sovereign bonds), corporations (corporate bonds), and municipalities (municipal bonds). Key bond characteristics include face value (typically $1,000), coupon rate (annual interest as a percentage of face value), maturity date, and credit rating. When a bond trades at its face value, it is said to be trading "at par." Above face value is "at a premium," and below is "at a discount."

## Yield Concepts

The coupon rate is the stated interest rate, but the yield tells you the actual return. Current yield = Annual Coupon / Current Market Price. Yield to Maturity (YTM) is the total annualized return if the bond is held until maturity, accounting for coupon payments, capital gain/loss, and reinvestment. YTM is the most comprehensive yield measure and is the standard for comparing bonds. Yield to Call (YTC) applies to callable bonds and assumes the issuer redeems the bond at the earliest call date.

## The Yield Curve

The yield curve plots yields across different maturities for bonds of similar credit quality (typically government bonds). A normal yield curve slopes upward — longer maturities have higher yields to compensate for greater uncertainty. A flat yield curve suggests economic uncertainty, while an inverted yield curve (short-term rates exceed long-term rates) has historically been a reliable predictor of recession. Central bank policy, inflation expectations, and supply/demand dynamics all influence the shape of the yield curve.

## Bond Pricing and Interest Rate Risk

Bond prices and interest rates move inversely. When rates rise, existing bond prices fall, and vice versa. Duration measures a bond's sensitivity to interest rate changes — a duration of 5 means a 1% rate increase causes approximately a 5% price decline. Modified duration provides a more precise sensitivity measure. Convexity captures the curvature in the price-yield relationship. Investment bankers and traders use these metrics to manage portfolio risk and structure transactions.

## Credit Risk and Ratings

Credit risk is the risk that the issuer fails to make payments. Credit rating agencies (Moody's, S&P, Fitch) assign ratings from AAA/Aaa (highest quality) to D (default). Investment grade bonds (BBB-/Baa3 and above) have lower yields but greater safety. High yield (or "junk") bonds (below BBB-/Baa3) offer higher yields to compensate for higher default risk. The difference between a bond's yield and a risk-free benchmark (like Treasuries) is called the credit spread, which reflects the market's perception of default risk.`,
    videos: [
      { title: "Bond Investing for Beginners", url: "https://www.youtube.com/watch?v=nUbBn8CpEYM", duration: "14:55" },
      { title: "The Yield Curve Explained", url: "https://www.youtube.com/watch?v=b5RMOMq5CTo", duration: "8:30" },
      { title: "Bond Duration Explained", url: "https://www.youtube.com/watch?v=ubHIkIDdt3g", duration: "10:45" },
    ],
    codeExamples: [
      {
        language: "excel",
        code: `=== Bond Formulas in Excel ===

Bond Price:        =PRICE(settlement, maturity, coupon_rate, yield, redemption, frequency)
Yield to Maturity: =YIELD(settlement, maturity, coupon_rate, price, redemption, frequency)
Current Yield:     =Annual_Coupon / Current_Price
Duration:          =DURATION(settlement, maturity, coupon_rate, yield, frequency)
Modified Duration: =MDURATION(settlement, maturity, coupon_rate, yield, frequency)

Example - Bond Price Calculation:
=PRICE("2024-01-01", "2034-01-01", 0.05, 0.06, 100, 2)
Result: ~92.56 (bond trades at a discount because yield > coupon)`,
      },
    ],
    quiz: [
      {
        question: "What happens to bond prices when interest rates rise?",
        options: [
          "Bond prices rise",
          "Bond prices fall",
          "Bond prices stay the same",
          "It depends on the coupon rate",
        ],
        correct: 1,
      },
      {
        question: "What does an inverted yield curve typically signal?",
        options: [
          "Strong economic growth",
          "Rising inflation",
          "A potential recession",
          "Increasing corporate profits",
        ],
        correct: 2,
      },
    ],
  },

  "cib-5-1": {
    id: "cib-5-1",
    title: "Banking Basics",
    content: `# Commercial Banking

Commercial banking forms the foundation of the financial system, serving as the primary intermediary between depositors and borrowers. Understanding how commercial banks operate is essential context for anyone entering corporate and investment banking.

## Core Functions of Commercial Banks

Commercial banks serve three primary functions: accepting deposits, making loans, and facilitating payments. Banks take deposits from individuals and businesses (current accounts, savings accounts, time deposits) and lend that money out at higher interest rates. The difference between lending rates and deposit rates — the net interest margin (NIM) — is the primary source of revenue for commercial banks. Banks also generate fee income from services like cash management, trade finance, and foreign exchange transactions.

## The Lending Process

When a bank makes a loan, it goes through a rigorous credit analysis process. This includes evaluating the borrower's creditworthiness (the 5 C's of Credit: Character, Capacity, Capital, Collateral, and Conditions), performing financial analysis, stress testing repayment ability, and structuring appropriate loan terms. Loans can be secured (backed by collateral) or unsecured, and can have fixed or variable interest rates. The bank's credit committee reviews and approves loans above certain thresholds.

## Credit Analysis

Credit analysis is the systematic evaluation of a borrower's ability and willingness to repay debt. Analysts examine historical financial statements, project future cash flows, assess industry and competitive dynamics, and evaluate management quality. Key credit metrics include the Debt Service Coverage Ratio (DSCR = Net Operating Income / Total Debt Service), leverage ratios, and liquidity measures. Banks also use internal rating models that assign a credit grade to each borrower, which determines pricing and provisioning requirements.

## Banking Regulation and Capital Requirements

Banks are heavily regulated to protect depositors and maintain financial stability. Basel III (and its successor Basel IV) sets minimum capital requirements, including Common Equity Tier 1 (CET1) ratios, leverage ratios, and liquidity requirements (LCR and NSFR). Banks must maintain adequate capital buffers to absorb losses. Regulations also require banks to hold provisions (loan loss reserves) against expected credit losses, following accounting standards like IFRS 9 and CECL.

## Relationship Management

In corporate banking, relationship managers (RMs) serve as the primary point of contact for business clients. They coordinate across product teams (lending, treasury, trade finance, capital markets) to deliver comprehensive banking solutions. The goal is to deepen the relationship by cross-selling products while managing the overall risk exposure to each client. Strong relationships with corporate clients often serve as a gateway to investment banking mandates.`,
    videos: [
      { title: "How Banks Work and Make Money", url: "https://www.youtube.com/watch?v=iYRiYBay2Uc", duration: "11:30" },
      { title: "Credit Analysis Process Explained", url: "https://www.youtube.com/watch?v=O4aPOL9cYKQ", duration: "13:15" },
    ],
    codeExamples: [
      {
        language: "formula",
        code: `=== Key Credit Metrics ===

Net Interest Margin (NIM) = (Interest Income - Interest Expense) / Average Earning Assets

Debt Service Coverage Ratio (DSCR) = Net Operating Income / Total Debt Service
  - DSCR > 1.0x means the borrower generates enough income to cover debt payments
  - Banks typically require DSCR > 1.25x

Loan-to-Value (LTV) = Loan Amount / Collateral Value
  - Lower LTV = lower risk for the bank

Capital Adequacy Ratio (CAR) = (Tier 1 Capital + Tier 2 Capital) / Risk-Weighted Assets
  - Basel III minimum: 8% total, 4.5% CET1`,
      },
    ],
    quiz: [
      {
        question: "What is Net Interest Margin?",
        options: [
          "Total revenue minus expenses",
          "The difference between lending rates and deposit rates",
          "The bank's profit margin on trading",
          "Interest earned on government bonds",
        ],
        correct: 1,
      },
      {
        question: "What does DSCR measure?",
        options: [
          "A bank's capital adequacy",
          "The borrower's ability to service debt from operating income",
          "The interest rate spread on loans",
          "The collateral coverage ratio",
        ],
        correct: 1,
      },
    ],
  },

  "cib-6-1": {
    id: "cib-6-1",
    title: "Corporate Loans",
    content: `# Corporate Lending

Corporate lending is one of the most important products in commercial and investment banking. Understanding loan structures, credit facilities, and syndication is essential for banking professionals.

## Types of Corporate Loans

Corporate loans come in several forms. Term Loans provide a lump sum that is repaid over a set period with scheduled amortization (Term Loan A) or a bullet repayment at maturity (Term Loan B). Revolving Credit Facilities (revolvers) work like a corporate credit card — the borrower can draw and repay up to a committed limit. Bridge Loans provide short-term financing, typically to bridge the gap until permanent financing is arranged. Working Capital Facilities fund day-to-day operations, while Acquisition Facilities specifically finance M&A transactions.

## Loan Structuring

Structuring a corporate loan involves defining the key terms: principal amount, interest rate (fixed or floating, typically benchmarked to SOFR or EURIBOR plus a spread), maturity, amortization schedule, collateral (if secured), and covenants. Financial covenants are conditions the borrower must maintain — such as maximum leverage (Net Debt / EBITDA), minimum interest coverage (EBITDA / Interest), and minimum liquidity levels. Breach of covenants can trigger an event of default.

## Syndicated Lending

Large corporate loans are often too big for a single bank to hold on its balance sheet. In syndication, a lead arranger (the mandated lead arranger, or MLA) structures the loan and invites other banks to participate. The lead arranger earns arrangement fees, while participating banks earn commitment fees and interest income. The loan is documented under a common agreement (often based on LMA or LSTA standards). Syndicated loans are a key revenue source for investment banks and often serve as a gateway to other mandates.

## Credit Facilities and Covenants

A credit facility agreement typically includes affirmative covenants (things the borrower must do — provide financial statements, maintain insurance), negative covenants (things the borrower must not do — incur additional debt beyond limits, make restricted payments), financial covenants (ratios to maintain), and events of default (conditions that allow the lender to accelerate repayment). Covenant-lite (cov-lite) loans, which have fewer financial maintenance covenants, have become increasingly common in the leveraged loan market.

## Loan Pricing

The pricing of a corporate loan reflects the borrower's credit risk, the loan's structural features, and market conditions. Pricing components include the interest rate margin (spread over the benchmark rate), commitment fees (charged on undrawn portions of revolvers), upfront/arrangement fees, and utilization fees. Credit ratings, leverage levels, and industry dynamics all influence the spread. Banks also consider the broader relationship profitability — a bank may price a loan aggressively if it expects to win additional mandates from the client.`,
    videos: [
      { title: "Syndicated Loans Explained", url: "https://www.youtube.com/watch?v=D5enIdXdEAo", duration: "9:40" },
      { title: "Leveraged Loans and CLOs", url: "https://www.youtube.com/watch?v=zJHQNwbchh8", duration: "12:55" },
    ],
    codeExamples: [
      {
        language: "excel",
        code: `=== Loan Pricing Example ===

Loan Amount:          $500,000,000
Benchmark Rate:       SOFR = 5.25%
Credit Spread:        +250 bps (2.50%)
All-in Interest Rate: =5.25% + 2.50% = 7.75%
Annual Interest Cost: =500000000 * 0.0775 = $38,750,000

Commitment Fee on Undrawn Revolver:
Revolver Size:        $200,000,000
Drawn Amount:         $50,000,000
Undrawn Amount:       =200000000 - 50000000 = $150,000,000
Commitment Fee Rate:  0.50%
Annual Fee:           =150000000 * 0.005 = $750,000`,
      },
    ],
    quiz: [
      {
        question: "What is a revolving credit facility?",
        options: [
          "A loan that rotates between banks",
          "A facility where the borrower can draw and repay up to a committed limit",
          "A short-term bridge loan",
          "A loan with a rotating interest rate",
        ],
        correct: 1,
      },
      {
        question: "What happens when a borrower breaches a financial covenant?",
        options: [
          "Nothing — covenants are advisory",
          "The interest rate automatically doubles",
          "It can trigger an event of default",
          "The loan is automatically forgiven",
        ],
        correct: 2,
      },
    ],
  },

  "cib-7-1": {
    id: "cib-7-1",
    title: "Trade Finance",
    content: `# Trade Finance

Trade finance encompasses the financial instruments and products that facilitate international trade. It bridges the gap between exporters who want payment assurance and importers who want goods assurance, making global commerce possible.

## Letters of Credit (LCs)

A Letter of Credit is a guarantee issued by a bank on behalf of the importer (applicant), promising to pay the exporter (beneficiary) upon presentation of compliant documents. The issuing bank essentially substitutes its own creditworthiness for that of the importer. Types include Documentary LCs (require shipping documents), Standby LCs (serve as backup guarantees), Confirmed LCs (a second bank adds its guarantee), and Irrevocable LCs (cannot be modified without all parties' consent). LCs are governed by UCP 600 rules published by the International Chamber of Commerce (ICC).

## Bank Guarantees

Bank guarantees protect parties in trade transactions against non-performance. Common types include Performance Guarantees (ensuring a contractor completes work as agreed), Advance Payment Guarantees (protecting prepayments), Bid Bonds (ensuring winners honor their bids), and Retention Money Guarantees. Unlike LCs, guarantees are typically "pay on first demand" — the bank pays when the beneficiary makes a compliant demand, regardless of disputes between the underlying parties.

## Documentary Collections

Documentary collections are a simpler and cheaper alternative to LCs. The exporter's bank sends shipping documents to the importer's bank with instructions to release them only upon payment (Documents against Payment, or D/P) or upon acceptance of a draft (Documents against Acceptance, or D/A). Unlike LCs, the banks do not guarantee payment — they only act as intermediaries. Documentary collections are governed by URC 522.

## Supply Chain Finance

Modern trade finance has evolved to include supply chain finance solutions. Reverse factoring (or supplier finance) allows suppliers to receive early payment on their invoices, funded by a bank based on the buyer's creditworthiness (and therefore at a lower rate). Factoring involves selling receivables to a bank or factor at a discount for immediate cash. These products help optimize working capital for both buyers and suppliers throughout the supply chain.

## Trade Finance Risk and Compliance

Trade finance carries unique risks including country risk (political instability, sanctions), documentary risk (discrepancies in documents), fraud risk, and foreign exchange risk. Banks must also comply with strict Anti-Money Laundering (AML) and Know Your Customer (KYC) requirements. Sanctions screening is critical — banks can face enormous fines for processing transactions involving sanctioned entities or countries.`,
    videos: [
      { title: "Letters of Credit Explained", url: "https://www.youtube.com/watch?v=8tqkFPIrog0", duration: "10:20" },
      { title: "Trade Finance Basics", url: "https://www.youtube.com/watch?v=yNWWFkOIJtU", duration: "8:55" },
    ],
    quiz: [
      {
        question: "What does a Letter of Credit guarantee?",
        options: [
          "That the goods will be of good quality",
          "Payment to the exporter upon presentation of compliant documents",
          "That the shipment will arrive on time",
          "That exchange rates will remain stable",
        ],
        correct: 1,
      },
      {
        question: "What is the difference between LCs and documentary collections?",
        options: [
          "LCs are cheaper than documentary collections",
          "Documentary collections provide a bank guarantee; LCs do not",
          "LCs provide a bank guarantee; documentary collections do not",
          "There is no difference — they are the same product",
        ],
        correct: 2,
      },
    ],
  },

  "cib-8-1": {
    id: "cib-8-1",
    title: "FX & Treasury",
    content: `# Treasury and Foreign Exchange

Treasury management and foreign exchange operations are critical functions within corporate and investment banking. They involve managing liquidity, funding, and currency exposures for both the bank itself and its corporate clients.

## Foreign Exchange Fundamentals

The FX market is a decentralized over-the-counter (OTC) market where currencies are traded 24 hours a day. Currency pairs are quoted as base/quote (e.g., EUR/USD = 1.10 means 1 euro costs 1.10 US dollars). The bid-ask spread represents the dealer's profit. Spot transactions settle in T+2 business days, while forward transactions settle at a future date at an agreed rate. The forward rate differs from the spot rate due to interest rate differentials between the two currencies — this relationship is described by Covered Interest Rate Parity.

## FX Products

Banks offer various FX products to clients. Spot transactions are the simplest — exchanging currencies at the current market rate. FX Forwards lock in an exchange rate for a future date, allowing companies to hedge currency exposure on future receipts or payments. FX Swaps combine a spot and a forward transaction — useful for managing short-term funding in different currencies. Currency Options give the holder the right (but not obligation) to exchange currencies at a predetermined rate, providing flexibility while protecting against adverse movements. Cross-Currency Swaps exchange principal and interest in different currencies over the life of the swap.

## Corporate Treasury Management

Corporate treasury is responsible for managing a company's cash, liquidity, funding, and financial risk. Key functions include cash management (forecasting cash flows, optimizing cash positions across subsidiaries), funding and debt management (negotiating credit facilities, managing maturity profiles), risk management (hedging FX, interest rate, and commodity exposures), and bank relationship management. Treasury operations are often centralized in a Treasury Center or In-House Bank to achieve economies of scale.

## Interest Rate Risk Management

Interest rate risk arises from mismatches between the repricing dates of assets and liabilities. Banks and corporations use Interest Rate Swaps (exchanging fixed-rate payments for floating-rate payments, or vice versa) to manage this risk. The notional amount of outstanding interest rate swaps exceeds $400 trillion globally. Other products include interest rate caps (maximum rate), floors (minimum rate), and collars (combination of cap and floor). The benchmark rates (SOFR, EURIBOR, SONIA) are critical reference points for pricing these instruments.

## Liquidity Management

Effective liquidity management ensures an institution can meet its financial obligations as they come due. This involves maintaining adequate cash reserves, managing the maturity profile of assets and liabilities, establishing contingency funding plans, and meeting regulatory liquidity requirements (Liquidity Coverage Ratio and Net Stable Funding Ratio under Basel III). Money market instruments — commercial paper, certificates of deposit, repurchase agreements (repos) — are key tools for short-term liquidity management.`,
    videos: [
      { title: "Foreign Exchange Market Explained", url: "https://www.youtube.com/watch?v=2f7CU03CjRg", duration: "11:40" },
      { title: "Interest Rate Swaps Explained", url: "https://www.youtube.com/watch?v=IpFk9Fa-LKA", duration: "9:25" },
    ],
    codeExamples: [
      {
        language: "excel",
        code: `=== FX Forward Rate Calculation ===

Spot Rate (EUR/USD):       1.1000
EUR Interest Rate (1 year): 3.50%
USD Interest Rate (1 year): 5.25%

Forward Rate = Spot x (1 + r_quote) / (1 + r_base)
Forward Rate = 1.1000 x (1 + 0.0525) / (1 + 0.0350)
Forward Rate = 1.1000 x 1.0525 / 1.0350
Forward Rate = 1.1186

The USD is at a forward discount vs EUR because USD rates are higher.`,
      },
    ],
    quiz: [
      {
        question: "What does Covered Interest Rate Parity explain?",
        options: [
          "Why some currencies are stronger than others",
          "The relationship between spot rates, forward rates, and interest rate differentials",
          "Why central banks set different interest rates",
          "The impact of inflation on currency values",
        ],
        correct: 1,
      },
      {
        question: "What is an Interest Rate Swap?",
        options: [
          "Exchanging the principal of two loans",
          "Exchanging fixed-rate payments for floating-rate payments (or vice versa)",
          "Swapping loans between two banks",
          "Converting a loan from one currency to another",
        ],
        correct: 1,
      },
    ],
  },

  "cib-9-1": {
    id: "cib-9-1",
    title: "M&A Process",
    content: `# The M&A Process

Mergers and Acquisitions (M&A) advisory is one of the most prestigious and lucrative services offered by investment banks. Understanding the end-to-end deal process is critical for anyone aspiring to work in investment banking.

## Overview and Motivations

Companies pursue M&A for strategic reasons: achieving growth (entering new markets, acquiring new products/technologies), gaining synergies (cost savings from combining operations, revenue synergies from cross-selling), increasing market share, diversification, or acquiring undervalued assets. The global M&A market typically sees $3-5 trillion in annual deal volume. Investment banks advise both buyers (buy-side advisory) and sellers (sell-side advisory) throughout the transaction process.

## Sell-Side M&A Process

A sell-side process is initiated when a company or its shareholders decide to sell. The investment bank runs a structured auction process: First, the bank prepares marketing materials — a teaser (anonymous one-page summary) and a Confidential Information Memorandum (CIM, a detailed 50-100 page document about the company). Then it identifies and contacts potential buyers, who sign Non-Disclosure Agreements (NDAs) before receiving the CIM. Interested buyers submit Indicative Offers (non-binding). Selected buyers enter the data room for due diligence and submit Final Binding Offers. The seller selects the winning bid, negotiates the definitive agreement (SPA — Share Purchase Agreement), and closes the transaction.

## Buy-Side M&A Process

On the buy side, the investment bank helps the acquirer identify targets, perform valuation analysis, structure the offer, conduct due diligence, arrange financing, and negotiate terms. The bank also provides a Fairness Opinion — an independent assessment of whether the price is fair from a financial perspective. Buy-side engagements can be proactive (the buyer initiates) or reactive (responding to a sell-side auction).

## Due Diligence

Due diligence is the comprehensive investigation of the target company before completing the acquisition. It covers financial due diligence (auditing financial statements, quality of earnings analysis), commercial due diligence (market position, competitive dynamics), legal due diligence (contracts, litigation, regulatory compliance), tax due diligence, and operational due diligence. The data room — a secure virtual platform — contains thousands of documents for buyers to review.

## Regulatory and Closing

M&A transactions often require regulatory approvals, including antitrust review (to ensure the merger does not create monopolistic market concentration), sector-specific regulatory approvals (banking, telecom, defense), and shareholder votes. Between signing the definitive agreement and closing, there is typically a period of several months for regulatory clearance. Material Adverse Change (MAC) clauses protect the buyer if the target's condition deteriorates significantly before closing.`,
    videos: [
      { title: "M&A Process Overview", url: "https://www.youtube.com/watch?v=jb5Eaoye_0Q", duration: "15:30" },
      { title: "How M&A Deals Work", url: "https://www.youtube.com/watch?v=UTzVGYQ6oTs", duration: "12:10" },
      { title: "Investment Banking M&A Explained", url: "https://www.youtube.com/watch?v=VLJbfwWjctA", duration: "10:45" },
    ],
    quiz: [
      {
        question: "What is a CIM in the context of M&A?",
        options: [
          "Corporate Investment Manual",
          "Confidential Information Memorandum — a detailed document about the company for sale",
          "Chief Investment Manager",
          "Credit and Investment Monitoring report",
        ],
        correct: 1,
      },
      {
        question: "What is a Fairness Opinion?",
        options: [
          "A legal ruling that a deal is fair",
          "A regulatory approval document",
          "An independent assessment by a bank that the price is fair from a financial perspective",
          "A shareholder vote result",
        ],
        correct: 2,
      },
    ],
  },

  "cib-9-2": {
    id: "cib-9-2",
    title: "Deal Types",
    content: `# M&A Deal Types

Not all M&A transactions are the same. Understanding the different deal structures, motivations, and considerations is essential for investment banking professionals.

## Mergers vs. Acquisitions

While often used interchangeably, mergers and acquisitions are technically different. A merger is the combination of two companies into one entity — often structured as a "merger of equals" (though one company usually dominates). An acquisition occurs when one company (the acquirer) purchases another (the target). Acquisitions can be friendly (the target's board recommends the deal) or hostile (the acquirer goes directly to shareholders against the board's wishes, through a tender offer or proxy fight).

## Horizontal, Vertical, and Conglomerate M&A

Horizontal mergers combine companies in the same industry at the same stage of the value chain (e.g., two pharmaceutical companies merging). These deals typically focus on cost synergies through eliminating redundancies and achieving economies of scale. Vertical mergers combine companies at different stages of the value chain (e.g., a manufacturer acquiring a supplier), seeking to improve supply chain control and capture margins. Conglomerate mergers combine companies in unrelated industries for diversification benefits.

## Payment Structures

Deals can be structured in various ways. All-Cash deals provide certainty of value to the seller but require the buyer to have cash or arrange financing. All-Stock deals issue new shares of the acquirer to the target's shareholders — the final value depends on the acquirer's stock price at closing. Mixed consideration combines cash and stock. Earn-outs tie part of the purchase price to the target's future performance, bridging valuation gaps between buyer and seller. The tax implications differ significantly across structures.

## Leveraged Buyouts (LBOs)

An LBO is an acquisition funded primarily with debt (typically 60-80% of the purchase price). Private equity firms are the primary sponsors of LBOs. The target company's assets and cash flows serve as collateral for the debt. The PE firm contributes equity (20-40%), uses the target's free cash flow to repay debt over 3-7 years, and aims to exit at a higher valuation through an IPO, secondary sale, or strategic sale. LBOs are one of the most important deal types in investment banking.

## Other Deal Structures

Divestitures occur when a company sells a division or subsidiary, often to focus on core operations. Spin-offs create a new independent company by distributing shares to existing shareholders. Carve-outs are partial IPOs of a subsidiary. Joint ventures create a new entity owned by two or more companies to pursue a specific opportunity. Management buyouts (MBOs) involve the existing management team acquiring the company, often backed by a PE firm. Each structure has distinct financial, tax, legal, and strategic implications.`,
    videos: [
      { title: "Types of Mergers and Acquisitions", url: "https://www.youtube.com/watch?v=rPmjwXGwB2o", duration: "8:30" },
      { title: "Leveraged Buyouts Explained", url: "https://www.youtube.com/watch?v=MqP3Aq0vNGM", duration: "11:20" },
    ],
    quiz: [
      {
        question: "What distinguishes a hostile acquisition from a friendly one?",
        options: [
          "The price paid is higher in hostile deals",
          "The acquirer goes directly to shareholders without the board's recommendation",
          "Hostile deals always involve cash payment",
          "Friendly deals do not require regulatory approval",
        ],
        correct: 1,
      },
      {
        question: "In a typical LBO, what percentage of the purchase price is funded by debt?",
        options: ["10-20%", "30-40%", "50-60%", "60-80%"],
        correct: 3,
      },
      {
        question: "What is an earn-out?",
        options: [
          "The total return on an investment",
          "A portion of the purchase price tied to the target's future performance",
          "The premium paid above market price",
          "The tax benefit of an acquisition",
        ],
        correct: 1,
      },
    ],
  },

  "cib-10-1": {
    id: "cib-10-1",
    title: "ECM",
    content: `# Equity Capital Markets (ECM)

Equity Capital Markets is the division of an investment bank responsible for helping companies raise capital by issuing equity securities. ECM sits at the intersection of investment banking and sales & trading.

## Initial Public Offerings (IPOs)

An IPO is the process by which a private company sells shares to public investors for the first time. The investment bank (underwriter) guides the company through the entire process: selecting the exchange, preparing the registration statement (S-1 in the US), conducting due diligence, determining the offering price through a bookbuilding process, and allocating shares. The roadshow — a series of presentations to institutional investors — generates demand and helps price the offering. IPOs typically price at a discount to expected market value ("IPO pop") to ensure a successful first day of trading.

## Secondary Offerings

After the IPO, companies may raise additional equity through follow-on offerings (also called secondary offerings or seasoned equity offerings). Dilutive offerings issue new shares (increasing share count), while non-dilutive offerings sell existing shares held by insiders or early investors. Accelerated bookbuilds (ABBs) are a fast-track process where the bank markets and prices the offering within hours, minimizing market risk. Block trades involve large sales of existing shares, often at a small discount.

## Rights Issues and Private Placements

Rights issues offer existing shareholders the right to purchase additional shares at a discount, typically to raise capital while giving current investors the first opportunity to participate. PIPEs (Private Investments in Public Equity) involve selling shares to a select group of institutional investors without a public offering. Convertible securities — bonds that can be converted into equity — are another ECM product that combines features of debt and equity.

## Bookbuilding and Pricing

The bookbuilding process is how investment banks determine the optimal price for an equity offering. The bank and company set an initial price range, then institutional investors submit indications of interest (price and quantity). The bank builds an "order book," analyzes demand at different price levels, and recommends a final price that balances the company's desire for maximum proceeds with the need for a successful aftermarket performance. Overallotment options ("greenshoe") allow the bank to sell up to 15% more shares than planned if demand is strong.

## ECM Fees and Economics

Investment banks earn underwriting fees for IPOs, typically 3-7% of the total proceeds (the "gross spread"). Fees are split among the lead bookrunner(s), co-managers, and other syndicate members based on their roles and economics allocation. The league tables — rankings of investment banks by deal volume — are highly competitive, and a bank's ECM ranking significantly influences its ability to win future mandates.`,
    videos: [
      { title: "How an IPO Works", url: "https://www.youtube.com/watch?v=JjFbAoKsAGU", duration: "10:15" },
      { title: "IPO Process Step by Step", url: "https://www.youtube.com/watch?v=xBJjjPnKjas", duration: "14:30" },
    ],
    quiz: [
      {
        question: "What is the bookbuilding process?",
        options: [
          "Writing a company's financial history",
          "Collecting investor demand at various prices to determine the optimal offering price",
          "Creating the S-1 registration statement",
          "Building a list of potential acquisition targets",
        ],
        correct: 1,
      },
      {
        question: "What is a greenshoe option?",
        options: [
          "A put option for investors",
          "An overallotment option allowing the bank to sell up to 15% more shares if demand is strong",
          "A shoe company's stock option plan",
          "An option to withdraw the IPO",
        ],
        correct: 1,
      },
    ],
  },

  "cib-11-1": {
    id: "cib-11-1",
    title: "DCM",
    content: `# Debt Capital Markets (DCM)

Debt Capital Markets is the division of an investment bank responsible for helping issuers raise capital through debt instruments. DCM covers investment-grade bonds, high-yield bonds, and syndicated loans.

## Investment Grade Bond Issuance

Investment grade (IG) issuers — companies rated BBB-/Baa3 or above — access the bond market regularly to fund operations, refinance maturing debt, or finance acquisitions. The process involves mandate selection (choosing lead banks), documentation (preparing the offering circular/prospectus), credit rating process (engaging with Moody's, S&P, Fitch), investor marketing (roadshows and calls), bookbuilding (collecting orders), pricing, and settlement. IG bond spreads (the premium over government bonds) reflect the issuer's credit quality, with AAA-rated issuers paying the tightest spreads.

## High Yield Bonds

High yield (HY) bonds are issued by companies rated below BBB-/Baa3. They carry higher yields to compensate investors for greater credit risk. HY bonds are a key component of leveraged finance — they are commonly used in LBOs, recapitalizations, and by companies with elevated leverage. The HY issuance process involves more extensive marketing and diligence compared to IG bonds. Covenant packages in HY bonds are typically more restrictive, providing investors with greater protection against adverse actions by the issuer.

## Syndicated Loans vs. Bonds

Both syndicated loans and bonds are debt instruments, but they differ in important ways. Loans are typically floating rate (SOFR + spread), while bonds are usually fixed rate. Loans are generally senior secured with maintenance covenants, while bonds may be unsecured with incurrence covenants. Loans are prepayable without penalty, while bonds often have call protection. Loans trade in the secondary market among institutional investors (CLOs, credit funds), while bonds trade more broadly. In a leveraged capital structure, the ranking is typically: revolving credit facility, term loan, senior secured bonds, senior unsecured bonds, subordinated bonds.

## The Issuance Process

A typical bond issuance follows these steps: 1) The issuer mandates banks as bookrunners. 2) Banks prepare marketing materials and the preliminary offering document. 3) The issuer obtains credit ratings. 4) A roadshow presents the credit story to investors. 5) Books open with initial price guidance. 6) Orders are collected and the book is built. 7) Pricing is set based on demand (often tighter than initial guidance if demand is strong). 8) Allocation of bonds to investors. 9) Settlement (typically T+5 for new issues). 10) Bonds begin trading in the secondary market.

## Private Placements and Schuldschein

Not all debt is issued publicly. US Private Placements (USPP) are sold directly to institutional investors (primarily insurance companies) without SEC registration, offering longer maturities and more flexible documentation. The Schuldschein market (German-origin) provides an alternative for European issuers seeking private debt. Green bonds, social bonds, and sustainability-linked bonds are a rapidly growing segment where proceeds or terms are tied to environmental or social objectives.`,
    videos: [
      { title: "Bond Issuance Process Explained", url: "https://www.youtube.com/watch?v=5SkHKubveng", duration: "11:50" },
      { title: "High Yield Bonds Explained", url: "https://www.youtube.com/watch?v=ePB3CiJHQdo", duration: "13:20" },
    ],
    codeExamples: [
      {
        language: "formula",
        code: `=== Typical Leveraged Capital Structure (Priority of Claims) ===

1. Revolving Credit Facility (RCF) — Senior Secured, Floating Rate
2. Term Loan A (TLA)              — Senior Secured, Floating Rate, Amortizing
3. Term Loan B (TLB)              — Senior Secured, Floating Rate, Bullet
4. Senior Secured Notes            — Senior Secured, Fixed Rate
5. Senior Unsecured Notes          — Senior Unsecured, Fixed Rate
6. Subordinated / Mezzanine Notes  — Junior, Fixed Rate (higher coupon)
7. Preferred Equity                — Equity-like
8. Common Equity                   — Residual claim

Lower in the structure = higher risk = higher yield required`,
      },
    ],
    quiz: [
      {
        question: "What is the key difference between investment grade and high yield bonds?",
        options: [
          "IG bonds are issued by governments; HY bonds by companies",
          "IG bonds are rated BBB-/Baa3 or above; HY bonds are rated below that",
          "IG bonds have longer maturities than HY bonds",
          "HY bonds always have lower interest rates",
        ],
        correct: 1,
      },
      {
        question: "In a typical leveraged capital structure, which debt has the highest priority?",
        options: [
          "Senior unsecured bonds",
          "Subordinated notes",
          "Revolving credit facility (senior secured)",
          "Common equity",
        ],
        correct: 2,
      },
    ],
  },

  "cib-12-1": {
    id: "cib-12-1",
    title: "Pitch Books",
    content: `# Investment Banking Pitch Books

Pitch books are the primary marketing tool used by investment bankers to win mandates from clients. Creating compelling, data-driven presentations is a core skill for junior bankers.

## Types of Pitch Books

There are several types of pitch books, each with a distinct purpose. Credentials Pitches showcase the bank's experience, track record, and capabilities to win new relationships. Deal-Specific Pitches propose a specific transaction (e.g., "why you should acquire Company X" or "why now is the right time to IPO"). Market Update Pitches provide clients with current market conditions, recent transactions, and strategic observations. Management Presentations are prepared for the client company to present to potential buyers or investors during a deal process.

## Key Sections of a Pitch Book

A typical investment banking pitch book includes: an Executive Summary with key recommendations; a Situation Overview analyzing the client's current position; a Market Overview with industry trends, comparable companies, and recent transactions; Valuation Analysis (DCF, comparable company analysis, precedent transactions); Strategic Alternatives (different paths the client could pursue — sell, acquire, IPO, recapitalize); a Transaction Overview with proposed deal structure and timeline; and Bank Credentials showing relevant deal experience and league table rankings.

## Creating Effective Visuals

Investment banking presentations are highly visual and data-driven. Key visual elements include trading comparables tables ("football field" charts showing valuation ranges), organizational charts for deal teams, process timelines, market share pie charts, financial performance graphs, and transaction structure diagrams. Formatting standards are extremely precise — alignment, font sizes, colors, and page layouts follow strict internal guidelines. Banks typically use templates with proprietary color schemes and design elements.

## The Pitch Process

The pitch process begins when a company (or its existing advisor) invites banks to compete for a mandate. Banks assemble a pitch team, research the company and industry, build valuation models, and prepare the pitch book — often over several intense days. The live pitch presentation (usually 60-90 minutes) is led by senior bankers (Managing Directors) with support from Vice Presidents and Associates. Key success factors include demonstrating deep industry expertise, presenting a compelling strategic vision, showing relevant deal experience, and building personal rapport with the client.

## Junior Banker's Role

For analysts and associates, pitch book creation is a major part of the job. This involves extensive financial modeling, gathering market data from Bloomberg and Capital IQ, creating and formatting slides, conducting comparable company and precedent transaction analysis, and coordinating with senior bankers on messaging. Attention to detail is paramount — a single typo or misaligned chart can undermine the bank's credibility. The iterative review process often involves multiple rounds of revisions under tight deadlines.`,
    videos: [
      { title: "Investment Banking Pitch Books", url: "https://www.youtube.com/watch?v=rr6sF7n2XKA", duration: "12:45" },
      { title: "How to Create a Pitch Book", url: "https://www.youtube.com/watch?v=DXLb3bCbI7U", duration: "9:30" },
    ],
    quiz: [
      {
        question: "What is a 'football field' chart in investment banking?",
        options: [
          "A chart showing sports industry valuations",
          "A horizontal bar chart showing valuation ranges from different methodologies",
          "A field diagram for organizing deal teams",
          "A chart showing competitive market positions",
        ],
        correct: 1,
      },
      {
        question: "What is the primary purpose of a credentials pitch?",
        options: [
          "To propose a specific M&A transaction",
          "To showcase the bank's experience and win new client relationships",
          "To present market data to investors",
          "To prepare financial models for a deal",
        ],
        correct: 1,
      },
    ],
  },

  "cib-13-1": {
    id: "cib-13-1",
    title: "DCF Model",
    content: `# Discounted Cash Flow (DCF) Valuation

The DCF model is the most fundamental and theoretically rigorous valuation methodology in investment banking. It values a company based on the present value of its projected future free cash flows.

## DCF Framework

The basic principle of a DCF is simple: a company is worth the present value of all the cash it will generate in the future. In practice, this involves two components: (1) the present value of free cash flows during an explicit forecast period (typically 5-10 years), and (2) the present value of a terminal value that captures the value of all cash flows beyond the forecast period. The terminal value typically represents 60-80% of total enterprise value, which is why its assumptions are critically important.

## Projecting Free Cash Flows

Unlevered Free Cash Flow (UFCF) is the cash available to all capital providers (both debt and equity holders). The calculation starts with EBIT, subtracts taxes (at the marginal tax rate), adds back depreciation and amortization (non-cash charges), subtracts capital expenditures (investments in PP&E), and adjusts for changes in net working capital. Each component requires careful projection based on historical trends, management guidance, industry benchmarks, and the analyst's judgment about future growth and margins.

## Building the Revenue Forecast

Revenue projections are the foundation of the DCF. Approaches include top-down (starting with market size and estimating market share), bottom-up (building from unit economics — price x volume for each product/segment), and consensus-based (using analyst estimates as a starting point). Growth rates should reflect the company's competitive position, industry dynamics, and macroeconomic environment. It is important to model different scenarios (base, upside, downside) to understand the range of possible outcomes.

## Operating Assumptions

After revenue, you project each line of the income statement. COGS and gross margin should reflect the company's cost structure and pricing power. SG&A and R&D expenses can be projected as a percentage of revenue or grown independently. Depreciation should be linked to the PP&E balance and capital expenditure plan. Working capital changes are driven by DSO, DIO, and DPO assumptions. Each assumption should be supported by historical analysis and forward-looking judgment.

## Putting It Together

The projected UFCF for each year is discounted back to the present using WACC (Weighted Average Cost of Capital) as the discount rate. The formula for the present value of each year's cash flow is: PV = UFCF / (1 + WACC)^n, where n is the number of years. The sum of all discounted cash flows plus the discounted terminal value gives Enterprise Value. Subtracting net debt gives Equity Value, and dividing by diluted shares outstanding gives the implied share price.`,
    videos: [
      { title: "DCF Model Tutorial", url: "https://www.youtube.com/watch?v=fd_emLLzJnk", duration: "22:30" },
      { title: "How to Build a DCF Model", url: "https://www.youtube.com/watch?v=znBLJkiJCYk", duration: "18:15" },
      { title: "Aswath Damodaran on Valuation", url: "https://www.youtube.com/watch?v=Z5chrxMuBoo", duration: "25:00" },
    ],
    codeExamples: [
      {
        language: "excel",
        code: `=== Unlevered Free Cash Flow Calculation ===

Revenue                           1,000
- COGS                             (600)
= Gross Profit                      400
- SG&A                             (150)
- R&D                               (50)
= EBITDA                            200
- Depreciation & Amortization        (40)
= EBIT                              160
- Taxes (@ 25%)                      (40)
= NOPAT (Net Operating Profit)      120
+ Depreciation & Amortization         40
- Capital Expenditures               (60)
- Increase in Net Working Capital    (15)
= Unlevered Free Cash Flow           85

=== DCF in Excel ===
PV of each year's UFCF:  =UFCF / (1 + WACC)^Year
Sum of PV of UFCFs:       =SUM(PV_Year1:PV_Year10)
PV of Terminal Value:     =Terminal_Value / (1 + WACC)^Last_Year
Enterprise Value:         =Sum_PV_UFCFs + PV_Terminal_Value
Equity Value:             =Enterprise_Value - Net_Debt
Price per Share:          =Equity_Value / Diluted_Shares`,
      },
    ],
    quiz: [
      {
        question: "What does Unlevered Free Cash Flow represent?",
        options: [
          "Cash available only to equity holders",
          "Cash available to all capital providers (debt and equity)",
          "Total revenue minus total expenses",
          "Net income after dividends",
        ],
        correct: 1,
      },
      {
        question: "What typically represents 60-80% of a company's DCF enterprise value?",
        options: [
          "The first year's free cash flow",
          "The terminal value",
          "Revenue projections",
          "Working capital changes",
        ],
        correct: 1,
      },
      {
        question: "How do you get from Enterprise Value to Equity Value?",
        options: [
          "Add net debt",
          "Subtract net debt",
          "Multiply by the P/E ratio",
          "Divide by WACC",
        ],
        correct: 1,
      },
    ],
  },

  "cib-13-2": {
    id: "cib-13-2",
    title: "WACC & Terminal Value",
    content: `# WACC and Terminal Value

WACC (Weighted Average Cost of Capital) and Terminal Value are two of the most critical — and debated — components of a DCF model. Small changes in either can significantly impact the valuation outcome.

## WACC: Weighted Average Cost of Capital

WACC is the blended cost of a company's capital — the return required by both debt holders and equity holders, weighted by their proportion in the capital structure. The formula is: WACC = (E/V) x Re + (D/V) x Rd x (1 - T), where E is market value of equity, D is market value of debt, V = E + D, Re is cost of equity, Rd is cost of debt, and T is the tax rate. The (1 - T) adjustment on debt reflects the tax deductibility of interest — a key advantage of debt financing.

## Cost of Equity (CAPM)

The cost of equity is typically estimated using the Capital Asset Pricing Model (CAPM): Re = Rf + Beta x (Rm - Rf), where Rf is the risk-free rate (typically the 10-year government bond yield), Beta measures the stock's volatility relative to the market (a beta of 1.2 means the stock is 20% more volatile than the market), and (Rm - Rf) is the equity risk premium (typically 5-7% based on historical data). A size premium may be added for smaller companies. Country risk premiums are added for emerging market companies.

## Cost of Debt

The cost of debt (Rd) is the interest rate the company pays on its borrowings. For publicly traded bonds, this is the yield to maturity. For private companies, it can be estimated based on the company's credit rating and current market spreads. The after-tax cost of debt is lower because interest payments are tax-deductible, so the effective cost is Rd x (1 - T). Using the current marginal cost of debt (what the company would pay to issue new debt today) is generally preferred over the historical average.

## Terminal Value: Perpetuity Growth Method

The perpetuity growth method (Gordon Growth Model) assumes free cash flows grow at a constant rate forever: Terminal Value = FCF_last x (1 + g) / (WACC - g), where g is the perpetuity growth rate. The growth rate should typically be at or below the long-term GDP growth rate (2-3% for developed economies) because no company can grow faster than the economy indefinitely. Small changes in g have an enormous impact on the terminal value, so this assumption must be well-justified.

## Terminal Value: Exit Multiple Method

The exit multiple method assumes the company is sold at the end of the forecast period at a multiple of its final-year financial metrics: Terminal Value = EBITDA_last x Exit Multiple. The exit multiple is typically based on current trading multiples for comparable companies. This method is more market-based and is often used as a sanity check against the perpetuity growth method. Both methods should produce similar results — significant divergence suggests one or more assumptions need revisiting.

## Sensitivity Analysis

Because small changes in WACC and terminal value assumptions dramatically impact the DCF result, sensitivity analysis is essential. The standard approach is to create a data table showing implied share prices across a range of WACC values (rows) and terminal growth rates or exit multiples (columns). This shows stakeholders the range of possible valuations and highlights which assumptions matter most.`,
    videos: [
      { title: "WACC Explained Step by Step", url: "https://www.youtube.com/watch?v=0inqw9cCJnM", duration: "14:20" },
      { title: "Terminal Value Calculation", url: "https://www.youtube.com/watch?v=VnXfjUY6bWE", duration: "11:55" },
    ],
    codeExamples: [
      {
        language: "excel",
        code: `=== WACC Calculation in Excel ===

Risk-Free Rate (Rf):         4.00%    (10-yr Treasury yield)
Beta:                        1.15     (from Bloomberg/regression)
Equity Risk Premium (ERP):   6.00%    (historical average)
Cost of Equity (Re):         =4.00% + 1.15 * 6.00% = 10.90%

Cost of Debt (Rd):           6.50%    (YTM on existing bonds)
Tax Rate:                    25.00%
After-Tax Cost of Debt:      =6.50% * (1 - 25%) = 4.88%

Equity Weight (E/V):         60.0%
Debt Weight (D/V):           40.0%

WACC = (60% x 10.90%) + (40% x 4.88%) = 8.49%

=== Terminal Value ===

Perpetuity Growth Method:
Last Year FCF:    $120M
Growth Rate (g):  2.5%
TV = 120 * (1 + 2.5%) / (8.49% - 2.5%) = $2,053M

Exit Multiple Method:
Last Year EBITDA: $200M
Exit Multiple:    10.0x
TV = 200 * 10.0 = $2,000M

=== Sensitivity Table (Data Table in Excel) ===
Use DATA TABLE function with WACC in rows, growth rate in columns
=TABLE(WACC_cell, Growth_Rate_cell)`,
      },
    ],
    quiz: [
      {
        question: "Why is the cost of debt multiplied by (1 - Tax Rate) in the WACC formula?",
        options: [
          "Because debt holders pay taxes on their interest income",
          "Because interest payments are tax-deductible, reducing the effective cost",
          "Because the tax rate reduces the principal amount",
          "Because debt is always cheaper after accounting for inflation",
        ],
        correct: 1,
      },
      {
        question: "What is a typical perpetuity growth rate used in DCF terminal values for developed economies?",
        options: ["0%", "2-3%", "8-10%", "15-20%"],
        correct: 1,
      },
    ],
  },

  "cib-14-1": {
    id: "cib-14-1",
    title: "Comps Analysis",
    content: `# Comparable Company and Comparable Transaction Analysis

Comparable analysis — often called "comps" — is one of the three core valuation methodologies alongside DCF and LBO analysis. It values a company by comparing it to similar companies (trading comps) or similar transactions (transaction comps / precedent transactions).

## Trading Comparables (Public Comps)

Trading comps value a company by looking at how similar publicly traded companies are valued by the market. The process involves: (1) selecting a peer group of similar companies based on industry, size, growth, profitability, and geography; (2) gathering financial data and calculating key metrics; (3) computing valuation multiples; and (4) applying those multiples to the target company's financials. The most common multiples are EV/EBITDA, EV/Revenue, P/E, and P/Book (for financial institutions).

## Selecting the Peer Group

Choosing the right comparable companies is both art and science. Companies should be similar in terms of: industry/sub-sector, business model, size (revenue, market cap), growth profile, margin structure, geographic exposure, and capital structure. In practice, a peer group typically includes 8-15 companies. If perfect comparables are unavailable, you can expand to adjacent sectors or use sub-groups with different weightings.

## Key Multiples and Their Uses

EV/EBITDA is the most widely used multiple in M&A because it is capital structure-neutral and not affected by differences in depreciation or tax policies. EV/Revenue is useful for high-growth or unprofitable companies. P/E is common for equity investors but is affected by capital structure and tax differences. Industry-specific multiples matter: EV/EBITDAR for airlines and retail (R = rent), Price/Book for banks, EV/Reserves for oil & gas companies, EV/Subscriber for media and telecom.

## Transaction Comparables (Precedent Transactions)

Precedent transaction analysis looks at prices paid in recent M&A transactions involving similar companies. This method captures the control premium — the additional price acquirers pay above the market price for control of the company (typically 20-40%). Transaction comps are identified by searching databases (Capital IQ, Bloomberg, Mergermarket) for deals in the same industry within the last 3-5 years. Key metrics include EV/EBITDA, EV/Revenue, and the premium paid to the unaffected share price.

## Applying Comps to Derive Valuation

To value the target, you apply the median or mean multiple from your peer group/transactions to the target's corresponding financial metric. For example: if the median EV/EBITDA for comparable companies is 10.0x and the target has EBITDA of $200M, the implied Enterprise Value is $2.0B. You typically present a range using the 25th-75th percentile of multiples. The "football field" chart in a pitch book displays the valuation range from each methodology side by side.`,
    videos: [
      { title: "Comparable Company Analysis Tutorial", url: "https://www.youtube.com/watch?v=PIPTnVMPHgg", duration: "16:40" },
      { title: "Trading Comps vs Transaction Comps", url: "https://www.youtube.com/watch?v=5CaFaGIJxgI", duration: "10:30" },
    ],
    codeExamples: [
      {
        language: "excel",
        code: `=== Comparable Company Analysis Template ===

Company    | EV ($B) | Revenue ($B) | EBITDA ($B) | EV/Revenue | EV/EBITDA | P/E
-----------|---------|-------------|-------------|------------|-----------|------
Company A  |   15.0  |     8.0     |     2.0     |    1.9x    |    7.5x   | 18.0x
Company B  |   22.0  |    10.5     |     3.2     |    2.1x    |    6.9x   | 15.5x
Company C  |   18.5  |     9.2     |     2.8     |    2.0x    |    6.6x   | 16.2x
Company D  |   25.0  |    12.0     |     3.5     |    2.1x    |    7.1x   | 17.8x
-----------|---------|-------------|-------------|------------|-----------|------
Mean       |         |             |             |    2.0x    |    7.0x   | 16.9x
Median     |         |             |             |    2.0x    |    7.0x   | 16.9x

Target EBITDA: $250M
Implied EV at Median EV/EBITDA: =250 * 7.0 = $1,750M
Less: Net Debt: ($400M)
Equity Value: $1,350M
/ Diluted Shares: 100M
Implied Price: $13.50`,
      },
    ],
    quiz: [
      {
        question: "Why is EV/EBITDA preferred over P/E for M&A valuation?",
        options: [
          "P/E is always higher than EV/EBITDA",
          "EV/EBITDA is capital structure-neutral and unaffected by tax and depreciation differences",
          "P/E includes the control premium",
          "EV/EBITDA is simpler to calculate",
        ],
        correct: 1,
      },
      {
        question: "What is a control premium?",
        options: [
          "The fee paid to the investment bank",
          "The additional price paid above market price for control of a company",
          "The premium charged by credit rating agencies",
          "The cost of regulatory approval",
        ],
        correct: 1,
      },
      {
        question: "How do you convert Enterprise Value to Equity Value?",
        options: [
          "Add net debt to Enterprise Value",
          "Subtract net debt from Enterprise Value",
          "Multiply Enterprise Value by the P/E ratio",
          "Divide Enterprise Value by shares outstanding",
        ],
        correct: 1,
      },
    ],
  },

  "cib-15-1": {
    id: "cib-15-1",
    title: "LBO Basics",
    content: `# Leveraged Buyout (LBO) Modeling

The LBO is one of the most important transaction types in investment banking and private equity. LBO modeling tests your ability to combine accounting, finance, and credit analysis into a single integrated framework.

## What is an LBO?

A Leveraged Buyout is the acquisition of a company using a significant amount of borrowed money (leverage). A private equity sponsor typically contributes 30-40% equity and finances the remainder with debt (60-70%). The target company's assets and future cash flows serve as collateral for the debt. The PE firm aims to generate returns through three levers: debt paydown (using the company's cash flows to repay debt), operational improvements (growing EBITDA through revenue growth and margin expansion), and multiple expansion (selling at a higher valuation multiple than the purchase price).

## The LBO Model Structure

An LBO model is built in Excel and typically includes: (1) Transaction assumptions — purchase price, financing structure (types and amounts of debt), and equity contribution. (2) Sources and Uses — sources of capital (debt tranches, equity) must equal uses (purchase price, fees, refinanced debt). (3) Projected financial statements — 5-7 year projections of income statement, balance sheet, and cash flow statement. (4) Debt schedule — tracking each debt tranche's balance, interest, amortization, and mandatory/optional repayments. (5) Returns analysis — calculating IRR and money-on-money (MoM) multiple at exit.

## Key LBO Metrics

The primary return metric is IRR (Internal Rate of Return) — PE firms typically target 20-25%+ IRR. Money-on-Money (MoM) = Exit Equity Value / Initial Equity Investment — a 3.0x MoM means the PE firm tripled its money. Cash-on-Cash return is another measure. On the credit side, key metrics include Leverage (Total Debt / EBITDA), Interest Coverage (EBITDA / Interest Expense), and Fixed Charge Coverage (EBITDA - CapEx) / (Interest + Mandatory Amortization). Lenders focus on these metrics to ensure the company can service its debt.

## What Makes a Good LBO Candidate?

PE firms look for specific characteristics in LBO targets: stable and predictable cash flows (to reliably service debt), strong market position with defensible competitive advantages, opportunities for operational improvement, limited capital expenditure requirements (more cash available for debt repayment), a capable management team, and a clear path to exit (IPO, strategic sale, or secondary buyout). Industries like healthcare, business services, software, and consumer staples are frequently targeted.

## Exit Strategies and Returns Attribution

The PE firm plans its exit from day one. Common exit routes include: selling to a strategic buyer (often at a higher multiple due to synergies), selling to another PE firm (secondary buyout), or taking the company public (IPO). Returns can be decomposed into three sources: EBITDA growth (operational improvements), multiple expansion (selling at a higher multiple), and leverage effect (debt paydown). Understanding this attribution helps investors evaluate the quality and sustainability of returns.`,
    videos: [
      { title: "LBO Modeling Tutorial", url: "https://www.youtube.com/watch?v=MqP3Aq0vNGM", duration: "20:15" },
      { title: "Leveraged Buyout Explained Simply", url: "https://www.youtube.com/watch?v=BXgBB2GKNHA", duration: "11:30" },
      { title: "Private Equity Returns Analysis", url: "https://www.youtube.com/watch?v=QBzBsJyoce0", duration: "14:50" },
    ],
    codeExamples: [
      {
        language: "excel",
        code: `=== Simple LBO Model ===

TRANSACTION ASSUMPTIONS:
Purchase EV/EBITDA:     8.0x
Target EBITDA:          $100M
Purchase Enterprise Value: $800M
Net Debt at Purchase:   $50M
Equity Value:           $750M

SOURCES & USES:
Sources:                      Uses:
Senior Debt (4.0x):  $400M    Purchase Equity:      $750M
Sub Debt (2.0x):     $200M    Refinance Debt:        $50M
Sponsor Equity:      $250M    Transaction Fees:      $50M
Total Sources:       $850M    Total Uses:           $850M

5-YEAR PROJECTION (Simplified):
Year:               0      1      2      3      4      5
EBITDA:            100    108    117    126    136    147
- Interest:               (36)   (33)   (29)   (25)   (21)
- Taxes:                  (18)   (21)   (24)   (28)   (32)
- CapEx:                  (20)   (20)   (22)   (22)   (24)
= FCF for Debt Paydown:    34     43     51     61     70

Total Debt:        600    566    523    472    411    341
Net Debt/EBITDA:   6.0x   5.2x   4.5x   3.7x   3.0x   2.3x

EXIT ANALYSIS (Year 5):
Exit EV/EBITDA:     8.0x (no multiple expansion)
Exit EV:            =147 * 8.0 = $1,176M
- Net Debt:         ($341M)
Exit Equity Value:  $835M
Equity Invested:    $250M
MoM:               =835/250 = 3.3x
IRR:               =IRR({-250, 0, 0, 0, 0, 835}) ≈ 27.3%`,
      },
    ],
    quiz: [
      {
        question: "What are the three main levers of LBO returns?",
        options: [
          "Revenue growth, cost cutting, and pricing power",
          "Debt paydown, EBITDA growth, and multiple expansion",
          "Interest rate reduction, tax optimization, and asset sales",
          "Market timing, sector rotation, and diversification",
        ],
        correct: 1,
      },
      {
        question: "If a PE firm invests $200M in equity and exits at $600M equity value, what is the MoM?",
        options: ["2.0x", "3.0x", "4.0x", "6.0x"],
        correct: 1,
      },
      {
        question: "What makes a good LBO candidate?",
        options: [
          "High growth but negative cash flows",
          "Stable cash flows, strong market position, and low CapEx needs",
          "Extremely high leverage already",
          "Companies with declining revenues",
        ],
        correct: 1,
      },
    ],
  },

  "cib-16-1": {
    id: "cib-16-1",
    title: "Excel Skills",
    content: `# Excel for Finance

Excel is the primary tool for financial analysis in investment banking. Mastering Excel shortcuts, functions, and modeling best practices is essential for productivity and accuracy.

## Essential Functions for Finance

The most critical Excel functions for finance include: VLOOKUP/XLOOKUP (finding data in tables), INDEX/MATCH (more flexible lookups), SUMPRODUCT (weighted calculations), IF/IFERROR (conditional logic and error handling), NPV/XNPV (net present value with regular/irregular cash flows), IRR/XIRR (internal rate of return), PMT (loan payments), and DATA TABLE (sensitivity analysis). Financial modelers also rely heavily on SUM, AVERAGE, MIN, MAX, COUNT, and ROUND functions.

## Keyboard Shortcuts

Speed in Excel separates top analysts from average ones. Essential shortcuts include: Ctrl+C/V/X (copy/paste/cut), Ctrl+Z/Y (undo/redo), Ctrl+1 (format cells), Ctrl+Shift+L (add filters), F2 (edit cell), F4 (toggle absolute/relative references), Alt+= (autosum), Ctrl+Shift+1 (number format), Ctrl+Shift+4 (currency format), Ctrl+Shift+5 (percentage format), Ctrl+Page Up/Down (navigate sheets), and Ctrl+Arrow (jump to end of data range). The best bankers rarely touch the mouse.

## Financial Modeling Best Practices

Professional financial models follow strict conventions: use blue font for hardcoded inputs and black font for formulas; separate assumptions, calculations, and outputs onto different sheets; use consistent time periods across all sheets; build in error checks and balance checks; avoid hardcoding numbers inside formulas; use named ranges for key assumptions; and structure models to flow from left to right and top to bottom. Models should be transparent enough for another analyst to follow without explanation.

## Building a Three-Statement Model

The three-statement financial model integrates the income statement, balance sheet, and cash flow statement. Start with historical data (3-5 years), then project revenue and expenses to build the income statement. Use working capital assumptions (DSO, DIO, DPO) and CapEx/depreciation schedules to project the balance sheet. The cash flow statement reconciles net income to cash and ensures the balance sheet balances. A circular reference arises because interest expense depends on debt, which depends on cash, which depends on interest — this is resolved using an iterative calculation or a circuit breaker.

## Advanced Techniques

Advanced Excel techniques for banking include: scenario/sensitivity analysis using DATA TABLE (two-variable) and CHOOSE functions (scenario toggling), dynamic charts that update with model inputs, consolidation models that aggregate multiple business units, waterfall charts for bridge analysis, and automated formatting using conditional formatting. For LBO models, you will need to build debt schedules with mandatory amortization, cash sweeps, and revolver draws. Mastering these techniques will make you significantly more effective and valued as a junior banker.`,
    videos: [
      { title: "Excel for Investment Banking", url: "https://www.youtube.com/watch?v=Sy4mhBBKXEw", duration: "18:45" },
      { title: "Financial Modeling Best Practices", url: "https://www.youtube.com/watch?v=E3Px4YQHIGM", duration: "15:30" },
    ],
    codeExamples: [
      {
        language: "excel",
        code: `=== Essential Finance Formulas ===

NPV with irregular dates:
=XNPV(discount_rate, cash_flows, dates)

IRR with irregular dates:
=XIRR(cash_flows, dates)

Loan Payment (PMT):
=PMT(rate/12, nper*12, -pv)    // monthly payment
Example: =PMT(0.06/12, 30*12, -500000) = $2,998/month

Two-Variable Sensitivity Table:
1. Set up row input (e.g., WACC) and column input (e.g., growth rate)
2. Top-left cell references the output (e.g., share price)
3. Select entire table → Data → What-If Analysis → Data Table
4. Row input cell = growth rate assumption cell
5. Column input cell = WACC assumption cell

Scenario Toggle with CHOOSE:
=CHOOSE(Scenario_Number, Base_Value, Upside_Value, Downside_Value)
Where Scenario_Number is 1 (Base), 2 (Upside), or 3 (Downside)

Dynamic Named Ranges:
=OFFSET(Sheet1!$A$1, 0, 0, COUNTA(Sheet1!$A:$A), 1)`,
      },
    ],
    quiz: [
      {
        question: "What color convention is used for hardcoded inputs in financial models?",
        options: ["Black font", "Blue font", "Red font", "Green font"],
        correct: 1,
      },
      {
        question: "What causes the circular reference in a three-statement model?",
        options: [
          "Revenue depends on expenses",
          "Interest expense depends on debt, which depends on cash, which depends on interest",
          "Assets must equal liabilities plus equity",
          "Tax calculations reference pre-tax income",
        ],
        correct: 1,
      },
    ],
  },

  "cib-17-1": {
    id: "cib-17-1",
    title: "Behavioral Prep",
    content: `# Behavioral Interview Preparation

Behavioral questions are a critical component of investment banking interviews. They assess your motivation, communication skills, teamwork, leadership, and cultural fit. Strong technical skills mean nothing if you cannot pass the behavioral round.

## "Tell Me About Yourself" (Your Story)

This is almost always the first question in any banking interview. Your answer should be a concise 2-minute narrative that covers: your background (where you are from, education), what sparked your interest in finance/banking, key experiences that built relevant skills (internships, projects, leadership roles), and why you are here today interviewing for this specific role. The key is to create a logical narrative arc — each experience should naturally lead to the next, culminating in your interest in this particular bank and role. Practice until it sounds natural, not rehearsed.

## "Why Investment Banking?"

This question tests whether you understand what bankers actually do and whether you are motivated by the right things. Strong answers reference: intellectual stimulation (complex financial analysis, working on transformative deals), exposure to senior executives and learning about diverse industries, the structured training and skill development, working on transactions that shape the business landscape, and the meritocratic culture. Avoid mentioning money as a primary motivation. Show that you understand the demanding lifestyle and are prepared for it.

## "Why This Bank?"

Research the specific bank's strengths, recent deals, culture, and strategic direction. Reference specific transactions the bank has led (check the bank's press releases and league table rankings), the bank's reputation in specific sectors or products, conversations you have had with current employees, unique training programs or culture aspects, and the bank's market position and recent strategic moves. Generic answers that could apply to any bank will not impress interviewers.

## Teamwork and Leadership Questions

Questions like "Tell me about a time you worked in a team" or "Describe a leadership experience" require structured answers using the STAR method: Situation (set the context), Task (what was your responsibility), Action (what specifically did you do), Result (what was the outcome, quantified if possible). Choose examples that demonstrate relevant skills: working under pressure, managing competing priorities, resolving conflicts, taking initiative, and delivering results. Banking is a team sport — show you can collaborate effectively.

## Handling Difficult Questions

Prepare for challenging questions like: "What is your biggest weakness?" (give a genuine answer with specific steps you have taken to improve), "Tell me about a time you failed" (show self-awareness and what you learned), "Where do you see yourself in 5 years?" (show ambition within banking — do not say PE or hedge funds at this stage), and "Why should we hire you over other candidates?" (highlight your unique combination of skills, experiences, and motivation). Authenticity matters — interviewers can detect scripted answers.`,
    videos: [
      { title: "Investment Banking Behavioral Interview", url: "https://www.youtube.com/watch?v=eOEjC8v4oZI", duration: "14:20" },
      { title: "Tell Me About Yourself - Banking", url: "https://www.youtube.com/watch?v=es7XtrlsDIQ", duration: "11:45" },
    ],
    quiz: [
      {
        question: "What does the STAR method stand for?",
        options: [
          "Strategy, Tactics, Analysis, Results",
          "Situation, Task, Action, Result",
          "Summary, Timeline, Approach, Review",
          "Strengths, Targets, Achievements, References",
        ],
        correct: 1,
      },
      {
        question: "What should you avoid saying when asked 'Why Investment Banking?'",
        options: [
          "I enjoy complex financial analysis",
          "I want to work on transformative deals",
          "Primarily because of the high salary",
          "I appreciate the structured training",
        ],
        correct: 2,
      },
    ],
  },

  "cib-18-1": {
    id: "cib-18-1",
    title: "Technical Prep",
    content: `# Technical Interview Preparation

Technical questions are the core of investment banking interviews. They test your understanding of accounting, valuation, M&A, and LBO concepts. Interviewers want to see that you can think clearly about financial concepts and communicate your answers in a structured way.

## "Walk Me Through a DCF"

This is the most common technical question. A strong answer: "A DCF values a company based on the present value of its future free cash flows. First, you project unlevered free cash flows for 5-10 years by starting with EBIT, subtracting taxes, adding back depreciation, subtracting capital expenditures, and adjusting for changes in working capital. Then you calculate a terminal value using either the perpetuity growth method or exit multiple method. You discount all cash flows back to the present using WACC as the discount rate. The sum gives you Enterprise Value. Subtract net debt to get Equity Value, and divide by diluted shares for the implied share price."

## "Walk Me Through the Three Financial Statements"

"The three statements are the income statement, balance sheet, and cash flow statement. The income statement shows revenue, expenses, and profitability over a period — starting with revenue and ending with net income. The balance sheet is a snapshot showing assets equals liabilities plus equity at a point in time. The cash flow statement starts with net income, adjusts for non-cash items and working capital changes in the operating section, shows capital expenditures and acquisitions in the investing section, and debt and equity activity in the financing section. They are linked: net income flows from the income statement to the balance sheet (retained earnings) and cash flow statement. Cash from the cash flow statement becomes the cash balance on the balance sheet."

## Accounting Questions

Common accounting questions include: "If depreciation increases by $10, what happens to each statement?" (Income: EBIT falls by $10, Net Income falls by $6 assuming 40% tax; Cash Flow: starts $6 lower but adds back $10 of D&A, net +$4; Balance Sheet: PP&E falls by $10, cash rises by $4, retained earnings falls by $6). "What is the difference between cash and accrual accounting?" "How does an inventory write-down affect the statements?" "Walk me through a $100 asset purchase with 50% debt and 50% cash."

## Valuation Questions

"What are the main valuation methodologies?" (DCF, comparable companies, precedent transactions, and LBO analysis). "When would you use each one?" "How do you pick comparable companies?" "Why might the same company have different valuations under each method?" "If you could only use one valuation method, which would you choose and why?" (DCF — it is based on intrinsic value rather than market sentiment, though it is highly sensitive to assumptions). Enterprise Value vs. Equity Value questions are also common: "Is it possible for EV to be less than Equity Value?" (Yes — if the company has more cash than debt, net debt is negative).

## M&A and LBO Questions

"Why would a company acquire another company?" (Synergies, growth, market share, strategic positioning). "Is an acquisition accretive or dilutive?" (Compare the target's P/E to the acquirer's — if target P/E is lower, the deal is likely accretive to EPS). "Walk me through a basic LBO." "What makes a good LBO candidate?" "How do you determine the maximum purchase price in an LBO?" (Work backward from the minimum acceptable IRR to determine how much equity can be contributed and how much debt can be supported).`,
    videos: [
      { title: "IB Technical Interview Questions", url: "https://www.youtube.com/watch?v=W0pOhqJDRwQ", duration: "22:10" },
      { title: "Walk Me Through a DCF", url: "https://www.youtube.com/watch?v=fd_emLLzJnk", duration: "15:30" },
      { title: "Accounting Interview Questions", url: "https://www.youtube.com/watch?v=EKGFE5rgGMc", duration: "18:40" },
    ],
    codeExamples: [
      {
        language: "formula",
        code: `=== $10 Depreciation Increase — Impact on All Three Statements ===

INCOME STATEMENT:
  Depreciation:    +$10
  EBIT:            -$10
  Tax Savings:     +$4  (at 40% tax rate)
  Net Income:      -$6

CASH FLOW STATEMENT:
  Net Income:      -$6
  Add back D&A:    +$10
  Net Cash Impact: +$4

BALANCE SHEET:
  Cash:            +$4
  PP&E:            -$10
  Total Assets:    -$6
  Retained Earnings: -$6
  Balance Sheet:   STILL BALANCES ✓`,
      },
    ],
    quiz: [
      {
        question: "If depreciation increases by $10 (40% tax rate), what is the net impact on cash flow?",
        options: ["-$10", "-$6", "+$4", "+$10"],
        correct: 2,
      },
      {
        question: "When is an acquisition accretive to EPS?",
        options: [
          "When the target is larger than the acquirer",
          "When the target's P/E is lower than the acquirer's P/E",
          "When the deal is financed with 100% cash",
          "When the target has higher revenue growth",
        ],
        correct: 1,
      },
      {
        question: "Can Enterprise Value be less than Equity Value?",
        options: [
          "No, never",
          "Yes, if net debt is negative (more cash than debt)",
          "Yes, if the company is unprofitable",
          "Only for private companies",
        ],
        correct: 1,
      },
    ],
  },

  "cib-19-1": {
    id: "cib-19-1",
    title: "Case Studies",
    content: `# M&A Case Studies and Brain Teasers

Case studies and brain teasers are used in investment banking interviews to assess your analytical thinking, business judgment, and ability to structure problems under pressure.

## The M&A Case Study Format

A typical M&A case study presents a scenario: "Company A is considering acquiring Company B. Should they proceed?" You may receive financial data, industry context, and strategic rationale. Structure your analysis as follows: (1) Evaluate the strategic rationale — does the deal make strategic sense? What are the synergies? (2) Perform a valuation — what is Company B worth? What premium is reasonable? (3) Assess the financial impact — is the deal accretive or dilutive? Can it be financed? (4) Identify risks — integration challenges, regulatory hurdles, cultural fit. (5) Recommend — proceed, modify, or walk away, with clear reasoning.

## Accretion/Dilution Analysis

A core component of M&A case studies is determining whether the acquisition is accretive (increases acquirer's EPS) or dilutive (decreases EPS). For an all-stock deal: compare the target's P/E to the acquirer's P/E — if the target's P/E is lower, the deal is accretive. For a cash deal: compare the target's earnings yield to the after-tax cost of debt used to fund the acquisition. For mixed deals, you need to calculate pro forma combined EPS by combining earnings and share counts, accounting for synergies, transaction adjustments, and financing costs.

## Synergy Analysis

Synergies are the additional value created by combining two companies. Cost synergies (usually more reliable) include eliminating duplicate functions (HR, IT, finance), renegotiating supplier contracts, closing overlapping facilities, and reducing headcount. Revenue synergies (harder to achieve and quantify) include cross-selling products, accessing new markets, and combining technologies. In your analysis, estimate synergies conservatively, phase them in over 2-3 years, and account for one-time costs to achieve them (restructuring charges, integration costs).

## Brain Teasers and Market Sizing

Some banks still ask brain teasers and market sizing questions: "How many golf balls fit in a school bus?" or "Estimate the revenue of all Starbucks in London." The key is not the exact answer but your approach. Structure the problem, state assumptions clearly, round numbers for easy math, and walk through the logic step by step. For market sizing: start with population, narrow to the relevant segment, estimate frequency and spend per occasion, and multiply through. Show your work and demonstrate clear analytical thinking.

## Practice Case: Should Company A Acquire Company B?

Consider this framework: Company A (large consumer goods company, EV/EBITDA of 12x, stable 3% growth) is considering acquiring Company B (smaller organic foods brand, EV/EBITDA of 15x, growing 15% annually). Analyze: (1) Strategic fit — complements A's portfolio, access to fast-growing organic segment. (2) Valuation — B commands a premium valuation; is it justified by growth? (3) Synergies — distribution leverage, procurement savings, shared R&D. (4) Risks — cultural clash, overpaying for growth, integration complexity. (5) Financing — how should A fund the deal? Impact on leverage and credit rating.`,
    videos: [
      { title: "M&A Case Study Interview", url: "https://www.youtube.com/watch?v=p7Nt7IzEOOQ", duration: "16:50" },
      { title: "Accretion Dilution Analysis Tutorial", url: "https://www.youtube.com/watch?v=2LqU4ULIzqo", duration: "14:25" },
    ],
    codeExamples: [
      {
        language: "formula",
        code: `=== Quick Accretion/Dilution Test ===

ALL-STOCK DEAL:
Acquirer P/E:  20.0x  →  Earnings Yield = 1/20 = 5.0%
Target P/E:    15.0x  →  Earnings Yield = 1/15 = 6.7%
Result: ACCRETIVE (target earns more per dollar of value)

ALL-CASH DEAL:
Target Earnings Yield:       6.7%
After-Tax Cost of Debt:      4.0%  (6% pretax x (1-33%))
Result: ACCRETIVE (target earns 6.7% vs 4.0% cost)

=== Market Sizing Framework ===
Example: "Estimate annual coffee shop revenue in a city"

Population of city:          2,000,000
% that drinks coffee:        60% → 1,200,000
% that buys from shops:      40% → 480,000
Visits per week:             3
Avg spend per visit:         $5
Weekly revenue:              480,000 × 3 × $5 = $7.2M
Annual revenue:              $7.2M × 52 = ~$374M`,
      },
    ],
    quiz: [
      {
        question: "In an all-stock deal, when is the acquisition accretive?",
        options: [
          "When the acquirer's stock price rises",
          "When the target's P/E ratio is lower than the acquirer's",
          "When the deal size exceeds $1 billion",
          "When synergies are greater than integration costs",
        ],
        correct: 1,
      },
      {
        question: "What is the most important thing in answering brain teasers?",
        options: [
          "Getting the exact right answer",
          "Answering as quickly as possible",
          "Showing a structured approach and clear logical thinking",
          "Using advanced mathematical formulas",
        ],
        correct: 2,
      },
    ],
  },

  "cib-20-1": {
    id: "cib-20-1",
    title: "Networking",
    content: `# Networking and Applications

Breaking into investment banking requires more than just technical knowledge. Strategic networking and thoughtful application preparation are often the difference between getting an interview and being overlooked.

## The Importance of Networking

Investment banking recruitment is heavily relationship-driven. Many positions are filled through employee referrals and networking before they are even posted publicly. Networking serves multiple purposes: it helps you learn about different banks and roles, provides insider knowledge about the interview process, builds relationships that can lead to referrals, and demonstrates the social skills that are essential in a client-facing role. Start networking early — ideally 6-12 months before application deadlines.

## How to Network Effectively

Reach out to alumni, connections through LinkedIn, and professionals you meet at industry events. When sending a cold email or LinkedIn message, keep it concise: introduce yourself, explain the connection (same university, mutual contact, shared interest), ask for a specific and reasonable request (a 15-20 minute informational interview), and make it easy for them to say yes. During informational interviews, ask thoughtful questions about their career path, what they enjoy about their role, and advice for breaking in. Do NOT ask for a job directly — focus on building a genuine relationship.

## Building Your Application

Your resume should be concise (one page), quantified (use numbers to demonstrate impact), and tailored to banking. Highlight relevant experiences: finance internships, leadership roles, academic achievements, and any financial analysis or modeling you have done. Use strong action verbs and focus on results. Your cover letter should explain your "why" — why banking, why this bank, and why you. Reference specific deals, people you have spoken with (with permission), and what differentiates this bank from competitors.

## The Recruitment Timeline

For summer internships (the primary pathway into full-time banking), applications typically open 12-18 months in advance. At top banks, the process includes: online application, online tests (numerical, verbal, situational judgment), a first-round interview (often video-based with behavioral and basic technical questions), and a final round (superday) with 3-5 back-to-back interviews covering behavioral, technical, and fit questions. Off-cycle and lateral recruitment follows a less structured timeline but still requires extensive preparation.

## Following Up and Maintaining Relationships

After every networking conversation or interview, send a thank-you email within 24 hours. Reference specific topics you discussed to show genuine engagement. Maintain relationships over time by sharing relevant articles, congratulating contacts on deals or promotions, and providing periodic updates on your own progress. This is not transactional — the best networkers build authentic, mutually beneficial relationships. Even if you do not get the role this time, maintaining the relationship can open doors in the future. The finance community is smaller than you think, and your reputation follows you throughout your career.`,
    videos: [
      { title: "Networking for Investment Banking", url: "https://www.youtube.com/watch?v=qRnXaOJiIeo", duration: "12:30" },
      { title: "How to Break into Investment Banking", url: "https://www.youtube.com/watch?v=sBl5vXGQRFo", duration: "15:45" },
    ],
    quiz: [
      {
        question: "What is the primary purpose of an informational interview?",
        options: [
          "To ask directly for a job offer",
          "To learn about the person's career path and build a genuine relationship",
          "To practice your technical interview answers",
          "To negotiate salary expectations",
        ],
        correct: 1,
      },
      {
        question: "When should you typically start networking for summer internship applications?",
        options: [
          "The week before the deadline",
          "1-2 months before applications open",
          "6-12 months before application deadlines",
          "Only after receiving an interview invitation",
        ],
        correct: 2,
      },
      {
        question: "What should you do within 24 hours of a networking conversation?",
        options: [
          "Send your resume",
          "Call them to follow up",
          "Send a personalized thank-you email referencing specific discussion topics",
          "Connect with all their LinkedIn contacts",
        ],
        correct: 2,
      },
    ],
  },
};
